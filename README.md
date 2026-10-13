# PASSWORD CHALLENGE — DIGIFIESTA 2026

A two-screen Flask website with a blue, black, and white theme.

## Features
- Page 1: event name, instructions, password form, attempt counter.
- 10 incorrect guesses trigger a 30-second lockout.
- Attempts and lockout are stored in the Flask session cookie, so refreshing or reopening the same browser session does not reset the challenge.
- Correct password opens the success page.
- “GO TO ROUND 2” reveals the message directing participants to the board.

## Run locally (Windows PowerShell)

1. Install Python 3.11+.
2. Extract this ZIP.
3. Open PowerShell in the extracted `password-challenge` folder.
4. Run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:CHALLENGE_PASSWORD="RCB@Goa21"
$env:FLASK_SECRET_KEY="replace-this-with-a-long-random-secret"
python app.py
```

5. Open `http://127.0.0.1:5000` in your browser.

If PowerShell blocks activation, run the commands without activating the environment:
```powershell
py -m pip install -r requirements.txt
py app.py
```

## Deploy
For a hosted deployment, set these environment variables in your hosting provider:
- `CHALLENGE_PASSWORD`: the answer players must enter.
- `FLASK_SECRET_KEY`: a long, random secret value.
- Start command: `gunicorn app:app`

Do not use the sample secret key for a public deployment.

## Important
- The sample challenge answer is `RCB@Goa21`. Change it using the `CHALLENGE_PASSWORD` environment variable before the event if needed.
- Flask's default session is cookie-based and signed, not encrypted. It prevents casual tampering but is not a complete anti-cheat system. For a public competition with determined participants, use server-side sessions/storage and add rate limiting.
