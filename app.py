from flask import Flask

from db import init_db
from routes.auth_routes import auth_bp
from routes.book_routes import book_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)
app.secret_key = "simple_library_secret"

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(book_bp)
app.register_blueprint(admin_bp)

# Initialize DB (safe for deployment)
init_db()

# Run locally
if __name__ == "__main__":
    app.run()