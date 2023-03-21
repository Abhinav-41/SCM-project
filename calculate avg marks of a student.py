# Get the total number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Initialize a variable to store the total marks
total_marks = 0

# Get the marks for each subject and add it to the total_marks variable
for i in range(num_subjects):
    marks = float(input(f"Enter the marks for subject {i+1}: "))
    total_marks += marks

