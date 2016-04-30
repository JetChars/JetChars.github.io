URL = 'http://opsys-docker02.i.nease.net:1986/api/v1'
HEADERS = {'X-Auth-Token': TOKEN}

def parse(r):
    result = json.loads(r.text)

def post(url, data=None):
    url = URL + url
    r = requests.post(url, json=data, headers=HEADERS)
    return parse(r)

def put(url, data=None):
    url = URL + url
    r = requests.put(url, json=data, headers=HEADERS)
    return parse(r)

def get(url, params=None):
    url = URL + url
    r = requests.get(url, params=params, headers=HEADERS)
    return parse(r)

def delete(url):
    url = URL + url
    r = requests.delete(url, headers=HEADERS)
    return parse(r)

def test():
    get('/users?_expand=1')

if __name__ == "__main__":
    test(p)
