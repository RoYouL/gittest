"""团队成员与功能模块配置"""

# 项目负责人
OWNER = "Alice"

# 核心功能列表（各分支会在此处添加内容）
FEATURES = [
    "用户注册",
    "数据仪表盘",     # feature/dashboard 新增
    "图表可视化",     # feature/dashboard 新增
]

# 模块负责人（各分支会修改同一行，故意制造冲突）
MODULE_OWNER = "Carol（负责仪表盘模块）"  # feature/dashboard 修改


def get_team_info():
    return {
        "owner": OWNER,
        "features": FEATURES,
        "module_owner": MODULE_OWNER,
    }
