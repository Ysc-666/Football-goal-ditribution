import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\\个人文件\\自学\\Kaggle\\world cup matches\\match_events.csv')
goals = df[df['event_type'] == 'Goal']

# Data reading and inspection
# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df['event_id'].duplicated().sum())




regular_goals = goals[goals['minute'] <= 90]


goal_by_minute = regular_goals['minute'].value_counts().sort_index()

# Create a goal time distribution chart
plt.figure(figsize=(15, 6))
plt.bar(goal_by_minute.index, goal_by_minute.values, color='steelblue')
plt.xlabel('Minute')
plt.ylabel('Number of Goals')
plt.title('Goal Time Distribution (Regular Time)')

plt.xticks(range(0, 91, 5))
# plt.savefig('distribution of goals in each minutes',dpi = 1080,bbox_inches = 'tight')
plt.show()


# Pie Chart of Goals Distribution by Half
goals = df[df['event_type'] == 'Goal'].copy()
# def classify(m):
#     if m <= 45:
#         return 'First Half'
#     elif m <= 90:
#         return 'Second Half'
#     else:
#         return 'Extra Time'
# goals['half'] = goals['minute'].apply(classify)
goals['half'] = goals['minute'].apply(lambda m:
    'First Half' if m<=45
    else 'Second Half' if m<=90
    else 'Extra Time')
counts = goals['half'].value_counts()
# print(counts)


plt.figure(figsize = (8,8))
plt.pie(counts.values,
        labels = counts.index,
        autopct = '%1.1f%%',
        startangle = 90,
        colors = ['#66b3ff', '#ff9999', '#99ff99'])
plt.title('Distribution of goals')
plt.axis('equal')
# plt.savefig('half_comparison.png',dpi = 1080,bbox_inches = 'tight')
plt.show()




# Bar chart of goals scored in each time period
bins = [0,15,30,45,60,75,90]
goals = df[df['event_type'] == 'Goal'].copy()
labels = ['1-15','16-30','31-45','46-60','61-75','76-90']
regular = goals[goals['minute'] <= 90].copy()
regular['interval'] = pd.cut(regular['minute'],bins = bins,labels = labels)
interval_counts = regular['interval'].value_counts().sort_index()
# print(interval_counts)

plt.figure(figsize=(9, 5))
plt.bar(interval_counts.index, interval_counts.values, color='steelblue')
plt.title('Goals by 15-Minute Interval')
plt.xlabel('Interval (minute)')
plt.ylabel('Number of Goals')
for i, v in enumerate(interval_counts.values):    
    plt.text(i, v + 0.5, str(v), ha='center')
# plt.savefig('interval_analysis.png', dpi=1080, bbox_inches='tight')
plt.show()