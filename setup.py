from setuptools import setup, find_packages

__version__ = "0.1"


setup(
    name="flask_ex",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    install_requires=["flask", "flask-sqlalchemy", "bpython"],
    entry_points={"console_scripts": ["flask_ex = app:cli"]},
)
