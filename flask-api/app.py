from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/name', methods=['GET'])
def greet_name():
    name = request.args.get('name')
    if not name:
        return jsonify({'message': 'Hello, World!'}), 200
    return jsonify({'message': 'Hello, {}!'.format(name)}), 200

if __name__ == '__main__':
    app.run()

