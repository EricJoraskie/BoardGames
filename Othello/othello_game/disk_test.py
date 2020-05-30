from disk import Disk


def test_constructor():
    d = Disk(100, 41432)
    assert d.column == 100
    assert d.color is False


def test_repr():
    d = Disk(100, 41432)
    assert str(d) == "|[N 41432, 100]|"

# Halo and Chain aren't particularly testable,
# as they're realyy just a conditional handoff


def test_halo_run():
    d = Disk(10, 10)
    d.node_dict[0] = Disk(122, 33)
    d.color, d.node_dict[0].display_on = True, True
    d.node_dict[0].node_dict[0] = Disk(85, 64)
    d.halo_run(0, True)
    assert d.node_dict[0].node_dict[0].halo_tag is True


def test_run():
    d = Disk(10, 10)
    d.node_dict[0] = Disk(122, 33)
    d.color, d.node_dict[0].display_on = True, True
    d.node_dict[0].node_dict[0] = Disk(85, 64)
    d.run(0, True)
    assert d.node_dict[0].color is False
