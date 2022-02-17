from cProfile import label
import os
from turtle import color
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":
    rootFile = './checkpoints'
    curveList = [[],[],[],[],[],[]]
    LabelList = []
    print(curveList)
    flagTest = 100
    flagTest50 = 100
    fileIndex = 0
    for filename in os.listdir(rootFile):
        LabelList.append(filename)
        evalFile = os.path.join(rootFile, filename, "eval0.log")
        with open(evalFile) as f:
            lines = f.readlines()
            for line in lines:
                flagTest50 += 1
                flagTest += 1
                if line[:14] == 'test: Epoch 50':
                    flagTest50 = 0
                elif line[:5] == 'test:':
                    flagTest = 0
                if flagTest == 5:
                    numstr = float(line.split("Acc@1 ")[1].split("(")[1][:9])
                    curveList[fileIndex].append(numstr)
                if flagTest50 == 17:
                    numstr = float(line.split("Acc@1 ")[1].split("(")[1][:9])
                    curveList[fileIndex].append(numstr)
        fileIndex += 1
    
    xList = list(range(51))
    print(LabelList)
    plt.plot(xList, curveList[0], color='green', label = LabelList[0])
    plt.plot(xList, curveList[1], color='red', label = LabelList[1])
    plt.plot(xList, curveList[2], color='skyblue', label = LabelList[2])
    plt.plot(xList, curveList[3], color='blue', label = LabelList[3])
    plt.plot(xList, curveList[4], color='black', label = LabelList[4])
    plt.plot(xList, curveList[5], color='yellow', label = LabelList[5])
    plt.legend()
    outputFigure = "./output/actionRecognition.png"
    plt.savefig(outputFigure)
    plt.show()


                