TEXT_COLOR = 0.7


class Tracker:

    def __init__(self, Board):
        """Initiates GameTracker Object"""
        self.bd = Board
        self.computer_moves = []
        self.turn_tracker = True
        self.tag_count = 0
        self.disks_on_board = 0
        self.white_disks = 0
        self.black_disks = 0
        self.game_over = False
        self.run_game_is_over = False

    #
    # *** DISPLAY ***
    #

    def turn_display(self, comp_turn, game_over):
        """Displays turn at top of board adn displays endgame message"""
        fill(TEXT_COLOR, 0, 0)
        textSize(self.bd.TEXT)
        # Turn and Game Over
        if comp_turn and not game_over:
            text("White turn", 0, self.bd.TEXT)
        elif not comp_turn and not game_over:
            text("Black turn", 0, self.bd.TEXT)
        else:
            text("Game Over", 0, self.bd.TEXT)
            # End game message
            if self.black_disks > self.white_disks:
                text("You win with {0} disks.\nI had {1}. Nice Job.".format
                     (self.black_disks, self.white_disks),
                     self.bd.TEXT, self.bd.HEIGHT - self.bd.TEXT*2)
            elif self.black_disks < self.white_disks:
                text("I win with {0} disks.\nYou only had {1} >:)".format
                     (self.white_disks, self.black_disks),
                     self.bd.TEXT, self.bd.HEIGHT - self.bd.TEXT*2)
            elif self.black_disks == self.white_disks:
                text("Tied, {0} - {0}...\nI hate ties...".format(32),
                     self.bd.TEXT, self.bd.HEIGHT - self.bd.TEXT*2)

    #
    # *** GAMEPLAY TRACKING ***
    #

    def tag(self):
        """Records number of halo-tagged items and adds to move list"""
        for i in range(len(self.bd.disks)):
            for item in self.bd.disks[i]:
                if item.halo_tag:
                    self.tag_count += 1
                    self.computer_moves.append(item)

    def scanner(self):
        """Scans the board and updates attributes"""
        for i in range(len(self.bd.disks)):
            for item in self.bd.disks[i]:
                if item.display_on:
                    self.disks_on_board += 1
                    if not self.turn_tracker and item.color == 0:
                        item.halo()
                    elif self.turn_tracker and item.color == 1:
                        item.halo()
                    if item.color == 0:
                        self.black_disks += 1
                    if item.color == 1:
                        self.white_disks += 1

    def tag_reset(self):
        """Resets halo tags to avoid move overlap"""
        for i in range(len(self.bd.disks)):
            for item in self.bd.disks[i]:
                item.halo_tag = False

    def board_scan_reset(self):
        """Resets game counters"""
        self.tag_count = 0
        self.computer_moves = []
        self.tag_reset()
        self.black_disks, self.white_disks, self.disks_on_board = 0, 0, 0

    def board_scan(self):
        """Changes turn, scans board, checks for game end, runs move_avail"""
        if not self.game_over and self.disks_on_board != self.bd.board_size:
            self.turn_tracker = not self.turn_tracker
            self.scanner()
            if self.disks_on_board == self.bd.board_size or self.game_over:
                self.game_over = True
                self.run_game_is_over = frameCount
                return True
            else:
                if self.moves_avail():
                    return True
                else:
                    return False
        else:
            self.scanner()

    def moves_avail(self):
        """Check what moves are available for the given player's turn"""
        if self.turn_tracker:
            self.tag()
            if self.tag_count:
                return True
            else:
                return False
        else:
            self.tag()
            if self.tag_count:
                return False
            else:
                return True
