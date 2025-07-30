# 监控SSH端口映射

监控ssh映射的端口，确保SSH反向隧道连接的稳定性。

## 项目简介

这是一个用于监控和维护SSH反向隧道连接的Python工具集。它能够自动检测SSH端口映射状态，并在连接断开时重新建立连接，确保远程服务器可以通过指定端口访问本地服务。

## 功能特性

1. **端口监控** - 检测指定的SSH映射端口是否正常工作
2. **进程管理** - 自动查找并终止异常的SSH进程
3. **远程控制** - 在远程服务器上执行命令终止已有进程
4. **自动重连** - 当连接断开时自动重新建立SSH反向隧道
5. **定时检测** - 支持周期性检测连接状态

## 工作原理

1. 检查远程服务器上的指定端口是否可达
2. 如果端口不可达，则执行以下操作：
   - 查找本地符合特征的SSH进程并终止
   - 在远程服务器上执行脚本终止对应的进程
   - 重新建立SSH反向隧道连接

## 使用方法

### 配置文件示例

```python
cfg = {
    # 映射本地端口到远程服务器的命令
    'local_map_cmd': 'ssh -CNfgR 55022:127.0.0.1:22 root@1.gdx.gdx -o TCPKeepAlive=yes',
    # 查找本地的进程名称
    'local_progress_name': 'ssh',
    # 查找本地进程的命令行包含的字符
    'local_progress_cmd_tags': ['-CNfgR', '55022'],
    # 检查服务器的地址端口与协议，查看是否能正常连接
    'server_chk_addr': '1.gdx.gdx:55022',
    # 终止服务器已存在的进程的命令
    # netstat -anltp|grep 55022|grep 0.0.0.0|awk '{print $7}'| cut -d'/' -f1|xargs kill -9
    'server_close_cmd': 'ssh root@1.gdx.gdx "/root/kill55022.sh"'
}
```

### 启动监控

```bash
bash demo.sh
```

### crontab配置
```bash
*/5  * * * * /Users/admin/MoninterSshMaps/call_by_crontab.sh 
```

## 核心组件

- [check_port.py](check_port.py) - 检查远程端口是否可达
- [get_process.py](get_process.py) - 获取本地符合条件的进程ID
- [get_netconn_pids.py](get_netconn_pids.py) - 获取监听指定端口的进程ID
- [server_kill.py](server_kill.py) - 在服务器端终止监听指定端口的进程
- [moniter_client.py](moniter_client.py) - 主监控逻辑实现
- [main.py](main.py) - 程序入口和配置文件

## 依赖库

- psutil - 用于获取系统和进程信息
- Python 3.x

## 安装依赖

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install psutil
```

## 使用场景

适用于需要长期保持SSH反向隧道连接的场景，例如：
- 内网服务器需要被外网访问
- 远程设备的远程管理
- 穿透防火墙访问内网服务