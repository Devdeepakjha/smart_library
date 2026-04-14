from datetime import datetime, timedelta
from flask import session


def is_logged_in():
    return "user_id" in session


def is_admin():
    return session.get("role") == "Admin"


def today_str():
    return datetime.now().strftime("%Y-%m-%d")


def add_days_str(days):
    return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")

