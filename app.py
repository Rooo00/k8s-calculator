from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/resta')
def resta():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify(resultado=a - b)
    except (TypeError, ValueError):
        return jsonify(error="Parámetros 'a' y 'b' deben ser números"), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)