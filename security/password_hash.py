import bcrypt

class PasswordHasher:

    def hash(self, password):
        result = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()

        ).decode("utf-8")
        return result

    def verify(self, password, password_hash):

        return bcrypt.checkpw(
            password.encode("utf-8"),
            password_hash.encode("utf-8")
        )