from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from datetime import datetime

from db import get_db
from utils.helpers import is_logged_in, today_str, add_days_str

book_bp = Blueprint("book", __name__)


@book_bp.route("/", endpoint="home")
def home():
    if is_logged_in():
        return redirect(url_for("book.dashboard"))

    conn = get_db()
    categories = [r["category"] for r in conn.execute("SELECT DISTINCT category FROM books ORDER BY category").fetchall()]
    featured = conn.execute("SELECT * FROM books ORDER BY issue_count DESC, book_id DESC LIMIT 8").fetchall()
    conn.close()
    return render_template("index.html", categories=categories, featured=featured)


@book_bp.route("/dashboard", endpoint="dashboard")
def dashboard():
    if not is_logged_in():
        return redirect(url_for("auth.login"))

    conn = get_db()
    total_books = conn.execute("SELECT COUNT(*) AS c FROM books").fetchone()["c"]
    issued_books = conn.execute("SELECT COUNT(*) AS c FROM books WHERE availability = 'No'").fetchone()["c"]
    available_books = conn.execute("SELECT COUNT(*) AS c FROM books WHERE availability = 'Yes'").fetchone()["c"]
    categories = [r["category"] for r in conn.execute("SELECT DISTINCT category FROM books").fetchall()]
    top_books = conn.execute("SELECT * FROM books ORDER BY issue_count DESC LIMIT 5").fetchall()

    issued = conn.execute(
        """
        SELECT ib.*, b.title, b.author
        FROM issued_books ib
        JOIN books b ON b.book_id = ib.book_id
        WHERE ib.user_id = ? AND ib.returned = 0
        ORDER BY ib.issue_date DESC
        """,
        (session["user_id"],),
    ).fetchall()
    conn.close()

    return render_template(
        "dashboard.html",
        total_books=total_books,
        issued_books=issued_books,
        available_books=available_books,
        categories=categories,
        top_books=top_books,
        issued=issued,
    )


@book_bp.route("/books", endpoint="books")
def books():
    if not is_logged_in():
        return redirect(url_for("auth.login"))

    q = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()

    conn = get_db()
    categories = [r["category"] for r in conn.execute("SELECT DISTINCT category FROM books").fetchall()]

    sql = "SELECT * FROM books WHERE 1=1"
    params = []
    if q != "":
        session["recent_search"] = q
        sql += " AND (title LIKE ? OR author LIKE ? OR category LIKE ?)"
        like = "%" + q + "%"
        params.append(like)
        params.append(like)
        params.append(like)
    if category != "":
        sql += " AND category = ?"
        params.append(category)
    sql += " ORDER BY title"

    all_books = conn.execute(sql, tuple(params)).fetchall()

    recommended = conn.execute(
        "SELECT * FROM books ORDER BY issue_count DESC, book_id DESC LIMIT 5"
    ).fetchall()

    random_books = []
    if len(all_books) == 0:
        random_books = conn.execute("SELECT * FROM books ORDER BY RANDOM() LIMIT 4").fetchall()

    conn.close()

    return render_template(
        "books.html",
        books=all_books,
        categories=categories,
        q=q,
        category=category,
        recent_search=session.get("recent_search", ""),
        recommended=recommended,
        random_books=random_books,
    )


@book_bp.route("/book/<int:book_id>", endpoint="book_detail")
def book_detail(book_id):
    if not is_logged_in():
        return redirect(url_for("auth.login"))

    conn = get_db()
    book = conn.execute("SELECT * FROM books WHERE book_id = ?", (book_id,)).fetchone()
    if book is None:
        conn.close()
        flash("Book not found.", "error")
        return redirect(url_for("book.books"))

    my_issue = conn.execute(
        "SELECT * FROM issued_books WHERE user_id = ? AND book_id = ? AND returned = 0",
        (session["user_id"], book_id),
    ).fetchone()

    reviews = conn.execute(
        """
        SELECT r.review, r.created_at, u.username
        FROM reviews r
        JOIN users u ON u.id = r.user_id
        WHERE r.book_id = ?
        ORDER BY r.id DESC
        """,
        (book_id,),
    ).fetchall()
    conn.close()

    return render_template("book_detail.html", book=book, my_issue=my_issue, reviews=reviews, today=today_str())


