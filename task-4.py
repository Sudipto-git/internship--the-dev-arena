# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('sales_data.csv')
print(df.head())

# %%
df.isna().sum()
df.drop_duplicates()

# %% [markdown]
# calculating metrics

# %%
df['Total_Sales'].mean()


# %%
df['Total_Sales'].median()


# %%
df['Total_Sales'].mode()

# %%
skew = df['Total_Sales'].skew()
if skew > 0:
    print(f"The distribution is positively skewed with the value {skew}.")
elif skew < 0:
    print(f"The distribution is negatively skewed with the value {skew} .")
else:
    print("The distribution is symmetric.") 

# %%
kurtosis = df['Total_Sales'].kurt()
print(f"The kurtosis of the Total_Sales distribution is {kurtosis}.") 

# %% [markdown]
# Counting based metrics

# %%
df.count()

# %%
df['Total_Sales'].value_counts()

# %% [markdown]
# Corelation analysis

# %%
df.corr(numeric_only=True)

# %% [markdown]
# Visualisation---- Line Chart

# %%
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Total_Sales"], marker='o')
plt.title("Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)
plt.grid()
plt.tight_layout()
plt.show()

# %% [markdown]
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Sales Performance Report</title>
#     <style>
#         body { font-family: sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 20px; }
#         h2 { color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }
#         .highlight { font-weight: bold; color: #e67e22; }
#     </style>
# </head>
# <body>
#     <h2>Sales Performance Report</h2>
#     <p>The data reveals highly volatile <strong>Total Sales</strong> from January through April 2024.</p>
#     <ul>
#         <li><span class="highlight">Peaks:</span> Mid-January and March recorded highs exceeding <strong>$350,000</strong>.</li>
#         <li><span class="highlight">Troughs:</span> Frequent drops to near-zero suggest inconsistent demand or data reporting gaps.</li>
#     </ul>
#     <p>Overall, the trend remains erratic with no definitive growth trajectory established during this period.</p>
# </body>
# </html>

# %% [markdown]
# Visualisation ---- Bar Chart

# %%
plt.figure()
df.groupby('Product')['Total_Sales'].sum().plot(kind='bar')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# %% [markdown]
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Product Sales Analysis</title>
#     <style>
#         body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 30px auto; padding: 20px; border: 1px solid #eee; border-radius: 8px; }
#         h2 { color: #1a5fb4; border-bottom: 2px solid #1a5fb4; padding-bottom: 10px; }
#         .highlight { font-weight: bold; color: #d1403f; }
#         .stat-box { background-color: #f8f9fa; padding: 15px; border-left: 5px solid #1a5fb4; margin: 15px 0; }
#     </style>
# </head>
# <body>
#     <h2>Total Sales by Product Report</h2>
#     <div class="stat-box">
#         <p><strong>Laptops</strong> are the top performers, reaching nearly <span class="highlight">$3.9M</span> in sales. <strong>Tablets</strong> and <strong>Phones</strong> follow as strong mid-tier contributors, each generating approximately $2.9M.</p>
#     </div>
#     <p>In contrast, <strong>Headphones</strong> and <strong>Monitors</strong> represent the lowest revenue streams, both falling below the $1.5M mark.</p>
# </body>
# </html>

# %% [markdown]
# Histogram

# %%
plt.figure()
plt.hist(df["Total_Sales"], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75)
plt.show()

# %% [markdown]
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Sales Report</title>
#     <style>
#         body{font-family:'Segoe UI',sans-serif;line-height:1.4;color:#333;max-width:500px;margin:10px auto;padding:15px;border:1px solid #ddd;border-radius:8px;box-shadow:0 2px 5px rgba(0,0,0,0.1)}
#         h2,h3{margin:5px 0;color:#2c3e50;border-bottom:1px solid #3498db}
#         h3{color:#2980b9;border:0;font-size:1.1em}
#         .sh{font-weight:700;color:#e67e22}
#         hr{border:0;border-top:1px solid #eee;margin:10px 0}
#         footer{font-style:italic;font-size:0.9em;color:#666}
#     </style>
# </head>
# <body>
#     <h2>Sales Analysis</h2>
#     <h3>Revenue</h3>
#     <p><strong>Laptops</strong> lead at <span class="sh">$3.9M</span>. Tablets/Phones follow ($2.9M), while Headphones/Monitors lag below $1.5M.</p>
#     <hr>
#     <h3>Distribution</h3>
#     <p>Data is <strong>right-skewed</strong>; most transactions are low-value (<span class="sh">$0-$50k</span>), with few reaching the $350k peak.</p>
#     <hr>
#     <footer>Laptops drive volume; business relies on high-frequency, low-value sales.</footer>
# </body>
# </html>

# %% [markdown]
# Scatter Plot

# %%
plt.figure()
plt.scatter(df["Product"], df["Price"], alpha=0.5)
plt.title("Product vs Price")
plt.xlabel("Product")
plt.ylabel("Price")
plt.grid()
plt.show()

# %% [markdown]
# <!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sales Summary</title><style>body{font:13px/1.4 sans-serif;color:#333;max-width:500px;margin:5px auto;padding:10px;border:1px solid #ddd;border-radius:5px;box-shadow:0 2px 4px #0001}h2,h3{margin:4px 0;color:#2c3e50;border-bottom:1px solid #3498db}h3{color:#2980b9;border:0;font-size:1.1em}.s{font-weight:700;color:#e67e22}hr{border:0;border-top:1px solid #eee;margin:8px 0}footer{font-style:italic;font-size:.85em;color:#666}</style></head><body><h2>Sales Analysis</h2><h3>Revenue</h3><p><strong>Laptops</strong> lead at <span class="s">$3.9M</span>. Tablets/Phones follow (~$2.9M); Monitors/Headphones lag (~$1.4M).</p><hr><h3>Trends</h3><p>Data is <strong>right-skewed</strong>; most sales are <span class="s">$0-$100k</span>. Prices range widely from $2k to $50k across all lines.</p><hr><footer>Laptops and broad pricing drive the current revenue model.</footer></body></html>
# 

# %% [markdown]
# Insights and report writing---
# All the report are written below their respected graphs.

# %% [markdown]
# Error handling

# %%
try:
    df= pd.read_csv('sales_data.csv')
    print("Successfully loaded the data.")
except FileNotFoundError:
    print("Error: The file 'sales_data.csv' was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except pd.errors.ParserError:
    print("Error: There was a parsing error while reading the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# %%
required_cols = ["Date", "Product", "Price", "Total_Sales"]

for col in required_cols:
    if col not in df.columns:
        print(f"Error: Missing required column '{col}' in the dataset.")
    else:
        print(f"Column '{col}' is present.")

# %%
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
print(df["Date"].dtypes)
df["Total_Sales"] = pd.to_numeric(df["Total_Sales"], errors='coerce')
print(df["Total_Sales"].dtypes)

# %%



