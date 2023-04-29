from passlib.context import CryptContext

crypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_pass(plain, hashed):
    return crypt_context.verify(plain, hashed)


def hash_pass(pwd):
    return crypt_context.hash(pwd)
