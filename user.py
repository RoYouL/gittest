"""用户模块"""

import uuid


def create_user(username: str, email: str) -> dict:
    user = {
        "id": str(uuid.uuid4()),
        "username": username,
        "email": email,
        "avatar": f"https://avatar.example.com/{username}.png",
        "is_active": False,
    }
    return user
