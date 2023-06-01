from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.etherscan import api
from app.extensions import db
from app.models.transaction import Transaction, get_last_block_number

# Creates a default Background Scheduler
sched = BackgroundScheduler()


def record_live_transactions(app):
    """Background job to record live transactions from Etherscan API"""

    with app.app_context():
        data = api.get_transactions(
            start_block=get_last_block_number())

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
