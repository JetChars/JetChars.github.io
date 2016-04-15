''' mydomaintrace developed with dnspython 
'''



import urllib
import re
from contextlib import closing
import dns.resolver
import dns.name
import dns.rdatatype
import dns.rdataclass
import dns.message
import dns.query
import dns.resolver
# test dnspython

# root dnsserver
# http://ftp.internic.net/domain/named.cache


#answers = dns.resolver.query('mail.qiye.163.com')

# for rdata in answers:
#     print rdata
#     print dir(rdata)
# with closing(urllib.urlopen("http://ftp.internic.net/domain/named.cache")) as page:
#     for eachline in page.readlines():
#         if not re.search('^;', eachline):
#             item = eachline.split()
#             if item[2] != 'A':
#                 print item

# dns.query.udp("z.cn", "64.99.80.30")

# def digquery(qname,nx):
# nameserver = nx
nameserver = "192.5.5.241"
nameserver_ports = {}
port = 53
search = []
timeout = 2.0
lifetime = 30.0
keyring = None
keyname = None
keyalgorithm = dns.tsig.default_algorithm
edns = -1
ednsflags = 0
payload = 0
cache = None
flags = None
retry_servfail = False
rotate = False

query = dns.name.from_text("mail.qiye.163.com")
rdtype = dns.rdatatype.from_text("A")
rdcls = dns.rdataclass.from_text("IN")
request = dns.message.make_query(query, rdtype, rdcls)

response = dns.query.tcp(request, nameserver)
answer = dns.resolver.Answer("com.", rdtype, rdcls, response)

print(type(response))

print response