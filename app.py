from flask import Flask
from config import init_app, db
from controller.my_data_controller import my_data_controller
from model.my_data import MyData

app = Flask(__name__)
print("✅ Flask app created")

init_app(app)
print("✅ Config initialized")

app.register_blueprint(my_data_controller)
print("✅ Blueprint registered")

with app.app_context():
    db.create_all()
    print("✅ Tables created")

if __name__ == '__main__':
    print("🚀 Starting server...")
    app.run(debug=True)