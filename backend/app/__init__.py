from flask import Flask, request, jsonify
from config import Config
from app.models.transaction import Transaction
from app.extensions import db
from app.scheduler import scheduler
from app.etherscan import api
import functools


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize database
    db.init_app(app)

    # Initialize scheduler
    scheduler.sched.add_job(functools.partial(
        scheduler.record_live_transactions, app=app), 'interval', seconds=5)
    scheduler.sched.start()

    @app.route("/transactions", methods=['GET'])
    def get_transactions():
        """Get transactions from database"""

        # Get query parameters
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per-page", 50, type=int)
        start_time = request.args.get("start-time", None, type=int)
        end_time = request.args.get("end-time", None, type=int)

        if (start_time is not None) and (end_time is not None):
            transactions = Transaction.query.filter(
                Transaction.txn_timestamp.between(start_time, end_time)).paginate(page=page, per_page=per_page)
        else:
            transactions = Transaction.query.paginate(
                page=page, per_page=per_page)

        results = {
            "results": [txn.to_dict() for txn in transactions],
            "pagination": {
                "count": transactions.total,
                "page": page,
                "per_page": per_page,
                "pages": transactions.pages,
            },
        }
        return jsonify(results), 200

    @app.route("/transaction", methods=['GET'])
    def get_transaction_by_hash():
        """Get transaction by hash from database"""

        # Get query parameters
        hash = request.args.get("hash", None, type=str)
        if hash is None:
            return jsonify({"error": "No hash provided"}), 400

        transaction = Transaction.query.filter_by(txn_hash=hash).first()
        if transaction is None:
            transaction = api.get_transaction_by_hash(hash)
            if transaction is None:
                return jsonify({"error": "Transaction not found"}), 404

            results = {
                "block_number": int(transaction['blockNumber'], base=16),
                "txn_hash": transaction['transactionHash'],
                "gas_price": str(int(transaction['effectiveGasPrice'], base=16)),
                "gas_used": str(int(transaction['gasUsed'], base=16)),
            }
            return jsonify(results), 200

        return jsonify(transaction.to_dict()), 200

    return app
