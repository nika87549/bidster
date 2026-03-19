
# from flask import Flask
# from auth import auth, bcrypt

# app = Flask(__name__)
# bcrypt.init_app(app)

# app.register_blueprint(auth, url_prefix="/api/auth")

# @app.route("/")
# def home():
#     return {"message": "Bidster backend is running"}

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask
# from auth import auth, bcrypt
# from auction import auction_bp

# app = Flask(__name__)
# bcrypt.init_app(app)

# app.register_blueprint(auth, url_prefix="/api/auth")
# app.register_blueprint(auction_bp, url_prefix="/api/auction")

# @app.route("/")
# def home():
#     return {"message": "Bidster backend is running"}

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask
# from auth import auth, bcrypt
# from auction import auction_bp
# from admin import admin_bp

# app = Flask(__name__)
# bcrypt.init_app(app)

# app.register_blueprint(auth, url_prefix="/api/auth")
# app.register_blueprint(auction_bp, url_prefix="/api/auction")
# app.register_blueprint(admin_bp, url_prefix="/api/admin")

# @app.route("/")
# def home():
#     return {"message": "Bidster backend is running"}

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask
# from auth import auth, bcrypt
# from auction import auction_bp
# from admin import admin_bp
# from stats import stats_bp

# app = Flask(__name__)
# bcrypt.init_app(app)

# app.register_blueprint(auth, url_prefix="/api/auth")
# app.register_blueprint(auction_bp, url_prefix="/api/auction")
# app.register_blueprint(admin_bp, url_prefix="/api/admin")
# app.register_blueprint(stats_bp, url_prefix="/api/stats")

# @app.route("/")
# def home():
#     return {"message": "Bidster backend is running"}

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask
# from auth import auth, bcrypt
# from auction import auction_bp
# from admin import admin_bp
# from stats import stats_bp
# from payments import payments_bp

# app = Flask(__name__)
# bcrypt.init_app(app)

# app.register_blueprint(auth, url_prefix="/api/auth")
# app.register_blueprint(auction_bp, url_prefix="/api/auction")
# app.register_blueprint(admin_bp, url_prefix="/api/admin")
# app.register_blueprint(stats_bp, url_prefix="/api/stats")
# app.register_blueprint(payments_bp, url_prefix="/api/payments")

# @app.route("/")
# def home():
#     return {"message": "Bidster backend is running"}

# if __name__ == "__main__":
#     app.run(debug=True)


# from profile import profile_bp

# app.register_blueprint(profile_bp, url_prefix="/api/profile")


# from flask import send_from_directory
# import os

# @app.route("/uploads/<path:filename>")
# def uploaded_file(filename):
#     upload_folder = os.path.join(os.path.dirname(__file__), "uploads")
#     return send_from_directory(upload_folder, filename)


# from chat import chat_bp
# app.register_blueprint(chat_bp, url_prefix="/api/chat")



from flask import Flask, send_from_directory
from auth import auth, bcrypt
from auction import auction_bp
from admin import admin_bp
from stats import stats_bp
from payments import payments_bp
from profile import profile_bp
from chat import chat_bp
from flask_socketio import SocketIO
import os

app = Flask(__name__)
bcrypt.init_app(app)

# Socket.IO
socketio = SocketIO(app, cors_allowed_origins="*")

# Blueprints
app.register_blueprint(auth, url_prefix="/api/auth")
app.register_blueprint(auction_bp, url_prefix="/api/auction")
app.register_blueprint(admin_bp, url_prefix="/api/admin")
app.register_blueprint(stats_bp, url_prefix="/api/stats")
app.register_blueprint(payments_bp, url_prefix="/api/payments")
app.register_blueprint(profile_bp, url_prefix="/api/profile")
app.register_blueprint(chat_bp, url_prefix="/api/chat")

@app.route("/")
def home():
    return {"message": "Bidster backend is running"}

# Avatar uploads
@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    upload_folder = os.path.join(os.path.dirname(__file__), "uploads")
    return send_from_directory(upload_folder, filename)

# Start server
if __name__ == "__main__":
    socketio.run(app, debug=True)