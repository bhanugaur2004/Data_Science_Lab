import matplotlib.pyplot as plt

students = ["Amit", "Bhavya", "Chetan", "Deepak", "Esha"]
marks = [85, 92, 78, 88, 95]

plt.barh(students, marks)

plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Student Marks - Horizontal Bar Chart")

plt.show()