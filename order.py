"""订单模块"""


def calculate_price(price: float) -> float:
    price = price * 1.13  # 加 13% 增值税
    price = price * 0.9  # 打九折优惠
    return price
