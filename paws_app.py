from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Rescue dog data
dogs = {
    "Buddy": {"breed": "Labrador", "age": "2 years", "status": "Present", "volunteer": "Sarah", "health": "Vaccinated", "notes": "Friendly"},
    "Rocky": {"breed": "German Shepherd", "age": "3 years", "status": "At Vet", "volunteer": "Mark", "health": "Needs checkup", "notes": "Limping"},
    "Luna": {"breed": "Beagle", "age": "1 year", "status": "Adoption Event", "volunteer": "Priya", "health": "Vaccinated", "notes": "Family interested"},
    "Charlie": {"breed": "Golden Retriever", "age": "4 years", "status": "Present", "volunteer": "Alex", "health": "Healthy", "notes": ""},
}

@app.route("/")
def index():
    total = len(dogs)
    present = sum(1 for d in dogs.values() if d["status"] == "Present")
    vet = sum(1 for d in dogs.values() if d["status"] == "At Vet")
    adoption = sum(1 for d in dogs.values() if d["status"] == "Adoption Event")
    missing = sum(1 for d in dogs.values() if d["status"] == "Missing")

    return render_template("index.html",
                           total=total, present=present, vet=vet,
                           adoption=adoption, missing=missing,
                           date=datetime.now().strftime("%d-%m-%Y"))

@app.route("/dogs", methods=["GET", "POST"])
def dogs_page():
    if request.method == "POST":
        for name in dogs:
            dogs[name]["status"] = request.form.get(name, dogs[name]["status"])
        return redirect(url_for("dogs_page"))
    return render_template("dogs.html", dogs=dogs, date=datetime.now().strftime("%d-%m-%Y"))

@app.route("/profile/<name>")
def profile(name):
    dog = dogs.get(name)
    return render_template("profile.html", name=name, dog=dog, date=datetime.now().strftime("%d-%m-%Y"))

@app.route("/volunteers", methods=["GET", "POST"])
def volunteers():
    if request.method == "POST":
        for name in dogs:
            dogs[name]["volunteer"] = request.form.get(name, dogs[name]["volunteer"])
        return redirect(url_for("volunteers"))
    return render_template("volunteers.html", dogs=dogs, date=datetime.now().strftime("%d-%m-%Y"))

@app.route("/reports")
def reports():
    return render_template("reports.html", dogs=dogs, date=datetime.now().strftime("%d-%m-%Y"))

if __name__ == "__main__":
    app.run(debug=True)
