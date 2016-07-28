import pandas as pd
import os
os.chdir('/Users/haozeng/Desktop/BI_Analyst_HW')
data = pd.read_csv('NEISS2014.csv')
top3_bodypart = data['body_part'].value_counts().iloc[:3]
top3_bodypart
low3_bodypart = data['body_part'].value_counts().sort_values().iloc[:3]
low3_bodypart
n_skateboard =len(data[data['narrative'].str.contains('SKATEBOARD')])
n_skateboard
data_sk = data[data['narrative'].str.contains('SKATEBOARD')]
male_p = data_sk['sex'].value_counts().iat[0] / float(n_skateboard)
female_p = 1- male_p
mean_age = data_sk['age'].mean()
mean_age
count_n = data['diag'].value_counts()
hosp_n = data[data['disposition'] == 4]['diag'].value_counts()
(hosp_n / count_n).idxmax()
(hosp_n / count_n).max()
leav_n = data[data['disposition'] == 6]['diag'].value_counts()
(leav_n / count_n).max()
(leav_n / count_n).idxmax()
%history -f indeed.py
