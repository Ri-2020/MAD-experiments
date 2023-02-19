import matplotlib.pyplot as plt

# Example list of marks
marks = [1, 2, 3, 2, 1, 3, 3, 4, 2, 1, 2, 3, 4, 4, 4]

plt.hist(marks, bins=max(marks)-min(marks)+1, align='left', rwidth=0.8)

# Add x and y labels
plt.xlabel('Marks')
plt.ylabel('Frequency')

# Show the plot
plt.savefig('plot.png')
