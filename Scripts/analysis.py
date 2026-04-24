import pandas as pd
#load dataset
df=pd.read_csv('data/incident_data.csv')
df.columns = df.columns.str.strip()
print("columns:", df.columns)

#convert data columns
df['Created_Date'] = pd.to_datetime(df['Created_Date'])
df['Resolved_Date'] = pd.to_datetime(df['Resolved_Date'])

#calculate MTTR
df['MTTR_hrs'] = (df['Resolved_Date'] - df['Created_Date']).dt.total_seconds() / 3600

print("Mean Time to Resolve (MTTR) in hours:")
print('Average MTTR:', df['MTTR_hrs'].mean())
print(df[['Incident_ID', 'MTTR_hrs']])

#saving Cleaned dataset
df.to_csv('data/Cleaned_incident_data.csv', index=False)