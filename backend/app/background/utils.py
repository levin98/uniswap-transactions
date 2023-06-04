from app.etherscan import api
from app.models.transaction import Transaction
from app.extensions import db
from datetime import datetime


def record_historical_data(app, start_time, end_time):
    """Background job to record historical transactions from Etherscan API"""

    block_start = api.get_block_number_by_timestamp(start_time)
    block_end = api.get_block_number_by_timestamp(end_time)

    if block_start == "" or block_end == "":
        return

    data = api.get_transactions(
        start_block=block_start, end_block=block_end)

    with app.app_context():
        for txn in data:
            if Transaction.query.filter_by(txn_hash=txn['hash']).first() is not None:
                continue

            transaction = Transaction(
                block_number=int(txn['blockNumber']),
                txn_hash=txn['hash'],
                txn_timestamp=datetime.fromtimestamp(int(txn['timeStamp'])),
                gas_price=txn['gasPrice'],
                gas_used=txn['gasUsed']
            )
            db.session.add(transaction)
            db.session.commit()
