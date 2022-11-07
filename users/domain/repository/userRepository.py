from ..model.userModel import User
class userRepositoryInterface:
    def getAllUsers() -> list:
        pass

    def postUsers(user:User):
        pass

    def getUserById(id:int)->User:
        pass

    def deleteUser(id:int):
        pass

    def updateUser(id:int, body: User)->User:
        pass
