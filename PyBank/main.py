import pandas as pd
import os

#importing data / dataframes
data_file1 = os.path.join("budget_data_1.csv")
data1 = pd.read_csv(data_file1)
df1 = pd.DataFrame(data1)

data_file2 = os.path.join("budget_data_2.csv")
data2 = pd.read_csv(data_file2)
df2 = pd.DataFrame(data2)

#merging and cleaning data
df = df1.append(df2)
df['Date'] = df['Date'].replace({'2009':'09','2010':'10','2011':'11','2012':'12','2013':'13','2014':'14',
                                '2015':'15','2016':'16'}, regex=True)
df['Revenue'] = pd.to_numeric(df['Revenue'])

#calculating variables
count = str((len(set(df['Date']))))
total = sum(df['Revenue'])
avg = round(df['Revenue'].mean())
mx = df['Revenue'].argmax()
mn = df['Revenue'].argmin()

#display report
print("Financial Analysis")
print("------------------------")
print("Total Months: " + count)
print("Total Revenue: $" + str(total))
print("Average Revenue Change: $" + str(avg))
print("Greatest Increase In Revenue: " + str(df.iloc[mx,0]) + " ($" + str(df.iloc[mx,1]) + ")")
print("Greatest Decrease In Revenue: " + str(df.iloc[mn,0]) + " ($" + str(df.iloc[mn,1]) + ")")

#output lines to text file
outF = open("myOutFile.txt", "w")
outF.write("-----------------------")
outF.write("\n")
outF.write("Financial Analysis")
outF.write("\n")
outF.write("------------------------")
outF.write("\n")
outF.write("Total Months: " + count)
outF.write("\n")
outF.write("Total Revenue: $" + str(total))
outF.write("\n")
outF.write("Average Revenue Change: $" + str(avg))
outF.write("\n")
outF.write("Greatest Increase In Revenue: " + str(df.iloc[mx,0]) + " ($" + str(df.iloc[mx,1]) + ")")
outF.write("\n")
outF.write("Greatest Decrease In Revenue: " + str(df.iloc[mn,0]) + " ($" + str(df.iloc[mn,1]) + ")")
outF.close()
