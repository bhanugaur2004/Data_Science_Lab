import matplotlib.pyplot as plt
students = ["Amit", "Bhavya", "Chetan", "Deepak"]
python = [85, 92, 78, 88]
math = [80, 89, 85, 91]
dbms = [88, 86, 82, 90]
x = range(len(students))
width = 0.25
plt.bar([i - width for i in x], python,
        width=width, label="Python")
plt.bar(x, math,
        width=width, label="Mathematics")
plt.bar([i + width for i in x], dbms,
        width=width, label="DBMS")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance - Grouped Bar Chart")
plt.xticks(x, students)
plt.legend()
plt.show()