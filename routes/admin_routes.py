from flask import Blueprint, render_template, request, redirect, url_for, flash

from db import get_db
from utils.helpers import is_logged_in, is_admin

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin", endpoint="admin")
def admin():
    if not is_logged_in():
        return redirect(url_for("auth.login"))
    if not is_admin():
        flash("Admin access only.", "error")
        return redirect(url_for("book.dashboard"))

    conn = get_db()
    total_books = conn.execute("SELECT COUNT(*) AS c FROM books").fetchone()["c"]
    total_users = conn.execute("SELECT COUNT(*) AS c FROM users").fetchone()["c"]
    total_issued = conn.execute("SELECT COUNT(*) AS c FROM issued_books WHERE returned = 0").fetchone()["c"]

    users = conn.execute("SELECT id, username, role FROM users ORDER BY id DESC").fetchall()
    books = conn.execute("SELECT * FROM books ORDER BY book_id DESC LIMIT 80").fetchall()
    issued = conn.execute(
        """
        SELECT ib.*, u.username, b.title
        FROM issued_books ib
        JOIN users u ON u.id = ib.user_id
        JOIN books b ON b.book_id = ib.book_id
        WHERE ib.returned = 0
        ORDER BY ib.issue_date DESC
        """
    ).fetchall()
    conn.close()

    return render_template(
        "admin.html",
        total_books=total_books,
        total_users=total_users,
        total_issued=total_issued,
        users=users,
        books=books,
        issued=issued,
    )


@admin_bp.route("/admin/book/add", methods=["POST"], endpoint="admin_add_book")
def admin_add_book():
    if not is_logged_in():
        return redirect(url_for("auth.login"))
    if not is_admin():
        flash("Admin access only.", "error")
        return redirect(url_for("book.dashboard"))

    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()
    category = request.form.get("category", "").strip()
    description = request.form.get("description", "").strip()
    summary = request.form.get("summary", "").strip()
    cover_image = request.form.get("cover_image", "").strip()

    if title == "" or author == "" or category == "" or description == "" or summary == "" or cover_image == "":
        flash("Please fill all book fields.", "error")
        return redirect(url_for("admin.admin"))

    conn = get_db()
    conn.execute(
        """
        INSERT INTO books (title, author, category, description, summary, cover_image, availability, issue_count)
        VALUES (?, ?, ?, ?, ?, ?, 'Yes', 0)
        """,
        (title, author, category, description, summary, cover_image),
    )
    conn.commit()
    conn.close()

    flash("Book added.", "success")
    return redirect(url_for("admin.admin"))


@admin_bp.route("/admin/book/edit/<int:book_id>", methods=["POST"], endpoint="admin_edit_book")
def admin_edit_book(book_id):
    if not is_logged_in():
        return redirect(url_for("auth.login"))
    if not is_admin():
        flash("Admin access only.", "error")
        return redirect(url_for("book.dashboard"))

    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()
    category = request.form.get("category", "").strip()
    description = request.form.get("description", "").strip()
    summary = request.form.get("summary", "").strip()
    cover_image = request.form.get("cover_image", "").strip()
    availability = request.form.get("availability", "Yes").strip()

    conn = get_db()
    conn.execute(
        """
        UPDATE books
        SET title = ?, author = ?, category = ?, description = ?, summary = ?, cover_image = ?, availability = ?
        WHERE book_id = ?
        """,
        (title, author, category, description, summary, cover_image, availability, book_id),
    )
    conn.commit()
    conn.close()

    flash("Book updated.", "success")
    return redirect(url_for("admin.admin"))


@admin_bp.route("/admin/book/delete/<int:book_id>", methods=["POST"], endpoint="admin_delete_book")
def admin_delete_book(book_id):
    if not is_logged_in():
        return redirect(url_for("auth.login"))
    if not is_admin():
        flash("Admin access only.", "error")
        return redirect(url_for("book.dashboard"))

    conn = get_db()
    conn.execute("DELETE FROM reviews WHERE book_id = ?", (book_id,))
    conn.execute("DELETE FROM issued_books WHERE book_id = ?", (book_id,))
    conn.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
    conn.commit()
    conn.close()

    flash("Book deleted.", "success")
    return redirect(url_for("admin.admin"))

