import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import random
import argparse

def main():
  parser = argparse.ArgumentParser(description="Triangular Classifier.")
  parser.add_argument('-n', dest="n", required=True,  type=int, help="The number of vertices.")
  parser.add_argument('-p', dest="p", required=False, type=int, help="The number to add to both x and y of the triangle to scale the perimeter.")
  parser.set_defaults(p=0)

  args = parser.parse_args()
  n = args.n
  p = args.p

  x = []
  y = []
  classes = []

  for _ in range(0, n):
    x.append(random.randint(0, 8) + random.random())
    y.append(random.randint(0, 8) + random.random())
    classes.append(random.randint(0,1))

  plt.scatter(x, y, c=classes)
  plt.title(f"n = {n}")

  # Define triangle vertices
  triangle_x = [3+p, 7-p, 7-p, 3+p]  # Close the triangle by adding the first point at the end
  triangle_y = [3+p, 3+p, 7-p, 3+p]

  # Plot the triangle on the same plot
  plt.plot(triangle_x, triangle_y, 'b-', marker='o', markersize=8, label='Triangle')
  plt.grid(True)
  plt.legend()
  plt.show() 

if __name__ == "__main__":
    main()