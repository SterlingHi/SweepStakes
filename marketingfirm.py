from sweepstakes import  Sweepstakes
from userinter import UserInterface


class MarketingFirm:

    def __init__(self, name):
        self.name = name
        self.sweepstakes_storage = []

    def change_marketing_firm_name(self):
        new_name = UserInterface.get_user_input_string("Enter marketing firm's name.")
        self.name = new_name
        return self.menu()

    def create_sweepstakes(self):
        sweepstakes_name = UserInterface.get_user_input_string("Enter sweepstakes name.")
        sweepstakes = Sweepstakes(sweepstakes_name)
        self.sweepstakes_storage.append(sweepstakes)
        return self.menu()

    def select_sweepstakes(self):
        sweepstakes = Sweepstakes(self)
        chosen_sweepstakes = UserInterface.display_sweepstakes_selection_menu(self.sweepstakes_storage)
        return sweepstakes.menu(chosen_sweepstakes)

    def menu(self):
        validated_user_selection = (False, None)
        UserInterface.display_marketing_firm_menu_options(self.name)
        user_selection = UserInterface.get_user_input_number("Please make a selection.")
        while validated_user_selection[0] is False:
            if user_selection == 1:
                self.create_sweepstakes()
            elif user_selection == 2:
                self.change_marketing_firm_name()
            elif user_selection == 3:
                self.select_sweepstakes()
            validated_user_selection = UserInterface.validate_user_selection(validated_user_selection)
        return validated_user_selection[0]