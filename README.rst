flask-auth-username-is-email
============================

Flask-Auth is a flask extension that offers database-agnostic (but still 
fairly plug-and-play) role-based user authentication. Sounds impressive, 
right?

This is Not What You Think it is, Probably
==========================================

I needed to use a <= 254 character email address as a username (don't ask).
Basically I did a recursive s/username/email/g and modified some docs. I've 
changed the name from Flask-Auth so the unwary won't use my monkey-patched BS
and get a horrible, horrible surprise. Further caveats include:

* A some point in the past the tests stopped working. I'm going to fix them when I have a chance, but just know that you can't enable a virtualenv, install Flask and run test_auth.py.

* The docs in the repo I forked this from refer to an example using mongoalchemy. I saw nothing in the repo that had anything to do with mongoalchemy so I took that reference out.

Features
--------

* Uses a <= 254 char email address as username. Use another version if you want
  a regular username! Use another version anyway!
* Set of functions to assist in user session management (logging in and out,
  getting the current user, expiring sessions, encrypting passwords, etc).
* Base user class AuthUser that can be used with most ORM's.
* Plug-and-play model for Google App Engine (and a working example for 
  SQLAlchemy).
* Straightforward permission model to differentiate access rights between 
  (groups of) users.

Documentation
-------------
Documentation for original may be found on `PyPI <http://packages.python.org/Flask-Auth/>`_. Again, you should just use the original.
