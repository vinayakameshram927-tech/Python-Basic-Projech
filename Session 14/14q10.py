import numpy as np
print("++++  Student Marks Analyzer  ++++")

# Generate random marks for 10 students and 5 subjects
marks = np.random.randint(30, 101, (10, 5))

# Print the marks array
print("Student Marks:")
print(marks)

# Calculate total marks for each student
total = np.sum(marks, axis=1)
print("\nTotal Marks:")
print(total)

# Calculate average marks for each student
average = np.mean(marks, axis=1)
print("\nAverage Marks:")
print(average)

# Find student with highest total marks
highest = np.argmax(total)
print("\nStudent with Highest Total Marks:")
print("Student Number:", highest + 1)
print("Total Marks:", total[highest])

# Find student with lowest total marks
lowest = np.argmin(total)
print("\nStudent with Lowest Total Marks:")
print("Student Number:", lowest + 1)
print("Total Marks:", total[lowest])

# Calculate overall class mean
class_mean = np.mean(marks)
print("\nOverall Class Mean:", class_mean)

# Calculate overall class standard deviation
class_std = np.std(marks)
print("Overall Class Standard Deviation:", class_std)

# Reshape the array (demonstration)
reshaped = marks.reshape(5, 10)
print("\nReshaped Array (5 x 10):")
print(reshaped)

# Find the indices of the top 3 students
top3 = np.argsort(total)[-3:][::-1]

print("\nTop 3 Students:")
print(top3 + 1)

# Extract marks of the top 3 students
print("\nMarks of Top 3 Students:")
print(marks[top3])