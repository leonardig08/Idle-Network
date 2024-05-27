import pygame_gui as gu
import pygame as pg
from guielements import *


class Gui:
    def __init__(self, surface):
        self.mainsurface = surface
        self.buttons1 = []
        self.stats = []
        self.upgrades = []
        self.currentpage = 1
        self.close = Button(10, 10, 50, 50, self.changemain, self.mainsurface, "X", 40, 5)
        self.buttons2 = [self.close]
        self.buttons3 = [self.close]

    def add_button1(self, button):
        self.buttons1.append(button)

    def add_button2(self, button):
        self.buttons2.append(button)

    def add_button3(self, button):
        self.buttons3.append(button)

    def add_stat(self, stat):
        self.stats.append(stat)

    def add_upgrade(self, upgrade):
        upgrade.size = (750, 100)
        if len(self.upgrades) == 0:
            coeff = 100
        else:
            coeff = 10
        upgrade.cords = (500 - (750/2), coeff + 200*len(self.upgrades))
        newupgrade = Upgrade(upgrade.cords[0], upgrade.cords[1], upgrade.size[0], upgrade.size[1], upgrade.surf, upgrade.content, upgrade.textsize, upgrade.target)
        del upgrade
        self.upgrades.append(newupgrade)

    def changeupgrade(self):
        self.currentpage = 2

    def changemain(self):
        self.currentpage = 1

    def changeresearch(self):
        self.currentpage = 3

    def update(self):
        if self.currentpage == 1:
            for button in self.buttons1:
                button.draw()
            for stat in self.stats:
                stat.update()
        elif self.currentpage == 2:
            for button in self.buttons2:
                button.draw()
            for upgrade in self.upgrades:
                upgrade.draw()
        elif self.currentpage == 3:
            for button in self.buttons3:
                button.draw()
