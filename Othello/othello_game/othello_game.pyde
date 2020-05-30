from board import Board
from tracker import Tracker
from game_controller import GameController
from ai import othelloAI

LINE_WIDTH = 1
TILE_DIM = 100
TILE_NUM = 8
BKGD = 0.4
HEIGHT = TILE_DIM*TILE_NUM + LINE_WIDTH*TILE_NUM - 1

ai = othelloAI()
bd = Board(TILE_NUM, TILE_DIM, HEIGHT, LINE_WIDTH, ai)
tr = Tracker(bd)
gc = GameController(tr, ai)


def setup():
    size(HEIGHT, HEIGHT)
    colorMode(RGB, 1)
    bd.generate_board()
    tr.board_scan()


def draw():
    background(0, BKGD, 0)
    bd.display_board()
    tr.turn_display(tr.turn_tracker, tr.game_over)
    if frameCount == gc.delay + 120:
        gc.update()
    if frameCount == tr.run_game_is_over + 10 and tr.game_over:
        gc.game_is_over()


def mousePressed():
    gc.make_play(mouseX, mouseY)
