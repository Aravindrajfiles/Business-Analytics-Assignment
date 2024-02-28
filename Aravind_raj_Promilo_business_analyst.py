#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


citivice = pd.read_excel(r"C:\promilo\7.xlsx")
conversion = pd.read_excel(r"C:\promilo\4.xlsx")
demograph = pd.read_excel(r"C:\promilo\6.xlsx")
event_report = pd.read_excel(r"C:\promilo\3.xlsx")
gender_report = pd.read_excel(r"C:\promilo\8.xlsx")
goo_ads_report = pd.read_excel(r"C:\promilo\12.xlsx")
pages_screens_report = pd.read_excel(r"C:\promilo\5.xlsx")
trafic_aquisition = pd.read_excel(r"C:\promilo\2.xlsx")
user_aquisition = pd.read_excel(r"C:\promilo\1.xlsx")
user_by_age = pd.read_excel(r"C:\promilo\11.xlsx")
user_by_interest = pd.read_excel(r"C:\promilo\9.xlsx")
user_by_language = pd.read_excel(r"C:\promilo\10.xlsx")


# In[3]:


citivice


# In[4]:


citivice.isnull().sum()


# In[6]:


conversion


# In[7]:


conversion.isnull().sum()


# In[8]:


demograph


# In[9]:


demograph.isnull().sum()


# In[10]:


event_report


# In[11]:


event_report.isnull().sum()


# In[12]:


report = event_report.loc[179]
report


# In[13]:


null_event_name_rows = event_report[event_report['Event name'].isnull()]
print(null_event_name_rows)


# In[14]:


event_report.drop(index=179, inplace=True)


# In[15]:


event_report.isnull().sum()


# In[16]:


gender_report


# In[17]:


gender_report.isnull().sum()


# In[18]:


goo_ads_report


# In[19]:


goo_ads_report.isnull().sum()


# In[20]:


pages_screens_report


# In[21]:


pages_screens_report.isnull().sum()


# In[22]:


trafic_aquisition


# In[23]:


trafic_aquisition.isnull().sum()


# In[25]:


user_aquisition


# In[26]:


user_aquisition.isnull().sum()


# In[27]:


user_by_age


# In[28]:


user_by_age.isnull().sum()


# In[29]:


user_by_interest


# In[30]:


user_by_interest.isnull().sum()


# In[31]:


user_by_language


# In[32]:


user_by_language.isnull().sum()


# In[33]:


pd.set_option('display.max_columns', 500)


# # EDA
# 

# In[41]:


import warnings

# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[42]:


# Sort the DataFrame by the number of users
sorted_df = citivice.sort_values(by='Users', ascending=False)

# Select the top 15 cities
top_15_cities = sorted_df.head(15)

# Plot the barplot for the top 15 cities
plt.figure(figsize=(10, 6))
sns.barplot(x='Town/City', y='Users', data=top_15_cities)
plt.title('Top 15 Cities by Number of Users')
plt.xlabel('Town/City')
plt.ylabel('Number of Users')
plt.xticks(rotation=45)
plt.show()


# In[43]:


# Cost Analysis
plt.figure(figsize=(10, 6))
sns.lineplot(x='Google Ads cost', y='Cost per conversion', data=goo_ads_report)
plt.title('Cost per Conversion Over Time')
plt.xlabel('Google Ads Cost')
plt.ylabel('Cost per Conversion')
plt.show()


# In[45]:


towns_cities = ['Bengaluru', 'Patna', 'Hyderabad', 'Indore', 'Lucknow']
users = [6097, 1594, 1038, 983, 897]

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(towns_cities, users, color='blue')
plt.xlabel('Town/City')
plt.ylabel('Number of Users')
plt.title('Distribution of Users Across Towns/Cities')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[50]:


gender = ['Male', 'Female', 'Unknown']
users = [7218.0, 4944.0, 13142.0]

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(users, labels=gender, autopct='%1.1f%%', colors=['blue', 'coral', 'pink'], startangle=140)
plt.title('Distribution of Users by Gender')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[52]:


