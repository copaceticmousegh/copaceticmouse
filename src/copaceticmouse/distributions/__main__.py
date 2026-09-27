# demonstrate 10000 samples are uniform distribute

from cvdistributions import uniform
from cvdistributions import exponentialdist
from cvdistributions import poissondist
import matplotlib.pyplot as plt

points = [uniform() for _ in range(10000)]

e_points = [exponentialdist(0.5) for _ in range(10000)]

p_points = [poissondist(10) for _ in range(10000)]
#print(points)


plt.hist(points, bins=5, edgecolor="black")
plt.show()
plt.close()

plt.hist(e_points, bins=100, edgecolor="black")
plt.show()
plt.close()

plt.hist(p_points, bins=100, edgecolor="black")
plt.show()