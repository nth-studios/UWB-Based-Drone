import serial

import matplotlib.pyplot as plt
import numpy as np
import random

random.seed()

simNum = 1000
noiseVar = 0.2
filtered = True


x = [0, 5, 0, 0]
y = [0, 0, 5, 0]
z = [0, 0, 0, 3]
n = ["A1","A2","A3","A4"]


checkIn = False
print("Attempting to connect")
#usb port
#serialPort = serial.Serial(port = "COM4", baudrate=9600, timeout=10, stopbits=serial.STOPBITS_ONE)
serialPort = serial.Serial(port = "COM8", baudrate=115200, timeout=10, stopbits=serial.STOPBITS_ONE)

#bluetooth
#serialPort = serial.Serial(port = "COM11", baudrate=9600, timeout=1, stopbits=serial.STOPBITS_ONE)


if not serialPort.is_open:
    serialPort.open()

print("Successful connection")

fig, ax = plt.subplots()


randAm = noiseVar


ax.set_aspect('equal', adjustable='box')
ax.set_xlim((-0.5, 5.5))
ax.set_ylim((-0.5, 5.5))


# for i, txt in enumerate(n):
#     ax.annotate(txt, (x[i], y[i]))

#math stuff start
lstsqs = []
f = open("demo1.txt", "a")

while(True):
    if serialPort.inWaiting():


        sendStr = serialPort.readline()
        cur = sendStr.decode(encoding='ASCII',errors='ignore')
        bytecheck = cur.split(",")
        #print(bytecheck)
        if(int(bytecheck[1])==4):
            #print(float(bytecheck[7]), float(bytecheck[13]), float(bytecheck[19]), float(bytecheck[25]))

            r11 = float(bytecheck[7])
            r12 = float(bytecheck[13])
            r13 = float(bytecheck[19])
            r14 = float(bytecheck[25])

            matA = np.matrix([[2 * (x[0] - x[1]), 2 * (y[0] - y[1]), 2 * (z[0] - z[1])],
                              [2 * (x[0] - x[2]), 2 * (y[0] - y[2]), 2 * (z[0] - z[2])],
                              [2 * (x[0] - x[3]), 2 * (y[0] - y[3]), 2 * (z[0] - z[3])]])

            matB = np.matrix(
                [[(x[0] ** 2 - x[1] ** 2) + (y[0] ** 2 - y[1] ** 2) + (z[0] ** 2 - z[1] ** 2) + (
                            r12 ** 2 - r11 ** 2)],
                 [(x[0] ** 2 - x[2] ** 2) + (y[0] ** 2 - y[2] ** 2) + (z[0] ** 2 - z[2] ** 2) + (
                             r13 ** 2 - r11 ** 2)],
                 [(x[0] ** 2 - x[3] ** 2) + (y[0] ** 2 - y[3] ** 2) + (z[0] ** 2 - z[3] ** 2) + (
                             r14 ** 2 - r11 ** 2)]])

            lstsq = np.linalg.lstsq(matA, matB, rcond=None)[0]
            f.write(lstsq)
            print("Output Coordinates ALG:\n", lstsq)





