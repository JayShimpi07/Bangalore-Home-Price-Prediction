from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)   # allow cross-origin for frontend

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    locations = util.get_location_names()
    response = jsonify({
        "locations": locations
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form.get('total_sqft'))
        location = request.form.get('location')
        bhk = int(request.form.get('bhk'))
        bath = int(request.form.get('bath'))
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    estimated_price = util.get_estimated_price(location, total_sqft, bath, bhk)

    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(port=5000)
