#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    """
    welcome message.
    """

    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_data():
    """
    A JSON response containing a list of all usernames.
    """

    return jsonify(list(users.keys()))

@app.route('/status', methods=['GET'])
def status():
    """
    A message indicating the API status.
    """

    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
  The username to retrieve.
    """

    user = users.get(username)
    if user:
        return jsonify(user)
    return "User not found", 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Accepts JSON data with user details and adds it to the users dictionary.
    """

    user_data = request.json
    username = user_data['username']
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data})

if __name__ == '__main__':
    app.run(debug=True)
