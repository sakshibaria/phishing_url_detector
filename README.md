# 🔐 Phishing URL Detector (ML)

Detect whether a URL is phishing or legitimate using ML + simple URL features.

## 🧠 Features Used
- URL Length
- Presence of HTTPS
- Use of IP in domain
- Presence of '@'
- Use of dash (-)
- Dot count
- Slash count

## 📁 Files
- `sampled_phishing_data.csv` – 10K URL dataset (balanced)
- `phishing_detector.py` – Train + test the model
- `app.py` – Streamlit app
- `utils.py` – Feature extraction logic

## 🚀 Run It
```bash
pip install pandas scikit-learn streamlit joblib
python phishing_detector.py
streamlit run app.py
