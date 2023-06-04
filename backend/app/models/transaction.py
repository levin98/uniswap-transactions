from app.extensions import db
from sqlalchemy import desc


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

    def to_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


def get_last_block_number():
    """Get the last block number recorded in the database"""

    last_record = Transaction.query.order_by(
        desc(Transaction.txn_timestamp)).first()
    if last_record is not None:
        return last_record.block_number
    return 0
