# gevent is green event runner

import gevent
from gevent import socket

hosts = ['www.ericsson.com', 'www.publicissapient.com', 'www.neueda.com', 'www.crappytaxidermy.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname,host) for host in hosts]

gevent.joinall(jobs, timeout=5) # start all threads then join all

for job in jobs:
    print(job.value)
