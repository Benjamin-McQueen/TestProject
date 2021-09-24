from app import database


class User(database.Model):
    __tablename__ = 'user'
    table_args = {u'schema': 'main'}

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    pw = database.Column(database.String(120), nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.email}','{self.pw}')"