gender = ['Male', 'Female']
users = [7218.0, 4944.0]

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(users, labels=gender, autopct='%1.1f%%', colors=['blue', 'pink', 'lightsalmon'], startangle=140)
plt.title('Distribution of Users by Gender')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[54]:


campaigns = ['Shahid', 'A200Inst', 'B100Installs', 'Shahid (April)', 'Internships', 'App-3', 'B200 &A100Inst', '1to5NC-StateA200', '6to10NC-States-A200Inst', 'Browsing', 'Webinar', 'Colleges', 'Videos', 'Jobs', 'T1']
engaged_sessions = [6276, 968, 780, 546, 515, 763, 425, 462, 296, 112, 81, 50, 39, 32, 5]  # Engaged sessions for each campaign

# Create a DataFrame
data = pd.DataFrame({'Campaign': campaigns, 'Engaged Sessions': engaged_sessions})

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(data['Campaign'], data['Engaged Sessions'], color='brown')
plt.title('Engaged Sessions by Marketing Campaign')
plt.xlabel('Marketing Campaign')
plt.ylabel('Engaged Sessions')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[55]:


languages = ['English', 'Hindi', 'Marathi', 'Gujarati', 'Telugu', 'Tamil', 'Malayalam', 'Bengali', 'Chinese', 'Kannada', 'Panjabi', 'Persian', 'Spanish', 'Finnish', 'Japanese', 'Oriya', 'Afrikaans', 'Assamese', 'German', 'Malay', 'Nepali', 'Russian', 'Urdu', 'Sanskrit']
engaged_sessions = [40639, 798, 98, 100, 56, 43, 36, 18, 13, 31, 17, 6, 8, 4, 3, 2, 1, 1, 0, 1, 1, 1, 0, 0]

# Create horizontal bar plot
plt.figure(figsize=(10, 8))
plt.barh(languages, engaged_sessions, color='skyblue')
plt.xlabel('Engaged Sessions')
plt.ylabel('Language')
plt.title('Engaged Sessions by Language')
plt.tight_layout()
plt.show()


# In[57]:


interests = ['Shoppers', 'Media & Entertainment/Comics & Animation Fans', 'Technology/Mobile Enthusiasts',
             'Food & Dining/Cooking Enthusiasts', 'Sports & Fitness/Health & Fitness Buffs',
             'Lifestyles & Hobbies/Pet Lovers', 'Media & Entertainment/Music Lovers',
             'Media & Entertainment/TV Lovers', 'News & Politics/Avid News Readers',
             'Lifestyles & Hobbies/Outdoor Enthusiasts']
engaged_sessions = [15652, 15680, 15619, 12332, 8226, 7786, 8011, 7423, 7079, 7441]

# Create horizontal bar plot
plt.figure(figsize=(10, 8))
plt.barh(interests, engaged_sessions, color='green')
plt.xlabel('Engaged Sessions')
plt.ylabel('Interests')
plt.title('Top 10 Interests by Engaged Sessions')
plt.tight_layout()
plt.show()


# In[59]:


# Age groups and engagement rate data
age_groups = ['unknown', '18-24', '25-34', '65+', '55-64', '35-44', '45-54']
engagement_rate = [0.569098, 0.695308, 0.50478, 0.539829, 0.519411, 0.510424, 0.561862]

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(age_groups, engagement_rate, color='yellow')
plt.xlabel('Age Group')
plt.ylabel('Engagement Rate')
plt.title('Engagement Rate by Age Group')
plt.ylim(0, 1)  # Set y-axis limit to range from 0 to 1 for better visualization
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for reference
plt.tight_layout()
plt.show()


# In[63]:


pages = ['Flutter', 'MainActivity', 'feeds', 'login', 'my_rewards_screen',
         'storyboard', 'SignInHubActivity', 'registration_screen', 'feedDetails',
         'otp_screen']
views = [156708, 44326, 18514, 16883, 15381, 8189, 6650, 5501, 3971, 3291]

