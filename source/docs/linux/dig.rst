================================
dig -- Domain Information Groper
================================


``dig`` is much power that ``nslookup``

- simply type dig will get root domains
- cmd format -- ``dig @<dnsserver> <name> <querytype>``
    - if **dnsserver** not configured will used dnsserver at ``resolv.conf``
    - will query ``A`` type of data by default
    - search options
        - ``-c <class>`` -- default value is ``IN``
        - ``-f <querylist>``
        - ``-t <querytype>`` -- can be ommited by default
        - ``-t <name>`` -- can be ommited by default
        - ``-4|6`` -- ipv4/6
        - ``-x`` -- query reversely
    - query options
        - ``+domain=<domain>`` -- set query domain 
        - ``+[no]tcp`` -- use or disable tcp protocol
        - ``+trace`` -- following whole procedure
        - ``+short`` -- simplify the results
        - ``+[no]cmd|comment|stat`` -- will hide cmd/comment/stat section of info

C:\Users\gzcaiwenjie\Desktop\tt


- domain vs. search in ``resolv.conf``
    - https://github.com/rthalley/dnspython/blob/master/dns/resolver.py#L825-L831