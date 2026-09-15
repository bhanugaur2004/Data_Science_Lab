import matplotlib.pyplot as plt

students = ["Amit", "Bhavya", "Chetan", "Deepak"]
python_marks = [85, 92, 78, 88]
math_marks = [80, 89, 85, 91]

x = range(len(students))

plt.bar(x, python_marks, width=0.4, label="Python")
plt.bar([i + 0.4 for i in x], math_marks,
        width=0.4, label="Mathematics")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance")
plt.xticks([i + 0.2 for i in x], students)

plt.legend()
plt.show()