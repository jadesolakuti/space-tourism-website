from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/')
@app.route('/home')
def home_page():
    bg_image = '/background1.png'
    return render_template('homepage.html', bg=bg_image)


@app.route('/destination/moon')
@app.route('/destination')
def destinationA():
    bg_image = '/background2.png'
    return render_template('destinationA.html', bg=bg_image)

@app.route('/destination/mars')
def destinationB():
    bg_image = '/background2.png'
    return render_template('destinationB.html', bg=bg_image)

@app.route('/destination/europa')
def destinationC():
    bg_image = '/background2.png'
    return render_template('destinationC.html', bg=bg_image)

@app.route('/destination/titan')
def destinationD():
    bg_image = '/background2.png'
    return render_template('destinationD.html', bg=bg_image)

@app.route('/crew')
@app.route('/crew/commander')
def crewCommander():
    bg_image = '/background3.png'
    return render_template('crewA.html', bg=bg_image)

@app.route('/crew/missionspecialist')
def crewMission():
    bg_image = '/background3.png'
    return render_template('crewB.html', bg=bg_image)

@app.route('/crew/pilot')
def crewPilot():
    bg_image = '/background3.png'
    return render_template('crewC.html', bg=bg_image)


@app.route('/crew/flightengineer')
def crewEngineer():
    bg_image = '/background3.png'
    return render_template('crewD.html', bg=bg_image)

@app.route('/technology')
@app.route('/vehicle')
def launchVehicle():
    bg_image = '/background4.png'
    return render_template('techA.html', bg=bg_image)

@app.route('/spaceport')
def spaceport():
    bg_image = '/background4.png'
    return render_template('techB.html', bg=bg_image)

@app.route('/spacecapsule')
def spaceCapsule():
    bg_image = '/background4.png'
    return render_template('techC.html', bg=bg_image)


if __name__ == "__main__":
    app.run()