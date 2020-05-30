from board import Board
# Generate board function runs and AI method
from ai import othelloAI


def test_constructor():
    bd = Board(10, 100, 1009, 1, othelloAI())
    assert bd.disks == {}
    assert bd.setup == (4.0, 6.0)
    assert bd.HEIGHT == 1009.0


def test_generate_board():
    bd = Board(10, 100, 1009, 1, othelloAI())
    bd.generate_board()
    assert bd.disks[4][3].node_dict[1] is bd.disks[4][2]
    assert bd.disks[9][9].node_dict[7] is None
    assert bd.disks[6][0].node_dict[0] is None
    assert bd.disks[1][0].node_dict[4] is bd.disks[0][0]
    assert bd.disks[0][0].node_dict == {0: None,
                                        1: None,
                                        2: None,
                                        3: bd.disks[1][0],
                                        4: None,
                                        5: None,
                                        6: bd.disks[0][1],
                                        7: bd.disks[1][1]}
    assert bd.disks[9][9].node_dict == {0: bd.disks[8][8],
                                        1: bd.disks[9][8],
                                        2: None,
                                        3: None,
                                        4: bd.disks[8][9],
                                        5: None,
                                        6: None,
                                        7: None}
    assert bd.disks[0][4].node_dict == {0: None,
                                        1: bd.disks[0][3],
                                        2: bd.disks[1][3],
                                        3: bd.disks[1][4],
                                        4: None,
                                        5: None,
                                        6: bd.disks[0][5],
                                        7: bd.disks[1][5]}


def test_node_connect():
    bd = Board(5, 100, 508, 2, othelloAI())
    bd.generate_board()
    bd.node_connect(4, 2, bd.disks[4][1], 5)
    assert bd.disks[4][1].node_dict[5] is bd.disks[4][2]
    assert bd.disks[4][2].node_dict[1] is bd.disks[4][1]


def test_adjacent_corners():
    bd = Board(5, 12, 58, 2, othelloAI())
    bd.generate_board()
    assert bd.disks[0][0].node_dict[0] is None
    assert bd.disks[0][4].node_dict[1] == bd.disks[0][3]


def test_adjacent_edges():
    bd = Board(5, 12, 58, 2, othelloAI())
    bd.generate_board()
    assert bd.disks[0][3].node_dict[1] == bd.disks[0][2]
    assert bd.disks[4][3].node_dict[6] == bd.disks[4][4]


def test_standard_tile():
    bd = Board(5, 12, 58, 2, othelloAI())
    bd.generate_board()
    assert bd.disks[2][3].node_dict[1] is not None
    assert bd.disks[3][3].node_dict[2] == bd.disks[4][2]

# Adjacency Handoff not particularly testable.
