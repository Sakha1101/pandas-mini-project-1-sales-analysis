# 📊 Sales Data Cleaning & Analysis (Pandas)

## 📌 Objective
Clean messy sales data and analyze revenue performance by region.

---

## 🛠️ Work Done

**Data Cleaning**
- Removed missing values from critical fields (Order, Product, Sales, Quantity, Date)
- Standardized text (Region, Product, Customer)
- Fixed data types (numeric & datetime)

**Feature Engineering**
- Created `Revenue_After_Discount`
- Extracted `Order_Month` and `Order_Year`

**Analysis**
- Calculated revenue by region
- Identified top 3 revenue regions

---

## 📊 Key Insight
- Region-level revenue trends are reliable  
- Product-level insights may be biased  

---

## ⚠️ Data Note (Important)
- ~85% of records were removed due to missing critical fields  
- Remaining ~15% data was used for analysis  

### Why analysis is still valid:
- Region distribution before and after cleaning remained similar  
- Sales statistics (mean, median, spread) remained consistent  
- This indicates the cleaned data still represents overall trends  

👉 Therefore:
- Region-based insights are **reliable**  
- Product-level insights should be used **with caution**

---

## 🧰 Tools
Python, Pandas

---

## 📁 Files
- `sales_analysis.py`
- `sales_mini_project_1.csv`
