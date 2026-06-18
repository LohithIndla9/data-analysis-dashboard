# 📊 Professional Data Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An interactive, no-code dashboard for exploring and analyzing any CSV dataset — built with **Streamlit**, **Plotly**, and **scikit-learn**. Upload a file and instantly get KPIs, visualizations, automated insights, and advanced statistical models.

---

## ✨ Features

| Tab | What it does |
|---|---|
| **Overview** | Dataset preview, summary statistics, and a correlation heatmap |
| **Data Analysis** | Histograms, box plots, scatter plots, and category bar charts |
| **Insights** | Automated flags for missing values, duplicates, and high correlation |
| **Advanced Analysis** | ANOVA, ANCOVA, K-Means clustering, and Logistic Regression |

At the top of every dashboard, four live KPI cards show **row count**, **column count**, **missing values**, and **duplicate rows** the moment a file is uploaded.

---

## 🖥️ Preview

Upload a CSV → the app automatically detects numeric and categorical columns and tailors every chart and statistical tool to your data, no configuration needed.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# 2. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`) and upload a CSV to get started.

---

## 📁 Project Structure

```
.
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore           # Files excluded from version control
├── LICENSE             # MIT License
└── README.md           # Project documentation
```

---

## 🧠 Advanced Analysis Details

- **ANOVA** — tests whether a numeric variable differs significantly across categories
- **ANCOVA** — like ANOVA, but adjusts for a continuous covariate
- **K-Means Clustering** — groups rows into clusters based on numeric features (adjustable cluster count)
- **Logistic Regression** — trains a binary classifier and reports test accuracy

> 💡 Datasets larger than 2,000 rows are automatically sampled down for performance.

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — app framework
- [Pandas](https://pandas.pydata.org/) — data manipulation
- [Plotly](https://plotly.com/python/) — interactive charts
- [SciPy](https://scipy.org/) & [statsmodels](https://www.statsmodels.org/) — statistical tests
- [scikit-learn](https://scikit-learn.org/) — machine learning models

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue first to discuss what you'd like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## ⭐ Show Your Support

If this project helped you, consider giving it a star — it helps others find it too!
