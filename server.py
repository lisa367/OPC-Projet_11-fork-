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


def saveClubs(clubs_modified):
    clubs_data = {"clubs": clubs_modified}
    with open('clubs.json', 'w') as file:
        json.dump(clubs_data, file, indent=4)


def saveCometitions(competitions_modified):
    competitions_data = {"competitions": competitions_modified}
    with open('competitions.json', 'w') as file:
        json.dump(competitions_data, file, indent=4)


""" app = Flask(__name__)
app.secret_key = 'something_special' """


def create_app(test_config, clubs_list, competitions_list):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "something special"
    # app.secret_key = 'something_special'
    # app.config.from_mapping(SECRET_KEY="something_special")
    # app.config.from_object("test_config")
    app.config["TESTING"] = test_config.get("TESTING")

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        #club = [club for club in clubs if club['email'] == request.form['email']][0]
        try:
            club = [club for club in clubs_list if club['email'] == request.form['email']][0]
            return render_template('welcome.html', club=club, competitions=competitions_list)

        except IndexError:
            print("IndexError")
            flash("No club with that email. Please try agin.")
            return ("Mail not found")
        

    @app.template_filter("competitionDateFilter")
    def competitionDateFilter(date_value):
        current_date = dt.now()
        competition_date = dt.strptime(date_value, "%Y-%m-%d %H:%M:%S")
        return current_date < competition_date


    # app.jinja_env.filters["competitionDateFilter"] = competitionDateFilter


    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        foundClub = [c for c in clubs_list if c['name'] == club][0]
        foundCompetition = [c for c in competitions_list if c['name'] == competition][0]
        if competitionDateFilter(foundCompetition['date']) :
            if foundClub and foundCompetition:
                return render_template('booking.html',club=foundClub,competition=foundCompetition)
            else:
                flash("Something went wrong-please try again")
                return render_template('welcome.html', club=club, competitions=competitions_list)
        else:
            return ("You cannot book places from a past competition")


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        competition = [c for c in competitions_list if c['name'] == request.form['competition']][0]
        club = [c for c in clubs_list if c['name'] == request.form['club']][0]
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
                        competition['numberOfPlaces'] = str(int(competition['numberOfPlaces']) - placesRequired)
                        club['points'] = str(int(club['points']) - placesRequired)
                        flash('Great-booking complete!')

                        """ print(clubs)
                        print(competitions) """
                        
                        saveClubs(clubs_list)
                        saveCometitions(competitions_list)

            else:
                flash("You do not have enough points for this purchase")


        return render_template('welcome.html', club=club, competitions=competitions_list)


    # TODO: Add route for points display

    @app.route('/pointsDisplay',methods=['GET'])
    def pointsDisplay():
        return render_template('points_board.html', clubs_points=clubs_list)


    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))
    

    return app




if __name__ == "__main__":
    competitions = loadCompetitions()
    clubs = loadClubs()

    app = create_app({"TESTING": False}, clubs_list=clubs, competitions_list=competitions)
    app.run(debug=True)