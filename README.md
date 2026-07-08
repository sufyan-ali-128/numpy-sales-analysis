# 📊 NumPy Sales Data Analysis

A beginner data science project that analyzes 12 months of sales data using **NumPy** — covering statistics, boolean indexing, and business insights like quarterly performance and month-to-month growth.

## 🎯 Project Overview

This project takes a year's worth of sales data and answers real business questions:
- What are the total, average, highest, and lowest monthly sales?
- Which months performed above/below average?
- Which quarter had the best performance?
- What is the month-to-month growth trend?

## 🔧 Features / Analysis Performed

- Total & average yearly/monthly sales
- Highest and lowest sales (with corresponding month)
- Median and standard deviation of sales
- Boolean filtering (months above average, above 2000, below 1800)
- Quarter-wise sales breakdown using `reshape()` and `axis`
- Percentage contribution of each quarter
- Month-to-month growth percentage (vectorized calculation)

## 🧠 NumPy Concepts Used

| Concept | Used For |
|---|---|
| `np.sum()`, `np.mean()`, `np.median()`, `np.std()` | Core statistics |
| `np.max()`, `np.min()`, `np.argmax()`, `np.argmin()` | Finding best/worst performers |
| Boolean indexing | Filtering months by condition |
| `np.sort()` | Sorting sales data |
| `.reshape()` + `axis` parameter | Quarterly grouping and analysis |
| Array slicing (`[:-1]`, `[1:]`) | Vectorized month-to-month growth |

## 🖥️ Sample Output
```
Total yearly sales:  25800
Average monthly sales:  2150.0
Highest monthly sales:  3200
Month with highest sales:  December
Quarter with highest sales?:  Q4
Q1 contribution: 17.05%
```

## ▶️ How to Run
1. Make sure you have Python and NumPy installed:
    --> pip install numpy
3. Run the script:
    --> python Sales_Data_Analysis.py


## 📚 What I Learned

This project helped me understand how NumPy's vectorized operations (like slicing for growth calculation) are much faster and cleaner than using loops — and how `axis` parameter works for row-wise vs column-wise operations on multi-dimensional arrays.

## 👤 Author

**Sufyan Ali**  
BSCS Student | Aspiring Data Scientist  
[LinkedIn] --> www.linkedin.com/in/sufyanalidatascience

