"""团队成员与功能模块配置"""

# 项目负责人
OWNER = "Alice"

# 核心功能列表（各分支会在此处添加内容）
FEATURES = [
    "用户注册",
]

# 模块负责人（各分支会修改同一行，故意制造冲突）
MODULE_OWNER = "待分配"


def get_team_info():
    return {
        "owner": OWNER,
        "features": FEATURES,
        "module_owner": MODULE_OWNER,
    }
