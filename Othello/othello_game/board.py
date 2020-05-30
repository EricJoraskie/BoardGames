from disk import Disk


class Board:
    """A Board"""

    def __init__(self, TILE_NUM, TILE_WIDTH, HEIGHT, LINE_WIDTH, AI):
        # Board setup
        self.ai = AI
        self.LINE_WIDTH = LINE_WIDTH
        self.TILE_NUM = TILE_NUM
        self.TILE_WIDTH = TILE_WIDTH
        self.HEIGHT = HEIGHT
        self.TEXT = int(HEIGHT/16)
        self.disks = {}
        self.board_size = self.TILE_NUM**2
        self.setup = int((self.TILE_NUM/2) - 1), int((self.TILE_NUM/2) + 1)

    #
    # *** SETUP AND DISPLAY ***
    #

    def grid(self):
        """Builds grid"""
        fill(0)
        for i in range(1, self.TILE_NUM):
            i = i*self.TILE_WIDTH + self.LINE_WIDTH*i
            line(i, 0, i, self.HEIGHT)
            line(0, i, self.HEIGHT, i)

    def generate_board(self):
        """Creates board space with dict of Disk filled lists"""
        # Fills board with disks
        self.disks = {key: [Disk(key, x) for x in range(self.TILE_NUM)]
                      for key in range(self.TILE_NUM)}
        # AI processing set() solution function
        self.ai.fill_fin_avoid()
        # Loops through all disks to make appropriate connections
        for key in self.disks.keys():
            for item in range(len(self.disks[key])):
                self.adjacency_handoff(key, item, self.disks[key][item])
        # Place starting pieces
        for x in range(*self.setup):
            for y in range(*self.setup):
                if x == y:
                    self.disks[x][y].color = 1
                    self.disks[x][y].display_on = True
                else:
                    self.disks[x][y].color = 0
                    self.disks[x][y].display_on = True

    def display_board(self):
        """Displays the board"""
        self.grid()
        for i in range(len(self.disks)):
            for item in self.disks[i]:
                # Displays disks that were played
                if item.display_on:
                    item.display()
                # Displays possible moves
                elif item.halo_tag:
                    item.display_halo()

    #
    # *** NODE CONNECTING ***
    #

    # The numbers in this section are hard coded.
    # This is intentional for ease of reading.
    # These numbers are static and will scale properly to any size game
    # 0 - 7 in the following functions are representative of the
    # 8 possible adjacent squares for a given move.
    # Hard coding made for far easier reading and was an aesthetic choice.
    # For reference, this is a visual depiction of a node's adjacency mapping:
    #
    #              0   1   2
    #                \ | /
    #             4 -- N -- 3
    #                / | \
    #              5   6   7

    def node_connect(self, x, y, disk, num):
        """Connects a node to adjacent nodes based on node_dict posiiton"""
        disk.node_dict[num] = self.disks[x][y]

    def adjacent_corners(self, x, y, disk):
        """Connects for corner disks based on position"""
        if x == 0 and y == 0:
            self.node_connect(x+1, y, disk, 3)
            self.node_connect(x+1, y+1, disk, 7)
            self.node_connect(x, y+1, disk, 6)
        elif x == 0 and y == self.TILE_NUM-1:
            self.node_connect(x, y-1, disk, 1)
            self.node_connect(x+1, y-1, disk, 2)
            self.node_connect(x+1, y, disk, 3)
        elif x == self.TILE_NUM-1 and y == 0:
            self.node_connect(x-1, y, disk, 4)
            self.node_connect(x-1, y+1, disk, 5)
            self.node_connect(x, y+1, disk, 6)
        elif x == self.TILE_NUM-1 and y == self.TILE_NUM-1:
            self.node_connect(x-1, y-1, disk, 0)
            self.node_connect(x, y-1, disk, 1)
            self.node_connect(x-1, y, disk, 4)

    def adjacent_edges(self, x, y, disk):
        """Connects for edge disks based on position"""
        if y == 0:
            self.node_connect(x+1, y, disk, 3)
            self.node_connect(x-1, y, disk, 4)
            self.node_connect(x-1, y+1, disk, 5)
            self.node_connect(x, y+1, disk, 6)
            self.node_connect(x+1, y+1, disk, 7)
        elif x == 0:
            self.node_connect(x, y-1, disk, 1)
            self.node_connect(x+1, y-1, disk, 2)
            self.node_connect(x+1, y, disk, 3)
            self.node_connect(x, y+1, disk, 6)
            self.node_connect(x+1, y+1, disk, 7)
        elif y == self.TILE_NUM-1:
            self.node_connect(x-1, y-1, disk, 0)
            self.node_connect(x, y-1, disk, 1)
            self.node_connect(x+1, y-1, disk, 2)
            self.node_connect(x+1, y, disk, 3)
            self.node_connect(x-1, y, disk, 4)
        elif x == self.TILE_NUM-1:
            self.node_connect(x-1, y-1, disk, 0)
            self.node_connect(x, y-1, disk, 1)
            self.node_connect(x-1, y, disk, 4)
            self.node_connect(x-1, y+1, disk, 5)
            self.node_connect(x, y+1, disk, 6)

    def standard_tile(self, x, y, disk):
        """Connects the nodes for a disk with tiles in every direction"""
        self.node_connect(x-1, y-1, disk, 0)
        self.node_connect(x, y-1, disk, 1)
        self.node_connect(x+1, y-1, disk, 2)
        self.node_connect(x-1, y, disk, 4)
        self.node_connect(x+1, y, disk, 3)
        self.node_connect(x-1, y+1, disk, 5)
        self.node_connect(x, y+1, disk, 6)
        self.node_connect(x+1, y+1, disk, 7)

    def adjacency_handoff(self, x, y, disk):
        """Determines piece position, then sends to appropriate pre-connect"""
        if (x == 0 or y == 0 or
           x == self.TILE_NUM-1 or y == self.TILE_NUM-1):
            # Corner cases
            if (x == 0 and y == 0 or
               x == 0 and y == self.TILE_NUM-1 or
               x == self.TILE_NUM-1 and y == 0 or
               x == self.TILE_NUM-1 and y == self.TILE_NUM-1):
                self.adjacent_corners(x, y, disk)
            # Edge cases
            else:
                self.adjacent_edges(x, y, disk)
        # Normal position
        else:
            self.standard_tile(x, y, disk)
