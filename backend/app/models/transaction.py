from app.extensions import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    block_number = db.Column(db.Integer, nullable=False)
    txn_hash = db.Column(db.Text, nullable=False)
    txn_timestamp = db.Column(db.DateTime, nullable=False)
    gas_price = db.Column(db.Text, nullable=False)
    gas_used = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Txn "{self.txn_hash}" "{self.txn_timestamp}" "{self.gas_price}" "{self.gas_used}">'
