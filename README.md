# 🩺 Anemia Risk Prediction

This project predicts **anemia risk in women and children** using Machine Learning models and provides an **interactive dashboard** to analyze high-risk groups.  

---

## 📌 Project Overview
- Built a Machine Learning system to predict anemia risk using WHO prevalence data.  
- Trained and evaluated multiple models: Logistic Regression, Random Forest, SVM, Gradient Boosting, LightGBM, and ANN.  
- **Artificial Neural Network (ANN)** achieved the highest accuracy (**98.4%**).  
- Developed a **Streamlit dashboard** for real-time risk prediction across groups:
  - Reproductive-age women  
  - Non-pregnant women  
  - Children  

---

## 🚀 Features
- Data preprocessing, cleaning, and merging WHO datasets.  
- ML model training and evaluation with accuracy, F1 score, and feature analysis.  
- Interactive dashboard for user inputs and real-time predictions.  
- Group-level anemia risk detection (per category and overall).  

---

## 🛠️ Tech Stack
- **Python** (pandas, NumPy, matplotlib, seaborn, scikit-learn, LightGBM, TensorFlow/Keras)  
- **Streamlit** (for dashboard deployment)  
- **Joblib** (for model saving/loading)  

---

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Arushi0301/Anemia-Risk-Prediction.git
   cd Anemia-Risk-Prediction

2.Install dependencies:
  ```bash
pip install -r requirements.txt
```

3.Run the Streamlit app:
  ```bash
streamlit run app.py
```

4.Open in your browser:
```
http://localhost:8501
```
