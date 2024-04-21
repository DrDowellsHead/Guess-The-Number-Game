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
        width = 600
        height = 400

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width // 2) - (600 // 2)
        y = (screen_height // 2) - (400 // 2)

        self.window.geometry(f'{width}x{height}+{x}+{y}')

        # Variable for random numbers
        self.number_of_digits = None
        self.random_num = None
        self.victory = False
        # Attempts counter
        self.counter = 0
        self.attempt = tk.Label(window, text=f'Attempts: {self.counter}')
        self.attempt.pack()

        self.our_range = tk.Label(window, text='')
        self.our_range.pack()

        # Creating text above the input field for a range of numbers for the game
        self.field_num_entry = tk.Label(window, text='Entry number of digits: ')
        self.field_num_entry.pack()

        # Creating field for entry a range of numbers for the game
        self.field_entry = tk.Entry(window)
        self.field_entry.pack()

        # Creating button for a range of numbers for the game
        self.button_entry = tk.Button(window, text='Go!',
                                      command=lambda: (self.randoms_numbers(), self.display_input()))
        self.button_entry.pack()

        # self.input_text_label = tk.Label(text='')
        # self.input_text_label.pack()

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
        self.error_text = tk.Label(text='')
        self.error_text.pack()

    def display_input(self):
        user_input = self.field_entry.get()
        try:
            user_input = int(user_input)
            self.our_range.config(text=f'You have selected the range from 0 to {user_input}')
            self.our_range.pack()
        except ValueError:
            self.our_range.config(text="")
            self.our_range.pack()

    def randoms_numbers(self):
        """This function generate random numbers for game and increases attempt counter."""
        try:
            self.number_of_digits = int(self.field_entry.get())
            self.random_num = random.randint(0, self.number_of_digits)
            self.counter = 0
            self.attempt.config(text=f'Attempts: {self.counter}')

            self.victory = False
            self.error_text.destroy()
        except ValueError:
            self.error_text.config(text='Error! Please, entry the number.')
            self.error_text.pack()

    def check_guess(self):
        """This function get user entry and print result of guess."""

        try:
            user_number = int(self.field_num_guess.get())

            for widget in self.window.winfo_children():
                if isinstance(widget, tk.Label) and widget['text'] in [
                    'Exactly! Congratulations, you guessed the number!',
                    'Oops... More than the program planned.',
                    'Unfortunately, you indicated a number less than what the program guessed...',
                    'You have already guessed the number, please guess a new one']:
                    widget.destroy()
            if not self.victory:
                if user_number == self.random_num:
                    message = tk.Label(text='Exactly! Congratulations, you guessed the number!')
                    self.victory = True
                elif user_number > self.random_num:
                    message = tk.Label(text='Oops... More than the program planned.')
                elif user_number < self.random_num:
                    message = tk.Label(
                        text='Unfortunately, you indicated a number less than what the program guessed...')
                self.counter += 1
                self.attempt.config(text=f'Attempts: {self.counter}')
                self.attempt.pack()
            else:
                message = tk.Label(text='You have already guessed the number, please guess a new one')

            message.pack()
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
