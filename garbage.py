"""
垃圾生成器 - AI从0制造的垃圾
Garbage Generator - Garbage created by AI from scratch
"""

import random


GARBAGE_ITEMS = [
    "🗑️ 无用变量",
    "📦 空箱子",
    "🔧 坏掉的工具",
    "📄 空白文件",
    "🌀 死循环",
    "🐛 Bug",
    "💾 过期数据",
    "🧩 缺失的拼图",
    "🔗 失效的链接",
    "📡 无信号",
]


def generate_garbage(count: int = 5) -> list:
    """从0开始生成垃圾 / Generate garbage from scratch"""
    garbage = []
    for i in range(count):
        item = random.choice(GARBAGE_ITEMS)
        garbage.append(f"[{i + 1}] {item}")
    return garbage


def display_garbage(garbage: list) -> None:
    """展示垃圾 / Display garbage"""
    print("=" * 40)
    print("  AI从0制造的垃圾清单")
    print("  Garbage list created by AI from zero")
    print("=" * 40)
    for item in garbage:
        print(f"  {item}")
    print("=" * 40)
    print(f"  共 {len(garbage)} 件垃圾 / Total: {len(garbage)} items")
    print("=" * 40)


def main():
    """程序入口 / Main entry point"""
    print("🤖 AI正在从0开始制造垃圾...")
    print("🤖 AI is creating garbage from scratch...")
    print()
    garbage = generate_garbage(count=10)
    display_garbage(garbage)
    print()
    print("✅ 垃圾制造完成！/ Garbage creation complete!")


if __name__ == "__main__":
    main()
