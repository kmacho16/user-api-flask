class UserService:

    def __init__(self, repository) -> None:
        self.repository = repository

    def getAllUsers(self):
        return self.repository.getAllUsers()

    def postUsers(self, user):
        return self.repository.postUsers(user)
