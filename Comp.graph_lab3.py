import csv
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull


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


cv = ConvexHull(coord)
hull_dots = cv.vertices
# the vertices of the convex hull
inside_dots = set(range(len(coord))).difference(cv.vertices)
# the vertices inside the convex hull

coord_hull_dots = []
for i in hull_dots:
    coord_hull_dots.append(coord[i])

coord_inside_dots = []
for i in inside_dots:
    coord_inside_dots.append(coord[i])

x_ax, y_ax = [], []
x_ax_hull, y_ax_hull = [], []

for i in coord_inside_dots:
    x_ax.append(i[0])
    y_ax.append(i[1])

for i in coord_hull_dots:
    x_ax_hull.append(i[0])
    y_ax_hull.append(i[1])

fig = plt.figure()
fig.set_size_inches(convert_pixels_to_inches(960),convert_pixels_to_inches(540))
plt.plot(x_ax_hull, y_ax_hull, color='blue')
plt.scatter(x_ax, y_ax, color='black', s = 0.3)
plt.show()