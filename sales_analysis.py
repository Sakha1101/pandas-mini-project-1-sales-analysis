import pandas as pd


# =========================================================
# MINI PROJECT 1: SALES DATA CLEANING & ANALYSIS
# Objective:
# Clean messy sales data and analyze revenue by region
# =========================================================


# ---------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------
df = pd.read_csv("sales_mini_project_1.csv")


# ---------------------------------------------------------
# 2. INITIAL DATA AUDIT (Optional checks)
# Uncomment these lines if you want to inspect raw data
# ---------------------------------------------------------
# print("First 5 rows:\n", df.head())
# print("\nShape of dataset:", df.shape)
# print("\nColumn names:", list(df.columns))
# print("\nMissing values count:\n", df.isnull().sum())
# print("\nMissing values percentage:\n", round(df.isnull().sum() / len(df) * 100, 2))
# print("\nDuplicate row count:", df.duplicated().sum())
# print("\nDuplicate rows:\n", df[df.duplicated(keep=False)])


# ---------------------------------------------------------
# 3. CLEAN TEXT COLUMNS
# Standardize text format:
# - Remove leading/trailing spaces
# - Convert text to title case
# ---------------------------------------------------------
df["Customer_Name"] = df["Customer_Name"].str.strip().str.title()
df["Region"] = df["Region"].str.strip().str.title()
df["Product"] = df["Product"].str.strip().str.title()


# ---------------------------------------------------------
# 4. FIX DATA TYPES
# Convert columns to proper numeric/date formats
# errors='coerce' will convert invalid values to NaN / NaT
# ---------------------------------------------------------
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce",
    format="mixed",
    dayfirst=True
)


# ---------------------------------------------------------
# 5. HANDLE MISSING VALUES
# Keep only rows where critical business fields are present
# Critical fields:
# - Order_ID
# - Product
# - Sales
# - Quantity
# - Order_Date
#
# Discount is filled with 0 assuming no discount if blank
# ---------------------------------------------------------
df_clean = df.copy()

df_clean = df_clean.dropna(
    subset=["Order_ID", "Product", "Sales", "Quantity", "Order_Date"]
)

df_clean["Discount"] = df_clean["Discount"].fillna(0)


# ---------------------------------------------------------
# 6. DATA RELIABILITY CHECK (Optional analysis)
# Used to compare dataset before and after cleaning
# Helps justify if cleaned dataset is still representative
# ---------------------------------------------------------
# print("Before Cleaning - Region Distribution:\n", df["Region"].value_counts(normalize=True))
# print("\nAfter Cleaning - Region Distribution:\n", df_clean["Region"].value_counts(normalize=True))
# print("\nBefore Cleaning - Product Distribution:\n", df["Product"].value_counts(normalize=True))
# print("\nAfter Cleaning - Product Distribution:\n", df_clean["Product"].value_counts(normalize=True))
# print("\nBefore Cleaning - Sales Summary:\n", df["Sales"].describe())
# print("\nAfter Cleaning - Sales Summary:\n", df_clean["Sales"].describe())


# ---------------------------------------------------------
# 7. FEATURE ENGINEERING
# Create actual revenue after applying discount
# Formula:
# Revenue_After_Discount = Sales * (1 - Discount)
# ---------------------------------------------------------
df_clean["Revenue_After_Discount"] = (
    df_clean["Sales"] * (1 - df_clean["Discount"])
).round(2)


# ---------------------------------------------------------
# 8. CREATE TIME-BASED FEATURES
# Extract month and year from Order_Date
# Int64 is used to safely handle missing integer values
# ---------------------------------------------------------
df_clean["Order_Month"] = df_clean["Order_Date"].dt.month.astype("Int64")
df_clean["Order_Year"] = df_clean["Order_Date"].dt.year.astype("Int64")


# ---------------------------------------------------------
# 9. ANALYSIS
# A) Total revenue by region
# B) Top 3 regions by revenue
# ---------------------------------------------------------
df_regional_revenue = df_clean.groupby("Region", as_index=False).agg(
    Regional_Revenue=("Revenue_After_Discount", "sum")
)

df_top_revenue_region = (
    df_regional_revenue
    .sort_values(by="Regional_Revenue", ascending=False)
    .head(3)
    .reset_index(drop=True)
)


# ---------------------------------------------------------
# 10. OUTPUT
# ---------------------------------------------------------
print("Regional Revenue:\n")
print(df_regional_revenue)

print("\nTop 3 Revenue Regions:\n")
print(df_top_revenue_region)