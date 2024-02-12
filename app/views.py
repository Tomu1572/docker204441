from app import app




@app.route('/')
def home():
    return "Anyong says 'Hello world!'"
