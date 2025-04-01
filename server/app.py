from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # מאפשר ל-React (בדפדפן) לגשת ל-API (Cross-Origin Resource Sharing)

@app.route('/')
def home():
    return "Hello from the Python Server!"

@app.route('/api/data', methods=['GET'])
def get_data():
    # דוגמה פשוטה - מחזירים אובייקט JSON
    return jsonify({"message": "Hello from the server"})

if __name__ == '__main__':
    # מריצים על פורט 5000 לדוגמה
    app.run(debug=True, port=5000)
