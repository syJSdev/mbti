import os
import sys
from multiprocessing import cpu_count
root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
app_path = os.path.join(root_path, '.')
sys.path.append(app_path)
import settings  # noqa
proc_name = "mbti"
workers = cpu_count()
worker_class = 'gevent'
reload = settings.DEBUG
pidfile = os.path.join(root_path, 'deploy', proc_name + '.pid')
raw_env = []
pythonpath = ','.join([app_path, root_path])
loglevel = "debug"
access_log_format = '%(t)s %(h)s "%(f)s" "%(a)s" "%(r)s" %(s)s %(p)s %(L)s'
logpath = "/var/log/"
accesslog = os.path.join(logpath, 'mbti.gunicorn.access.log')
errorlog = os.path.join(logpath, 'mbti.gunicorn.error.log')
 
