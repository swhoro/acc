# kcptun udpspeeder udp2raw onekey_script
## 这是什么？
一键配置kcptun udpspeeder udp2raw，转发流量至 $$ 服务器
## 架构/模型
参考这个

https://github.com/wangyu-/UDPspeeder/wiki/UDPspeeder---kcptun-finalspeed---%24%24-%E5%90%8C%E6%97%B6%E5%8A%A0%E9%80%9Ftcp%E5%92%8Cudp%E6%B5%81%E9%87%8F

实际架构图：

![网络拓扑 ](https://user-images.githubusercontent.com/34229589/167377594-3f856c55-af7a-4809-819e-239207d46554.png)

## 配置
### 服务端
请确保服务端有以下文件:

<img width="160" alt="无标题" src="https://user-images.githubusercontent.com/34229589/167379204-cdc48ad1-d7c7-45de-9a3b-110cd95c611c.png">

server_linux_amd64: kcptun 服务器文件

speederv2_amd64: udpspeeder 文件

udp2raw_amd64_hw_aes: udp2raw 文件

config: udpspeeder和udp2raw密码文件

config配置：

![image](https://user-images.githubusercontent.com/34229589/167379399-c113938c-6e9b-4391-935f-206fab9dee3b.png)

第一行等于号后面写上udpspeeder密码，第二行等于号后面写上udp2raw密码

server.sh配置：

<img width="842" alt="3" src="https://user-images.githubusercontent.com/34229589/167379883-27a9e70f-4dca-4437-ace2-7758b963edb6.png">

第12行写上本地ss端口

## 客户端
请确保客户端有以下文件：

<img width="185" alt="无标题" src="https://user-images.githubusercontent.com/34229589/167380368-926e3344-2ff9-4c5f-95d1-42dbf82c898e.png">


client_linux_amd64: kcptun客户端文件

speederv2_amd64: udpspeeder 文件

udp2raw_amd64_hw_aes: udp2raw 文件

config: udpspeeder和udp2raw密码文件，需与服务器config保持一致

now: 配置选择文件

图中ip开头为配置文件，包含服务器地址以及端口号，第一行为服务器地址，第二行为服务器端口号。示例:

![image](https://user-images.githubusercontent.com/34229589/167380942-81136263-d60c-4d7e-8313-ba7779e72ca3.png)

**注意**：当使用流量转发时，请在配置文件中填入入口地址及端口，非服务器地址及端口

now文件用于选择当前配置，只需在文件中写入配置文件名即可。示例:

![image](https://user-images.githubusercontent.com/34229589/167381610-eec8ca7b-3b06-4a85-9a91-a4a337902469.png)

## 使用
分别上传server.sh和client.sh至服务端和客户端，并完成配置，赋予脚本和各文件执行权限(chmod 777 [文件名])

配置完成后服务端运行bash server.sh，客户端运行bash client.sh，选择1启动服务

运行后会显示一些基础配置信息

若要停止服务请进入脚本后选择2

## 案例
服务端为ubuntu，执行server.sh后，kcptun监听6999 udp端口，udp2raw监听6999 tcp端口，$$端口为tcp和udp的37092

本地ubuntu(ip地址为192.168.1.5)执行client.sh，作为客户端，kcptun监听37092 tcp端口，udpspeeder监听37092 udp端口

windows使用netch作为$$客户端，$$服务器地址为 192.168.1.5(即运行client.sh地址)，端口为37092(即kcptun和udpspeder端口)

## 其它
1.可以把服务器上$$监听地址设为127.0.0.1，即本地地址

2.防火墙阻断6999地址(服务端kcptun和udp2raw监听地址)，并放行ip白名单

3.为方便$$链接，服务端上kcptun和udp2raw应该监听同意端口，客户端上kcptun和udpspeeder应该监听同一段口

4.脚本执行目录下有日志文件(以log开头)，需手动删除
