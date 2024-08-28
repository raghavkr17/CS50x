import os
import requests
import urllib.parse
from flask import redirect, render_template, request, session
from functools import wraps

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def lookup(symbol):
    """Look up quote for symbol."""

    # Ensure symbol is properly quoted for URL
    symbol = urllib.parse.quote_plus(symbol)

    # Construct API URL with symbol and API key
    api_key = os.environ.get("API_KEY")
    url = f"https://cloud-sse.iexapis.com/stable/stock/{symbol}/quote?token={api_key}"

    try:
        # Make request to API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes

        # Print raw response for debugging (can be removed later)
        print("API Response:", response.text)
    except requests.RequestException as e:
        print("Request Exception:", e)
        # If the request fails, return None
        return None

    try:
        # Parse JSON response
        quote = response.json()

        # Return relevant data if keys are present
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError) as e:
        print("Parsing Exception:", e)
        # If response parsing fails or keys are missing, return None
        return None

def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
