#import required libraries
import pandas as pd
import matplotlib.pyplot as plt

#load sales data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [50000, 55000, 62000, 58000, 70000, 75000]
}
df = pd.DataFrame(data)

#check the data
print(df.head())

#create a line chart
plt.figure(figsize=(8,5))
plt.plot(df['Month'], df['Sales'], marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales (₹)')
plt.grid(True)
plt.show() 