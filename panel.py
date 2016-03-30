from bottle import get, post, run, template, request
import requests

TOR_EXIT_NODE_IPS = []
r = requests.get('https://check.torproject.org/exit-addresses')
r_lines = r.content.split('\n')
for line in r_lines:
    if line.startswith('ExitAddress'):
        TOR_EXIT_NODE_IPS.append(line.split(' ')[1])

LOGIN_FORM_HTML = '<p><h2>CryptoWall Tracker Admin</h2></p><form method="post" action=""><p><input type="text" name="username" value=""></p><p><input type="password" name="password" value=""></p><p class="submit"><input type="submit" name="commit" value="Login"></p></form>'

@get('/administration/login')
def show_login():
    return LOGIN_FORM_HTML

@post('/administration/login')
def get_logininfo():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == 'yonathan' and password == 'Crypt3d':
        if request.remote_addr in TOR_EXIT_NODE_IPS:
            return '<font color="red"><b>Your IP address seems to be listed as being a Tor exit node. You have been logged out.<b></font>'
        else:
            return 'Thank you for playing my game, you have reported to the Internet Police. You can review your report at <a href="http://internetpolice.us/">internetpolice.us</a><br /><center><img width="450px" src="http://internetpolice.us/images/internet-police.svg"></center>'
    else:
        return '<font colo="red">Login failed, wrong credentials?</font><br />' + LOGIN_FORM_HTML

run(host='localhost', port=8080)