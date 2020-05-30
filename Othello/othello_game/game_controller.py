class GameController:
    """An othello GameController"""

    def __init__(self, Tracker, AI):
        """Initiates GameController Object"""
        self.ai = AI
        self.tr = Tracker
        self.delay = False

    #
    # *** MAKING A PLAY ***
    #

    def update(self):
        """If it's the computer's turn, has the computer make a play"""
        if not self.tr.game_over and self.tr.turn_tracker:
            self.computer_play()

    def validate_in(self, xcoord, ycoord):
        """Determines whether a disk is already played in the space"""
        x = int(xcoord/(self.tr.bd.TILE_WIDTH + self.tr.bd.LINE_WIDTH))
        y = int(ycoord/(self.tr.bd.TILE_WIDTH + self.tr.bd.LINE_WIDTH))
        if not self.tr.turn_tracker and self.tr.bd.disks[x][y].halo_tag:
            return True, x, y
        else:
            return False, x, y

    def make_play(self, xcoord, ycoord):
        """Plays the disk if legal move, and completes turn if turn is over"""
        vi = self.validate_in(xcoord, ycoord)
        if vi[0]:
            self.player_play(0, vi[1], vi[2])

    def player_play(self, color, x, y):
        """Places Disk on board, flips disks, and runs end of turn checks"""
        self.tr.bd.disks[x][y].color,
        self.tr.bd.disks[x][y].display_on = color, True
        self.tr.bd.disks[x][y].chain()
        self.tr.board_scan_reset()
        # Checks for computer move, if none, then checks for another move
        if self.tr.board_scan():
            self.delay = frameCount
            return
        else:
            self.tr.board_scan_reset()
            if not self.tr.board_scan():
                return
            # If none, ends game.
            else:
                self.tr.board_scan_reset()
                self.tr.scanner()
                self.tr.game_over = True
                self.tr.run_game_is_over = frameCount

    def computer_play(self):
        """AI chooses a Disk to play"""
        # Depending on game flow, helped randomize when smack showed up
        # This is more of an Easter Egg than anything.
        if (self.tr.disks_on_board != 0 and (self.tr.disks_on_board % 6 == 0 or
                                             self.tr.disks_on_board % 6 == 3) and self.tr.turn_tracker):
            self.ai.talk_smack()
        # Computer identifies possible moves to analyze
        for item in self.tr.computer_moves:
            self.ai.coordinate_extractor(item)
        # Computer chooses move
        choice = self.ai.choose_move()
        # Makes play
        choice = self.tr.bd.disks[choice[0]][choice[1]]
        self.ai.moves_reset()
        choice.color, choice.display_on = 1, True
        choice.chain()
        # Checks for player move, if none, checks for another move
        self.tr.board_scan_reset()
        if not self.tr.board_scan():
            return
        else:
            self.tr.board_scan_reset()
            if self.tr.board_scan():
                self.delay = frameCount
                return
            # If none, ends game
            else:
                if not self.tr.game_over:
                    self.tr.board_scan_reset()
                    self.tr.scanner()
                    self.tr.game_over = True
                    self.tr.run_game_is_over = frameCount

    #
    # *** END GAME ***
    #

    def game_is_over(self):
        """Log's player's score to file and sorts info in file"""
        player_name = self.input('Please enter your name to log score!') + ' '
        scores_list = []
        try:
            # Read the lines of a file into a list
            with open('scores.txt', 'r') as scores:
                for line in scores:
                    scores_list.append(line.strip())
                # Add the player's score
                scores_list.append(player_name + str(self.tr.black_disks))
                # Sort the list based on scores
                scores_list = sorted(scores_list,
                                     key=lambda x: x[-2:],
                                     reverse=True)
            # Just a quick Print out of the top 5 high scores:
            if len(scores_list) >= 5:
                print('Top scores:')
                for item in range(5):
                    print(scores_list[item])
            # Write the list in lines to the file
            with open('scores.txt', 'w') as scores:
                for line in scores_list:
                    scores.write(line + '\n')
        except BaseException:
            print('Scores tracking file not found :(')
        return

    def input(self, message=''):
        """Java style processing input function"""
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
