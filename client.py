import yaml
import os
import subprocess

print("1 启动/重启服务")
print("2 结束服务")

print("请输入选项")
choice = input()
choice = int(choice)


def killAll():
    os.system("pkill client_linux_")
    os.system("pkill speederv2_")
    os.system("pkill udp2raw_am")


if choice == 1:
    killAll()

    c = 0
    with open("./client.yaml", "r") as f:
        c = yaml.load(f, Loader=yaml.FullLoader)

    listening_port = c["listening_port"]
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
    udpspeeder_pass = servers[i]["udpspeeder_pass"]
    udp2raw_pass = servers[i]["udp2raw_pass"]

    print(f"服务器：{name}")
    print(f"kcptun和udpspeeder监听端口：{listening_port}")
    print(f"远程地址：{ip}")
    print(f"远程端口：{port}")
    print(f"udpspeeder密码：{udpspeeder_pass}")
    print(f"udp2raw密码：{udp2raw_pass}")
    print()

    if not os.path.exists("log_kcp"):
        os.mknod("log_kcp")

    if not os.path.exists("log_speeder"):
        os.mknod("log_speeder")

    if not os.path.exists("log_udp2raw"):
        os.mknod("log_udp2raw")

    cmdKcp = f"./client_linux_amd64 -r \"{ip}:{port}\" -l \":{listening_port}\" -mode fast3 -nocomp -sockbuf 1677217 -dscp 46 -autoexpire 900 2>log_kcp"
    # print(cmdKcp)
    subprocess.Popen(cmdKcp, shell=True)

    cmdSpeeder = f"./speederv2_amd64 -c -l 0.0.0.0:{listening_port} -r 127.0.0.1:6999 -k \"{udpspeeder_pass}\" -f 2:2 --timeout 1 >log_speeder"
    # print(cmdSpeeder)
    subprocess.Popen(cmdSpeeder, shell=True)

    cmdUdp2raw = f"./udp2raw_amd64_hw_aes -c -l 127.0.0.1:6999 -r {ip}:{port} -k \"{udp2raw_pass}\" --raw-mode faketcp -a >log_udp2raw"
    # print(cmdUdp2raw)
    subprocess.Popen(cmdUdp2raw, shell=True)

if choice == 2:
    killAll()
