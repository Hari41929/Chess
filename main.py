import pygame as p
import ChessEngine
import pieces

p.init()

w = h = 580
di = 8
sqr_size = h // di
max_fps = 15
IMAGES = {}

def Loadimage():
    pass

def main():
    screen = p.display.set_mode((w, h))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.Gamestate()
    Loadimage()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawgamestate(screen, gs)  # Call the drawgamestate function here
        clock.tick(max_fps)
        p.display.flip()

def drawgamestate(screen, gs):
    drawsqr(screen)
    drawpieces(screen, gs.board)

def drawsqr(screen):
    colors = [p.Color("white"), p.Color("black")]
    for r in range(di):
        for c in range(di):
            color = colors[(r + c) % 2]
            rect = p.Rect(c * sqr_size, r * sqr_size, sqr_size, sqr_size)
            p.draw.rect(screen, color, rect)

def drawpieces(screen, board):
   pass
if __name__ == "__main__":
    main()
