import matplotlib.pyplot as plt

names = ['A', 'B', 'C']
marks = [80, 90, 70]

# Line Chart
plt.plot(names, marks)
plt.title("Line Chart")
plt.show()

# Bar Chart
plt.bar(names, marks)
plt.title("Bar Chart")
plt.show()

# Histogram
plt.hist(marks)
plt.title("Histogram")
plt.show()

# Pie Chart
plt.pie(marks, labels=names, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
