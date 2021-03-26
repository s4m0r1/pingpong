from bottle import route, run, template
import os

TEXT=os.environ['PING_PONG_TEXT']

@route('/')
def index():
    return template('{{TEXT}}', TEXT=TEXT)

run(host='localhost', port=8080)