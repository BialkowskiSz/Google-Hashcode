#
# Google Hash Code 2018 - Online Qualification Round
#
# Copyright (c) 2018 Team "conDITional'); DROP TABLE OPPONENTS; /*"
# Authors: Szymon Bialkowski and Simon Unsworth
#
# Version 1.0
#

from heapq import heappush, heappop

class vehicle:

    def __init__(self, location=[0,0]):
        self.location       = location
        self.drives         = []
        self.driving        = False
        self.finishedStep   = 0

    def determineClosestDrive(self, driver):
        heap    = []
       # bonus   = 0
        waiting = 0
        for i, value in enumerate(driver.allDrives):
            if not value:
                continue
            distanceToPickup = abs(self.location[0] - value[0]) + abs(self.location[1] - value[1])
            arrivalTime      = driver.currentStep + distanceToPickup
            if arrivalTime <= value[4]:
                #bonus = driver.rideOnTimeBonus
                if (value[4] - arrivalTime) > 0:
                    waiting = value[4] - arrivalTime

            #   Metric for time wasted
            steps = distanceToPickup + waiting # - bonus
            distanceToDestination = abs(value[0] - value[2]) + abs(value[1] + value[3])
            ETA = driver.currentStep + distanceToPickup + waiting + distanceToDestination
            #   If will arrive on time
            if ETA <= value[5]:
                heappush(heap, {steps: i})

        try:
            chosenDrive = heappop(heap).values()[0]
            self.drives.append(chosenDrive)
            self.driving = True
            self.location = [driver.allDrives[chosenDrive][2], driver.allDrives[chosenDrive][3]]
            self.finishedStep = ETA
            driver.allDrives[chosenDrive] = []
        except IndexError:
            pass

    def checkAvailability(self, driver):
        if driver.currentStep == self.finishedStep:
            self.driving = False
        return self.driving




class drivingRides(object):

    def __init__(self, Rows, Columns, fleetVehicles, rideOnTimeBonus, noOfSteps, drives):
        self.Rows               = Rows
        self.Columns            = Columns
        self.drivers            = [ vehicle() for _ in range(fleetVehicles) ]
        self.rideOnTimeBonus    = rideOnTimeBonus
        self.noOfSteps          = noOfSteps
        self.allDrives          = drives
        self.currentStep        = 0

    def incrementStep(self):
        self.currentStep += 1





def readFile(filename):
    with open(filename, 'r') as file:
        r, c, f, n, b, t = [int(i) for i in file.readline().split(' ')]
        drives = []
        for i in range(n):
            drives.append([int(i) for i in file.readline().split(' ')])
        return r, c, f, n, b, t, drives

def writeFile(filename, driver):
    with open(filename, 'w') as file:
        for singleDriver in driver.drivers:
            file.write("{} {}\n".format(len(singleDriver.drives), ' '.join([ str(i) for i in singleDriver.drives ])))



def main():

    filename = raw_input("Enter name of file: ")
    readPath = "input/"     + filename
    writePath = "output/"   + filename
    r, c, f, n, b, t, drives = readFile(readPath)
    driver = drivingRides(r, c, f, b, t, drives)

    for singleDriver in driver.drivers:
        singleDriver.determineClosestDrive(driver)


    for step in range(driver.noOfSteps):
        for singleDriver in driver.drivers:
            if not singleDriver.checkAvailability(driver):
                singleDriver.determineClosestDrive(driver)
        driver.incrementStep()

    writeFile(writePath, driver)


if __name__ == "__main__":
    main()