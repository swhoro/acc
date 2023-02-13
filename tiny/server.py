import yaml
import os
import subprocess

print("1 启动/重启服务")
print("2 结束服务")

print("请输入选项")
choice = input()
choice = int(choice)


def killAll():
    os.system("pkill tinyvpn_amd")


if choice == 1:
    killAll()

    c = 0
    with open("./server.yaml", "r") as f:
        c = yaml.load(f, Loader=yaml.FullLoader)

    listening_port = c["listening_port"]
    password = c["password"]

    if not os.path.exists("log_tiny"):
        os.mknod("log_tiny")

    print(f"监听端口：{listening_port}")
    print(f"密码：{password}")

    cmdTiny = f"./tinyvpn_amd64 -s -l0.0.0.0:{listening_port} -f2:4 -k \"{password}\" --timeout 0 >log_tiny"
    subprocess.Popen(cmdTiny, shell=True)

if choice == 2:
    killAll()
