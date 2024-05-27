import pygame
import pygame as pg
from guielements import Button, Stat, Upgrade
from gradient import fill_gradient
from gui import Gui
import elements

running = True


class Game:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700

    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.SRCALPHA)
        self.mainsurf = pg.Surface((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT), pygame.SRCALPHA)
        pg.display.set_caption('Netsim')
        self.clock = pg.time.Clock()
        self.running = True
        self.gui = Gui(self.mainsurf)
        func = 2
        self.gui.add_button1(Button(170, 600, 320, 90, self.gui.changeupgrade, self.mainsurf, "UPGRADE", 65))
        self.gui.add_button1(Button(510, 600, 340, 90, self.gui.changeresearch, self.mainsurf, "RESEARCH", 65))
        self.server = elements.Server(self.mainsurf, (90, 300))
        self.pc = elements.Pc(self.mainsurf, (800, 300))
        self.cable = elements.Cable(self.mainsurf, self.server, self.pc)
        self.gui.add_stat(Stat(800, 70, 45, "Bits", self.mainsurf, "bits", self.pc))
        self.gui.add_upgrade(Upgrade(0, 0, 0, 0, self.mainsurf, "Server Speed", 45, self.server.upgrade))
        self.gui.add_upgrade(Upgrade(0, 0, 0, 0, self.mainsurf, "Cable Speed", 45, self.cable.upgrade))

    def update(self):
        fill_gradient(self.mainsurf, pg.Color("midnight blue"), pg.Color("purple3"), None, True, True)
        self.gui.update()
        checker = (self.gui.currentpage == 1)
        self.server.update(checker)
        self.cable.update(checker)
        self.pc.update(checker)
        self.screen.blit(self.mainsurf, (0, 0))
        pg.display.flip()
        self.clock.tick(60)

    def game(self):
        while self.running:
            self.event_handler(pg.event.get())
            self.update()

    def event_handler(self, events):
        for event in events:
            if event.type == elements.GENERATE:
                self.server.gendata(self.cable)
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.running = False
                break
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.gui.currentpage == 1:
                    for button in self.gui.buttons1:
                        button.checkmouse()
                elif self.gui.currentpage == 2:
                    for upgrade in self.gui.upgrades:
                        upgrade.checkmouse()
                    for button in self.gui.buttons2:
                        button.checkmouse()
                elif self.gui.currentpage == 3:
                    for button in self.gui.buttons3:
                        button.checkmouse()


if __name__ == '__main__':
    game = Game()
    game.game()
