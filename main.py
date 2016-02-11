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

class grid:
    def __init__(self, lLignes):
        print("lol")
        print("kek")
        ## parse ##
        self.gridSize = [int(lLignes.pop(0)),
                         int(lLignes.pop(0))]
        self.droneNumber = int(lLignes.pop(0))
        self.maxTickNumber = int(lLignes.pop(0))
        self.droneMaxLoad = int(lLignes.pop(0))
        self.productNumber = int(lLignes.pop(0))

        self.productList = [int(j) for j in lLignes.pop(0).split(' ')]

        self.warehouseNumber = int(lLignes.pop(0))
        
        self.warehouseList = [  {
                                    "coord":[ int(j) for j in lLignes.pop(0).split(' ')],
                                    "items":[ int(j) for j in lLignes.pop(0).split(' ')],
                                    "orderList": [],
                                    "needs" :  [0]*self.productNumber
                                }
                                for i in range(self.warehouseNumber)
                             ]

        self.orderNumber = int(lLignes.pop(0))

        self.orderList =    [
                                {
                                    "coord":[ int(j) for j in lLignes.pop(0).split(' ')],
                                    "itemsNumber":int(lLignes.pop(0)),
                                    "itemsList":[ int(j) for j in lLignes.pop(0).split(' ')],
                                    "warehouse": None                           
                                }
                                for i in range(self.orderNumber)
                            ]
    def assignWarehouseToOrder(self, order):
        bestWH = self.warehouseList[0]
        bestDist = LARGE_NUMBER
        for warehouse in self.warehouseList:
            dist = getDistance(warehouse, order)
            if(dist < bestDist):
                bestWH = warehouse
                bestDist = dist

        order["warehouse"] = warehouse

    def computeNeeds(self, warehouse):
        for order in warehouse.orderList:
            

    def run(self):
        print("Assigning Warehouses to Houses")
        for order in self.orderList:
            self.assignWarehouseToOrder(order)
        print("Computing needs and oveflow")
        for warehouse in self.warehouseList:
            self.computeNeeds(warehouse)
        
            

f = open(ADD, 'r')
mainGrid = grid(f.read().split('\n'))
mainGrid.run()
f.close()
