
import matplotlib.pyplot as plt
import csv


def convert_pixels_to_inches(x):
    return x/96


coord = []
with open("/Users/vrublevskyi.o/Downloads/DS5.txt", 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        coord.append(line[0].split(' '))

for i, line in enumerate(coord):
    for j, value in enumerate(line):
        coord[i][j] = int(value)

x_ax, y_ax=[], []

for i in coord:
    x_ax.append(i[0])
    y_ax.append(i[1])


fig = plt.figure()
fig.set_size_inches(convert_pixels_to_inches(960),convert_pixels_to_inches(540))
plt.scatter(x_ax, y_ax, color='black');

plt.show()