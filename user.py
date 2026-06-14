"""用户模块"""


def create_user(username: str, email: str) -> dict:
    user = {
        "username": username,
        "email": email,
    }
    return user
