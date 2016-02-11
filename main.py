#!/usr/bin/env python3


from sys import argv

DELIMITER = '\\'

if len(argv) < 2:
    ADD = "D:\\Programmation\\hashcode\\HashCode2016\\code\\hashcode16\\test.txt"
else:
    ADD = ''.join([i + DELIMITER for i in  argv[1].split(DELIMITER)[:-1]])


class grid:
    def __init__(self, lLignes):

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
                                    "items":[ int(j) for j in lLignes.pop(0).split(' ')]
                                }
                                for i in range(self.warehouseNumber)
                             ]

        self.orderNumber = int(lLignes.pop(0))

        self.orderList =    [
                                {
                                    "coord":[ int(j) for j in lLignes.pop(0).split(' ')],
                                    "itemsNumber":int(lLignes.pop(0)),
                                    "itemsList":[ int(j) for j in lLignes.pop(0).split(' ')]
                                }
                                for i in range(self.orderNumber)
                            ]
                        
        




f = open(ADD, 'r')
mainGrid = grid(f.read().split('\n'))
f.close()
