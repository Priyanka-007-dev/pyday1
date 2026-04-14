import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

#  Calculate average marks per student
df["AVERAGE"] = (df["MATH"] + df["SCIENCE"] + df["ENGLISH"]) / 3

#  Find topper
topper = df.loc[df["AVERAGE"].idxmax()]

#  Count students above average
class_avg = df["AVERAGE"].mean()
above_avg_count = (df["AVERAGE"] > class_avg).sum()

#  Bonus: Add grade column
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

df["GRADE"] = df["AVERAGE"].apply(get_grade)

#  Bonus: Subject-wise average
subject_avg = {
    "MATH": df["MATH"].mean(),
    "SCIENCE": df["SCIENCE"].mean(),
    "ENGLISH": df["ENGLISH"].mean()
}

#  Output
print("Student Data:\n")
print(df)

print("\nTopper:")
print(topper["NAME"], "-", topper["AVERAGE"])

print("\nStudents Above Class Average:", above_avg_count)

print("\nSubject-wise Average:")
for subject, avg in subject_avg.items():
    print(f"{subject}: {avg}")
