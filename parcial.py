from flask import Flask
from flask import jsonify
import json
import  hashlib
from flask import render_template

app = Flask(__name__)

@app.route('/')
def name():
	return 'Charles Acevedo Diaz T00039395'

@app.route('/hash/<string:s>/json')
def hashStringJ(s):
	SHA384 = hashlib.sha384(s.encode())
	SHA256 = hashlib.sha256(s.encode())
	SHA224 = hashlib.sha224(s.encode())
	SHA512 = hashlib.sha512(s.encode())
	SHA1 = hashlib.sha1(s.encode())

	j = {"sha256": SHA256.hexdigest(), "sha384": SHA384.hexdigest(), "sha224": SHA224.hexdigest(), "sha512": SHA512.hexdigest(), "sha1": SHA1.hexdigest()}


	return jsonify(j)

@app.route('/hash/<string:s>')
def hashString(s):
	SHA384 = hashlib.sha384(s.encode())
	SHA256 = hashlib.sha256(s.encode())
	SHA224 = hashlib.sha224(s.encode())
	SHA512 = hashlib.sha512(s.encode())
	SHA1 = hashlib.sha1(s.encode())

	


	return render_template('index.html', SHA384=SHA384.hexdigest(), SHA256=SHA256.hexdigest(), SHA224=SHA224.hexdigest(), SHA512=SHA512.hexdigest(), SHA1=SHA1.hexdigest())

		
if __name__ == '__main__':
	app.run(debug=True) 