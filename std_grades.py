from functools import reduce

# 1. Data: List of dictionaries to store student information
students = []

# Function to add student information to the list
# Each student has a name, a list of grades, and a subject
def add_student(name, grades, subject):
    students.append({"name": name, "grades": grades, "subject": subject})

# Basic grade processing functions
# Calculate the average of a list of grades
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

# Get the highest grade from a list of grades
def get_highest_grade(grades):
    return max(grades) if grades else 0

# Get the lowest grade from a list of grades
def get_lowest_grade(grades):
    return min(grades) if grades else 0

# Assigning a function to a variable (Requirement #2)
# Here, we assign the calculate_average function to avg_function
avg_function = calculate_average

# List of functions (Requirement #3)
# We store several functions in a list for easy access
grade_functions = [calculate_average, get_highest_grade, get_lowest_grade]

# Passing functions as arguments (Requirement #4)
# This function accepts a function as an argument and applies it to each student's grades
def process_grades(students, func):
    return [func(student["grades"]) for student in students]

# Returning functions (Requirement #5)
# This function returns different grade calculation functions based on a given metric
def choose_grade_function(metric):
    if metric == "average":
        return calculate_average
    elif metric == "highest":
        return get_highest_grade
    elif metric == "lowest":
        return get_lowest_grade

# Mapping (Requirement #6)
# Use map to apply calculate_average to each student's grades
def map_averages():
    return list(map(lambda student: calculate_average(student["grades"]), students))

# Filtering (Requirement #7)
# Use filter to get students with an average grade above a certain threshold
def high_achievers(threshold=80):
    return list(filter(lambda student: calculate_average(student["grades"]) > threshold, students))

# Reducing (Requirement #8)
# Use reduce to sum all grades across all students
def sum_all_grades():
    return reduce(lambda acc, student: acc + sum(student["grades"]), students, 0)

# List Comprehensions (Requirement #10)
# Generate a summary report for students with names and average grades using a list comprehension
def student_summary():
    return [{"name": student["name"], "average": calculate_average(student["grades"])} for student in students]

# Recursion (Requirement #11)
# Recursive function to calculate the sum of a student's grades
# This function demonstrates recursion by summing each grade in the list one at a time
def sum_grades(grades):
    if not grades:
        return 0
    return grades[0] + sum_grades(grades[1:])

# Demonstrate each function within the menu for active use
def menu():
    while True:
        print("\n--- Student Grade Processing System ---")
        print("1. Add Student")
        print("2. View Averages") # (Using Mapping)
        print("3. View High Achievers") # (Using Filtering)
        print("4. Calculate Total Grades") # (Using Reduction)
        print("5. Generate Summary Report") # (Using List Comprehension)
        print("6. Display Grade Calculations for Each Student")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Prompt the user to enter a student's information
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grades = list(map(int, input("Enter grades separated by spaces: ").split()))
            add_student(name, grades, subject)

        elif choice == "2":
            # Mapping: Calculate average grades for each student
            averages = map_averages()
            print("Average grades:", averages)

        elif choice == "3":
            # Filtering: Find students with high average grades
            achievers = high_achievers()
            print("High Achievers:")
            for student in achievers:
                print(f"{student['name']} with average grade {calculate_average(student['grades'])}")

        elif choice == "4":
            # Reduction: Calculate the total of all grades across students
            total_grades = sum_all_grades()
            print(f"Total of all grades: {total_grades}")

        elif choice == "5":
            # List Comprehension: Generate a summary report for each student
            summary = student_summary()
            print("\n--- Student Summary Report ---")
            for student in summary:
                print(f"Student: {student['name']}, Average Grade: {student['average']}")
            print("--------------------------------")

        elif choice == "6":
            # Using function lists and passing functions to demonstrate all options
            for student in students:
                print(f"\n--- Grades for {student['name']} ---")
                for func in grade_functions:
                    result = func(student["grades"])
                    func_name = func.__name__.replace('_', ' ').title()
                    print(f"{func_name}: {result}")

                # Choose a function dynamically based on user input
                metric = input("Enter metric to calculate (average/highest/lowest): ").strip().lower()
                grade_func = choose_grade_function(metric)
                result = grade_func(student["grades"])
                print(f"{metric.title()} grade for {student['name']}: {result}")

                # Recursively sum grades
                total_recursive = sum_grades(student["grades"])
                print(f"Sum of grades (using recursion): {total_recursive}")

        elif choice == "7":
            # Exit the menu loop
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the menu function to start the program
menu()
