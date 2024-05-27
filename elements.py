import pygame as pg

GENERATE = pg.USEREVENT + 1
class Server(pg.sprite.Sprite):
    def __init__(self, mainsurf, xy):
        super().__init__()
        self.image = pg.Surface((100, 100), pg.SRCALPHA)
        self.image.blit(pg.transform.scale(pg.image.load("assets/resource/image_7.png"), (100, 100)), (0, 0))
        self.surf = mainsurf
        self.loc = xy
        self.rect = self.image.get_rect()
        self.speed = 5000
        self.speedcoeff = 1
        pg.time.set_timer(GENERATE, self.speed)


    def update(self, mode):
        if mode:
            self.surf.blit(self.image, self.loc)

    def gendata(self, cable):
        cable.points.append(0)
    def upgrade(self):
        print("Called")
        pg.time.set_timer(GENERATE, 0)
        self.speedcoeff += 0.5
        pg.time.set_timer(GENERATE, round(self.speed / self.speedcoeff))



class Cable(pg.sprite.Sprite):
    def __init__(self, mainsurf, server, pc):
        super().__init__()
        self.server = server
        self.pc = pc
        self.serverport = (server.loc[0] + 100, server.loc[1] + 50)
        self.pcport = (pc.loc[0], pc.loc[1] + 50)
        self.length = self.pcport[0] - self.serverport[0]
        self.image = pg.Surface((self.length, 10), pg.SRCALPHA)
        self.loc = self.serverport
        self.cablespeedcoeff = 1
        self.surf = mainsurf
        self.points = []

    def update(self, mode):
        self.image.fill((0, 0, 0))
        for i in self.points.copy():
            circlesurf = pg.Surface((10, 10), pg.SRCALPHA)
            pg.draw.circle(circlesurf, (0, 0, 255, 150), (5, 5), 5, 0)
            self.image.blit(circlesurf, (i, 0))
            index = self.points.index(i)
            print(self.cablespeedcoeff)
            self.points[index] += 1 * self.cablespeedcoeff
            if self.points[index] > self.length:
                self.points.pop(index)
                self.pc.register()
        if mode:
            self.surf.blit(self.image, self.loc)
    def upgrade(self):
        self.cablespeedcoeff += 1


class Pc(pg.sprite.Sprite):
    def __init__(self, mainsurf, xy):
        super().__init__()
        self.surf = mainsurf
        self.loc = xy
        self.image = pg.Surface((100, 100), pg.SRCALPHA)
        self.image.blit(pg.transform.scale(pg.image.load("assets/resource/image_8.png"), (100, 100)), (0, 0))
        self.bits = 0

    def update(self, mode):
        if mode:
            self.surf.blit(self.image, self.loc)

    def register(self):
        self.bits += 1
