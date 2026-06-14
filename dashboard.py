"""仪表盘模块 — feature/dashboard 分支新增"""

from typing import List, Dict


def calculate_summary(data: List[Dict]) -> Dict:
    total = len(data)
    active = sum(1 for d in data if d.get("active"))
    return {
        "total": total,
        "active": active,
        "inactive": total - active,
    }


def render_bar_chart(values: List[int], label: str = "数据") -> str:
    lines = [f"{label}:"]
    for i, v in enumerate(values):
        lines.append(f"  第{i+1}项 | {'█' * v} {v}")
    return "\n".join(lines)
