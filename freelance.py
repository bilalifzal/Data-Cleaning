import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Dataset Load karna
df = pd.read_csv('globalAirQuality.csv')
df2 = df.copy()

# 2. Datetime conversion aur columns banana
df2['timestamp'] = pd.to_datetime(df2['timestamp'])
df2['year'] = df2['timestamp'].dt.year
df2['month'] = df2['timestamp'].dt.month
df2['day'] = df2['timestamp'].dt.day
df2['hour'] = df2['timestamp'].dt.hour


country_counts = df2['country'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', colors=['gold', 'lightcoral'])
plt.title('Country-wise Data Distribution (Pie Chart)')
plt.tight_layout()
plt.show()

# --- GRAPH 1: Line Chart (AQI Trend Over Time) ---
plt.figure(figsize=(12, 5))
plt.plot(df2['timestamp'], df2['aqi'], color='orange', linewidth=0.8)
plt.title('1. Global Air Quality Index (AQI) Trend Over Time', fontsize=12, fontweight='bold')
plt.xlabel('Timestamp')
plt.ylabel('AQI')
plt.grid(True)
plt.show()


# --- GRAPH 2: Histogram (AQI Distribution) ---
plt.figure(figsize=(8, 4))
plt.hist(df2['aqi'], bins=30, color='skyblue', edgecolor='black')
plt.title('2. AQI Distribution (Frequency Histogram)', fontsize=12, fontweight='bold')
plt.xlabel('AQI Value')
plt.ylabel('Frequency (Count)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# --- GRAPH 3: Scatter Plot (Temperature vs Humidity) ---
plt.figure(figsize=(8, 4))
plt.scatter(df2['temperature'], df2['humidity'], color='purple', alpha=0.3, s=15)
plt.title('3. Temperature vs Humidity (Scatter Plot)', fontsize=12, fontweight='bold')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# --- GRAPH 4: Bar Chart (Average AQI by City) ---
city_avg_aqi = df2.groupby('city')['aqi'].mean()

plt.figure(figsize=(8, 4))
city_avg_aqi.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('4. Average AQI Comparison Across Cities', fontsize=12, fontweight='bold')
plt.xlabel('City')
plt.ylabel('Average AQI')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# --- GRAPH 5: Box Plot (PM2.5 Spread across Cities) ---
# Yeh check karne ke liye ke kis city mein PM2.5 ki values kitni zyadah fluctuate (spread) hoti hain
plt.figure(figsize=(8, 4))
df2.boxplot(column='pm25', by='city', grid=False, patch_artist=True)
plt.title('5. PM2.5 Spread Across Different Cities', fontsize=12, fontweight='bold')
plt.xlabel('City')
plt.ylabel('PM2.5 Levels')
plt.suptitle('') 
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()