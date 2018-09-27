import click
from flask import Flask
from flask.cli import FlaskGroup, with_appcontext
from flask_sqlalchemy import SQLAlchemy

import os
import sys

db = SQLAlchemy()


def create_app():
    app = Flask("wiki")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
    db.init_app(app)

    return app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Management script for the flask-ex application."""


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


@cli.command("bpython", short_help="Runs a shell in the app context.")
@with_appcontext
def bpython():
    """Runs an interactive Python shell in the context of a given
    Flask application.  The application will populate the default
    namespace of this shell according to it's configuration.
    This is useful for executing small snippets of management code
    without having to manually configure the application.
    """
    from flask.globals import _app_ctx_stack
    from bpython.cli import main
    import bpython

    app = _app_ctx_stack.top.app
    banner = "Python %s on %s\nApp: %s [%s]\nInstance: %s" % (
        sys.version,
        sys.platform,
        app.import_name,
        app.env,
        app.instance_path,
    )
    ctx = {}

    # Support the regular Python interpreter startup script if someone
    # is using it.
    startup = os.environ.get("PYTHONSTARTUP")
    if startup and os.path.isfile(startup):
        with open(startup, "r") as f:
            eval(compile(f.read(), startup, "exec"), ctx)

    ctx.update(app.make_shell_context())

    bpython.embed(banner=banner, locals_=ctx)


@cli.command("bpython_curses", short_help="Runs a shell in the app context.")
@with_appcontext
def bpython_curses():
    """Runs an interactive Python shell in the context of a given
    Flask application.  The application will populate the default
    namespace of this shell according to it's configuration.
    This is useful for executing small snippets of management code
    without having to manually configure the application.
    """
    from flask.globals import _app_ctx_stack
    from bpython.cli import main
    import bpython

    app = _app_ctx_stack.top.app
    banner = "Python %s on %s\nApp: %s [%s]\nInstance: %s" % (
        sys.version,
        sys.platform,
        app.import_name,
        app.env,
        app.instance_path,
    )
    ctx = {}

    # Support the regular Python interpreter startup script if someone
    # is using it.
    startup = os.environ.get("PYTHONSTARTUP")
    if startup and os.path.isfile(startup):
        with open(startup, "r") as f:
            eval(compile(f.read(), startup, "exec"), ctx)

    ctx.update(app.make_shell_context())

    main(banner=banner, locals_=ctx)
