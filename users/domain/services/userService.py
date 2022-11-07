from flask import jsonify

class UserService:

    def __init__(self, repository):
        self.repository = repository()

    def getAllUsers(self):
        return self.repository.getAllUsers()

    def postUsers(self, user):
        return self.repository.postUsers(user)
    
    def getUserById(self, id):
        return self.repository.getUserById(id)

    def deleteUser(self, id):
        self.repository.deleteUser(id)
        return jsonify (
            message="User deleted",
            id=id
        )

    def updateUser(self, id, body):
        updatedUser = self.repository.updateUser(id, body)
        return jsonify (
            message="User updated",
            user=id
        )

