# 🛡️ Network Intrusion Detection System using Machine Learning  

![Python](https://img.shields.io/badge/Python-3.8-blue.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  
![ML](https://img.shields.io/badge/Machine%20Learning-Intrusion%20Detection-orange.svg)  

## 📌 Project Overview  
This project implements a **Network Intrusion Detection System (NIDS)** using machine learning algorithms to detect malicious activities within computer networks.  
It analyzes network traffic data and classifies it as **Normal** or **Anomalous**, thereby helping administrators detect unauthorized access, exploits, and cyberattacks.  

---

## 🚀 Features  
- Detects abnormal behaviors in computer networks  
- Real-time monitoring and classification of network traffic  
- Supports multiple ML classifiers:
  - Decision Tree Classifier (DTC)  
  - K-Nearest Neighbor (KNN)  
  - Bernoulli Naive Bayes (BNB)  
- Uses **NSL-KDD dataset** for training & testing  
- Accuracy & misclassification comparison graphs  
- GUI for user-friendly interaction  

---

## 🏗️ System Architecture  
```
Network Packets → Feature Extractor → Feature Selector → Classifier → Alerts
```

---

## 🎯 Objectives  
- Detect abnormal activities in a computer/network  
- Dynamically monitor real-time events  
- Prevent unauthorized access & privilege escalation  
- Reduce false alarms and improve accuracy  

---

## 📊 Dataset  
We used the **NSL-KDD dataset**, which contains four categories of attacks:  
- **DoS (Denial of Service)** – Overloading system resources  
- **U2R (User to Root)** – Privilege escalation  
- **R2L (Remote to Local)** – Unauthorized remote access  
- **Probing** – Network scanning & vulnerability detection  

📥 Download dataset: [NSL-KDD Dataset](https://www.unb.ca/cic/datasets/nsl.html)  

---

## ⚙️ Tech Stack  
**Languages & Tools:**  
- Python 3.8.3 (ML & Data Processing)  
- Java 8, HTML, CSS, JS (Frontend/GUI support)  

**Libraries:**  
- scikit-learn  
- pandas, numpy  
- matplotlib  
- tkinter / web GUI (optional)  

**Hardware Requirements:**  
- RAM: 4GB+  
- Processor: Intel Core i3+  

---

## 🔑 Installation & Usage  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/thapaswin125/network-ids-ml.git
cd network-ids-ml
```

### 2️⃣ Create and activate virtual environment (optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Download and place dataset  
- Download **NSL-KDD dataset** from [here](https://www.unb.ca/cic/datasets/nsl.html)  
- Place `Train.csv` and `Test.csv` inside the `dataset/` folder  

### 5️⃣ Run the model training script  
```bash
python train_model.py
```

### 6️⃣ Run the GUI / main program  
```bash
python app.py
```

---

## 🔑 Implementation Details  
### Preprocessing  
- Scaling (Standardization)  
- Label Encoding  
- Feature Selection (Random Forest, RFE)  

### Model Training Example  
```python
# K-Nearest Neighbor
KNN_Classifier = KNeighborsClassifier(n_jobs=-1)
KNN_Classifier.fit(X_train, Y_train)

# Bernoulli Naive Bayes
BNB_Classifier = BernoulliNB()
BNB_Classifier.fit(X_train, Y_train)

# Decision Tree
DTC_Classifier = tree.DecisionTreeClassifier(criterion='entropy', random_state=0)
DTC_Classifier.fit(X_train, Y_train)
```

### Prediction  
- Classifies incoming packets as **Normal** or **Anomaly**  

### Evaluation  
- Accuracy comparison between models  
- Confusion matrix & performance visualization  

---

## 📌 Future Scope  
- Extend detection to **HTTP-specific web server attacks**  
- Add **Denial of Service (DoS) detection**  
- Integrate **NIDS + HIDS** for hybrid anomaly detection  
- Improve accuracy using ensemble & deep learning techniques  

---

## 📷 Screenshots / Results  
(Add GUI screenshots, accuracy graphs, confusion matrices here)  

---

## ✅ Conclusion  
This IDS highlights how **machine learning techniques** can strengthen cybersecurity. While it does not completely prevent intrusions, it equips administrators with powerful tools to **detect, classify, and mitigate threats** efficiently.  

---

## 📜 License  
This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.  
