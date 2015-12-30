Flask-Auth
==========

Flask-Auth is a flask extension that offers database-agnostic (but still 
fairly plug-and-play) role-based user authentication. Sounds impressive, 
right?

Features
--------

* Uses a <= 254 char email address as username. Use another version if you want
  a regular username! 
* Set of functions to assist in user session management (logging in and out,
  getting the current user, expiring sessions, encrypting passwords, etc).
* Base user class AuthUser that can be used with most ORM's.
* Plug-and-play model for Google App Engine (and a working example for 
  SQLAlchemy).
* Straightforward permission model to differentiate access rights between 
  (groups of) users.

Documentation
-------------
Documentation for original may be found on `PyPI <http://packages.python.org/Flask-Auth/>`_.
