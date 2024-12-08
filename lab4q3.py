# List of course codes
course_codes = ["CS1001", "CS1002", "CS1003"]

# List of course names
course_names = ["Python", "Data Structures", "Algorithms"]

# Combining both lists into the desired format
combined_courses = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]

# Display the result
print(combined_courses)
