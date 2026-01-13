from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
import time 

app = Flask(__name__)

# ---------------------------
# DATABASE CONFIG
# ---------------------------
# mysql+pymysql://user:password@host:port/database
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:ahmadzia@database:3306/university"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ---------------------------
# MODEL (TABLE)
# ---------------------------
class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
               


#for i in range(10):
 #   try:
with app.app_context():
    db.create_all()
    #    print("Database connected")
     #   break
    #except OperationalError as e:
     #    print(e)
      #   time.sleep(10)


# ---------------------------
# ROUTES
# ---------------------------
@app.route('/api/items/', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify(
        [{"id": item.id, "name": item.name} for item in items]
        )


@app.route('/api/items/create', methods=['GET'])
def create_item():
    item = Item(name="Item from DB")
    db.session.add(item)
    db.session.commit()
    return {"message": "Item inserted"}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

