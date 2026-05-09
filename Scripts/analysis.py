import pandas as pd
#load dataset
df=pd.read_csv('data/incident_data.csv')
#Removes hidden spaces. Prevents random failures - Key Errors
df.columns = df.columns.str.strip()
#Instead of guessing column names, you can see exactly what pandas read
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
def priority_weight(priority):
    if priority == 'High':
        return 3
    elif priority == 'Medium':
        return 2
    else:
        return 1

df['Priority_Score'] = df['Priority'].apply(priority_weight)
df['Weighted_MTTR'] = df['MTTR_hrs'] * df['Priority_Score']

#add SLA compliance column
# SLA targets
def sla_target(priority):
    if priority == 'High':
        return 8
    elif priority == 'Medium':
        return 24
    else:
        return 48

# apply SLA target
df['SLA_Target_hrs'] = df['Priority'].apply(sla_target)

# breach check
df['SLA_Breach'] = df['MTTR_hrs'] > df['SLA_Target_hrs']

print("\nMean Time to Resolve (MTTR) in hours:")
print("Average MTTR:", df['MTTR_hrs'].mean())

print("\nIncident MTTR Details:")
print(df[['Incident_ID', 'Priority', 'MTTR_hrs']])

print("\nSLA Compliance Details:")
print(df[['Incident_ID', 'Priority', 'MTTR_hrs',
          'SLA_Target_hrs', 'SLA_Breach', 'Priority_Score', 'Weighted_MTTR']])

# -----------------------------
# SAVE CLEANED DATASET
# -----------------------------

df.to_csv('data/Cleaned_incident_data.csv', index=False)

print("\nCleaned dataset saved successfully!")
