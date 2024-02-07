import random
import tkinter as tk


class Game:
    """This game offer to choice range of random number.
    Then user can guess number.
    Game will be give help if user guess wrong number.
    Good Luck!"""

    def __init__(self, window):
        # Creating a window as an argument to the root class
        self.window = window
        self.window.title('Guess The Number')
        # Documentation
        self.help = tk.Label(text=__doc__)

        # Window Alignment
        self.screen_width = window.winfo_screenwidth()
        self.screen_height = window.winfo_screenheight()

        self.x = (self.screen_width // 2) - (600 // 2)
        self.y = (self.screen_height // 2) - (600 // 2)

        # Variable for random numbers
        self.number_of_digits = None
        self.random_num = None
        # Attempts counter
        self.attempt = 0

        # Creating text above the input field for a range of numbers for the game
        self.field_num_entry = tk.Label(window, text='Entry number of digits: ')
        self.field_num_entry.pack()

        # Creating field for entry a range of numbers for the game
        self.field_entry = tk.Entry(window)
        self.field_entry.pack()

        # Creating button for a range of numbers for the game
        self.button_entry = tk.Button(window, text='Go!', command=self.randoms_numbers)
        self.button_entry.pack()

        # Creating text above the input field for guess
        self.field_text_guess = tk.Label(window, text='Guess the number: ')
        self.field_text_guess.pack()

        # Creating field for guess
        self.field_num_guess = tk.Entry(window)
        self.field_num_guess.pack()

        # Creating button for guess
        self.button_guess = tk.Button(window, text='I`m Feeling Lucky!', command=self.check_guess)
        self.button_guess.pack()

        # Variable for preparation of error
        self.error_text = None


    def randoms_numbers(self):
        """This function generate random numbers for game and increases attempt counter."""
        try:
            self.number_of_digits = int(self.field_entry.get())
            self.random_num = random.randint(0, self.number_of_digits)
            self.attempt += 1
        except ValueError:
            self.error_text = tk.Label(text='Error! Please, entry the number.')
            self.error_text.pack()


    def check_guess(self):
        """This function get user entry and print result of guess."""

        try:
            user_number = int(self.field_num_guess.get())
            self.attempt += 1

            if user_number == self.random_num:
                message_1 = tk.Label(text='Exactly! Congratulations, you guessed the number!')
            elif user_number > self.random_num:
                message_2 = tk.Label(text='Oops... More than the program planned.')
            elif user_number < self.random_num:
                message_3 = tk.Label(text='By the way, you indicated a number less than what the program guessed...')
        except ValueError:
            self.error_text = tk.Label(text='Error! Please, entry the number.')


def main():
    """This function realize drawing Tkinter window."""

    root = tk.Tk()
    game = Game(root)
    root.mainloop()


# Implements running the function main() first
if __name__ == '__main__':
    main()
