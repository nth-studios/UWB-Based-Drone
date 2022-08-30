import matplotlib.pyplot as plt
import numpy as np
import random

random.seed()

simNum = 1000
noiseVar = 0.2


y = [0, 1.5, 0, 0]#, 2.5]
x = [0, 0, 1.5, 0]#, 2.5]
z = [0, 0, 0, 1.5]#, 0]
n = ["A1","A2","A3","A4"]#,"A5"]

fig, ax = plt.subplots()


randAm = noiseVar

#ax.annotate("PT", (point[0], point[1]))


ax.set_aspect('equal', adjustable='box')
ax.set_xlim((-0.5, 5.5))
ax.set_ylim((-0.5, 5.5))

#circle1 = plt.Circle((0, 0), rangeA1, color='b', fill=False)
#circle2 = plt.Circle((0, 5), rangeA2, color='b', fill=False)
#circle3 = plt.Circle((5, 5), rangeA3, color='b', fill=False)
#circle4 = plt.Circle((5, 0), rangeA4, color='b', fill=False)

#ax.add_patch(circle1)
#ax.add_patch(circle2)
#ax.add_patch(circle3)
#ax.add_patch(circle4)


# for i, txt in enumerate(n):
#     ax.annotate(txt, (x[i], y[i]))

#math stuff start
pointX = []
pointY = []
pointZ = []
calcX = []
calcY = []
calcZ = []
errors = []

for i in range(simNum):

    point = [random.random()*5, random.random()*5, random.random()*3]


    rangeA1 = np.sqrt((x[0]-point[0])**2 + (y[0]-point[1])**2 + (z[0]-point[2])**2) + (random.random()-0.5)*randAm
    rangeA2 = np.sqrt((x[1]-point[0])**2 + (y[1]-point[1])**2 + (z[1]-point[2])**2) + (random.random()-0.5)*randAm
    rangeA3 = np.sqrt((x[2]-point[0])**2 + (y[2]-point[1])**2 + (z[2]-point[2])**2) + (random.random()-0.5)*randAm
    rangeA4 = np.sqrt((x[3]-point[0])**2 + (y[3]-point[1])**2 + (z[3]-point[2])**2) + (random.random()-0.5)*randAm

    print(rangeA1, rangeA2, rangeA3, rangeA4)#, rangeA5)


    matA = np.matrix([[2*(x[0]-x[1]), 2*(y[0]-y[1]), 2*(z[0]-z[1])],
                      [2*(x[0]-x[2]), 2*(y[0]-y[2]), 2*(z[0]-z[2])],
                      [2*(x[0]-x[3]), 2*(y[0]-y[3]), 2*(z[0]-z[3])]])#,
                      #[2*(x[0]-x[3]), 2*(y[0]-y[3]), 2*(z[0]-z[3])]])

    matX = np.matrix([[point[0]], [point[1]], [point[2]]])

    matB = np.matrix([[(x[0]**2-x[1]**2)+(y[0]**2-y[1]**2)+(z[0]**2-z[1]**2)+(rangeA2**2-rangeA1**2)],
                      [(x[0]**2-x[2]**2)+(y[0]**2-y[2]**2)+(z[0]**2-z[2]**2)+(rangeA3**2-rangeA1**2)],
                      [(x[0]**2-x[3]**2)+(y[0]**2-y[3]**2)+(z[0]**2-z[3]**2)+(rangeA4**2-rangeA1**2)]])

    matAT = np.transpose(matA)
    matATA = np.matmul(matAT, matA)
    #print(np.linalg.det(matATA))

    matATB = np.matmul(matAT, matB)
    matLST = np.divide(matATB, matATA)

    lstsq = np.linalg.lstsq(matA, matB, rcond=None)[0]

    truArr = np.array([[True, False, False],
                       [False, True, False],
                       [False, False, True],])

    lstmn = []
    lstmn.append([np.extract(truArr, matLST)[0]])
    lstmn.append([np.extract(truArr, matLST)[1]])
    lstmn.append([np.extract(truArr, matLST)[2]])
    lstmn =  np.array(lstmn)

    print()
    print("Input Coordinates:\n", matX)
    print("Output Coordinates ALG:\n", lstsq)
    print("Output Coordinates MAN:\n", lstmn)

    error = matX - lstsq
    print("Estimation Error:\n", error)

    print()

    calcX.append(float(lstsq[0]))
    calcY.append(float(lstsq[1]))
    calcZ.append(float(lstsq[2]))
    pointX.append(point[0])
    pointY.append(point[1])
    pointZ.append(point[2])

    error = np.sqrt((float(lstsq[0]) - point[0]) ** 2 + (float(lstsq[1]) - point[1]) ** 2
                      + (float(lstsq[2]) - point[2]) ** 2)
    errors.append(error)

#ax.annotate("Error", (float(lstsq[0]), float(lstsq[1])))

ax.scatter(pointX, pointY, label = "Tag")
ax.scatter(calcX, calcY, label = "Calculated")




errorX = []
errorY = []

errnum = 0

for i in range(len(errors)):
    if(errors[i]>0.5):
        errorX.append(calcX[i])
        errorY.append(calcY[i])
        errnum+=1

ax.scatter(errorX, errorY, label = "Errors", color="r")
ax.scatter(x, y, label = "Anchors")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          ncol=4)

print(max(errors))
print(errnum)
print("Error percentage: " + str(errnum/simNum*100) + "%")
# print(matA)
# print(matAT)
# print(matATA)
#
# print(matX)
# print(matB)
plt.show()