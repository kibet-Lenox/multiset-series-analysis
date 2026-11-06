import pandas as pd
import matplotlib.pyplot as plt

Sample_school = pd.DataFrame({
    "School_name": ["Bomet Boys", "Kericho High", "Tenwek High", "Kericho Tea", "Kipsuter Boys"],
    "Average_att_pct": [82, 65, 73, 92, 52],
    "County": ["Bomet", "Kericho", "Bomet", "Kericho", "Narok"]
})

School_infrastructure = pd.DataFrame([
    ["Bomet Boys", 18, True, 18, "Bomet"],
    ["Kericho High", 25, True, 25, "Kericho"],
    ["Tenwek High", 19, False, 19, "Bomet"],
    ["Kericho Tea", 12, False, 12, "Kericho"],
    ["Kipsuter Boys", 10, False, 10, "Narok"]
], columns=["School", "no_classrooms", "Water_access", "no_classrooms", "County_name"])

School_infrastructure = School_infrastructure.loc[:, ~School_infrastructure.columns.duplicated()]

Sample_school = Sample_school.rename(columns={
    "School_name": "school",
    "County": "region",
    "Average_att_pct": "avg_att_pct"
})

School_infrastructure = School_infrastructure.rename(columns={
    "County_name": "region",
    "School": "school"
})

School_infrastructure = School_infrastructure.drop_duplicates()

Combined = pd.merge(Sample_school, School_infrastructure, on=["school", "region"], how="inner")

corr = Combined["avg_att_pct"].corr(Combined["no_classrooms"])
print(f"Correlation: {corr:.3f}")

plt.scatter(Combined["no_classrooms"], Combined["avg_att_pct"])
plt.xlabel("Number of Classrooms")
plt.ylabel("Average Attendance %")
plt.title("Attendance vs Classrooms")
plt.show()

if corr > 0.5:
    print(f"Strong positive influence: More classrooms -> higher attendance (r={corr:.3f})")
elif corr > 0.2:
    print(f"Weak positive influence: Slight increase in attendance (r={corr:.3f})")
elif corr < -0.2:
    print(f"Negative influence: More classrooms -> lower attendance (r={corr:.3f})")
else:
    print(f"No significant influence on attendance (r={corr:.3f})")
