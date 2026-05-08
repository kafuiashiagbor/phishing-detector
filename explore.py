import pandas as pd 

#opens the CSV file and reads everything inside it. 
df = pd.read_csv("Phishing_Legitimate_full.csv")

#Fetches the first 5 rows in the table
print("First 5 rows:")
print(df.head())

#This returns two numbers which are the number of rows and the number of columns. 
print("\nShape:", df.shape)

#Prints all column names
print("\nColumns:", df.columns.tolist())

# checks every single cell and marks it True if it's empty, False if it has data.
print("\nMissing values:", df.isnull().sum().sum())

print("\nClass distribution:")
print(df["CLASS_LABEL"].value_counts())