# %% [markdown]
# Day-1

# %%
import pandas as pd
 

# %%


# %% [markdown]
# Day-2

# %%
df = pd.read_csv("/Volumes/X/coding/code/internship- the dev arena/sales_data.csv")
df.head()
df.info()
df.shape
df.dtypes
df.columns

# %%
print(pd.read_csv("/Volumes/X/coding/code/internship- the dev arena/sales_data.csv"))

# %% [markdown]
# Day-3

# %%
df.isna().sum()

# %%
df.dropna()

# %%
df.drop_duplicates()

# %% [markdown]
# calculating revenue

# %%
df['Revenue'] = df['Quantity'] * df['Price']
df = df.drop('Total_Sales', axis=1)
df.head()

# %% [markdown]
# Find best product

# %%
product_revenue = df.groupby('Product')['Revenue'].sum()
print(product_revenue)
best_product = product_revenue.idxmax()
best_revenue = product_revenue.max()
print(f"The product with the highest total revenue is: {best_product} with revenue of {product_revenue.max()}")

# %% [markdown]
# Format Output and a adding insights
# 
# 

# %%
print(f"Best Product: {best_product}")
print(f"Total Revenue: {best_revenue:,.2f}")

# Adding an insight
if best_revenue > 100000:
    print("Insight: This product is a top performer and contributes significantly to overall sales.")
else:
    print("Insight: While this product leads, there is room to boost its sales further.")


