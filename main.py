import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import random
import argparse

def main():
  parser = argparse.ArgumentParser(description="Triangular Classifier.")
  parser.add_argument('-n', dest="n", required=True, type=int, help="The number of vertices.")
  parser.add_argument('-f', dest="f", required=True, type=float, help="Noise in the data.")


  args = parser.parse_args()
  n = args.n
  f = args.f

  x = []
  y = []
  classes = []

  for _ in range(0, n):
    x.append(random.randint(0, 9) + random.random())
    y.append(random.randint(0, 9) + random.random())
    label = 1
    if(x[-1]>7):
        label = 0
    if(y[-1]<3):
        label = 0
    if(y[-1]>x[-1]):
        label = 0
        
    if(random.randint(0, 99) < f*100):
        label = 1 - label
    classes.append(label)

  plt.scatter(x, y, c=classes)
  plt.title(f"n = {n}")
  plt.show() 

if __name__ == "__main__":
    main()