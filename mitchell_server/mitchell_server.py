import flask
import logging
import os
import sys
import waitress
import json
import werkzeug.middleware.proxy_fix
import apscheduler.schedulers.background

app = flask.Flask(__name__)
app.wsgi_app = werkzeug.middleware.proxy_fix.ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_port=1)

dir_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(dir_path, 'config', os.getenv('CONFIG'))
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
    app.config.update(config)

log_format = '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
try:
    home = os.getenv('HOME')
    logfile_path = os.path.join(home, app.config['LOGFILE'])
    stream = open(logfile_path, 'a+')
except:
    print("No logfile specified")
    stream = sys.stdout
logging.basicConfig(
    format=log_format, 
    level=app.config['LOG_LEVEL'],
    stream=stream
)
log = logging.getLogger(__name__)

app.scheduler = apscheduler.schedulers.background.BackgroundScheduler()
app.scheduler.start()



@app.route('/')
def index():
    return flask.render_template('index.html')




def main():
    log.info('Starting up SlickList Server')
    log.info(f'LOG_LEVEL is {app.config["LOG_LEVEL"]}')

    if 'UNIX_SOCKET' in app.config:
        log.info('unix_socket')
        waitress.serve(app, unix_socket=app.config['UNIX_SOCKET'], unix_socket_perms='666')
    else:
        log.info('no socket')
        waitress.serve(app, port=app.config['PORT'])


if __name__ == '__main__':
    main()
