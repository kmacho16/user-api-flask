from config import app
from models import *

import users.application.UserController


if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0')