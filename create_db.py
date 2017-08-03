from app import db
from models import Pizza, Choice


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
