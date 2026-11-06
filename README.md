
##School Infrastructure and Attendance Analysis

A county-level analysis of school infrastructure influence on student attendance percentage in Bomet, Kericho, and Narok counties.
Evaluates classroom capacity against attendance rates and reports findings to the National Office of Education.

##What It Does

- Cleans duplicated infrastructure records and standardizes school datasets
- Merges attendance and infrastructure data by school and region
- Calculates correlation between number of classrooms and attendance percentage
- Generates scatter plot for attendance vs classroom capacity with influence interpretation

##Setup

pip install pandas matplotlib
##Usage
from analysis import Combined

corr = Combined["avg_att_pct"].corr(Combined["no_classrooms"])
print(f"Correlation: {corr:.3f}")
##Sample Output
Correlation: -0.009
No significant influence of school infrastructure on attendance (r=-0.009) - attendance is driven by factors beyond classroom capacity.
##Stack

Python, pandas, matplotlib

