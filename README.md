# 🌾 Crop Recommendation System

A **Machine Learning** based web application that recommends the **best suitable crop** to grow according to soil nutrients and climatic conditions.

This project uses a trained **scikit-learn** model to predict crops like Rice, Maize, Wheat, Cotton, Coconut, and many more.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)

---

## ✨ Features

- User-friendly web interface to input soil and weather parameters
- Real-time crop prediction using a pre-trained model
- Clean and responsive design with HTML templates
- Uses **Random Forest** (or similar) model saved as `model.pkl`
- Includes data preprocessing pipeline (`preprocessor.pkl`)

---

## 🛠️ Technologies Used

- **Backend**: Python + Flask
- **Machine Learning**: scikit-learn
- **Frontend**: HTML, CSS (static folder), Jinja2 templates
- **Model**: Pickle files (`model.pkl`, `preprocessor.pkl`)
- **Dataset**: Crop Recommendation Dataset

---

## 📁 Project Structure


---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/BhavnikSolanki/Crop_Recommendation_System.git
cd Crop_Recommendation_System
```

### 2. Create and activate Virtual environment (Recommended)
```
python -m venv venv
```
# Windows
```
venv\Scripts\activate
```

# Mac/Linux
```
source venv/bin/activate
```
#
## 3. Install required packages
```
pip install -r requirements.txt
```
###4. Run the application
```
python app.py
```
Open your browser and go to: http://127.0.0.1:5000/ (or the port shown in terminal)

📊 Dataset
The project uses the standard Crop Recommendation Dataset containing:

N, P, K values
Temperature, Humidity, pH, Rainfall
22 different crop labels

Dataset is located inside the crop_recommendation_dataset/ folder.

🤝 How to Use

Run the app using python app.py
Fill in the 7 parameters (Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall)
Click Predict to get the recommended crop


📄 Contributing
Feel free to contribute by:

Improving the UI/UX
Adding more models (XGBoost, Deep Learning, etc.)
Adding feature importance visualization
Deploying to Heroku / Render / Railway


📝 Note

There is an old file named redme.txt — you can safely delete it after using this README.md.
This project is built with Flask (not Streamlit).


Made with 💚 for Farmers & Agritech Enthusiasts
