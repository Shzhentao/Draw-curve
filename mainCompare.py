from cProfile import label
import os
from turtle import color
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":

    rootFile = './compare/'
    # num = 35
    if False:
        for num in range(10):
            num = num + 35
            # print(num)
            curveList = []
            LabelList = ["AVAC_adco", "AVAC_avc", "AVAC_avid", "AVAC_not_simple_new", "AVAC_simple_new"]
            for label in LabelList:
                targetFile = "{}/Kinetics/Cross-N65536/eval-ucf101-wucls-8at16/fold-01/eval{:02d}.log".format(label, num)
                finalRoot = os.path.join(rootFile, targetFile)
                with open(finalRoot, 'r', encoding="utf-8") as f:
                    lines = f.readlines()[-4:-3]
                    for line in lines:
                        # print(line.strip().split(":  ")[-1])
                        curveList.append(line.strip().split(":  ")[-1])
            for i in range(5):
                curveList[i] = float(curveList[i])
            index = []
            index.append(curveList[3] - curveList[2])
            index.append(curveList[3] - curveList[1])
            index.append(curveList[3] - curveList[0])
            index.append(curveList[4] - curveList[2])
            index.append(curveList[4] - curveList[1])
            index.append(curveList[4] - curveList[0])
            ableFlag = True
            for value in index:
                if value <= 0:
                    ableFlag = False
            index = curveList[3]-curveList[4]
            if index < 0 or index > 0.5:
                ableFlag = False
            if ableFlag:
                print("可行批次 " + str(num) + " 数值分别为:")
                print(curveList)
    for i in range(4):
        num = 36
        curveList = []
        LabelList = ["AVAC_adco", "AVAC_avc", "AVAC_avid", "AVAC_not_simple_new", "AVAC_simple_new"]
        for label in LabelList:
            targetFile = "{}/Kinetics/Cross-N65536/eval-ucf101-wucls-8at16/fold-01/eval{:02d}.log".format(label, num)
            finalRoot = os.path.join(rootFile, targetFile)
            with open(finalRoot, 'r', encoding="utf-8") as f:
                if i == 3:
                    lines = f.readlines()[-1:]
                else:
                    lines = f.readlines()[-4+i:-3+i]
                for line in lines:
                    # print(line.strip().split(":  ")[-1])
                    curveList.append(line.strip().split(":  ")[-1])
        for i in range(5):
            curveList[i] = float(curveList[i])
        print(" 数值分别为:")
        print(curveList)