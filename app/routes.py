from flask import Blueprint

from app import db_manager
from .views.hello_world import (
    hello_world,
)

bp = Blueprint('routes', __name__)

# alias
db = db_manager.session


# Request management
@bp.before_app_request
def before_request():
    db()


@bp.teardown_app_request
def shutdown_session(response_or_exc):
    db.remove()


# Public views
bp.add_url_rule('/', view_func=hello_world)
