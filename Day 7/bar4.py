import matplotlib.pyplot as plt

students = ["Amit", "Bhavya", "Chetan", "Deepak"]
marks = [85, 92, 78, 88]

colors = ["red", "blue", "green", "orange"]

plt.bar(students, marks, color=colors)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()