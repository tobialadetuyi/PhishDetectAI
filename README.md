# 🛡️ PhishDetectAI

**By Oluwatobi Aladetuyi - CyberAegis**

PhishDetectAI is an AI-powered phishing detection system designed to analyze and classify email and message content for potential phishing threats. Ideal for businesses, cybersecurity researchers, and individuals who want to protect themselves against phishing attacks.

## 🚀 Features

- 🧠 **NLP-powered classification** - Uses Logistic Regression + TF-IDF vectorization
- 📝 **Text preprocessing** - Automatically removes stopwords, lemmatizes text, handles encoding
- 📊 **Confidence scores** - Get probability estimates for each prediction (0-100%)
- 🔐 **API-ready** - Easily integrate into web or enterprise platforms
- 🧪 **Comprehensive testing** - Unit tests for model, predictions, and input validation
- ✅ **Production-ready** - Error handling, logging, input validation, model integrity checks
- 📈 **Detailed metrics** - Accuracy, precision, recall, F1-score, confusion matrix
- 🐳 **Docker-ready** - Easy deployment with containerization
- 🚀 **CI/CD integrated** - GitHub Actions for automated testing and linting

## 📦 Tech Stack

| Layer        | Tools / Libraries                           |
|--------------|---------------------------------------------|
| Language     | Python 3.10+                                |
| UI Framework | Streamlit                                   |
| ML/NLP       | Scikit-learn, NLTK                          |
| Data         | Pandas, NumPy                               |
| Testing      | Pytest                                      |
| Linting      | Flake8                                      |
| DevOps       | GitHub Actions                              |
| Deployment   | Docker, Streamlit Cloud, Heroku, Render    |

## 📁 Project Structure

```
PhishDetectAI/
├── app/
│   └── app.py                 # Streamlit web application
├── notebook/
│   └── training.py            # ML model training pipeline
├── model/
│   ├── phishing_classifier.pkl         # Trained model (pickled)
│   ├── phishing_classifier.md5         # Model integrity checksum
│   └── training_metrics.json           # Training metrics & performance
├── data/
│   └── emails.csv             # Training dataset (1000+ samples)
├── tests/
│   ├── test_sanity.py         # Basic sanity tests
│   ├── test_model.py          # Model training & inference tests
│   └── test_app.py            # App input validation & prediction tests
├── .github/workflows/
│   └── ci.yml                 # GitHub Actions CI/CD pipeline
├── requirements.txt           # Python dependencies (pinned versions)
├── .gitignore
└── README.md
```

**How it fits together:** On push/PR to main, GitHub Actions runs flake8 linting and pytest. The training pipeline loads `data/emails.csv`, preprocesses text (lowercasing, stopword removal, lemmatization), trains a Logistic Regression model with TF-IDF vectorization, and saves it as `model/phishing_classifier.pkl`. The Streamlit app loads that pre-trained model, accepts user input, validates it, makes predictions with confidence scores, and displays results to the user.

## 🚀 How to run it

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tobialadetuyi/PhishDetectAI.git
   cd PhishDetectAI
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Train the Model

To train the model on the dataset:

```bash
python notebook/training.py
```

**Output:**
- Trained model saved to `model/phishing_classifier.pkl`
- Model checksum saved to `model/phishing_classifier.md5`
- Training metrics saved to `model/training_metrics.json`

### Run the Streamlit App

To start the web interface:

```bash
streamlit run app/app.py
```

The app will open in your default browser at `http://localhost:8501`

### Run Tests

Execute the full test suite:

```bash
pytest tests/ -v
```

Run specific test file:

```bash
pytest tests/test_model.py -v
pytest tests/test_app.py -v
```

### Run Linting

Check code style with flake8:

```bash
flake8 . --max-line-length=100
```

## 📊 Model Performance

After training, check `model/training_metrics.json` for:
- **Accuracy** - Overall correctness
- **Precision** - False positive rate
- **Recall** - False negative rate (important for security)
- **F1-Score** - Harmonic mean of precision and recall
- **Confusion Matrix** - Breakdown of correct/incorrect predictions
- **Cross-Validation Scores** - Model stability across different data splits

## 🔐 Security Features

✅ **Input Validation**
- Maximum input length enforcement (5000 characters)
- UTF-8 encoding validation
- Empty input detection

✅ **Model Security**
- MD5 checksum verification for model integrity
- Pickle validation to prevent tampering
- Structured error handling

✅ **Code Quality**
- Automated linting with flake8
- Comprehensive unit tests
- Type hints for better maintainability

## 📈 Expanding the Dataset

For production use, consider these sources:

1. **SpamAssassin Corpus** - https://spamassassin.apache.org/publiccorpus/
2. **UCI ML Repository** - https://archive.ics.uci.edu/dataset/327
3. **Kaggle Datasets:**
   - [Phishing Email Dataset](https://www.kaggle.com/datasets/subhajournal/phishingemails)
   - [Spam Classification](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
4. **ENRON Email Dataset** - https://www.cs.cmu.edu/~enron/

## 🐳 Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:

```bash
docker build -t phishdetectai .
docker run -p 8501:8501 phishdetectai
```

## 📝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Disclaimer

This tool is provided for educational and security research purposes. While it aims to detect phishing messages, it is **not 100% accurate**. Always verify suspicious messages independently and follow best security practices:

- Never click links or download attachments from untrusted sources
- Always verify sender information
- Use multi-factor authentication
- Keep software updated
- Report phishing to your email provider

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Oluwatobi Aladetuyi**
- GitHub: [@tobialadetuyi](https://github.com/tobialadetuyi)
- Organization: CyberAegis

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the test suite for usage examples

---

**Made with ❤️ for cybersecurity enthusiasts**
