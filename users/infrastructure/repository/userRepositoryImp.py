from  users.domain.repository.userRepository import userRepositoryInterface
from ..userSchema import UserSchema
from ...domain.model.userModel import User as UserDto
from models import User, db

class UserRepositoryImp(userRepositoryInterface):
    def getAllUsers() -> list:
        data = User.query.all()
        userSchema = UserSchema(many=True)
        dump_data = userSchema.dump(data)
        return dump_data

    def postUsers(user: UserDto):
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
