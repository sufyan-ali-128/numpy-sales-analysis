import numpy as np
sales = np.array([1200,1500,1700,1600,
                  1800,2100,2500,2200,
                  2600,2400,3000,3200])

months = np.array(["January", "February", "March", "April",
                    "May", "June","July", "August", 
                    "September", "October", "November", "December"])

# Total yearly sales
total_sales = np.sum(sales)
print(f"Total yearly sales:  {total_sales}")

# Average monthly sales
average_sales = np.mean(sales)
print(f"Average monthly sales:  {average_sales}")

# Highest monthly sales
highest_sale = np.max(sales)
print(f"Highest monthly sales:  {highest_sale}")

# Lowest monthly sales
lowest_sale = np.min(sales)
print(f"Lowest monthly sales:  {lowest_sale}")

# Month with highest sales
highest_sale_month = months[np.argmax(sales)]
print(f"Month with highest sales:  {highest_sale_month}")

# Month with lowest sales
lowest_sale_month = months[np.argmin(sales)]
print(f"Month with lowest sales:  {lowest_sale_month}")

# Median sales
median_sales = np.median(sales)
print(f"Median of sales: {median_sales}")

# Standard deviation of sales 
standard_deviation = np.std(sales)
print(f"Standard deviation of sales:   {standard_deviation}")

# Months with sales greater than the average
month_with_sales = months[ sales > average_sales ]
print(f"Months with sales greater than the average:  {month_with_sales}")

# Number of months with sales above 2000
months_above_2000 = len(months [sales > 2000])
print(f"Number of months with sales above 2000:  {months_above_2000}")

# Number of months below 1800
months_below_1800 = len(months[sales < 1800])
print(f"Number of months below 1800:   {months_below_1800}")

# Difference between highest and lowest sales
difference = highest_sale - lowest_sale
print(f"Difference between highest and lowest sales:  {difference}")

# Sort the sales data
sorted_sales = np.sort(sales)
print(f"Sorted sales data:  {sorted_sales}")

# Which quarter (Q1, Q2, Q3, Q4) had the highest sales?
quarterly = sales.reshape(4,3)
quarter_totals = np.sum(quarterly , axis=1)
highest_quarter_sale = np.argmax(quarter_totals)
quarter_names = np.array(["Q1", "Q2", "Q3", "Q4"])
highest_quarter_sales = quarter_names[highest_quarter_sale]
print(f"Quarter with highest sales?:  {highest_quarter_sales}" )
print(f"Total sales of highest quarter:   {quarter_totals[highest_quarter_sale]}" )

# What was the average sales for each quarter?
avg_of_quarter = np.mean(quarterly , axis=1)
print("========== Quarterly Report ==========")
print(f"Q1 Average: {np.round(avg_of_quarter[0] ,2)}")
print(f"Q2 Average: {np.round(avg_of_quarter[1] ,2)}")
print(f"Q3 Average: {np.round(avg_of_quarter[2] ,2)}")
print(f"Q4 Average: {np.round(avg_of_quarter[3] ,2)}")

# Percentage contribution of each quarter
percentage_contribution = (  quarter_totals / total_sales)*100
print("========== Percentage contribution Report ==========")
print(f"Q1 contribution: {np.round(percentage_contribution[0] ,2)}%")
print(f"Q2 contribution: {np.round(percentage_contribution[1] ,2)}%")
print(f"Q3 contribution: {np.round(percentage_contribution[2] ,2)}%")
print(f"Q4 contribution: {np.round(percentage_contribution[3] ,2)}%")

# What was the month-to-month growth percentage?
previous = sales[:-1]
current = sales[1:]
growth = ((current - previous) / previous) * 100
print("==========  Month-to-Month growth  ==========")
for i in range(len(growth)):
    print(f"{months[i]} --> {months[i+1]} : {np.round(growth[i] , 2)}%")
    