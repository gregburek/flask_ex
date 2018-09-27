# flask, flask-sqlalchemy and bpython bug report example app

I am trying to use a bpython-curses shell as a flask cli command, but am having problems.

After reading bpython/bpython#676, it appeared that using bpython-curses in a flask context would be possible. However, if I use the same entry_point as bpython https://github.com/bpython/bpython/blob/master/setup.py#L251 I get a `NameError: name 'bpython' is not defined` error.

The following shows the default flask shell, bpython and bpython-curses attempting to interact with a flask-sqlalchemy app:

```
$ pipenv run flask_ex shell
Python 3.6.5 (default, Apr 12 2018, 14:38:09)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)] on darwin
App: wiki [production]
Instance: /Users/gburek/code/flask-ex/instance
>>> from app import db, User
>>> me = User('admin', 'admin@example.com')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: __init__() takes 1 positional argument but 3 were given
>>> user = User(username='admin', email='admin@example.com')
>>> db.session.add(user)
>>> db.session.commit()
>>> User.query.all()
[<User 'admin'>]
>>>
now exiting InteractiveConsole...

$ pipenv run flask_ex bpython
Python 3.6.5 (default, Apr 12 2018, 14:38:09)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)] on darwin
App: wiki [production]
Instance: /Users/gburek/code/flask-ex/instance
>>> from app import db, User
>>> user = User(username='admin', email='admin@example.com')
>>> db.session.add(user)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    db.session.add(user)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/sqlalchemy/orm/scoping.py", line 153, in do
    return getattr(self.registry(), name)(*args, **kwargs)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/sqlalchemy/util/_collections.py", line 1001, in __call__
    return self.registry.setdefault(key, self.createfunc())
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/sqlalchemy/orm/session.py", line 2950, in __call__
    return self.class_(**local_kw)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py", line 141, in __init__
    self.app = app = db.get_app()
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py", line 912, in get_app
    'No application found. Either work inside a view function or push'
RuntimeError: No application found. Either work inside a view function or push an application context. See http://flask-sqlalchemy.pocoo.org/contexts/.
>>>

$ pipenv run flask_ex bpython_curses
Traceback (most recent call last):
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/bin/flask_ex", line 11, in <module>
    load_entry_point('flask-ex', 'console_scripts', 'flask_ex')()
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/click/core.py", line 764, in __call__
    return self.main(*args, **kwargs)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/flask/cli.py", line 557, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/click/core.py", line 717, in main
    rv = self.invoke(ctx)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/click/core.py", line 1137, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/click/core.py", line 956, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/click/decorators.py", line 17, in new_func
    return f(get_current_context(), *args, **kwargs)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/flask/cli.py", line 412, in decorator
    return __ctx.invoke(f, *args, **kwargs)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/click/decorators.py", line 17, in new_func
    return f(get_current_context(), *args, **kwargs)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/flask/cli.py", line 412, in decorator
    return __ctx.invoke(f, *args, **kwargs)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/Users/gburek/code/flask-ex/app.py", line 101, in bpython_curses
    main(banner=banner, locals_=ctx)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/bpython/cli.py", line 1959, in main
    banner=banner)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/bpython/cli.py", line 1844, in curses_wrapper
    return func(stdscr, *args, **kwargs)
  File "/Users/gburek/.local/share/virtualenvs/flask-ex-03Wix3mp/lib/python3.6/site-packages/bpython/cli.py", line 1905, in main_curses
    bpython.args.exec_code(interpreter, args)
NameError: name 'bpython' is not defined
```

Any idea how to get the bpython-curses entry point to work?