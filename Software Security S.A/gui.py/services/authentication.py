import bcrypt # type: ignore

def authenticate_user(username, password):
    hashed_password = get_hashed_password_from_db(username)
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

def get_hashed_password_from_db(username):
    # Simulação de busca no banco de dados
    return b'$2b$12$K9Q1Y0Q....'  # Exemplo de hash
