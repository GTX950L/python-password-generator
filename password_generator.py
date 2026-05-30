"""
密码生成器 —— Python 入门练手项目

功能：
  随机生成指定长度和类型的密码
  可混合大小写字母、数字、特殊符号
"""

import random
import string


def 生成密码(长度=12, 包含大写=True, 包含数字=True, 包含符号=True):
    """
    生成一个随机密码

    参数：
      长度：密码长度（默认12）
      包含大写：是否包含大写字母
      包含数字：是否包含数字
      包含符号：是否包含特殊符号

    返回：
      生成的密码字符串
    """
    # 基础字符：小写字母
    字符池 = list(string.ascii_lowercase)

    # 按需要添加字符类型
    if 包含大写:
        字符池 += list(string.ascii_uppercase)
    if 包含数字:
        字符池 += list(string.digits)
    if 包含符号:
        字符池 += list("!@#$%^&*()-_=+[]{}|;:,.<>?")

    # 确保每种选中的类型至少出现一次
    密码列表 = []

    # 先放一个，保证每种都有
    密码列表.append(random.choice(string.ascii_lowercase))
    if 包含大写:
        密码列表.append(random.choice(string.ascii_uppercase))
    if 包含数字:
        密码列表.append(random.choice(string.digits))
    if 包含符号:
        密码列表.append(random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?"))

    # 随机填充剩余长度
    密码列表 += [random.choice(字符池) for _ in range(长度 - len(密码列表))]

    # 打乱顺序
    random.shuffle(密码列表)

    return "".join(密码列表)


def 评估密码强度(密码):
    """简单评估密码强度"""
    长度 = len(密码)
    有大写 = any(c.isupper() for c in 密码)
    有数字 = any(c.isdigit() for c in 密码)
    有符号 = any(not c.isalnum() for c in 密码)

    分数 = 0
    if 长度 >= 8:
        分数 += 1
    if 长度 >= 12:
        分数 += 1
    if 长度 >= 16:
        分数 += 1
    if 有大写:
        分数 += 1
    if 有数字:
        分数 += 1
    if 有符号:
        分数 += 1

    if 分数 <= 2:
        return "弱 🔴"
    elif 分数 <= 4:
        return "中等 🟡"
    else:
        return "强 🟢"


def 密码生成器():
    """主程序"""
    print("=" * 45)
    print("🔐 随机密码生成器")
    print("=" * 45)

    while True:
        print("\n🔧 请设置密码参数（直接回车使用默认值）：")

        try:
            长度输入 = input("  密码长度（默认12）：").strip()
            长度 = int(长度输入) if 长度输入 else 12

            大写输入 = input("  包含大写字母？(y/n，默认y)：").strip().lower()
            包含大写 = 大写输入 != "n"

            数字输入 = input("  包含数字？(y/n，默认y)：").strip().lower()
            包含数字 = 数字输入 != "n"

            符号输入 = input("  包含符号？(y/n，默认y)：").strip().lower()
            包含符号 = 符号输入 != "n"

            数量输入 = input("  生成几个密码？（默认1）：").strip()
            数量 = int(数量输入) if 数量输入 else 1

            print(f"\n{'─' * 45}")
            print("📋 生成的密码：")
            print("─" * 45)

            for i in range(数量):
                密码 = 生成密码(长度, 包含大写, 包含数字, 包含符号)
                强度 = 评估密码强度(密码)
                print(f"  {i+1}. {密码}  [{强度}]")

            print("─" * 45)

            再来 = input("\n🔄 再来一次？(y/n，默认y)：").strip().lower()
            if 再来 == "n":
                break

        except ValueError:
            print("⚠️  输入无效！请输入数字。")
            continue

    print("\n👋 感谢使用！记得把密码保存在安全的地方。")


if __name__ == "__main__":
    密码生成器()
