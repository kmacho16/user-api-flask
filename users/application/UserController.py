from config import app
from flask import request, jsonify

from ..domain.services.userService import UserService
from ..infrastructure.repository.userRepositoryImp import UserRepositoryImp
from ..domain.model.userModel import User

userService = UserService(UserRepositoryImp)

@app.route('/users', methods=['GET'])
def index():
    return userService.getAllUsers()

@app.route('/users', methods=['POST'])
def post():
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