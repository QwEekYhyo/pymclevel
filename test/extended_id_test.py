from schematic import MCSchematic

__author__ = 'Rio'

def test_schematic_extended_ids():
    s = MCSchematic(shape=(3, 2, 2))
    s.Blocks[0,0,0] = 2048
    s.compress()
    s.decompress()
    assert s.Blocks[0,0,0] == 2048
