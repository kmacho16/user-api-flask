from  users.domain.repository.userRepository import userRepositoryInterface
from ..userSchema import UserSchema
from ...domain.model.userModel import User as UserDto
from models import User, db

class UserRepositoryImp(userRepositoryInterface):
    def getAllUsers(self) -> list:
        data = User.query.all()
        userSchema = UserSchema(many=True)
        dump_data = userSchema.dump(data)
        return dump_data

    def postUsers(self, user: UserDto):
        newUser = User(
            typeDocument = user.typeDocument,
            numDocument = user.numDocument,
            name=user.name,
            lastName=user.lastname,
            hobbie = user.hobbie
        )
        db.session.add(newUser)
        db.session.commit()
        return newUser.id
    
    def getUserById(self, id: int) -> User:
        user = User.query.filter_by(id=id).first()
        userSchema = UserSchema()
        dump_data = userSchema.dump(user)
        return dump_data

    def updateUser(self, id: int) -> User:
        return super().updateUser()

    def deleteUser(self, id: int):
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
        return id
    
    def updateUser(self, id: int, body: UserDto) -> User:
        self.deleteUser(id)
        updatedUser = User(
            id=id,
            typeDocument = body.typeDocument,
            numDocument = body.numDocument,
            name=body.name,
            lastName=body.lastname,
            hobbie = body.hobbie
        )
        db.session.add(updatedUser)
        db.session.commit()
        return updatedUser

