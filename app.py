from flask import Flask, render_template, request

app = Flask(__name__)


# =========================
# ROUND 1 ANSWERS
# =========================

correct_answers = {
    "q1": "0",
    "q2": "1",
    "q3": "1",
    "q4": "2",
    "q5": "2",
    "q6": "0",
    "q7": "2",
    "q8": "1",
    "q9": "3",
    "q10": "1",
    "q11": "0",
    "q12": "1",
    "q13": "2",
    "q14": "2",
    "q15": "2",
    "q16": "1",
    "q17": "2",
    "q18": "1",
    "q19": "0",
    "q20": "0",
    "q21": "0",
    "q22": "0",
    "q23": "1",
    "q24": "0",
    "q25": "1",
    "q26": "0",
    "q27": "1",
    "q28": "1",
    "q29": "0",
    "q30": "0"
}


# =========================
# HOME
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# REGISTER
# =========================

@app.route("/register")
def register():
    return render_template("register.html")


# =========================
# ROUND 1
# =========================

@app.route("/round1", methods=["POST"])
def round1():

    name = request.form.get("name")

    return render_template(
        "round1.html",
        name=name
    )


# =========================
# SUBMIT ROUND 1
# =========================

@app.route("/submit_round1", methods=["POST"])
def submit_round1():

    score = 0

    for question, correct_answer in correct_answers.items():

        user_answer = request.form.get(question)

        if user_answer == correct_answer:
            score += 1

    return render_template(
        "result.html",
        score=score,
        total=30
    )


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)