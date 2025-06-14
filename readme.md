# SDJZU校园网自动登录

自动检测并登录SDJZU校园网的Python脚本。

## 前情提要

NMD校园网限制两台设备，多设备用户库库顶号，一怒之下怒了一下！
妈妈再也不用担心手动打开浏览器输入账号密码会累死了！

## 特性

- 🚀 自动检测网络连接状态
- 🔄 断线自动重连
- 💡 智能跳过已连接状态
- 🛡️ 登录状态验证
- ⚡ 快速便捷，一键运行

## 使用方法

1. 修改用户信息：
```python
USERNAME = "你的学号"
PASSWORD = "你的密码"
```

2. 安装依赖并运行：
```bash
pip install requests
python AutoCampusLogin.py
```

## 工作原理

- 检测网络状态，如果已连接则退出
- 获取校园网登录页面重定向URL
- 自动填写并提交登录信息
- 验证登录结果

## 使用场景

- 📱 多设备用户的救星
- 🏠 宿舍网络频繁掉线
- 💻 开发调试时网络中断
- 🎮 游戏时突然断网需要快速重连

## 注意事项

⚠️ 请保护好您的账号密码信息，仅在校园网环境下使用。
⚠️ 建议将脚本添加到系统启动项或定时任务中，实现真正的自动化。

## 许可证

本项目基于 MIT 许可证开源，详见 [LICENSE](LICENSE) 文件。

---

## AI 声明

本README文档由 AI 编写。