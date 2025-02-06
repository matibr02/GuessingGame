import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Store the random number and the number of attempts
number = random.randint(1, 10)  # Changed to 1-10
attempts = 0

@app.route('/', methods=['GET', 'POST'])
def guess_game():
    global attempts
    global number

    if request.method == 'POST':
        guess = request.form.get('guess')

        try:
            guess = int(guess)
        except ValueError:
            return render_template('index.html', message="Please enter a valid number.", attempts=attempts)

        attempts += 1

        if guess < number:
            message = "Too low! Try again."
        elif guess > number:
            message = "Too high! Try again."
        else:
            message = f"Correct! The number was {number}. It took you {attempts} attempts."
            # Reset the game after a correct guess
            number = random.randint(1, 10)  # Reset to a new number
            attempts = 0
        return render_template('index.html', message=message, attempts=attempts)

    return render_template('index.html', message="", attempts=attempts)

if __name__ == '__main__':
    app.run(debug=True)
