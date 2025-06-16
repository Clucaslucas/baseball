#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
baseball_game = pd.read_csv('0519 CUvUCONN BIA.csv')

print(baseball_game.isnull())
baseball_game.isnull().sum()
## 1.
baseball_game.replace('', None)

## 2. No duplicates

## 3. No need to change data to categorical

## 4.
baseball_game.drop(['VertApprAngle', 'HorzApprAngle'], axis=1)


# In[6]:


print(baseball_game.fillna(0))
#To account for null values in our data set all the values were retunred with a zero.



# In[12]:


## 5. renaming columns. make sure to rename at least one column of your dataframe. make sure to have a name that is representative of the column values.
baseball_game=baseball_game.rename(columns={'RelSpeed': 'Pitch_Speed'})
baseball_game = baseball_game.rename(columns={'RelSpeed': 'Pitch_Speed'})


# In[11]:


## 6. filter your data based on one condition or multiple conditions such that it helps you with solving the question/questions defined for the project.
print(baseball_game.head())
fastballs = baseball_game[baseball_game['TaggedPitchType'] == 'Fastball']
sliders = baseball_game[baseball_game['TaggedPitchType'] == 'Slider']


# In[16]:


#Draw a pie chart to represent the proportion of categorical data in a specific column 
#effectively and answer a question.
import matplotlib.pyplot as plt
pitch_type = baseball_game['TaggedPitchType'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(pitch_type, labels=pitch_type.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  
plt.title('Pitch Type Distribution')
plt.show()


# In[17]:


#Generate a meaningful boxplot to visualize the distribution of a numerical column in the dataset.



plt.figure(figsize=(8, 6))
plt.boxplot(baseball_game['Pitch_Speed'].dropna())
plt.title('Distribution of Pitch Speed')
plt.ylabel('Pitch Speed (mph)')
plt.show()



# In[18]:


plt.figure(figsize=(8, 8))
plt.boxplot(fastballs['Pitch_Speed'].dropna())
plt.title('Distribution of Fastballs')
plt.ylabel('Pitch Speed (mph)')
plt.show()

plt.figure(figsize=(8, 8))
plt.boxplot(sliders['Pitch_Speed'].dropna())
plt.title('Distribution of Sliders')
plt.ylabel('Pitch Speed (mph)')
plt.show()


# In[19]:


# Average exit velocity of each pitch. How hard each pitch gets hit on average.

mask1 = baseball_game['TaggedPitchType'] == 'Fastball'
mask2 = baseball_game['TaggedPitchType'] == 'Slider'
baseball_game_common = baseball_game[mask1 | mask2]
avgExitSpeed = baseball_game_common.groupby('TaggedPitchType')['ExitSpeed'].mean()
print(avgExitSpeed)



# In[20]:


#Draw a scatter plot to answer a question you defined for the project better than only 
#answering using numerical measures.

## Filteration of data so that we only have softballs and sliders

#The exit velocity over distance over hit balls against fastballs and sliders

mask1 = baseball_game['TaggedPitchType'] == 'Fastball'
mask2 = baseball_game['TaggedPitchType'] == 'Slider'
baseball_game_common = baseball_game[mask1 | mask2]
baseball_game_common['TaggedPitchType'].value_counts()


plt.figure(figsize=(8, 8))
plt.scatter(baseball_game_common['ExitSpeed'], baseball_game_common['Distance'])
plt.title('Exit Speed vs. Distance')
plt.xlabel('Exit Speed (mph)')
plt.ylabel('Distance (feet)')
plt.show()

plt.figure(figsize=(4,6))
plt.scatter(baseball_game_common['TaggedPitchType'], baseball_game_common['Distance'])
plt.title('Most Common Pitches vs. Distance')
plt.xlabel('Fastball vs. Sliders')
plt.ylabel('Distance (feet)')
plt.show()


# In[21]:


mask3 = baseball_game['Pitcher'] == 'Cancellieri, Dominic'
mask4 = baseball_game['Pitcher'] == 'Quigley, Stephen'

mask3 = mask3 & ~baseball_game['ExitSpeed'].isna()
mask4 = mask4 & ~baseball_game['ExitSpeed'].isna()

# Apply masks
baseball_game_starters = baseball_game[mask3]
baseball_game_starters1 = baseball_game[mask4]

plt.figure(figsize=(8, 8))
plt.scatter(baseball_game_starters['ExitSpeed'], baseball_game_starters['Distance'])
plt.title('Creighton Starting Pitching')
plt.xlabel('Exit Speed (mph)')
plt.ylabel('Distance (feet)')
plt.show()

plt.figure(figsize=(8, 8))
plt.scatter(baseball_game_starters1['ExitSpeed'], baseball_game_starters1['Distance'])
plt.title('UConn Starting Pitching')
plt.xlabel('Exit Speed (mph)')
plt.ylabel('Distance (feet)')
plt.show()



# In[ ]:




