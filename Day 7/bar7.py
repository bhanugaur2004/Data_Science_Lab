import matplotlib.pyplot as plt

classes = ["Python", "DBMS", "Data Science", "Java"]

present = [45, 40, 42, 38]
absent = [5, 10, 8, 12]

plt.bar(classes, present, label="Present")
plt.bar(classes, absent, bottom=present, label="Absent")

plt.xlabel("Subjects")
plt.ylabel("Number of Students")
plt.title("Student Attendance")

plt.legend()

plt.show()