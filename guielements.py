import pygame as pg


class Stat:
    def __init__(self, x, y, textsize, unit, surf, varname, obj):
        self.cord = (x, y)
        self.textsize = textsize
        self.surf = surf
        self.font = pg.font.Font('assets/font/ret.ttf', textsize)
        self.unit = unit
        self.varname = varname
        self.obj = obj

    def update(self):
        text = f"{getattr(self.obj, self.varname)} {self.unit}"
        surf = self.font.render(text, True, (255, 255, 255))
        self.surf.blit(surf, self.cord)


class Button:
    def __init__(self, cordx, cordy, width, height, target, surface, text, textsize, radius=20):
        self.surf = surface
        self.size = width, height
        self.func = target
        self.cords = (cordx, cordy)
        self.target = target
        roundedsurf = pg.Surface((width, height), pg.SRCALPHA)
        rect = roundedsurf.get_rect()
        self.color = (0, 0, 0, 190)
        self.textcolor = (255, 255, 255, 255)
        self.textsize = textsize
        self.font = pg.Font('assets/font/ret.ttf', textsize)
        self.content = text
        self.text = self.font.render(text, True, self.textcolor)
        self.textrect = self.text.get_rect(center=(width / 2, height / 2))
        pg.draw.rect(roundedsurf, self.color, rect, 0, radius)
        self.rectsurf = roundedsurf.copy()
        self.rect = roundedsurf.get_rect()
        self.rect.topleft = self.cords
        self.texttuple = (self.text.get_width(), self.text.get_height())

    def draw(self):
        self.rectsurf.blit(self.text, self.textrect.topleft)
        self.surf.blit(self.rectsurf, self.cords)

    def checkmouse(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.target()


class Upgrade(Button):
    def __init__(self, cordx, cordy, width, height, surface, text, textsize, target):
        super().__init__(cordx, cordy, width, height, target, surface, text, textsize)

    def checkmouse(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.target()
            return True
