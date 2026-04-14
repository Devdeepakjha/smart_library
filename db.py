import sqlite3
import os

from seed.seed_books import build_seed_books

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def seed_data():
    conn = get_db()

    # default admin
    row = conn.execute("SELECT id FROM users WHERE username = ?", ("admin",)).fetchone()
    if row is None:
        conn.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            ("admin", "admin123", "Admin"),
        )

    # seed books (safe insert: skip if already exists)
    books = build_seed_books()
    for b in books:
        exists = conn.execute(
            "SELECT book_id FROM books WHERE title = ? AND author = ?",
            (b["title"], b["author"]),
        ).fetchone()
        if exists is None:
            conn.execute(
                """
                INSERT INTO books
                (title, author, category, description, summary, cover_image, availability, issue_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    b["title"],
                    b["author"],
                    b["category"],
                    b["description"],
                    b["summary"],
                    b["cover_image"],
                    "Yes",
                    0,
                ),
            )

    conn.commit()
    conn.close()


def init_db():
    if not os.path.exists(DB_PATH):
        conn = get_db()
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
    seed_data()

