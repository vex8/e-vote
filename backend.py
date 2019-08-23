# Mock backend
# Do not use on production

from flask import Flask, escape, request, send_file, jsonify, make_response

app = Flask(__name__, template_folder='.')
app.debug = True

@app.route('/<path:filename>')
def home(filename):
  return send_file(filename)

@app.route('/checktoken', methods=['GET', 'POST'])
def checkToken():
  json = request.get_json(force=True)
  ret = None
  if(json['token'] == 'abcd'):
    ret = jsonify({'code': 4, 'return': 'Token is valid.'})
  else:
    ret = jsonify({'code': 1, 'return': 'Token is invalid.'})
  resp = make_response(ret)
  resp.mimetype = 'application/json'
  return resp