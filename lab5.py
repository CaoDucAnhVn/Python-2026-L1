import pandas as pd


# =========================================
# 1. LOAD DATASETS
# =========================================

students = pd.read_csv("students.csv")
scores = pd.read_csv("scores.csv")


# =========================================
# 2. STUDENTS.CSV
# =========================================

# Display first five rows
print("First five rows:")
print(students.head())


# Find number of rows and columns
print("\nNumber of rows and columns:")
print(students.shape)


# Select name and GPA
print("\nName and GPA:")
print(students[["name", "GPA"]])


# Find students with GPA >= 3.5
print("\nStudents with GPA >= 3.5:")
high_gpa = students[students["GPA"] >= 3.5]
print(high_gpa)


# Sort students by GPA
print("\nStudents sorted by GPA:")
sorted_students = students.sort_values(
    "GPA",
    ascending=False
)
print(sorted_students)


# Average GPA by major
print("\nAverage GPA by major:")
average_gpa = students.groupby("major")["GPA"].mean()
print(average_gpa)


# =========================================
# 3. CHECK MISSING VALUES
# =========================================

print("\nMissing values in students.csv:")
print(students.isnull().sum())

print("\nMissing values in scores.csv:")
print(scores.isnull().sum())


# =========================================
# 4. FILL MISSING DATA
# =========================================

# Fill missing GPA with average GPA
students["GPA"] = students["GPA"].fillna(
    students["GPA"].mean()
)

# Fill missing age with average age
students["age"] = students["age"].fillna(
    students["age"].mean()
)

# Fill missing scores with average score
scores["python"] = scores["python"].fillna(
    scores["python"].mean()
)

scores["math"] = scores["math"].fillna(
    scores["math"].mean()
)

scores["database"] = scores["database"].fillna(
    scores["database"].mean()
)


# =========================================
# 5. MERGE DATASETS
# =========================================

merged = pd.merge(
    students,
    scores,
    on="student_id"
)

print("\nMerged data:")
print(merged)


# =========================================
# 6. CALCULATE AVERAGE SCORE
# =========================================

merged["average_score"] = merged[
    ["python", "math", "database"]
].mean(axis=1)

print("\nAverage score of each student:")
print(
    merged[
        ["student_id", "name", "average_score"]
    ]
)


# =========================================
# 7. TOP 5 STUDENTS
# =========================================

top5 = merged.sort_values(
    "average_score",
    ascending=False
).head(5)

print("\nTop 5 students:")
print(
    top5[
        ["student_id", "name", "major", "average_score"]
    ]
)


# =========================================
# 8. AVERAGE SCORE BY MAJOR
# =========================================

average_score_by_major = merged.groupby(
    "major"
)["average_score"].mean()

print("\nAverage score by major:")
print(average_score_by_major)