for i in range(simNum):



    print(rangeA1, rangeA2, rangeA3, rangeA4)

    matA = np.matrix([[2*(x[0]-x[1]), 2*(y[0]-y[1]), 2*(z[0]-z[1])],
                      [2*(x[0]-x[2]), 2*(y[0]-y[2]), 2*(z[0]-z[2])],
                      [2*(x[0]-x[3]), 2*(y[0]-y[3]), 2*(z[0]-z[3])]])

    matB = np.matrix([[(x[0]**2-x[1]**2)+(y[0]**2-y[1]**2)+(z[0]**2-z[1]**2)+(rangeA2**2-rangeA1**2)],
                      [(x[0]**2-x[2]**2)+(y[0]**2-y[2]**2)+(z[0]**2-z[2]**2)+(rangeA3**2-rangeA1**2)],
                      [(x[0]**2-x[3]**2)+(y[0]**2-y[3]**2)+(z[0]**2-z[3]**2)+(rangeA4**2-rangeA1**2)]])

    lstsq = np.linalg.lstsq(matA, matB, rcond=None)[0]

    # iteration 2

    rangeA12 = np.sqrt((x[0] - point[0]) ** 2 + (y[0] - point[1]) ** 2 + (z[0] - point[2]) ** 2) + (
                random.random() - 0.5) * randAm
    rangeA22 = np.sqrt((x[1] - point[0]) ** 2 + (y[1] - point[1]) ** 2 + (z[1] - point[2]) ** 2) + (
                random.random() - 0.5) * randAm
    rangeA32 = np.sqrt((x[2] - point[0]) ** 2 + (y[2] - point[1]) ** 2 + (z[2] - point[2]) ** 2) + (
                random.random() - 0.5) * randAm
    rangeA42 = np.sqrt((x[3] - point[0]) ** 2 + (y[3] - point[1]) ** 2 + (z[3] - point[2]) ** 2) + (
                random.random() - 0.5) * randAm

    print(rangeA12, rangeA22, rangeA32, rangeA42)

    matA = np.matrix([[2 * (x[0] - x[1]), 2 * (y[0] - y[1]), 2 * (z[0] - z[1])],
                      [2 * (x[0] - x[2]), 2 * (y[0] - y[2]), 2 * (z[0] - z[2])],
                      [2 * (x[0] - x[3]), 2 * (y[0] - y[3]), 2 * (z[0] - z[3])]])

    matB = np.matrix(
        [[(x[0] ** 2 - x[1] ** 2) + (y[0] ** 2 - y[1] ** 2) + (z[0] ** 2 - z[1] ** 2) + (rangeA22 ** 2 - rangeA12 ** 2)],
         [(x[0] ** 2 - x[2] ** 2) + (y[0] ** 2 - y[2] ** 2) + (z[0] ** 2 - z[2] ** 2) + (rangeA32 ** 2 - rangeA12 ** 2)],
         [(x[0] ** 2 - x[3] ** 2) + (y[0] ** 2 - y[3] ** 2) + (z[0] ** 2 - z[3] ** 2) + (rangeA42 ** 2 - rangeA12 ** 2)]])

    lstsq2 = np.linalg.lstsq(matA, matB, rcond=None)[0]

    # iteration 3

    rangeA13 = np.sqrt((x[0] - point[0]) ** 2 + (y[0] - point[1]) ** 2 + (z[0] - point[2]) ** 2) + (
            random.random() - 0.5) * randAm
    rangeA23 = np.sqrt((x[1] - point[0]) ** 2 + (y[1] - point[1]) ** 2 + (z[1] - point[2]) ** 2) + (
            random.random() - 0.5) * randAm
    rangeA33 = np.sqrt((x[2] - point[0]) ** 2 + (y[2] - point[1]) ** 2 + (z[2] - point[2]) ** 2) + (
            random.random() - 0.5) * randAm
    rangeA43 = np.sqrt((x[3] - point[0]) ** 2 + (y[3] - point[1]) ** 2 + (z[3] - point[2]) ** 2) + (
            random.random() - 0.5) * randAm

    print(rangeA13, rangeA23, rangeA33, rangeA43)

    matA = np.matrix([[2 * (x[0] - x[1]), 2 * (y[0] - y[1]), 2 * (z[0] - z[1])],
                      [2 * (x[0] - x[2]), 2 * (y[0] - y[2]), 2 * (z[0] - z[2])],
                      [2 * (x[0] - x[3]), 2 * (y[0] - y[3]), 2 * (z[0] - z[3])]])

    matB = np.matrix(
        [[(x[0] ** 2 - x[1] ** 2) + (y[0] ** 2 - y[1] ** 2) + (z[0] ** 2 - z[1] ** 2) + (
                    rangeA23 ** 2 - rangeA13 ** 2)],
         [(x[0] ** 2 - x[2] ** 2) + (y[0] ** 2 - y[2] ** 2) + (z[0] ** 2 - z[2] ** 2) + (
                     rangeA33 ** 2 - rangeA13 ** 2)],
         [(x[0] ** 2 - x[3] ** 2) + (y[0] ** 2 - y[3] ** 2) + (z[0] ** 2 - z[3] ** 2) + (
                     rangeA43 ** 2 - rangeA13 ** 2)]])

    lstsq3 = np.linalg.lstsq(matA, matB, rcond=None)[0]

    # matAT = np.transpose(matA)
    # matATA = np.matmul(matAT, matA)
    #
    # matATB = np.matmul(matAT, matB)
    # matLST = np.divide(matATB, matATA)



    # truArr = np.array([[True, False, False],
    #                    [False, True, False],
    #                    [False, False, True],])
    #
    # lstmn = []
    # lstmn.append([np.extract(truArr, matLST)[0]])
    # lstmn.append([np.extract(truArr, matLST)[1]])
    # lstmn.append([np.extract(truArr, matLST)[2]])
    # lstmn = np.array(lstmn)

    lstsqFIN = lstsq + lstsq2 + lstsq3
    lstsqFIN = lstsqFIN/3

    if(filtered):
        print()
        print("Input Coordinates:\n", matX)
        print("Output Coordinates ALG:\n", lstsqFIN)
        # print("Output Coordinates MAN:\n", lstmn)

        errorMat = matX - lstsqFIN
        print("Estimation Error:\n", errorMat)

        print()

        calcX.append(float(lstsqFIN[0]))
        calcY.append(float(lstsqFIN[1]))
        calcZ.append(float(lstsqFIN[2]))
        pointX.append(point[0])
        pointY.append(point[1])
        pointZ.append(point[2])

        error = np.sqrt((float(lstsqFIN[0]) - point[0]) ** 2 + (float(lstsqFIN[1]) - point[1]) ** 2
                        + (float(lstsqFIN[2]) - point[2]) ** 2)
        errors.append(error)
    else:
        print()
        print("Input Coordinates:\n", matX)
        print("Output Coordinates ALG:\n", lstsq)
        # print("Output Coordinates MAN:\n", lstmn)

        errorMat = matX - lstsq
        print("Estimation Error:\n", errorMat)

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
ax.scatter(calcX, calcY, label = "Calculated", color='g')




errorX = []
errorY = []

errnum = 0
avgErr = 0;

for i in range(len(errors)):
    if(errors[i]>0.5):
        errorX.append(calcX[i])
        errorY.append(calcY[i])
        errnum+=1
    avgErr += errors[i]


ax.scatter(errorX, errorY, label = "Errors", color="r")
ax.scatter(x, y, label = "Anchors")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          ncol=4)

print("Maximum error: ", max(errors))
print("Total number of errors ", errnum)
print("Error percentage: " + str(errnum/simNum*100) + "%")
print("Average error: ", str(avgErr/simNum))

# print(matA)
# print(matAT)
# print(matATA)
#
# print(matX)
# print(matB)
plt.show()
