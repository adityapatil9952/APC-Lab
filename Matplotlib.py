# Line Plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.show()


# ==========================================================


# title labels

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.title("Simple Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

# ===========================================================

# Markers

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker="o")

plt.show()

# ===========================================================

# Multiple Lines

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1)
plt.plot(x, y2)

plt.show()

# ===========================================================

# Bar chart

import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [80, 65, 90, 75]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

# ===========================================================

# Horizontal bar
 
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [80, 65, 90, 75]

plt.barh(students, marks)

plt.title("Student Marks")

plt.show()

# ===========================================================

# Scatter Plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 8, 7]

plt.scatter(x, y)

plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

# ===========================================================

# Pie chart

import matplotlib.pyplot as plt

subjects = ["Java", "Python", "C", "HTML"]
hours = [10, 8, 5, 7]

plt.pie(hours, labels=subjects)

plt.title("Study Hours")

plt.show()

# ===========================================================

# Histogram

import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 60, 65, 70, 70, 75, 80, 85, 90]

plt.hist(marks)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

# ===========================================================

# Legend

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1, label="Even Numbers")
plt.plot(x, y2, label="Odd Numbers")

plt.legend()

plt.show()

# ===========================================================

# Subplot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Line Graph")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Bar Graph")

plt.show()