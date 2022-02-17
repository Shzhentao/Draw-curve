import os
import matplotlib.pyplot as plt


if __name__ == "__main__":
    rootDir = "./input"
    relativelyIndex = 10
    numList = [[], [], [], [], []]
    # print(numList)
    firstDirIndex = 0
    label = []
    for firstDir in os.listdir(rootDir):
        evalFile = os.path.join(rootDir, firstDir, "eval0.log")
        with open(evalFile, 'r') as f:
            for line in f:
                relativelyIndex += 1
                if line[:5] == "test:":
                    relativelyIndex = 0
                if relativelyIndex == 3:
                    numString = line.strip().split("Acc@1 ")[-1][11:][:9]
                    num = float(numString)
                    numList[firstDirIndex].append(num)
        label.append(firstDir)
        firstDirIndex += 1
    x = list(range(len(numList[0])))
    label = ["AVC", "AVID", "AVAC NOT SIMPLE", "SCRATCH", "AVAC SIMPLE"]
    for index in range(5):
        plt.plot(x, numList[index], label = label[index])
        plt.legend(loc='upper left')
    outputFigure = "./output/audioRecognition.png"
    plt.savefig(outputFigure)
    plt.show()
    