# Create bar plot
plt.figure(figsize=(12, 8))
plt.barh(pages, views, color='red')
plt.xlabel('Views')
plt.ylabel('Pages & Screens')
plt.title('Top 10 Pages & Screens by Views')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest value at the top
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add gridlines for reference
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()


# In[64]:


import matplotlib.pyplot as plt
import numpy as np

# Data
channels = ['Unassigned', 'Display', 'Organic Search', 'Direct', 'Paid Search', 'Organic Social']
users = [20263, 9613, 7689, 4042, 2909, 11]
sessions = [13448, 18292, 21241, 13220, 6788, 16]
engaged_sessions = [1481, 10613, 17814, 7649, 3452, 12]
conversions = [114161, 20031, 33612, 18496, 7595, 19]

# Number of channel groups
num_channels = len(channels)

# Width of each bar
bar_width = 0.2

# x values for the groups
index = np.arange(num_channels)

# Create grouped bar plot
plt.figure(figsize=(12, 8))
plt.bar(index, users, bar_width, label='Users')
plt.bar(index + bar_width, sessions, bar_width, label='Sessions')
plt.bar(index + 2 * bar_width, engaged_sessions, bar_width, label='Engaged Sessions')
plt.bar(index + 3 * bar_width, conversions, bar_width, label='Conversions')

plt.xlabel('Session Default Channel Group')
plt.ylabel('Count')
plt.title('Traffic Acquisition Metrics by Channel Group')
plt.xticks(index + bar_width * 1.5, channels)
plt.legend()
plt.tight_layout()
plt.show()


# In[65]:


channels = ['Display', 'Organic Search', 'Paid Search', 'Direct', 'Unassigned', 'Organic Social']
new_users = [9957, 7652, 3025, 1903, 325, 10]
engaged_sessions = [12008, 18141, 4408, 4975, 1619, 13]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(channels, new_users, marker='o', label='New Users')
plt.plot(channels, engaged_sessions, marker='o', label='Engaged Sessions')
plt.title('User Acquisition by First User Default Channel Group')
plt.xlabel('First User Default Channel Group')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()


# In[70]:


event_names = ["screen_view", "notification_receive", "user_engagement", "notification_dismiss", "session_start"]
event_counts = [694729, 125146, 124836, 70128, 61163]

# Plot
plt.figure(figsize=(10, 6))
plt.bar(event_names, event_counts, color='purple')
plt.title('Top Events by Event Count')
plt.xlabel('Event Name')
plt.ylabel('Event Count')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()


# In[68]:


import matplotlib.pyplot as plt

# Data
event_names = ["notification_receive", "session_start", "first_open", "app_remove", "Promilo111_otp_screen"]
conversions = [94890, 56203, 22872, 12468, 1738]

# Plot
plt.figure(figsize=(10, 6))
plt.barh(event_names, conversions, color='lightgreen')
plt.title('Top Events by Conversions')
plt.xlabel('Conversions')
plt.ylabel('Event Name')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()


# In[71]:


campaign_names = ["App Installation for May --Shahid", "App Install-States-A200Inst-20Jun22",
                  "App Install-States-B100Installs-22Jun22", "App Install for April -- Shahid",
                  "Video-AppInstall-PS-Internships-11Jul22", "App promotion-App-3",
                  "App Instal-States-B200 &A100Inst-22Jun22", "App Install-1to5NC-StateA200-07Jul22",
                  "App Instal-6to10NC-States-A200Inst-07Jul22", "Video-AppInstall-PS-Browsing-11Jul22",
                  "Video-AppInstall-PS-Webinar-11Jul22", "Video-AppInstall-PS-Colleges-11Jul22",
                  "Video-AppInstall-PS-Videos-11Jul22", "Video-AppInstall-PS-Jobs-11Jul22",
                  "App installation for May 06-05-2022 T1"]
sessions = [10936, 1655, 1332, 976, 966, 945, 742, 610, 432, 188, 124, 77, 75, 49, 5]
engaged_sessions = [6276, 968, 780, 546, 515, 763, 425, 462, 296, 112, 81, 50, 39, 32, 5]

