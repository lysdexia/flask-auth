"""
============================
flask-auth-username-is-email
============================

Database-agnostic extension for Flask to support role-based authentication of
users. This is a piddly alteration to use "email" instead of "username". Don't be fooled by this pale imitation.

Links
-----

* `Documentation <http://packages.python.org/Flask-Auth>`_
* `Repository <https://github.com/lysdexia/flask-auth-username-is-email.git>`_

Revisions
---------
0.86
````
* Minor revision changing username to <= 254 character email address.

* Removed references to mongoalchemy in docs, as it ain't there in the first place.

0.85
````
* Updated to Flask 0.8 new naming scheme of using flask.ext for sqlalchemy.

* Fixed issue with importing sqlalchemy models.

0.8
```
Major revision.

* Not storing the entire user in the session anymore (which was convenient but bad practice) but only its __dict__.

* As a result of the above, the get_current_user call is now gone and replaced by get_current_user_data call. Similar functionality to the original call can now be obtained by doing AuthUser.load_current_user().

* Created SQLAlchemy plug-and-play model using constructor.

* Small bugfixes.

0.7
```
Added tests, permission example, bunch of bugfixes.

0.6
```
Added permission model, added examples, first release on PyPI.

0.1 - 0.5
`````````
Logging in, session management, encryption, etc.

"""
from setuptools import setup

setup(
    name='flask-auth-username-is-email',
    version='0.86',
    url='https://github.com/lysdexia/flask-auth-username-is-email/'
    license='MIT',
    author='Doug Shawhan',
    author_email='doug.shawhan@gmail.com',
    description='Auth extension for Flask, Modified to use Email as username.',
    long_description=__doc__,
    packages=[
        'flaskext',
        'flaskext.auth',
        'flaskext.auth.models',
    ],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='test_auth.suite',
)
