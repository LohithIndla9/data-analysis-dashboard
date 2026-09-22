
```markdown
# 📊 Professional Data Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.18%2B-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An interactive, no-code data science dashboard for exploring, profiling, and analyzing any CSV dataset — built with **Streamlit**, **Plotly**, **SciPy**, **statsmodels**, and **scikit-learn**. 

Upload any CSV file and instantly receive high-level KPIs, interactive distributions, automated data-quality insights, parametric hypothesis testing, and machine learning models — **with zero configuration required**.

---

## 🌟 Key Highlights

- **⚡ Zero-Config Dynamic Profiling:** Automatically detects and separates numeric (`int64`, `float64`) and categorical (`object`) columns.
- **🚀 In-Memory Caching:** Utilizes `@st.cache_data` to prevent costly re-reads on UI interaction.
- **📈 Responsive Plotly Visualizations:** Interactive D3-powered charts supporting zoom, pan, hover tooltips, and dynamic slicing.
- **🛡️ Smart Performance Downsampling:** Automatically downsamples datasets larger than 2,000 rows to ensure sub-second UI responsiveness.
- **🔬 Statistical Rigor:** Bridges exploratory data analysis with inferential statistics (ANOVA/ANCOVA) and machine learning (K-Means/Logistic Regression).

---

## 🏗️ Architecture & Data Flow

```text
[ Raw CSV Upload ]
        │
        ▼
[ Streamlit Cache: @st.cache_data ]
        │
        ▼
[ Smart Downsampling (> 2,000 rows -> 2,000 samples) ]
        │
        ▼
[ Dynamic Schema Partitioning ]
   ├── Numeric Columns (int64, float64)
   └── Categorical Columns (object)
        │
        ▼
[ Live Metric Cards Header ] ─── (Rows | Columns | Missing Cells | Duplicate Rows)
        │
        ├──► 1. Overview Tab ─────────► Preview, Summary Stats, Pearson Heatmap
        ├──► 2. Data Analysis Tab ────► Histograms, Box Plots, Scatter Plots, Bar Charts
        ├──► 3. Automated Insights ───► Missing Values, Duplicates, Multicollinearity (|r| > 0.8)
        └──► 4. Advanced Analysis ────► ANOVA, ANCOVA, Scaled K-Means, Logistic Classifier
```

---

## ✨ Features

| Tab | Feature | Description |
|---|---|---|
| **Header KPIs** | Live Metrics | Instant top-of-page view of **total rows**, **columns**, **missing values**, and **duplicate rows**. |
| **Overview** | Data Preview & Stats | View raw data (`df.head()`), 5-number descriptive statistics (`df.describe()`), and an interactive Pearson correlation heatmap. |
| **Data Analysis** | Exploratory Visuals | Univariate histograms & box plots (outlier detection), bivariate scatter plots, and categorical value frequency bar charts. |
| **Insights** | Automated Heuristics | Rule-based engine that flags missing data, duplicate entries, and severe feature multicollinearity ($|r| > 0.8$). |
| **Advanced Analysis** | Inferential Stats & ML | Parametric hypothesis tests (One-Way ANOVA & ANCOVA) and Machine Learning models (K-Means Clustering & Logistic Regression). |

---

## 🧠 Advanced Analysis Details

### 1. One-Way ANOVA (Analysis of Variance)
- **Purpose:** Tests whether the mean of a continuous numerical variable differs significantly across two or more discrete categories.
- **Mechanism:** Computes the $F$-statistic ($\frac{\text{Between-group variance}}{\text{Within-group variance}}$) and $p$-value using `scipy.stats.f_oneway`.
- **Hypothesis:** Rejects $H_0$ if $p < 0.05$, confirming statistically significant differences between group means.

### 2. ANCOVA (Analysis of Covariance)
- **Purpose:** Blends ANOVA and Ordinary Least Squares (OLS) regression to evaluate category differences **while controlling for a continuous covariate** (confounding factor).
- **Implementation:** Fits `ols('num ~ C(cat) + cov', data=df)` and generates a standard Type-II ANOVA table via `statsmodels`.

### 3. K-Means Clustering (Unsupervised ML)
- **Purpose:** Groups rows into $k$ distinct clusters based on feature similarity.
- **Preprocessing:** Standardizes features using `StandardScaler` to ensure Euclidean distance is not dominated by large-scale variables.
- **Interactive Control:** Includes a slider to adjust $k \in [2, 10]$ and visualizes cluster assignments across feature dimensions.

### 4. Logistic Regression (Supervised Classification)
- **Purpose:** Trains a binary classification model on a user-selected binary target.
- **Pipeline:** Extracts numeric features, synchronizes indices, splits data via `train_test_split`, trains `sklearn.linear_model.LogisticRegression`, and reports test set accuracy.

> 💡 **Performance Optimization:** Datasets larger than 2,000 rows are automatically sampled down to maintain smooth browser performance and eliminate charting latency.

---

## 🖥️ Preview & Usage Flow

1. **Upload:** Drop in any `.csv` file via the sidebar/uploader.
2. **Profile:** Immediately inspect the 4 live KPI metric cards at the top.
3. **Explore:** Navigate through the 4 tabs to view distributions, inspect correlation matrices, and review automated warnings.
4. **Model:** Head to the **Advanced Analysis** tab to run hypothesis tests or fit machine learning models with one click.

---

## 🚀 Getting Started

### Prerequisites
- **Python:** 3.9 or higher
- **Package Manager:** `pip`

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/reddysubhashboyalla-byte/data-analysis-dashboard.git
cd data-analysis-dashboard

# 2. (Recommended) Create a virtual environment
python -m venv venv

# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

After running the command, open the local URL shown in your terminal (typically `http://localhost:8501`) in your browser.

---

## 📁 Project Structure

```text
data-analysis-dashboard/
├── app.py              # Main application script with Streamlit UI & ML pipelines
├── requirements.txt    # Production dependencies (Streamlit, Pandas, Plotly, SciPy, statsmodels, scikit-learn)
├── .gitignore          # Excludes environments, caches, and build artifacts
├── LICENSE             # MIT Open-Source License
└── README.md           # Comprehensive project documentation
```

---

## 🛠️ Built With

- **[Streamlit](https://streamlit.io/)** — Reactive web application framework
- **[Pandas](https://pandas.pydata.org/)** — In-memory data manipulation & schema inspection
- **[Plotly Express](https://plotly.com/python/)** — D3-based interactive web visualizations
- **[SciPy](https://scipy.org/)** — Scientific computing and parametric statistical hypothesis testing
- **[statsmodels](https://www.statsmodels.org/)** — Econometric modeling, OLS, and Type-II ANOVA tables
- **[scikit-learn](https://scikit-learn.org/)** — Data preprocessing, K-Means clustering, and classification models

---

## 🔮 Future Roadmap

- [ ] **Dimensionality Reduction:** Add PCA (Principal Component Analysis) to project high-dimensional K-Means clusters onto 2D/3D plots.
- [ ] **Advanced Classification Metrics:** Add Confusion Matrix, Precision-Recall curves, F1-Score, and ROC-AUC for imbalanced datasets.
- [ ] **Interactive Imputation:** Allow users to choose missing value imputation strategies (Mean, Median, Mode, or KNN) directly from the UI.
- [ ] **Big Data Acceleration:** Integrate Polars / DuckDB for handling multi-gigabyte datasets without memory bottlenecks.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. **Fork** the project
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## ⭐ Show Your Support

If this project helped you or gave you insight into building data dashboards, please consider giving it a **Star** ⭐ — it helps the project reach more developers!
```
