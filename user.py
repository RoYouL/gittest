"""用户模块"""

import uuid


def create_user(username: str, email: str) -> dict:
    if not username or not email:
        raise ValueError("用户名和邮箱不能为空")
    if "@" not in email:
        raise ValueError("邮箱格式不正确")

    user = {
        "id": str(uuid.uuid4()),
        "username": username,
        "email": email,
        "role": "guest",
        "is_active": True,
    }
    return user
