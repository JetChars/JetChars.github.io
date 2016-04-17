''' mydomaintrace developed with dnspython 
'''



import urllib
import random
import socket
import sys
import re
import dns.resolver
import dns.name
import dns.rdatatype
import dns.rdataclass
import dns.message
import dns.query
import dns.rcode
import dns.opcode
import dns.exception

class NoNameserver(dns.exception.DNSException):
    '''empty name server'''
    pass

def get_root():
    '''get root name server list
    return a list of str list'''
    result = []
    while not result:
        try:
            page = urllib.urlopen("http://ftp.internic.net/domain/named.cache")
            a_records = []
            ns_records = []
            for nsitem in page.readlines():
                if nsitem.startswith(';'):
                    continue
                item = nsitem.split()
                if item[2] == 'A':
                    a_records.append(item)
                elif item[2] == 'NS':
                    ns_records.append(item)
            result = [a_records, ns_records]
        except (socket.error, EOFError, IOError):
            continue
        finally:
            page.close()
    return result

def digquery(qname, nameserver):
    '''simple query @nameserver
    return dns.message.Message
    '''
    nameserver = nameserver
    query = dns.name.from_text(qname)
    rdtype = dns.rdatatype.A
    rdcls = dns.rdataclass.IN
    request = dns.message.make_query(query, rdtype, rdcls)
    response = None
    if len(nameserver) == 0:
        raise NoNameserver
    while response is None:
        try:
            response = dns.query.tcp(request, nameserver, 10, af=socket.AF_INET)
        except (socket.error, EOFError, IOError, dns.exception.Timeout):
            response = None
            continue
    return response

def digtrace(query):
    '''mimic dig +trace'''
    # check name format
    if not re.match(r'^([0-9a-zA-Z\-]+\.)*[0-9a-zA-Z\-]+(\.)?$', query):
        print "invalid query name"
        sys.exit(1)
    # auto complete FQDN
    if re.match(r'^([0-9a-zA-Z\-]+\.)*[0-9a-zA-Z\-]+$', query):
        query = query+'.'


    # query = sys.argv[1]
    root = get_root()
    nsip = root[0][0][3]
    nsname = root[0][0][0]
    print '\n', "getting root servers:", '\n'
    for eachline in root[1]:
        eachline[1] = 'IN'
        print '\t'.join(eachline)
    print '\n', "randomly choose", nsname, '\n', "query from", nsname, '(', nsip, ')', '\n'
    result = digquery(query, nsip)
    while not result.answer:
        for rrset in result.authority:
            rs_records = str(rrset).split('\n')
            # if rrset.to_text().split()[0] == query
            # print rrset
            for eachitem in rs_records:
                item_elements = eachitem.split()
                # remove ttl part of record
                del item_elements[1]
                print '\t'.join(item_elements)
            # ends in status such as NXDOMAIN
            if result.rcode() != dns.rcode.NOERROR:
                sys.exit(0)
            # ends if record is Start_of_Authority
            if result.authority[0].to_text().split()[3] == "SOA":
                sys.exit(0)
        random.shuffle(result.additional)
        while len(result.additional) > 0 and result.additional[0].to_text().split()[3] == "AAAA":
            del result.additional[0]
        nsname = result.authority[0].to_text().split()[4]
        if len(result.additional) > 0:
            nsip = result.additional[0].to_text().split()[4]
        else:
            nsip = str(dns.resolver.query('ns1.oray.net.', 'A')[0])
        print '\n', "randomly choose", nsname, '\n', "query from", nsname, '(', nsip, ')', '\n'
        result = digquery(query, nsip)
        # print answer
    for rrset in result.answer:
        print rrset.to_text()



if __name__ == '__main__':

    # check args
    if len(sys.argv) == 1:
        print "-t,\t\tentering auto_test mode", '\n', "domain_name,\tdig +trace "
        sys.exit(0)
    # start auto tests
    if sys.argv[1] == '-t':
        TEST_LST = ["mail.qiye.163.com.",
                    "co-m.",
                    "bdt.cwj.tw.",
                    "tw.",
                    "com.",
                    "_sdfdsfs.163.com"]
        for QUERY in TEST_LST:
            print '\n\n\n\n', 'test domain_name', QUERY
            digtrace(QUERY)
    else:
        QUERY = sys.argv[1]
        digtrace(QUERY)


