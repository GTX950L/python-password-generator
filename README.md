# 🔐 随机密码生成器

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Level](https://img.shields.io/badge/练习-初学者-blue?style=flat-square)

</div>

一个用 Python 编写的命令行密码生成工具，支持自定义长度和字符类型，附带密码强度评估。

## ✨ 功能

- 🎛️ 可自定义密码长度（默认12位）
- 🔤 可选包含大写字母、数字、特殊符号
- 📊 自动评估密码强度（弱/中等/强）
- 📋 支持一次生成多个密码

## 🚀 快速开始

### 依赖
```bash
无额外依赖（仅用标准库）
```

### 运行
```bash
python password_generator.py
```

## 📖 使用说明

运行后按提示输入密码长度和字符类型选项，程序自动生成并评估强度。

## 🛠️ 用到的知识点

| 知识点 | 应用 |
|--------|------|
| string模块 | 获取大小写字母、数字字符集 |
| random模块 | 随机选择字符、打乱顺序 |
| 列表推导式 | 快速生成字符列表 |
| any()函数 | 检测密码中是否包含某类字符 |
| 函数默认参数 | 灵活配置密码生成规则 |

## 📷 运行效果

> 欢迎添加运行截图 Pull Request 😊

## 📝 后续可以增强

- [ ] 检查密码是否包含常见弱密码
- [ ] 增加密码历史记录
- [ ] 图形界面版本

## ❓ 常见问题

暂无

## 📄 License

MIT License
