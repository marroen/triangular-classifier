import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import random
import argparse

def assign_label(x, y, p):
  if(x>7-p):
      return 0
  if(y<3+p):
      return 0
  if(y>x):
      return 0
  return 1

def main():
  parser = argparse.ArgumentParser(description="Triangular Classifier.")
  parser.add_argument('-n', dest="n", required=False, type=int,   help="The number of vertices.")
  parser.add_argument('-f', dest="f", required=False, type=float, help="Noise in the data.")
  parser.add_argument('-p', dest="p", required=False, type=int,   help="The number to add to both x and y of the triangle to scale the perimeter.")
  parser.set_defaults(n=800)
  parser.set_defaults(f=0)
  parser.set_defaults(p=0)

  args = parser.parse_args()
  n = args.n
  f = args.f
  p = -args.p

  # Define triangle vertices
  triangle_x = [3+p, 7-p, 7-p, 3+p]  # Close the triangle by adding the first point at the end
  triangle_y = [3+p, 3+p, 7-p, 3+p]

  # 20 experiments
  experiments = []
  for exp_i in range(20):
    x = []
    y = []
    classes = []
    # Create n training points
    for _ in range(n):
      x.append(random.randint(0, 9) + random.random())
      y.append(random.randint(0, 9) + random.random())

      # Assign label 0 if point is outside the triangle
      label = assign_label(x[-1], y[-1], p)
        
      # Introduce noise by some percentage chance of flipping label
      if(random.randint(0, 99) < f*100):
          label = 1 - label
      classes.append(label)

    # Train kNN once per experiment
    knn = KNeighborsClassifier(n_neighbors=7)
    knn.fit(list(zip(x,y)), classes)
    misclassifications = 0
    
    # Test the trained kNN on 10k test points
    for _ in range (10000):
        x_1 = random.randint(0, 9) + random.random()
        y_1 = random.randint(0, 9) + random.random()
        
        # Count number of kNN misclassifications
        testlabel = assign_label(x_1, y_1, p)
        prediction = knn.predict([(x_1, y_1)])
        if(testlabel != prediction):
            misclassifications = misclassifications+1
      
    experiments.append(misclassifications)
    print(f"Misclassifications of {exp_i}: {misclassifications}")

  for _ in range(6):
    print()
  print(experiments)

  '''
  plt.scatter(x, y, c=classes)
  plt.title(f"n = {n}, f = {f}, p = {p}")

  # Plot the triangle on the same plot
  plt.plot(triangle_x, triangle_y, 'b-', marker='o', markersize=8, label='Triangle')
  plt.grid(True)
  plt.legend()
  plt.show()
  '''

if __name__ == "__main__":
    main()
