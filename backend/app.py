from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
# Accept JSON (frontend posts JSON)
data = request.get_json(force=True)
if not data:
return jsonify({'error': 'No JSON received'}), 400


# Basic processing — echo back with a confirmation message
name = data.get('name', 'Unknown')
email = data.get('email', '')
message = data.get('message', '')


# Example: pretend to save, validate, etc.
# Here we'll just return a processed response
response = {
'status': 'success',
'received': {
'name': name,
'email': email,
'message': message
},
'note': f'Thanks {name}! Your message was processed by Flask.'
}
return jsonify(response)


if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000, debug=False)
