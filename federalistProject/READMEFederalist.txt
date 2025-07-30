
Federalist Papers Analysis
==========================================
Author: Tushar Koushik

This project investigates the disputed authorship of several Federalist Papers using machine learning techniques. Drawing inspiration from Jockers and Witten’s 2010 study, we explore both unsupervised and supervised methods to analyze word usage patterns and generate evidence-based claims about paper authorship.
Files Included

--------------
- Federalist_Notebook.ipynb — the main notebook showing the workflow, analysis, and results.
- lexos_1gram_inALL_prop.csv — normalized 1-gram feature set, exported from Lexos.
- lexos_2gram_prop.csv — normalized 2-gram feature set, exported from Lexos.

How to Use  
----------
1. Open the 'Federalist_Notebook.ipynb' file using Jupyter Notebook (via Anaconda or VSCode).
2. Run each cell from top to bottom to reproduce the full analysis.
3. Make sure 'lexos_1gram_inALL_prop.csv' and `lexos_2gram_prop.csv` are in the same directory.
4. The notebook will:
   - Load the datasets
   - Clean and preprocess the data
   - Apply KMeans for clustering
   - Train and evaluate classification models (Logistic Regression, Random Forest)
   - Display performance metrics and predictions for the disputed papers

No additional libraries are needed beyond the standard Python stack (pandas, scikit-learn, matplotlib, seaborn).


Summary
-------
The goal of this project is to apply text mining and classification techniques to help identify the likely authors of the Disputed Papers, building on historical and statistical precedent. The notebook walks through:
- Data preparation using Lexos output
- Exploratory data analysis
- Clustering (unsupervised learning) to detect natural groupings
- Classification (supervised learning) to make author predictions
- A comparison of 1-gram vs. 2-gram performance

Methods
-------
- Data Source: We used 1-gram and 2-gram datasets generated in Lexos, which provide normalized word frequencies for each paper.
- Cleaning: We handled missing values and removed outliers by filtering rare or overly dominant tokens that could skew analysis.
- Clustering: KMeans clustering was used to explore natural groupings among the papers and identify stylistic similarities.
- Classification: Alongside Logistic Regression and Random Forest, we explored basic Decision Trees for their simplicity and interpretability. While they offered clear if-then rules, they were outperformed by the ensemble-based Random Forest model in accuracy and generalization.

Results Overview
----------------
- Clustering: Provided visual groupings that supported authorship theories but lacked definitive clarity.
  Classification:
    - Logistic Regression with 2-grams achieved high accuracy and offered strong evidence that the disputed papers resemble Madison’s style.
    - Random Forests supported these findings, offering interpretability via feature importance.

Results are compared to Jockers and Witten’s conclusions, and their 2010 paper is cited in the notebook.

References
----------
- Jockers, M.L., & Witten, D.M. (2010). A Comparative Study of Machine Learning Methods for Authorship Attribution. Literary and Linguistic Computing, 25(2), 215–223 (for data).
- Kleinman, S., LeBlanc, M.D., Drout, M., & Zhang, C. (2019). Lexos v3.2.0. https://github.com/WheatonCS/Lexos
- Wikipedia contributors. (2011). The Federalist Papers. Wikipedia. https://en.wikipedia.org/wiki/Federalist_Papers
- OpenAI. ChatGPT (o3-mini-high), Mar. 2024, https://chat.openai.com/.
