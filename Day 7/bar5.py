import matplotlib.pyplot as plt

students = ["Amit", "Bhavya", "Chetan", "Deepak"]
marks = [85, 92, 78, 88]

plt.bar(students, marks)

for i, mark in enumerate(marks):
    plt.text(i, mark+1, mark)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()