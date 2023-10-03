import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.words = ["python", "hangman", "computer", "programming", "interface", "developer", "learning", "challenge", "coding"]
        self.word_to_guess = random.choice(self.words).upper()
        self.remaining_attempts = 6
        self.guesses = set()

        self.word_display = tk.StringVar()
        self.update_word_display()

        self.word_label = tk.Label(root, textvariable=self.word_display, font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 18), width=5)
        self.entry.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.submit_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)

    def update_word_display(self):
        displayed_word = ""
        for letter in self.word_to_guess:
            if letter in self.guesses:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        self.word_display.set(displayed_word)

    def check_guess(self):
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if guess in self.guesses:
            self.result_label.config(text="You already guessed that letter.")
        else:
            self.guesses.add(guess)
            if guess not in self.word_to_guess:
                self.remaining_attempts -= 1

            self.update_word_display()

            if "_" not in self.word_display.get():
                self.result_label.config(text="Congratulations! You guessed the word!")
                self.submit_button.config(state=tk.DISABLED)
            elif self.remaining_attempts == 0:
                self.result_label.config(text=f"Game over! The word was '{self.word_to_guess}'.")
                self.submit_button.config(state=tk.DISABLED)
            else:
                self.result_label.config(text=f"Remaining attempts: {self.remaining_attempts}")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

