from config import app
from ..domain.services.userService import UserService
from ..infrastructure.repository.userRepositoryImp import UserRepositoryImp

userService = UserService(UserRepositoryImp)

@app.route('/users', methods=['GET'])
def index():
    return userService.getAllUsers()

def row2dict(row):
    d = {}
    for column in row.columns:
        d[column.name] = str(getattr(row, column.name))

    return d