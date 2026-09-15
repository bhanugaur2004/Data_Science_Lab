import matplotlib.pyplot as plt

students = ["Amit", "Bhavya", "Chetan", "Deepak", "Esha"]
marks = [85, 92, 78, 88, 95]

plt.bar(students, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()