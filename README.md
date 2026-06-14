# Git 多分支合并冲突练习项目

## 项目结构

- `story.txt`  — 会被多个分支修改，用于演示冲突
- `team.py`    — 团队成员信息，多分支同时修改同一行时产生冲突

## 分支规划

| 分支 | 说明 |
|------|------|
| `main` | 主分支，稳定版本 |
| `feature/login` | 开发登录功能 |
| `feature/dashboard` | 开发仪表盘功能 |

## 练习步骤

1. 查看各分支的修改内容
2. 尝试将 `feature/login` 合并进 `main`
3. 再将 `feature/dashboard` 合并进 `main` —— 这里会产生冲突
4. 手动解决冲突后提交

## 常用命令速查

```bash
git branch -a              # 查看所有分支
git checkout <branch>      # 切换分支
git merge <branch>         # 合并分支
git status                 # 查看冲突文件
git add <file>             # 标记冲突已解决
git commit                 # 完成合并提交
git log --oneline --graph  # 查看分支图
```
