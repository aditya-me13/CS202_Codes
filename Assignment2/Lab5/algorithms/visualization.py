import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Parse XML file
tree = ET.parse('coverage_new.xml')
root = tree.getroot()

# Extract coverage data
files = []
coverages = []

for package in root.findall(".//package"):
    for cls in package.findall(".//class"):
        filename = cls.get("filename")
        line_rate = float(cls.get("line-rate")) * 100
        files.append(filename)
        coverages.append(line_rate)

# Sort by coverage
sorted_indices = np.argsort(coverages)
files_sorted = np.array(files)[sorted_indices]
coverages_sorted = np.array(coverages)[sorted_indices]

# Plot file index vs coverage
plt.figure(figsize=(12, 6))
sns.barplot(x=np.arange(1, len(files) + 1), y=coverages_sorted, palette="Blues")
plt.xlabel("File Number (Sorted by Coverage)")
plt.ylabel("Coverage (%)")
plt.title("File Coverage Percentage")
plt.xticks(rotation=90)
plt.show()

# Plot coverage distribution
plt.figure(figsize=(8, 5))
sns.histplot(coverages, bins=np.arange(0, 110, 10), kde=True, color="blue")
plt.xlabel("Coverage (%)")
plt.ylabel("Number of Files")
plt.title("Coverage Distribution")
plt.show()

# Pie chart for coverage categories
full_coverage = sum(1 for c in coverages if c == 100)
partial_coverage = sum(1 for c in coverages if 0 < c < 100)
no_coverage = sum(1 for c in coverages if c == 0)

sizes = [no_coverage, partial_coverage, full_coverage]
labels = ["No Coverage", "Partial Coverage", "Full Coverage"]
colors = sns.color_palette("Blues", 3)

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)
plt.title("Coverage Categories")
plt.show()
