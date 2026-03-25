import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'month': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    'facecream': [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900],
    'facewash': [1500,1200,1340,1130,1740,1555,1890,2100,1760,1890,2100,1760],
    'toothpaste': [5200,5100,4550,5870,4560,4890,5200,6100,8300,7300,7400,6800],
    'bathingsoap': [9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400],
    'shampoo': [1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800],
    'profit': [12000,15000,13000,17000,16000,14000,15000,18000,19000,20000,21000,22000]
}

df = pd.DataFrame(data)

# a) Line Plot (Total Profit)
plt.figure()
plt.plot(df['month'], df['profit'], marker='o')
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()
plt.show()

# b) Multiline Plot (All products)
plt.figure()
plt.plot(df['month'], df['facecream'], label='Face Cream')
plt.plot(df['month'], df['facewash'], label='Face Wash')
plt.plot(df['month'], df['toothpaste'], label='Toothpaste')
plt.legend()
plt.title("Product Sales Data")
plt.show()

x = np.arange(len(df['month']))
width = 0.3

plt.figure()
plt.bar(x - width/2, df['facecream'], width, label='Face Cream')
plt.bar(x + width/2, df['facewash'], width, label='Face Wash')
plt.xticks(x, df['month'])
plt.legend()
plt.title("Face Products Sales")
plt.show()

total_sales = [
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum()
]

labels = ['Face Cream','Face Wash','Toothpaste','Bathing Soap','Shampoo']

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Yearly Product Sales Distribution")
plt.show()