# Plot
plt.figure(figsize=(12, 8))
plt.barh(campaign_names, sessions, color='skyblue', label='Sessions')
plt.barh(campaign_names, engaged_sessions, color='salmon', label='Engaged Sessions')

plt.xlabel('Number of Sessions')
plt.ylabel('Google Ads Campaign')
plt.title('Number of Sessions vs Engaged Sessions for Google Ads Campaigns')
plt.legend()
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()


# In[73]:


import matplotlib.pyplot as plt

# Data
languages = ["English", "Hindi", "Marathi", "Gujarati", "Telugu", "Tamil", "Malayalam",
             "Bengali", "Chinese", "Kannada", "Panjabi", "Persian", "Spanish",
             "Finnish", "Japanese", "Oriya", "Afrikaans", "Assamese", "German",
             "Malay", "Nepali", "Russian", "Urdu", "Sanskrit"]
engaged_sessions = [40639, 798, 98, 100, 56, 43, 36, 18, 13, 31, 17, 6, 8, 4, 3, 2, 1, 1, 1, 0, 1, 1, 0, 0]

# Plot
plt.figure(figsize=(12, 8))
plt.barh(languages, engaged_sessions, color='blue')

plt.xlabel('Engaged Sessions')
plt.ylabel('Language')
plt.title('Engaged Sessions by Language')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()


# In[74]:


languages = ["English", "Hindi", "Marathi", "Gujarati", "Telugu", "Tamil", "Malayalam",
             "Bengali", "Chinese", "Kannada", "Panjabi", "Persian", "Spanish",
             "Finnish", "Japanese", "Oriya", "Afrikaans", "Assamese", "German",
             "Malay", "Nepali", "Russian", "Urdu", "Sanskrit"]
users = [22495, 586, 85, 78, 43, 36, 17, 14, 13, 13, 9, 8, 6, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 0]
engagement_rate = [0.595147, 0.406314, 0.426087, 0.44843, 0.455285, 0.518072, 0.654545,
                   0.6, 1, 0.5, 0.708333, 0.4, 0.470588, 0.571429, 0.428571, 0.666667,
                   1, 1, 1, 0, 1, 1, 0, 0, 0]

# Sort languages based on users
sorted_languages = [lang for _, lang in sorted(zip(users, languages), reverse=True)]
sorted_users = sorted(users, reverse=True)
sorted_engagement_rate = [engagement_rate[languages.index(lang)] for lang in sorted_languages]

# Plot
plt.figure(figsize=(12, 6))
x = np.arange(len(sorted_languages[:10]))
bar_width = 0.35

fig, ax1 = plt.subplots()

ax1.bar(x, sorted_users[:10], color='b', alpha=0.7, label='Number of Users')
ax1.set_xlabel('Languages')
ax1.set_ylabel('Number of Users', color='b')
ax1.tick_params('y', colors='b')
ax1.set_xticks(x)
ax1.set_xticklabels(sorted_languages[:10], rotation=45, ha='right')

ax2 = ax1.twinx()
ax2.plot(x, sorted_engagement_rate[:10], color='r', marker='o', label='Engagement Rate')
ax2.set_ylabel('Engagement Rate', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.title('Top 10 Languages by Number of Users and Their Engagement Rate')

plt.show()


# # Recommendations for Optimizing Sales Performance

# In[75]:


import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
recommendations = ['Improve Marketing Strategies', 'Target Specific Customer Segments', 'Enhance Product Offerings']
expected_benefits = [30, 25, 20]  # Expected benefits percentage for each recommendation

# Plotting
plt.figure(figsize=(10, 6))
plt.barh(recommendations, expected_benefits, color='blue')
plt.xlabel('Expected Benefits (%)')
plt.title('Recommendations for Optimizing Sales Performance')
plt.gca().invert_yaxis()  # Invert y-axis to display the most important recommendation on top
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()


# In[ ]:




