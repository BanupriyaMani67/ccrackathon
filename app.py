
from flask import Flask, render_template, request, redirect, url_for, session
import time

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-key"

ALLOWED_PASSWORDS = {
    "21RCB18@",
    "2002proton#",
    "7420rohan@"
}

MAX_ATTEMPTS = 10
LOCK_SECONDS = 30


@app.route("/", methods=["GET", "POST"])
def index():
    now = time.time()

    locked_until = session.get("locked_until", 0)
    remaining = max(0, int(locked_until - now + 0.999))

    if remaining > 0:
        return render_template(
            "index.html",
            locked=True,
            remaining=remaining,
            message="Too many incorrect attempts. Please wait!"
        )

    # Unlock automatically when the timer ends
    if locked_until:
        session.pop("locked_until", None)
        session["attempts"] = 0

    message = ""
    attempts = session.get("attempts", 0)

    if request.method == "POST":
        password = request.form.get("password", "")

        if password in ALLOWED_PASSWORDS:
            session["solved"] = True
            session.pop("attempts", None)
            return redirect(url_for("success"))

        attempts += 1
        session["attempts"] = attempts

        if attempts >= MAX_ATTEMPTS:
            session["locked_until"] = time.time() + LOCK_SECONDS
            return render_template(
                "index.html",
                locked=True,
                remaining=LOCK_SECONDS,
                message="10 incorrect attempts reached!"
            )

        message = f"Incorrect password! Attempts used: {attempts}/{MAX_ATTEMPTS}"

    return render_template(
        "index.html",
        locked=False,
        remaining=0,
        message=message
    )


@app.route("/success")
def success():
    if not session.get("solved"):
        return redirect(url_for("index"))
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)