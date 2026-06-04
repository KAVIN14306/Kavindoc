#import required libraries
import pandas as pd
import matplotlib.pyplot as plt

#load weather data
data = {
    'Date': ['2025-01-01','2025-01-02','2025-01-03',
             '2025-01-04','2025-01-05','2025-01-06'],
    'Temperature': [28, 30, 29, 31, 33, 32],
    'Rainfall': [0, 5, 2, 10, 15, 8],
    'Humidity': [65, 68, 70, 72, 75, 73]
}

df = pd.DataFrame(data)
print(df)

#convert date column
df['Date'] = pd.to_datetime(df['Date'])

#check dataset information
print(df.info())
print(df.describe())

#check missing values
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

#visuaalize tempeerature trend
plt.figure(figsize=(8,5))
plt.plot(df['Date'], df['Temperature'], marker='o')
plt.title('Temperature Trend')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

#analyze rainfall pattern
plt.figure(figsize=(8,5))
plt.bar(df['Date'], df['Rainfall'])
plt.title('Rainfall Pattern')
plt.xlabel('Date')
plt.ylabel('Rainfall (mm)')
plt.show()

#analyze humidity trend
plt.figure(figsize=(8,5))
plt.plot(df['Date'], df['Humidity'], marker='s')
plt.title('Humidity Trend')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.grid(True)
plt.show()

#find correlation b\w variables
correlation = df[['Temperature',
                  'Rainfall',
                  'Humidity']].corr()

print(correlation)

#calculate average weather conditions
avg_temp = df['Temperature'].mean()
avg_rain = df['Rainfall'].mean()
avg_humidity = df['Humidity'].mean()

print("Average Temperature:", avg_temp)
print("Average Rainfall:", avg_rain)
print("Average Humidity:", avg_humidity)

#detect  weather trends
if df['Temperature'].iloc[-1] > df['Temperature'].iloc[0]:
    print("Temperature is increasing.")
else:
    print("Temperature is decreasing.")

#generate weather analysis report
print("Weather Analysis Summary")
print("------------------------")
print("Average Temperature:", round(avg_temp,2))
print("Average Rainfall:", round(avg_rain,2))
print("Average Humidity:", round(avg_humidity,2))

