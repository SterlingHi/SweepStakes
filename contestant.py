class Contestant:

    def __init__(self):
        self.contestant_first_name = None
        self.contestant_last_name = None
        self.contestant_email = None
        self.contestant_registration_number = None

    def notify(self, is_winner):
        is_winner = False
        if is_winner:
            ("Sorry you have not won this sweepstakes.")
        else:
            ("Congratulations! You have won the sweepstakes!")