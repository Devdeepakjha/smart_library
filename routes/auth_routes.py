from flask import Blueprint, render_template, request, redirect, url_for, session, flash

from db import get_db

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["GET", "POST"], endpoint="signup")
def signup():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if username == "" or password == "":
            flash("Please fill all fields.", "error")
            return redirect(url_for("auth.signup"))

        conn = get_db()
        row = conn.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
        if row is not None:
            conn.close()
            flash("Username already exists. Try another.", "error")
            return redirect(url_for("auth.signup"))

        conn.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, "User"),
        )
        conn.commit()
        conn.close()

        flash("Signup successful. Please login.", "success")
        return redirect(url_for("auth.login"))

    return render_template("signup.html")


@auth_bp.route("/login", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        ).fetchone()
        conn.close()

        if user is None:
            flash("Invalid username or password.", "error")
            return redirect(url_for("auth.login"))

        session["user_id"] = user["id"]
        session["username"] = user["username"]
        session["role"] = user["role"]
        flash("Login successful.", "success")
        return redirect(url_for("book.dashboard"))

    return render_template("login.html")


@auth_bp.route("/logout", endpoint="logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("auth.login"))

