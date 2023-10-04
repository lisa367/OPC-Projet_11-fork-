import json
from datetime import datetime as dt
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions

app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    #club = [club for club in clubs if club['email'] == request.form['email']][0]
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions)

    except IndexError:
        print("IndexError")
        flash("No club with that email. Please try agin.")
        return ("Mail not found")
    

@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])

    if placesRequired > 12:
        flash("You cannot purchase more than 12 places per competition")
        
    else:
        if int(club['points'] )> 0:

            if placesRequired > int(club['points']):
                flash("You do not have enough points for this purchase")
                
            else:
                if placesRequired > int(competition['numberOfPlaces']):
                    flash("You cannot buy more places than available")
                else:
                    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
                    club['points'] = int(club['points']) - placesRequired
                    flash('Great-booking complete!')
                    # flash("You cannot buy more places than available")

        else:
            flash("You do not have enough points for this purchase")


    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ =="__main__":
    app.run(debug=True)