
# coding: utf-8

# In[116]:


import pandas as pd
import os


# In[117]:


#importing data / dataframes
data_file1 = os.path.join("election_data_1.csv")
data1 = pd.read_csv(data_file1)
df1 = pd.DataFrame(data1)


# In[118]:


data_file2 = os.path.join("election_data_2.csv")
data2 = pd.read_csv(data_file2)
df2 = pd.DataFrame(data2)


# In[119]:


#merging and cleaning data
df = df1.append(df2)


# In[143]:


#calculating variables
count = str((len(set(df['Voter ID']))))


# In[144]:


#create revised dataframe (auto sorts desc)
df_list = df['Candidate'].value_counts()
df_list = df_list.reset_index()


# In[148]:


#Display
print("Election Results")
print("-----------------------")
print("Total Votes: " + count)
print("-----------------------")
#loop through each row in revised dataframe, display name and calculate percentage and total vote count
for index, row in df_list.iterrows():
    print(row['index'] + ": " + "{0:.0f}%".format(round(row['Candidate']/int(count),2)*100) + " (" + str(row['Candidate']) + ")")
print("-----------------------")
print("Winner: " + df_list.iloc[0,0]) # displays first in df_list which is automatically highest value
print("-----------------------")

#output lines to text file
outF = open("myOutFile.txt", "w")
outF.write("-----------------------")
outF.write("Election Results")
outF.write("\n")
outF.write("-----------------------")
outF.write("\n")           
outF.write("Total Votes: " + count)
outF.write("\n")           
outF.write("-----------------------")
outF.write("\n")           
for index, row in df_list.iterrows():
    outF.write(row['index'] + ": " + "{0:.0f}%".format(round(row['Candidate']/int(count),2)*100) + " (" + str(row['Candidate']) + ")")
    outF.write("\n")
outF.write("-----------------------")               
outF.write("\n")
outF.write("Winner: " + df_list.iloc[0,0]) 
outF.write("\n")
outF.write("-----------------------")                      
outF.close()


