import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import random
import argparse

def main():
  parser = argparse.ArgumentParser(description="Triangular Classifier.")
  parser.add_argument('-n', dest="n", required=False, type=int, help="The number of vertices.")
  args = parser.parse_args()
  n = args.n

  x = []
  y = []
  classes = []

  for _ in range(0, n):
    x.append(random.randint(0, 8) + random.random())
    y.append(random.randint(0, 8) + random.random())
    classes.append(random.randint(0,1))

  plt.scatter(x, y, c=classes)
  plt.show() 

if __name__ == "__main__":
    main()