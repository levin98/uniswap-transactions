from flask import Flask
from config import Config
from app.models.transaction import Transaction
from app.extensions import db
from app.scheduler import scheduler
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

    return app
