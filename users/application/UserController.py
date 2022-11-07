from config import app
from flask import request, jsonify

from ..domain.services.userService import UserService
from ..infrastructure.repository.userRepositoryImp import UserRepositoryImp
from ..domain.model.userModel import User

userService = UserService(UserRepositoryImp)

@app.route('/users', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        request_data = request.get_json()
        print(request_data)
        user = User(
            request_data['typeDocument'],
            request_data['numDocument'],
            request_data['name'],
            request_data['lastName'],
            request_data['hobbie']
            )
        id = userService.postUsers(user)
        return jsonify(
            username=user.name,
            id=id
        )
    return userService.getAllUsers()

@app.route("/users/<int:id>", methods=['GET','DELETE'])
def getById(id):
    if request.method == 'DELETE':
        return userService.deleteUser(id)
    return userService.getUserById(id)
