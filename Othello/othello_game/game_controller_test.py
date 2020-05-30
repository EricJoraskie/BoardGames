from game_controller import GameController
from tracker import Tracker
from board import Board
from ai import othelloAI


def test_constructor():
    gc = GameController(1, 2)
    assert gc.ai == 2
    assert gc.tr == 1
    assert gc.delay is False


def test_validate_in():
    gc = GameController(Tracker(Board(5, 1, 1, 1, othelloAI())), 1)
    out = gc.validate_in(2, 2)
    assert out == (False, 1, 1)

# Make play and player_play, computer_play, and
# game_is_over not really effectively testable
# Due to frameCount issue (even when i instantiated a
# variable called framecount in the test function)
# as well as file manipulation controls
# update also dependent on computer_play to test
