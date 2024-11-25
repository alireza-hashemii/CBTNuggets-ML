import matplotlib.pyplot as plt

x = [2.75, 4, 3.85, 3, 4.8, 1.13, 
    2.3, 3.7, 5, 4.05,1.5,1.8,1,3.3,
]

y = [33, 66, 60, 44, 88, 11, 30,
    54, 99, 66.5, 25, 27, 6, 62
]

plt.scatter(x, y)
plt.xlabel("GPA SCORE")
plt.ylabel("APPLY RATE")
plt.show()