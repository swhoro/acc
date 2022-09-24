# kcptun udpspeeder udp2raw onekey_script
## 这是什么？
一键配置kcptun udpspeeder udp2raw，转发流量至 $$ 服务器
## 架构/模型
参考这个

https://github.com/wangyu-/UDPspeeder/wiki/UDPspeeder---kcptun-finalspeed---%24%24-%E5%90%8C%E6%97%B6%E5%8A%A0%E9%80%9Ftcp%E5%92%8Cudp%E6%B5%81%E9%87%8F

实际架构图：

![网络拓扑 ](https://user-images.githubusercontent.com/34229589/167377594-3f856c55-af7a-4809-819e-239207d46554.png)

## 相关链接:

[kcptun](https://github.com/xtaci/kcptun)

[udpspeeder](https://github.com/wangyu-/UDPspeeder)

[udp2raw](https://github.com/wangyu-/udp2raw)

## 配置

### 服务端

请确保服务端有以下文件:

server_linux_amd64: kcptun服务器文件

speederv2_amd64: udpspeeder文件

udp2raw_amd64_hw_aes: udp2raw文件

server.yaml: 服务端配置文件

**server.yaml配置：**

```yaml
# 本地ss服务器端口
ss_port: 37092

# kcptun与udp2raw监听端口
listening_port: 6999

# udpspeeder和udp2raw密码
udpspeeder_pass: 12345
udp2raw_pass: 12345
```

### 客户端

请确保客户端有以下文件：

client_linux_amd64: kcptun客户端文件

speederv2_amd64: udpspeeder文件

udp2raw_amd64_hw_aes: udp2raw文件

client.yaml: 客户端配置文件

**client.yaml配置：**

```yaml
# 本地客户端监听端口
listening_port: 37092

#服务器组
servers:
    - name: my-acc            # 服务器名字
      ip: 1.2.3.4             # 服务器ip
      port: 6999              # 服务器监听端口
      udpspeeder_pass: 12345  # udpspeeder密码，应与服务端一致
      udp2raw_pass: 12345     # udp2raw密码，应与服务端一致
    - name: another-acc
      ip: 2.4.6.8
      port: 6999
      udpspeeder_pass: 12345
      udp2raw_pass: 12345
```

## 使用

分别上传服务端与客户端可执行文件

分别上传server.py和client.py至服务端和客户端，完成配置

服务端运行`python3 server.py`，客户端运行`python3 client.py`
