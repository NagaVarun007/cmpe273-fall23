from flask import Flask, request, jsonify
from app.database import fetch_and_transform_data
from app.google_sheets import push_data_to_sheets

app = Flask(__name__)

@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    data = fetch_and_transform_data()
    return jsonify(data)

@app.route('/push_to_sheets', methods=['POST'])
def push_to_sheets():
    data = request.get_json()
    success = push_data_to_sheets(data)
    
    if success:
        return jsonify({"message": "Data pushed to Google Sheets successfully"})
    else:
        return jsonify({"error": "Failed to push data to Google Sheets"})

if __name__ == '__main__':
    app.run(debug=True)
