"""Wissen Baum Engineering Solutions — internal HR dashboard.

Phase 0: minimal Flask foundation. No features yet.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Minimal test route proving Flask -> Jinja -> HTML works."""
    return render_template("index.html", title="HR Dashboard — Foundation")


@app.route("/styleguide")
def styleguide():
    """Internal reference sheet for the Phase 1A design system."""
    return render_template("styleguide.html", title="Design System — Style Guide")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
