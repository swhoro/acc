import yaml
import os
import subprocess

print("1 启动/重启服务")
print("2 结束服务")

print("请输入选项")
choice = input()
choice = int(choice)
print()


def killAll():
    os.system("pkill tinyvpn_amd")


if choice == 1:
    killAll()

    c = 0
    with open("./client.yaml", "r") as f:
        c = yaml.load(f, Loader=yaml.FullLoader)

    servers = c["servers"]

    print("请选择服务器:")
    i = 0
    while(i < len(servers)):
        print(f"{i+1} {servers[i]['name']}")
        i = i + 1
    i = int(input()) - 1

    name = servers[i]["name"]
    ip = servers[i]["ip"]
    port = servers[i]["port"]
    password = servers[i]["password"]

    print()
    print(f"服务器：{name}")
    print(f"远程地址：{ip}")
    print(f"远程端口：{port}")
    print(f"密码：{password}")
    print()

    if not os.path.exists("log_tiny"):
        os.mknod("log_tiny")

    cmdTiny = f"./tinyvpn_amd64 -c -r{ip}:{port} -f2:4 -k \"{password}\" --timeout 0 >log_tiny"
    subprocess.Popen(cmdTiny, shell=True)

if choice == 2:
    killAll()
