Django, HTML5, CSS3, bootstrap5 sacco project to input, capture and validate member id, transaction type...(Deposit, saving, withdrawal), display balance (deposit+savings-withdrawal) and print the transaction details showing the current date and time. Include serializers, consumers...

PROJECT STRUCTURE 

sacco_project/
sacco_project/
    asgi.py
    settings.py
    urls.py
    wsgi.py
    __init__.py
    app/
        models.py
        serializers.py
        views.py
        templates/
            base.html
            index.html
            transaction.html
        static/
            css/
                style.css
            js/
                script.js
        templates/
            base.html
            index.html
            transaction.html
    consumers/
        transaction_consumer.py
    migrations/
        __init__.py
        0001_initial.py
    db.sqlite3
