from flask.ext.frozen import Freezer
from main import app
import os

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app, with_static_files=True)

if __name__ == '__main__':
    app.debug = False
    # app.testing = True

    freezer.freeze()