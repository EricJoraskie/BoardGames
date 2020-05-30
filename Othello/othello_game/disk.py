STROKE = 3
CENTER = 50
TILE_WIDTH = 100
ADJACENT = 8
LINE_W = 1
DIAMETER = 90


class Disk:
    """A Disk"""

    def __init__(self, column, row):
        self.display_on = False
        self.color = False
        self.halo_tag = False
        self.column = column
        self.row = row
        # Eight way node attribute
        self.node_dict = {key: None for key in range(ADJACENT)}

    def __repr__(self):
        return "|[N " + str(self.row) + ", " + str(self.column) + "]|"

    # *** DISK AND VALID MOVE DISPLAY ***

    def display(self):
        """Draws disk"""
        fill(self.color)
        strokeWeight(STROKE)
        ellipse(self.column*TILE_WIDTH + LINE_W*self.column
                + CENTER, self.row*TILE_WIDTH + LINE_W*self.row
                + CENTER, DIAMETER, DIAMETER)

    def display_halo(self):
        """Draws possible move ring"""
        # Number > 1 makes fill-less disk. This 2 could be anything.
        fill(2)
        strokeWeight(STROKE)
        ellipse(self.column*TILE_WIDTH + LINE_W*self.column
                + CENTER, self.row*TILE_WIDTH + LINE_W*self.row
                + CENTER, DIAMETER, DIAMETER)

    # *** VALID MOVE DESIGNATION HANDLING ***

    def halo(self):
        """Triggers a possible move scan in all directions"""
        for i in range(len(self.node_dict)):
            if self.node_dict[i] and self.node_dict[i].display_on:
                if self.node_dict[i].color != self.color:
                    self.node_dict[i].halo_run(i, self.color)

    def halo_run(self, i, color):
        """Labels possible moves"""
        if self.node_dict[i]:
            if self.node_dict[i].display_on:
                if self.node_dict[i].color == color:
                    return
                else:
                    self.node_dict[i].halo_run(i, color)
            else:
                self.node_dict[i].halo_tag = True

    # *** DISK FLIP HANDLING ***

    def chain(self):
        """Triggers disks to flip scan in all directions"""
        for i in range(len(self.node_dict)):
            if self.node_dict[i] and self.node_dict[i].display_on:
                if self.node_dict[i].color != self.color:
                    self.node_dict[i].run(i, self.color)

    def run(self, i, color):
        """Flips valid disks"""
        if self.node_dict[i]:
            if self.node_dict[i].display_on:
                if self.node_dict[i].color == color:
                    self.color = color
                    return True
                else:
                    if self.node_dict[i].run(i, color):
                        self.color = color
                        return True
