import datetime
import json

from bottle import route, run, template
import humanize

from taskc.simple import TaskdConnection

@route('/')
def index():
    tc = TaskdConnection()
    tc.client_cert = "pki/client.cert.pem"
    tc.client_key = "pki/client.key.pem"
    tc.cacert_file = "pki/ca.cert.pem"
    with open("conf.json") as j:
        config = json.load(j)
    tc.server = config['server']
    tc.group = config['group']
    tc.username = config['username']
    tc.uuid = config['user_uuid']
    tc.connect()
    resp = tc.stats()
    d = dict([x.split(":") for x in resp.data])
    # do some humanizing of the data
    d.update({k: humanize.naturalsize(v) for k,v in d.items() if "bytes" in k or k == "user data"})
    d['uptime'] = humanize.naturaldelta(datetime.timedelta(seconds=int(d['uptime'])))
    # d['total bytes in'] =  humanize.naturalsize(d['total bytes in'])
    tpl = template("stats.tpl", response=d)
    return tpl

run(host='localhost', port=8080, debug=True, reloader=True)