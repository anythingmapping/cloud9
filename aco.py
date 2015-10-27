#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mostynl
#
# Created:     14/10/2015
# Copyright:   (c) mostynl 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Ant():
    def __init__(self):

        self.progress = 0
        self.target = 200
        self.go = True

    def moveAnt(self):
        while self.target >= self.progress:
            self.progress += 1
            print self.progress

    def targetUpdate(self,length):
        self.target = length
