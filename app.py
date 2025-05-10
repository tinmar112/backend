from flask import Flask, redirect, request, render_template

from pegs import pegs


app = Flask(__name__)

winning_combo: list[str] = ['','','','']
played: list[str] = []

@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/start')
def start():
    global winning_combo
    winning_combo = ['green','green','yellow','yellow']
    global played
    played = ['The combinations you have played will appear below.']
    return render_template('play.html', already_played=played)


@app.route('/play', methods=['POST'])
def play():
    if request.method == 'POST':
        
        first_colour = request.form['1st colour']
        second_colour = request.form['2nd colour']
        third_colour = request.form['3rd colour']
        fourth_colour = request.form['4th colour']
        
        chosen_combo = [first_colour, second_colour,
                        third_colour, fourth_colour]
        
        if chosen_combo == winning_combo:
            return redirect('/won')
        
        else :
            pegs_result = pegs(winning_combo, chosen_combo)

            global played
            played.append(f"{first_colour} {second_colour} {third_colour} {fourth_colour} => => => {pegs_result}")

            return render_template('play.html', 
                                   already_played=played)


@app.route('/won')
def won():
    return render_template('won.html')


if __name__ == '__main__':
    app.run(debug=True)