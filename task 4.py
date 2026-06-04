#Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt

#Create Sample Social Media Dataset
data = {
    'Date': ['2025-01-01','2025-01-02','2025-01-03',
             '2025-01-04','2025-01-05'],
    'Reach': [1200, 1500, 1800, 1700, 2200],
    'Likes': [120, 150, 180, 160, 250],
    'Comments': [20, 25, 30, 28, 40],
    'Shares': [10, 15, 20, 18, 25],
    'Followers': [5000, 5050, 5100, 5150, 5250]
}

df = pd.DataFrame(data)

print(df)


#Convert Date Column
df['Date'] = pd.to_datetime(df['Date'])

#Calculate Total Engagement
df['Engagement'] = (
    df['Likes'] +
    df['Comments'] +
    df['Shares']
)

print(df[['Date','Engagement']])


#Calculate Engagement Rate
df['Engagement_Rate'] = (
    df['Engagement'] /
    df['Reach']
) * 100

print(df[['Date','Engagement_Rate']])

#Calculate Average Reach
avg_reach = df['Reach'].mean()

print("Average Reach:", avg_reach)

#Find the Best Performing Post
best_post = df.loc[df['Reach'].idxmax()]

print("Best Performing Post:")
print(best_post)

#Visualize Reach Trend
plt.figure(figsize=(8,5))

plt.plot(
    df['Date'],
    df['Reach'],
    marker='o'
)

plt.title('Social Media Reach Trend')
plt.xlabel('Date')
plt.ylabel('Reach')
plt.grid(True)

plt.show()

#Visualize Engagement Trend
plt.figure(figsize=(8,5))

plt.bar(
    df['Date'],
    df['Engagement']
)

plt.title('Daily Engagement')
plt.xlabel('Date')
plt.ylabel('Engagement')

plt.show()

#Analyze Follower Growth
df['Follower_Growth'] = (
    df['Followers'].diff()
)

print(df[['Date',
          'Followers',
          'Follower_Growth']])

#Generate Summary Report
print("SOCIAL MEDIA ANALYSIS REPORT")
print("---------------------------")

print("Total Reach:",
      df['Reach'].sum())

print("Average Reach:",
      df['Reach'].mean())

print("Total Engagement:",
      df['Engagement'].sum())

print("Average Engagement Rate:",
      round(df['Engagement_Rate'].mean(),2),
      "%")



