# pythonOSC

这是一个使用osc制作的vrchat游戏插件


**特性**
- 获取 CPU、内存、GPU 等设备信息
- 通过 OSC 协议发送数据（需在使用端处理接收）
- 包含 AFK 检测脚本示例

**先决条件**
- Windows 或其他支持的操作系统
- Python 3.12 及以上（推荐）
- 运行GetDeviceInfo.py最佳显卡是N卡，A卡和I卡会有一些适配问题(如显存无法识别和占用率无法识别)

**安装依赖**
在命令行中运行：

```bash
pip install psutil py-cpuinfo GPUtil python-osc wmi
```

如果提示 `pip` 不是内部或外部命令，检查 Python 是否已添加到系统环境变量。若提示需要升级 `pip`：

```bash
python -m pip install --upgrade pip
```

**运行方法**
- 使用批处理启动（推荐）：

```powershell
# 启动获取设备信息脚本
bat\startDevice.bat

# 启动 AFK 检测脚本
bat\startAFK.bat
```

- 或者直接运行 Python 脚本：

```powershell
python py\GetDeviceInfo.py
python py\AFK.py
```

**项目结构**

- bat/
  - startAFK.bat  —— 启动 `py/AFK.py`
  - startDevice.bat —— 启动 `py/GetDeviceInfo.py`
- py/
  - AFK.py
  - GetDeviceInfo.py

**注意**
- 请在同一 Python 环境下安装依赖，避免虚拟环境混淆。
- 根据需要修改脚本中的 OSC 目标地址与端口。

**许可**
- 见仓库根目录的 `LICENSE` 文件。

欢迎提出改进建议或提交 Pull Request。
