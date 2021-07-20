import marketingfirm
from userinter import UserInterface
from marketingfirm import MarketingFirm
from sweepstakes import Sweepstakes


if __name__ == '__main__':
    run_program = UserInterface.display_message("\t\tWelcome to the sweepstakes.\t\t \tPress -1- to display menu.\t \tPress -2- to display sweepstakes.\t")
    marketing_firm_name = UserInterface.get_user_input_string("Enter marketing firm's name.")
    marketing_firm = MarketingFirm(marketing_firm_name)
    user_selection = UserInterface.get_user_input_number("Please enter your selection here:")
    if user_selection == 1:
        marketing_firm.menu()
    elif user_selection == 2:
        try:
            Sweepstakes.menu(UserInterface.display_sweepstakes_selection_menu())
        except TypeError:
            print("There are no sweepstakes entered at this time.")