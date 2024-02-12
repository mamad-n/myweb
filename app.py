import os
from flask import Flask
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    load_dotenv()

    @app.route('/')
    def home ():
        return f"your database url is : {os.getenv('DATABASE_URI')}"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)