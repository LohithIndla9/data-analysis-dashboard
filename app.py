import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Professional Data Dashboard", layout="wide")
st.title("Professional Data Analysis Dashboard")

# -----------------------------
# CACHE DATA
# -----------------------------
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# -----------------------------
# FILE UPLOAD
# -----------------------------
file = st.file_uploader("Upload CSV File", type=["csv"])

if file is not None:

    df = load_data(file)

    # Reduce size for speed
    if len(df) > 2000:
        df = df.sample(2000)

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object"]).columns.tolist()

    # -----------------------------
    # KPI
    # -----------------------------
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Missing", df.isnull().sum().sum())
    c4.metric("Duplicates", df.duplicated().sum())

    st.divider()

    # -----------------------------
    # TABS
    # -----------------------------
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Overview", "Data Analysis", "Insights", "Advanced Analysis"]
    )

    # =============================
    # OVERVIEW
    # =============================
    with tab1:

        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        st.subheader("Summary")
        st.dataframe(df.describe())

        if len(numeric_cols) > 1:
            st.subheader("Correlation Heatmap")
            fig = px.imshow(df[numeric_cols].corr(), text_auto=True)
            st.plotly_chart(fig)

    # =============================
    # DATA ANALYSIS
    # =============================
    with tab2:

        if len(numeric_cols) > 0:
            col = st.selectbox("Histogram Column", numeric_cols, key="hist")
            st.plotly_chart(px.histogram(df, x=col))

            col = st.selectbox("Box Column", numeric_cols, key="box")
            st.plotly_chart(px.box(df, y=col))

        if len(numeric_cols) > 1:
            x = st.selectbox("Scatter X", numeric_cols, key="sx")
            y = st.selectbox("Scatter Y", numeric_cols, key="sy")
            st.plotly_chart(px.scatter(df, x=x, y=y))

        if len(cat_cols) > 0:
            col = st.selectbox("Category Column", cat_cols, key="cat")
            counts = df[col].value_counts().reset_index()
            counts.columns = [col, "Count"]
            st.plotly_chart(px.bar(counts, x=col, y="Count"))

    # =============================
    # INSIGHTS
    # =============================
    with tab3:

        st.subheader("Insights")

        if df.isnull().sum().sum() > 0:
            st.write("• Missing values present")

        if df.duplicated().sum() > 0:
            st.write("• Duplicate rows found")

        if len(numeric_cols) > 1:
            corr = df[numeric_cols].corr()
            if (corr.abs() > 0.8).sum().sum() > len(numeric_cols):
                st.write("• High correlation detected")

    # =============================
    # ADVANCED ANALYSIS
    # =============================
    with tab4:

        st.subheader("Advanced Analysis")

        # ---------- ANOVA ----------
        if len(cat_cols) > 0 and len(numeric_cols) > 0:

            st.markdown("### ANOVA")

            cat = st.selectbox("Category", cat_cols, key="anova_cat")
            num = st.selectbox("Numeric", numeric_cols, key="anova_num")

            if st.button("Run ANOVA"):
                from scipy.stats import f_oneway

                groups = [df[df[cat] == c][num].dropna() for c in df[cat].unique()]

                if len(groups) > 1:
                    f, p = f_oneway(*groups)
                    st.write("F:", f)
                    st.write("P:", p)
                else:
                    st.warning("Not enough groups")

        else:
            st.warning("ANOVA needs categorical + numeric column")

        # ---------- ANCOVA ----------
        if len(cat_cols) > 0 and len(numeric_cols) > 1:

            st.markdown("### ANCOVA")

            cat = st.selectbox("Category", cat_cols, key="anc_cat")
            num = st.selectbox("Dependent", numeric_cols, key="anc_num")
            cov = st.selectbox("Covariate", numeric_cols, key="anc_cov")

            if st.button("Run ANCOVA"):
                try:
                    import statsmodels.api as sm
                    from statsmodels.formula.api import ols

                    model = ols(f'{num} ~ C({cat}) + {cov}', data=df).fit()
                    st.write(sm.stats.anova_lm(model, typ=2))

                except:
                    st.warning("ANCOVA failed")

        else:
            st.warning("ANCOVA needs 1 categorical + 2 numeric columns")

        # ---------- KMEANS ----------
        if len(numeric_cols) > 1:

            st.markdown("### KMeans")

            k = st.slider("Clusters", 2, 10, 3, key="kmeans_k")

            if st.button("Run KMeans"):

                from sklearn.cluster import KMeans
                from sklearn.preprocessing import StandardScaler

                X = df[numeric_cols].dropna()

                if len(X) > 0:
                    X_scaled = StandardScaler().fit_transform(X)

                    km = KMeans(n_clusters=k, random_state=42)
                    X["Cluster"] = km.fit_predict(X_scaled)

                    st.dataframe(X.head())
                    st.plotly_chart(px.scatter(X, x=numeric_cols[0], y=numeric_cols[1], color="Cluster"))
                else:
                    st.warning("No valid numeric data")

        else:
            st.warning("KMeans needs numeric columns")

        # ---------- LOGISTIC ----------
        if len(df.columns) > 1:

            st.markdown("### Logistic Regression")

            target = st.selectbox("Target (Binary)", df.columns, key="log_target")

            if st.button("Run Logistic"):

                if df[target].nunique() == 2:

                    from sklearn.linear_model import LogisticRegression
                    from sklearn.model_selection import train_test_split
                    from sklearn.metrics import accuracy_score

                    X = df[numeric_cols].drop(columns=[target], errors='ignore').dropna()
                    y = df[target].loc[X.index]

                    if len(X) > 0:
                        try:
                            X_train, X_test, y_train, y_test = train_test_split(X, y)

                            model = LogisticRegression()
                            model.fit(X_train, y_train)

                            acc = accuracy_score(y_test, model.predict(X_test))
                            st.success(f"Accuracy: {acc}")

                        except:
                            st.warning("Model error")
                    else:
                        st.warning("No valid data")

                else:
                    st.warning("Target must be binary")