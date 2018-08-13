from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
    def form_mp():
        rf = """<form action="/guess_game" method='GET'>
            Let's play 'Guess number' Game.<br>
            Rules:
            <ol>
                <li>Pick number between 1 and 999</li>
                <li>Be honest, don't cheat!</li>
                <li>I'll try to guess it in 10 tries</li>
            </ol>
            <label>LET'S BEGIN!<br>
                <input type="submit" value="start"/>
            </label>
        </form>
        """
        return rf

    if request.method == 'GET':
        return form_mp()


@app.route('/guess_game', methods=['GET', 'POST'])
def guess_game():
    def form_try_again(msg):
        rf = f"""{msg}<br><br>
            <button onclick="window.location.href='/guess_game'">Try again</button><br><br>
            <button onclick="window.location.href='/'">Home Page</button>"""
        return rf

    def get_next_guess(minimum, maximum):
        number = int((maximum - minimum) / 2) + minimum
        return number

    def form_gg():
        rf = f"""My guess: {guess}
        Attempt No: {counter}
        <form action='#' method='POST'>
            <input type="hidden" name="min" value="{guess_min}"/>
            <input type="hidden" name="max" value="{guess_max}"/>
            <input type="hidden" name="guess" value="{guess}"/>
            <input type="hidden" name="counter" value="{counter}"/>
            <div>Pick one:
                <input type="submit" name="choice" value="Too low"/>
                <input type="submit" name="choice" value="You guessed it!"/>
                <input type="submit" name="choice" value="Too much"/>
            </div>
        </form>"""
        return rf

    if request.method == 'GET':
        counter = 1
        guess_min = 1
        guess_max = 1000
        guess = get_next_guess(guess_min, guess_max)
        return form_gg()
    elif request.method == 'POST':
        counter = int(request.form['counter']) + 1
        if counter == 11:
            return form_try_again('You are cheating!')
        choice = request.form['choice']
        print(choice)
        if choice == 'Too low':
            guess_min = int(request.form['guess'])
            guess_max = int(request.form['max'])
        elif choice == 'Too much':
            guess_min = int(request.form['min'])
            guess_max = int(request.form['guess'])
        else:
            return form_try_again('Success!!')
        guess = get_next_guess(guess_min, guess_max)
        return form_gg()


if __name__ == '__main__':
    app.run()
