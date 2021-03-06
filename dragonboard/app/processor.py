import threading
import os
import time
import ProcessList as pl

class Processor():
    
    def __init__(self, app):
        self.app = app
        self.savePath = "./scans/"

    def scanImage(self):
        self.processThread = threading.Thread(target=self.run)
        self.processThread.start()

    def run(self):
        filename = "scan_" + self.getFileName() + ".jpg"
        saveTo = self.savePath + filename
        os.system("ffmpeg -i /dev/video0 -frames 1 " + saveTo)
        success = True
        list = []
        try:
            self.app.setInfoMessage("Scanning complete. Converting...")
            list = pl.process_list(saveTo, filename)
        except Exception as e:
            success = False
            print(e)

        rawData, displayText = self.processList(list)
        if success:
            self.app.displayList(rawData, displayText)
        else:
            self.app.displayList(None, "Something went wrong. Please try again.")

    def getFileName(self):
        timeStruct = time.strptime(time.ctime())
        return \
            self.padLeft(timeStruct.tm_year) + \
            self.padLeft(timeStruct.tm_mon) + \
            self.padLeft(timeStruct.tm_mday) + "_" + \
            self.padLeft(timeStruct.tm_hour) + \
            self.padLeft(timeStruct.tm_min) + \
            self.padLeft(timeStruct.tm_sec)

    def padLeft(self, num):
        if num < 10:
            return "0" + str(num)
        else:
            return str(num)

    def processList(self, list):
        print("===========1")
        print(list)
        print("===========2")
        rawData = {}
        for pair in list:
            toAdd = pair["quantity"]
            if pair["item"] in rawData:
                rawData[pair["item"]] += toAdd
            else:
                rawData[pair["item"]] = toAdd
        print(rawData)
        print("===========3")
        displayText = ""
        for key, value in rawData.items():
            displayText += "- " + key + ": " + str(value) + "\n"
        print(displayText)
        print("===========4")
        return rawData, displayText


