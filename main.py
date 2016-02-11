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
        self.currentTurn = 0
        self.gridSize = [int(lLignes.pop(0)),
                         int(lLignes.pop(0))]
        self.droneNumber = int(lLignes.pop(0))
        self.droneList = [  {   "coord" : [1,1],
                                "items":[0]*self.productNumber,
                                "turnAvailable":0,
                                "currentOrder":None
                            }  
                            for i in range(self.droneNumber)
                         ]

        self.droneInMission = []
        self.maxTickNumber = int(lLignes.pop(0))
        self.droneMaxLoad = int(lLignes.pop(0))
        self.productNumber = int(lLignes.pop(0))

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

    def findNextDrone(self)
        m = LARGE_NUMBER
        nextAvail = None
        for d in self.droneList:
            if(d["turnAvailable"] <= self.currentTurn)
                return (self.currentTurn, d)
            if(d["turnAvailable"] <= m)
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
            if(order["warehouse"]["itemList"][i] < order["itemList"][i])
                return False
        return True

    def doOrder(self, order, drone):
       drone["order"] = order
        

    def deliver(self):
        bestOrder = "kek"
        while bestOrder !=None:
            drone = self.findNextDrone()
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
