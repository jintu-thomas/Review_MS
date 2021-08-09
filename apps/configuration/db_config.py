from apps import app


app.config['MONGODB_SETTINGS'] = {
    'db': 'Reviews',
    'host': 'localhost',
    'port': 27017
}