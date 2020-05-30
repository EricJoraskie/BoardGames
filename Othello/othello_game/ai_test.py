from ai import othelloAI
from disk import Disk


def test_constructor():
    ai = othelloAI()
    assert ai.fin_priorities0 == {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                                  (5, 0), (6, 0), (7, 0)}
    assert ai.avoid3 == {(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)}
    assert ai.possible_moves == []


def test_coordinate_extractor():
    ai = othelloAI()
    d = Disk(-1000, '345')
    ai.coordinate_extractor(d)
    assert ai.possible_moves == [(-1000, '345')]


def test_moves_reset():
    ai = othelloAI()
    d = Disk(-1000, '345')
    ai.coordinate_extractor(d)
    ai.moves_reset()
    assert ai.possible_moves == []


def test_choose_move():
    ai = othelloAI()
    d = Disk(-1000, '345')
    ai.coordinate_extractor(d)
    ai.fill_fin_avoid()
    assert ai.choose_move() == (-1000, '345')
    ai.moves_reset()
    assert ai.choose_move() is None


def test_clear_bad_moves():
    ai = othelloAI()
    d = Disk(-1000, '345')
    d2 = Disk(1, 1)
    ai.coordinate_extractor(d)
    ai.coordinate_extractor(d2)
    ai.fill_fin_avoid()
    assert ai.clear_bad_moves() == [(-1000, '345')]


def test_last_resort():
    ai = othelloAI()
    d = Disk(-1000, '345')
    d2 = Disk(1, 1)
    ai.coordinate_extractor(d)
    ai.coordinate_extractor(d2)
    ai.fill_fin_avoid()
    assert ai.last_resort() == [(-1000, '345')]

# Smack talk not really testable
