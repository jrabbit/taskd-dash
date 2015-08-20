from bottle import route, run, template

from taskc.simple import TaskdConnection

@route('/')
def index():
    tc = TaskdConnection()
    tc.client_cert = "pki/client.cert.pem"
    tc.client_key = "pki/client.key.pem"
    tc.cacert_file = "pki/ca.cert.pem"
    tc.server = ""
    tc.group = "Public"
    tc.username = "jack"
    tc.uuid = ""
    tc.connect()
    resp = tc.stats()
    print resp.data
    tpl = template("stats.tpl", response=resp.data)
    return tpl

run(host='localhost', port=8080, debug=True, reloader=True)