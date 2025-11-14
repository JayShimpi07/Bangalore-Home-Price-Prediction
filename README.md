🏡 Bangalore Home Price Prediction

A complete Machine Learning + Flask backend + HTML/CSS/JS frontend + NGINX reverse proxy project that predicts home prices in Bangalore based on location, square feet, BHK, and bathrooms.

🔥 Features

✔ Predict house prices with ML model

✔ User-friendly web UI (HTML/CSS/JS)

✔ Flask backend API

✔ Uses NGINX reverse proxy (localhost) to load the project directly

✔ Ajax request to Flask API

✔ Model trained using real-world Bengaluru house price dataset

📦 Project Structure
BHP/
├── client/
│   ├── index.html       # Frontend UI
│   ├── styles.css       # Styling
│   └── app.js           # Calls backend API
│
├── server/
│   ├── server.py        # Flask backend server
│   ├── util.py          # ML model + prediction code
│   └── artifacts/
│       ├── columns.json
│       └── banglore_home_price_model.pickle
│
├── nginx/
│   └── nginx.conf       # (Configured reverse proxy)
│
├── README.md
└── requirements.txt

🚀 Getting Started
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Start the Flask Server
cd server
python server.py


Flask backend will run at:

http://127.0.0.1:5000

🌐 Running the Frontend with NGINX (Windows)

You configured Nginx so that visiting:

http://localhost/

automatically loads your frontend and proxies API requests to Flask.

✔ Your NGINX root serves the frontend:
location / {
    root   "D:\BHP\client";
    index  index.html index.htm app.html;
}

✔ API calls forwarded to Flask:
location /api/ {
    rewrite ^/api(.*) $1 break;
    proxy_pass http://127.0.0.1:5000;
}


This means:

Frontend URL
http://localhost/

API URLs

Frontend JS calls:

/api/get_location_names
/api/predict_home_price


NGINX forwards these to Flask.

3️⃣ Start NGINX

Open Command Prompt as administrator:

cd C:\nginx
nginx.exe


Restart Nginx after changes:

nginx.exe -s reload


Stop Nginx:

nginx.exe -s stop

📡 API Documentation
✔ Get All Locations
GET http://localhost/api/get_location_names


Response:

{
  "locations": ["1st Phase JP Nagar", "Whitefield", ...]
}

✔ Predict Home Price
POST http://localhost/api/predict_home_price


form-data payload:

Key	Value Example
total_sqft	1000
location	1st Phase JP Nagar
bhk	2
bath	2

Response:

{
  "estimated_price": 82.81
}

🧠 Machine Learning Model
✔ Steps performed

Data cleaning

Outlier removal

One-hot encoding for location

Linear Regression training

Pickle saved in /server/artifacts/

✔ Model files

columns.json → One-hot encoded columns

banglore_home_price_model.pickle → Trained model

🖼️ Screenshots

![alt text](image.png)

❗ Important Notes for NGINX Setup
✔ All frontend files must be inside:
D:\BHP\client

✔ Flask MUST run before NGINX forwards API calls

Start Flask:

python server.py


Then start NGINX:

nginx.exe

✔ If port is busy

Change Flask port:

app.run(port=5001)


Change NGINX accordingly:

proxy_pass http://127.0.0.1:5001;

🚀 Deployment (future scope)
You can deploy:

Frontend → GitHub Pages

Backend → Render.com / Railway.app

🧬 Requirements File

Add this as requirements.txt:

flask
flask-cors
numpy
pandas
scikit-learn

👨‍💻 Author

Jay Shimpi
GitHub: https://github.com/JayShimpi07