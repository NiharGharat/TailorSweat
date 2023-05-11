# Example lists of names and marks
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
marks = [85, 92, 78, 95, 88]

# Combine the two lists using zip()
combined = dict(zip(names, marks))

# Sort the combined list based on the marks (in descending order)
top_5 = sorted(combined, key = combined.get, reverse=True)[:2]


# Get the top 5 names and marks

print(top_5)
# Print the top 5 names and marks