@book_bp.route("/issue/<int:book_id>", methods=["POST"], endpoint="issue_book")
def issue_book(book_id):
    if not is_logged_in():
        return redirect(url_for("auth.login"))

    conn = get_db()
    book = conn.execute("SELECT * FROM books WHERE book_id = ?", (book_id,)).fetchone()
    if book is None:
        conn.close()
        flash("Book not found.", "error")
        return redirect(url_for("book.books"))

    if book["availability"] != "Yes":
        conn.close()
        flash("Book is not available right now.", "error")
        return redirect(url_for("book.book_detail", book_id=book_id))

    already = conn.execute(
        "SELECT id FROM issued_books WHERE user_id = ? AND book_id = ? AND returned = 0",
        (session["user_id"], book_id),
    ).fetchone()
    if already is not None:
        conn.close()
        flash("You already issued this book.", "info")
        return redirect(url_for("book.book_detail", book_id=book_id))

    issue_date = today_str()
    return_date = add_days_str(7)

    conn.execute(
        "INSERT INTO issued_books (user_id, book_id, issue_date, return_date, returned) VALUES (?, ?, ?, ?, 0)",
        (session["user_id"], book_id, issue_date, return_date),
    )
    conn.execute("UPDATE books SET availability = 'No' WHERE book_id = ?", (book_id,))
    conn.execute("UPDATE books SET issue_count = issue_count + 1 WHERE book_id = ?", (book_id,))
    conn.commit()
    conn.close()

    flash("Book Issued Successfully.", "success")
    return redirect(url_for("book.profile"))


@book_bp.route("/return/<int:book_id>", methods=["POST"], endpoint="return_book")
def return_book(book_id):
    if not is_logged_in():
        return redirect(url_for("auth.login"))

    conn = get_db()
    issue = conn.execute(
        "SELECT * FROM issued_books WHERE user_id = ? AND book_id = ? AND returned = 0",
        (session["user_id"], book_id),
    ).fetchone()
    if issue is None:
        conn.close()
        flash("No active issue found for this book.", "error")
        return redirect(url_for("book.profile"))

    conn.execute(
        "UPDATE issued_books SET returned = 1, returned_on = ? WHERE id = ?",
        (today_str(), issue["id"]),
    )
    conn.execute("UPDATE books SET availability = 'Yes' WHERE book_id = ?", (book_id,))
    conn.commit()
    conn.close()

    flash("Book Returned.", "success")
    return redirect(url_for("book.profile"))


@book_bp.route("/review/<int:book_id>", methods=["POST"], endpoint="add_review")
def add_review(book_id):
    if not is_logged_in():
        return redirect(url_for("auth.login"))

    review = request.form.get("review", "").strip()
    if review == "":
        flash("Review cannot be empty.", "error")
        return redirect(url_for("book.book_detail", book_id=book_id))

    if len(review) > 120:
        flash("Keep review short (max 120 characters).", "error")
        return redirect(url_for("book.book_detail", book_id=book_id))

    conn = get_db()
    book = conn.execute("SELECT book_id FROM books WHERE book_id = ?", (book_id,)).fetchone()
    if book is None:
        conn.close()
        flash("Book not found.", "error")
        return redirect(url_for("book.books"))

    conn.execute(
        "INSERT INTO reviews (user_id, book_id, review, created_at) VALUES (?, ?, ?, ?)",
        (session["user_id"], book_id, review, datetime.now().strftime("%Y-%m-%d %H:%M")),
    )
    conn.commit()
    conn.close()

    flash("Review added.", "success")
    return redirect(url_for("book.book_detail", book_id=book_id))


@book_bp.route("/profile", endpoint="profile")
def profile():
    if not is_logged_in():
        return redirect(url_for("auth.login"))

    conn = get_db()
    active = conn.execute(
        """
        SELECT ib.*, b.title, b.author
        FROM issued_books ib
        JOIN books b ON b.book_id = ib.book_id
        WHERE ib.user_id = ? AND ib.returned = 0
        ORDER BY ib.issue_date DESC
        """,
        (session["user_id"],),
    ).fetchall()

    history = conn.execute(
        """
        SELECT ib.*, b.title, b.author
        FROM issued_books ib
        JOIN books b ON b.book_id = ib.book_id
        WHERE ib.user_id = ? AND ib.returned = 1
        ORDER BY ib.returned_on DESC
        """,
        (session["user_id"],),
    ).fetchall()
    conn.close()

    return render_template("profile.html", active=active, history=history, today=today_str())

