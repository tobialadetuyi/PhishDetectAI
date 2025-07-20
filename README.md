# 🛡️ PhishDetectAII
# By Oluwatobi Aladetuyi - CyberAegis
PhishDetectAI is an AI-powered phishing detection system designed to analyze and classify email and message content for potential phishing threats. Ideal for businesses, cybersecurity researchers, and anti-fraud teams.



## 🚀 Features

- 🧠 NLP-powered phishing message classification
- 🔍 Detects suspicious phrases, patterns, and links
- 🔐 API-ready for integration into web or enterprise platforms
- 🧪 Tested on real phishing datasets
- 📊 Supports JSON output for automation pipelines
- Detects phishing emails (spam vs not spam)
- Trained using a Logistic Regression model
- Integrated with GitHub Actions for CI testing


## 📦 Tech Stack

| Layer        | Tools / Libraries                  |
|--------------|------------------------------------|
| Language     | Python 3.x                         |
| ML/NLP       | Scikit-learn, NLTK / SpaCy         |
| Backend API  | Flask or FastAPI                   |
| DevOps       | GitHub Actions                     |
| Deployment   | Docker, Heroku / Render (Optional) |

---

## 📁 Project Structure

```bash
PhishDetectAI/
├── app/                      # Flask/FastAPI app
│   ├── routes.py
│   ├── model.py
│   └── utils.py
├── data/                     # Datasets and samples
├── models/                   # Trained model files
├── tests/                    # Unit tests
├── .github/workflows/        # CI/CD configurations
├── requirements.txt
├── README.md
└── main.py

## How to Use

1. Place your dataset in `data/emails.csv`
2. Run the training script:

```bash
python notebook/training.py

pandas
scikit-learn
joblib
pytest
flake8
