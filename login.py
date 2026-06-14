"""登录模块 — feature/login 分支新增"""

import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def login(username: str, password: str, user_db: dict) -> bool:
    hashed = hash_password(password)
    return user_db.get(username) == hashed
