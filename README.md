# django_session
demo of django_session,

## Session

    The session framework lets you store and retrieve arbitary data on a per-site-visitor basis.
    It stores data on the server side and abstracts the sending and receiving of cookies. Cookies contain a session ID not the data itself.
    By default, Django stores sessions in your database.
    As it stores sessions in database so it is mandatory to run makemigrations and migrate to use session.
    It will create required tables.
    The Django sessions framework is entirely, and solely, cookie-based.
    django.contrib.sessions.middleware.SessionMiddleware
    django.contrib.sessions