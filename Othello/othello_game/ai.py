import random as rn


class othelloAI:

    def __init__(self):
        """Creates AI for othello"""
        # These are the coordinates of the tiles
        # of the utmost importance to take:
        self.top_priorities = {(0, 0), (0, 7), (7, 0), (7, 7)}
        self.mid_priorities = {(0, 2), (2, 0), (0, 5), (5, 0),
                               (2, 7), (7, 2), (5, 7), (7, 5)}
        self.bot_priorities = {(2, 2), (5, 5), (2, 5), (5, 2)}
        # Processing has a function called 'set()' which made making a set
        # using these list comprehensions more difficult than I anticipated.
        # This is still nicer than writing them all out.
        self.fin_priorities0 = {(i, 0) for i in range(8)}
        self.fin_priorities1 = {(0, i) for i in range(8)}
        self.fin_priorities2 = {(7, i) for i in range(8)}
        self.fin_priorities3 = {(i, 7) for i in range(8)}
        self.fin_priorities = None
        # These are squares the computer should avoid
        # IF POSSIBLE:
        # aac == at all costs... within reason of course
        self.avoid_aac = {(0, 6), (6, 0), (1, 0), (0, 1),
                          (1, 7), (7, 1), (6, 7), (7, 6),
                          (1, 1), (1, 6), (6, 1), (6, 6)}
        # Same Processing 'set()' issue as above
        self.avoid0 = {(i, 1) for i in range(1, 7)}
        self.avoid1 = {(1, i) for i in range(1, 7)}
        self.avoid2 = {(i, 6) for i in range(1, 7)}
        self.avoid3 = {(6, i) for i in range(1, 7)}
        self.avoid = None
        # Here is some smack talk:
        self.smack_talk = ["Oof.. first time playing, huh?\n",
                           "Not where, I would've played, "
                           "but I'm only a computer\n",
                           "Don't be embarrassed, I remember my first game.\n",
                           "I've got you rattled, don't I?\n",
                           "Is it not obvious I'm going to win?\n",
                           "I'm saying this as a friend.. Give up.\n",
                           "The little red 'x' in the upper right hand\n"
                           "corner is your out when you decide to quit...\n",
                           "My goodness you're sad to watch...\n"
                           "and I don't have feelings!\n",
                           "If you quit now, I won't tell "
                           "anyone how bad this was\n"]
        # List for moves in a given turn
        self.possible_moves = []

    def fill_fin_avoid(self):
        """Set handling to work around processing function"""
        self.fin_priorities = self.fin_priorities0
        self.fin_priorities.update(self.fin_priorities1)
        self.fin_priorities.update(self.fin_priorities2)
        self.fin_priorities.update(self.fin_priorities3)
        self.avoid = self.avoid0
        self.avoid.update(self.avoid1)
        self.avoid.update(self.avoid2)
        self.avoid.update(self.avoid3)
        for item in self.avoid_aac:
            if item in self.fin_priorities:
                self.fin_priorities.remove(item)

    def coordinate_extractor(self, disk):
        """Grabs coordinates from all the disks in the computer_moves"""
        self.possible_moves.append((disk.column, disk.row))

    def moves_reset(self):
        """Reset's available moves"""
        self.possible_moves = []

    def choose_move(self):
        """chooses a move to make"""
        top, mid, bot, edg = [], [], [], []
        for item in self.possible_moves:
            if item in self.top_priorities:
                top.append(item)
            elif item in self.mid_priorities:
                mid.append(item)
            elif item in self.bot_priorities:
                bot.append(item)
            elif item in self.fin_priorities:
                edg.append(item)
        if top:
            return top[0]
        elif mid:
            return mid[0]
        elif bot:
            return bot[0]
        elif edg:
            return edg[0]
        else:
            moves = self.clear_bad_moves()
            if moves:
                return moves[0]
            else:
                moves = self.last_resort()
                if moves:
                    return moves[0]
                else:
                    if self.possible_moves:
                        return rn.choice(self.possible_moves)
                    else:
                        return None

    def clear_bad_moves(self):
        """Filters out bad options"""
        better_moves = []
        for item in self.possible_moves:
            if item not in self.avoid_aac and item not in self.avoid:
                better_moves.append(item)
        return better_moves

    def last_resort(self):
        """tries to filter out worst options, if only bad available"""
        better_moves = []
        for item in self.possible_moves:
            if item not in self.avoid_aac:
                better_moves.append(item)
        return better_moves

    def talk_smack(self):
        """Prints smack talk to terminal"""
        # Originally had it print smack talk to the screen, but it
        # turned out to be way funnier in the terminal.
        print(rn.choice(self.smack_talk))
