# Mini project-2


# Ecommerce project using Numpy, Pandas, and Matplotlib

# USING PANDAS
import pandas as pd

# USING NUMPY 
import numpy as np

# USING MATPLOTLIB
import matplotlib.pyplot as plt

# DUMMY DATA 
data = {
    "Order_ID":[101,102,103,104,105,106,107,108,109,110,
                111,112,113,114,115,116,117,118,119,120,
                121,122,123,124,125,126,127,128,129,130],

    "Product":["Laptop","Mobile","Shoes","TShirt","Headphones",
               "Watch","Laptop","Shoes","Mobile","Watch",
               "TShirt","Headphones","Laptop","Mobile","Shoes",
               "Watch","Laptop","Headphones","TShirt","Mobile",
               "Shoes","Laptop","Watch","Headphones","Mobile",
               "TShirt","Shoes","Laptop","Watch","Mobile"],

    "Category":["Electronics","Electronics","Fashion","Fashion","Electronics",
                "Accessories","Electronics","Fashion","Electronics","Accessories",
                "Fashion","Electronics","Electronics","Electronics","Fashion",
                "Accessories","Electronics","Electronics","Fashion","Electronics",
                "Fashion","Electronics","Accessories","Electronics","Electronics",
                "Fashion","Fashion","Electronics","Accessories","Electronics"],

    "Quantity":[2,3,4,5,6,2,1,3,2,4,
                6,5,2,4,3,5,1,6,4,2,
                5,2,3,4,2,6,3,1,5,4],

    "Price":[50000,20000,2500,1000,1500,
             3000,50000,2500,20000,3000,
             1000,1500,50000,20000,2500,
             3000,50000,1500,1000,20000,
             2500,50000,3000,1500,20000,
             1000,2500,50000,3000,20000],

    "City":["Jaipur","Delhi","Mumbai","Pune","Bangalore",
            "Jaipur","Delhi","Mumbai","Pune","Bangalore",
            "Jaipur","Delhi","Mumbai","Pune","Bangalore",
            "Jaipur","Delhi","Mumbai","Pune","Bangalore",
            "Jaipur","Delhi","Mumbai","Pune","Bangalore",
            "Jaipur","Delhi","Mumbai","Pune","Bangalore"],

    "Month":["Jan","Jan","Feb","Feb","Mar",
             "Mar","Apr","Apr","May","May",
             "Jun","Jun","Jul","Jul","Aug",
             "Aug","Sep","Sep","Oct","Oct",
             "Nov","Nov","Dec","Dec","Jan",
             "Feb","Mar","Apr","May","Jun"]
}

df = pd.DataFrame(data)

# CONVERTING INTO CSV FILE
df.to_csv("ecommerce_sales.csv", index=False)

# READING CSV FILE
df =pd.read_csv("ecommerce_sales.csv")

# ADDING SALES COLUMN
df["Sales"] = df["Quantity"] * df["Price"]

# CALCULATE TOTAL REVENUE
total_sales = df["Sales"].sum()

# AVERAGE SALES VALUE
average_sales = np.mean(df["Sales"])

# HIGHEST SALE
highest_sale = np.max(df["Sales"])

# LOWEST SALE
lowest_sale = np.min(df["Sales"])

# BEST SELLING PRODUCT
best_selling = df.groupby("Product")["Quantity"].sum()

# TOP PRODUCT BY REVENUE
product_sales = df.groupby("Product")["Sales"].sum()

# FIND THE HIGHEST REVENUE PRODUCT
top_product = product_sales.idxmax()

# CITY-WISE SALES ANALYSIS 
city_sales = df.groupby("City")["Sales"].sum()

# CATEGORY-WISE SALES ANALYSIS
category_sales = df.groupby("Category")["Sales"].sum()

# TOP CATEGORY BY REVENUE
category_revenue = category_sales.idxmax()

# FIND THE TOP CITY
top_city = city_sales.idxmax()

# MONTHLY SALES TREND
month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales = monthly_sales.reindex(month_order)

def sales_summary():
 print("\n=== SALES SUMMARY ===")
 print("Total Revenue =", total_sales)
 print("Average Sale value =", average_sales)
 print("Highest Sale =", highest_sale)
 print("Lowest sale =", lowest_sale)


def product_analysis():
 print("\n=== PRODUCT ANALYSIS ===")
 print(product_sales)
 print("\nHighest Revenue Product =",top_product)
 print("\nBest Selling Product =",best_selling.idxmax())


def city_analysis():
 print("\n=== CITY ANALYSIS ===")
 print(city_sales)
 print("\nTop Performing City =", top_city)


def monthly_analysis():
   print("\n=== MONTHLY SALES ANALYSIS ===")
   print(monthly_sales)



def category_analysis():
 print("\n=== CATEGORY ANALYSIS ===")
 print(category_sales)
 print("\nTop Category by Revenue =",category_revenue)


def show_charts():

  plt.figure(figsize=(14,10))

# BAR CHART
  plt.subplot(2,2,1)
  product_sales.plot(kind="bar")
  plt.title("Revenue by Product")

# PIE CHART
  plt.subplot(2,2,2)
  category_sales.plot(kind="pie", autopct="%1.1f%%")
  plt.title("Category Revenue")
  plt.ylabel("")

# LINE CHART
  plt.subplot(2,2,3)
  monthly_sales.plot(kind="line", marker="o")
  plt.title("Monthly Sales Trend")

# HISTOGRAM
  plt.subplot(2,2,4)
  plt.hist(df["Sales"])
  plt.title("Sales Distribution")

  plt.tight_layout()
  plt.show()


while True:
    print("\n===== E-COMMERCE SALES ANALYSIS =====")
    print("1. Sales Summary")
    print("2. Product Analysis")
    print("3. City Analysis")
    print("4. Category Analysis")
    print("5. Monthly Analysis")
    print("6. Show Charts")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        sales_summary()

    elif choice == 2:
        product_analysis()

    elif choice == 3:
        city_analysis()

    elif choice == 4:
        category_analysis()

    elif choice == 5:
       monthly_analysis()

    elif choice == 6:
        show_charts()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")