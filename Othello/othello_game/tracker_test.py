from tracker import Tracker
# Tag, Tag reset and scanner require board, requires AI
from board import Board
from ai import othelloAI


def test_constructor():
    t = Tracker('Hi')
    assert t.bd == 'Hi'
    assert t.computer_moves == []
    assert t.tag_count == 0


def test_tag():
    t = Tracker(Board(5, 500, 500, 500, othelloAI()))
    t.bd.generate_board()
    t.bd.disks[1][1].halo_tag = True
    t.tag()
    assert t.tag_count == 1
    assert t.computer_moves == [t.bd.disks[1][1]]


def test_scanner():
    t = Tracker(Board(5, 500, 500, 500, othelloAI()))
    t.bd.generate_board()
    t.scanner()
    assert t.white_disks == 2
    assert t.black_disks == 2
    assert t.disks_on_board == 4


def test_tag_reset():
    t = Tracker(Board(5, 500, 500, 500, othelloAI()))
    t.bd.generate_board()
    t.bd.disks[1][1].halo_tag = True
    t.tag_reset()
    assert t.bd.disks[1][1].halo_tag is False


def test_board_scan_reset():
    t = Tracker(Board(5, 500, 500, 500, othelloAI()))
    t.bd.generate_board()
    t.bd.disks[1][1].halo_tag = True
    t.board_scan_reset()
    assert t.white_disks == 0
    assert t.black_disks == 0
    assert t.disks_on_board == 0
    assert t.computer_moves == []
    assert t.tag_count == 0


def test_board_scan():
    t = Tracker(Board(5, 500, 500, 500, othelloAI()))
    t.bd.generate_board()
    out = t.board_scan()
    assert out is False


def test_moves_avail():
    t = Tracker(Board(5, 500, 500, 500, othelloAI()))
    out = t.moves_avail()
    assert out is False
