# 📩 SMS Spam Classifier (Flask Backend)

This project is a **machine learning-based SMS spam detection system** built with **Flask**.  
It classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) and machine learning.

---

## 🚀 Features
- Preprocessing with **NLTK**: tokenization, stopword removal, stemming.
- Tried and tested multiple ML algorithms for performance comparison.
- Final model: **Multinomial Naive Bayes** (97% accuracy, 1.0 precision).
- REST API powered by **Flask**.
- JSON-based predictions for easy frontend/mobile integration.
- Postman support for testing.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Flask**
- **scikit-learn**
- **NLTK**
- **pandas**, **numpy**

---

## 📊 Model Performance

We trained and tested multiple algorithms. Below are the results:

| Algorithm                       | Accuracy   | Precision (Spam) |
| ------------------------------- | ---------- | ---------------- |
| **Naive Bayes (NB)**            | **0.9768** | **1.0000** ✅     |
| Support Vector Classifier (SVC) | 0.9758     | 0.9669           |
| Extra Trees Classifier (ETC)    | 0.9758     | 0.9669           |
| Random Forest (RF)              | 0.9729     | 0.9583           |
| Logistic Regression (LR)        | 0.9565     | 0.9604           |
| Bagging Classifier (BgC)        | 0.9555     | 0.8485           |
| Gradient Boosting (GBDT)        | 0.9507     | 0.9307           |
| Decision Tree (DT)              | 0.9333     | 0.8286           |
| AdaBoost                        | 0.9226     | 0.8372           |
| K-Nearest Neighbors (KN)        | 0.9081     | 1.0000           |


✅ **Chosen Model:** Multinomial Naive Bayes (best precision & accuracy balance).






---

## 📂 Project Structure
