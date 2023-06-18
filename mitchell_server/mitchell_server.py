import flask
import logging
import os
import sys
import waitress
import werkzeug.middleware.proxy_fix
import apscheduler.schedulers.background


app = flask.Flask(__name__)
app.wsgi_app = werkzeug.middleware.proxy_fix.ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_port=1)


# TODO: Make a more sustainable method for maintaining development and prduction
# environments
app.config['LOG_LEVEL'] = os.getenv('LOG_LEVEL', 'DEBUG')
app.config['PORT'] = '8000'

log_format = '%(levelname)s | %(name)s | %(message)s'
try:
    stream = open(os.getenv('LOGFILE'), 'a')
except:
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
    log.info('Starting up Mitchell Server')
    log.info(f'LOG_LEVEL is {app.config["LOG_LEVEL"]}')

    if 'UNIX_SOCKET' in app.config:
        log.info('unix_socket')
        waitress.serve(app, unix_socket=app.config['UNIX_SOCKET'], unix_socket_perms='666')
    else:
        log.info('no socket')
        waitress.serve(app, port=app.config['PORT'])


if __name__ == '__main__':
    main()
