from  users.domain.repository.userRepository import userRepositoryInterface
from ..userSchema import UserSchema
from models import User


class UserRepositoryImp(userRepositoryInterface):
    def getAllUsers() -> list:
        data = User.query.all()
        userSchema = UserSchema(many=True)
        dump_data = userSchema.dump(data)
        return dump_data