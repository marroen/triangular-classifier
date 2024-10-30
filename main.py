import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import random
import argparse

def main():
  parser = argparse.ArgumentParser(description="Triangular Classifier.")
  parser.add_argument('-n', dest="n", required=True, type=int, help="The number of vertices.")
  parser.add_argument('-f', dest="f", required=True, type=float, help="Noise in the data.")
  parser.add_argument('-p', dest="p", required=False, type=int, help="The number to add to both x and y of the triangle to scale the perimeter.")
  parser.set_defaults(p=0)

  args = parser.parse_args()
  n = args.n
  f = args.f
  p = -args.p

  x = []
  y = []
  classes = []


  # Define triangle vertices
  triangle_x = [3+p, 7-p, 7-p, 3+p]  # Close the triangle by adding the first point at the end
  triangle_y = [3+p, 3+p, 7-p, 3+p]

  for _ in range(0, n):
    x.append(random.randint(0, 9) + random.random())
    y.append(random.randint(0, 9) + random.random())
    label = 1
    if(x[-1]>7-p):
        label = 0
    if(y[-1]<3+p):
        label = 0
    if(y[-1]>x[-1]):
        label = 0
        
    if(random.randint(0, 99) < f*100):
        label = 1 - label
    classes.append(label)

  plt.scatter(x, y, c=classes)
  plt.title(f"n = {n}, f = {f}, p = {p}")



  # Plot the triangle on the same plot
  plt.plot(triangle_x, triangle_y, 'b-', marker='o', markersize=8, label='Triangle')
  plt.grid(True)
  plt.legend()
  plt.show() 
  
  knn = KNeighborsClassifier(n_neighbors=7)
  knn.fit(list(zip(x,y)), classes)
  counter = 0
  for _ in range (10000):
      x_1 = random.randint(0, 9) + random.random()
      y_1 = random.randint(0, 9) + random.random()
      
      testlabel = 1
      
      if(x_1>7-p):
          testlabel = 0
      if(y_1<3+p):
          testlabel = 0
      if(y_1>x_1):
          testlabel = 0
      
        
      prediction = knn.predict([(x_1, y_1)])
      
      if(testlabel != prediction):
          counter = counter+ 1
    
  print(counter)
      
      
      

if __name__ == "__main__":
    main()