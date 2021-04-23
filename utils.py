from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated='auto')

class Hash:
    @staticmethod
    def bcrypt(pwd):
        return pwd_cxt.hash(pwd)

    @staticmethod
    def verify(hpwd,pwd):
        return pwd_cxt.verify(hpwd,pwd)

class Token:
    pass