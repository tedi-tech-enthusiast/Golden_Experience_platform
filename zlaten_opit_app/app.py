from flask import Flask
from routes.user_routes import user_bp
from routes.consultant_routes import consultant_bp
from routes.consultation_routes import consultation_bp
import db

app = Flask(__name__)

# Регистрираме модулите (пътищата)
app.register_blueprint(user_bp)
app.register_blueprint(consultant_bp)
app.register_blueprint(consultation_bp)

if __name__ == "__main__":
    app.run(debug=True)
