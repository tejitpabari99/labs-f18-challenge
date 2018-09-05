from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
	return render_template('index.html')

@app.route('/pokemon/<int:poki_id>')
def pokimon(poki_id):
	r = requests.get('https://pokeapi.co/api/v2/pokemon/%s' % poki_id)
	name = r.json()
	return 'The pokemon with id %d is %s' % (poki_id, name["forms"][0]["name"])

@app.route('/pokemon/<poki>')
def pokimon_name(poki):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/%s' % poki)
    poki_id = r.json()
    url = poki_id["forms"][0]["url"]
    return 'The pokemon with name %s has id %s' % (poki, url[-2])

if __name__ == '__main__':
	app.run()
