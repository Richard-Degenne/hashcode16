#!/usr/bin/env python3


from sys import argv
from math import sqrt 

DELIMITER = '/'
LARGE_NUMBER = 10**10

if len(argv) < 2:
    ADD = "/home/eleve/hashcode16/test.txt"
else:
    ADD = ''.join([i + DELIMITER for i in  argv[1].split(DELIMITER)[:-1]])


def getDistance(pointA, pointB):
    return sqrt((pointA["coord"][0] - pointB["coord"][0])**2 + (pointA["coord"][1] - pointB["coord"][1])**2)

def normalize(l, n):
    return [ l.count(i) for i in range(n)]


class grid:
    def __init__(self, lLignes):
        print("lol")
        print("kek")
        ## parse ##
        self.f = open("output.txt", "w")
        self.currentTurn = 0
        self.gridSize = [int(lLignes.pop(0)),
                         int(lLignes.pop(0))]
        self.droneNumber = int(lLignes.pop(0))
        self.droneInMission = []
        self.maxTickNumber = int(lLignes.pop(0))
        self.droneMaxLoad = int(lLignes.pop(0))
        self.productNumber = int(lLignes.pop(0))
        self.droneList = [  {   "coord" : [1,1],
                                "itemList":[0]*self.productNumber,
                                "turnAvailable":0,
                                "currentOrder":None,
                                "id" : i,
                                "weight":0
                            }  
                            for i in range(self.droneNumber)
                         ]
        self.productList = [int(j) for j in lLignes.pop(0).split(' ')]

        self.warehouseNumber = int(lLignes.pop(0))
        
        self.warehouseList = [  {
                                    "coord":[ int(j) for j in lLignes.pop(0).split(' ')],
                                    "itemList":[ int(j) for j in lLignes.pop(0).split(' ')],
                                    "orderList": [],
                                    "needs" :  [0]*self.productNumber,
                                    "leftover": [0]*self.productNumber
                                }
                                for i in range(self.warehouseNumber)
                             ]

        self.orderNumber = int(lLignes.pop(0))

        self.orderList =    [
                                {
                                    "coord":[ int(j) for j in lLignes.pop(0).split(' ')],
                                    "itemsNumber":int(lLignes.pop(0)),
                                    "itemList":normalize([ int(j) for j in lLignes.pop(0).split(' ')], self.productNumber),
                                    "warehouse": None,
                                    "ready":False
                                }
                                for i in range(self.orderNumber)
                            ]

    def findNextDrone(self):
        m = LARGE_NUMBER
        nextAvail = None
        for d in self.droneList:
            if(d["turnAvailable"] <= self.currentTurn):
                return (self.currentTurn, d)
            if(d["turnAvailable"] <= m):
                m = d["turnAvailable"]
                nextAvail = d
        return (nextAvail["turnAvailable"], nextAvail)

    def assignWarehouseToOrder(self, order):
        bestWH = self.warehouseList[0]
        bestDist = LARGE_NUMBER
        for warehouse in self.warehouseList:
            dist = getDistance(warehouse, order)
            if(dist < bestDist):
                bestWH = warehouse
                bestDist = dist


        order["warehouse"] = warehouse
        warehouse["orderList"].append(order)

    def computeNeeds(self, warehouse):
        for order in warehouse["orderList"]:
            for i in range(self.productNumber):
                warehouse["needs"][i] += order["itemList"][i]
            
        for i in range(self.productNumber): # TODO: Inverser les boucles
            warehouse["leftover"][i] = warehouse["itemList"][i] -warehouse["needs"][i]
        
    def isOrderReady(self, order):
        for i in range(self.productNumber):
            if(order["warehouse"]["itemList"][i] < order["itemList"][i]):
                return False
        return True

    def output(self, cmd):
        self.f.write(cmd)

    def doOrder(self, order, drone):
        drone["order"] = order
    
    def fillDrone(self, drone, warehouse, item):
        order = drone["order"]
        warehouse = order["warehouse"]
        N = order["itemList"][item]
        n = (self.maxDroneLoad - drone["weight"]) // N
        order["itemList"][item] -= n
        drone["itemList"][item] += n
        drone["weight"] += n * self.productList[item]
        return n
 
    def doLoad(self, drone, item):
        order = drone["order"]
        warehouse = order["warehouse"]
        n = fillDrone(drone, warehouse, item)
        if n == 0:
            return 0
        self.output(str(drone["id"])+" L " + str(warehouse["id"]) + " " + str(item) + " " + n)
        return n

    def doStep(self, drone):
        order = drone["order"]
        warehouse = order["warehouse"]
        if(drone["full"] == False):
            hasLoaded = False
            for item in order["itemList"]:
                if(self.doLoad(drone, item)):
                    hasLoaded = True
            drone["full"] = True 

        if(drone["full"] == True):
            for item in order["itemList"]:
                self.doDeliver(drone, order, item)

    def deliver(self):
        bestOrder = "kek"
        while bestOrder !=None:
            self.currentTurn, drone = self.findNextDrone()
            if(drone["order"] != None):
                self.doStep(drone)
                continue
            bestDist = LARGE_NUMBER
            bestOrder = None
            for order in self.orderList:
                if(order["ready"]):
                    dist = getDistanceToComplete(order, drone)
                    if(dist < bestDist):
                        bestDist = dist
                        bestOrder = order
            doOrder(bestOrder, drone) 
            

    def run(self):
        print("Assigning Warehouses to Houses")
        for order in self.orderList:
            self.assignWarehouseToOrder(order)
        print("Computing needs and oveflow")
        for warehouse in self.warehouseList:
            self.computeNeeds(warehouse)
            print(warehouse)
        print("Computing ready orders")
        for order in self.orderList:
            order["ready"] = self.isOrderReady(order)
        

        print("Assigning drones")
        self.deliver()
        
            

f = open(ADD, 'r')
mainGrid = grid(f.read().split('\n'))
mainGrid.run()
f.close()
