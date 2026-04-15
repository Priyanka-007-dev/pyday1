import pandas as pd

# Read CSV file
df = pd.read_csv("employees.csv")

#  Average salary per department
avg_salary = df.groupby("DEPT")["SALARY"].mean()
print("Average Salary per Department:")
print(avg_salary)

#  Highest paid employee per department
highest_paid = df.loc[df.groupby("DEPT")["SALARY"].idxmax()]
print("\nHighest Paid Employee per Department:")
print(highest_paid)

#  Bonus: Count employees per department
count_emp = df.groupby("DEPT")["NAME"].count()
print("\nEmployee Count per Department:")
print(count_emp)

#  Bonus: Sort departments by average salary
sorted_dept = avg_salary.sort_values(ascending=False)
print("\nDepartments sorted by Average Salary:")
print(sorted_dept)
