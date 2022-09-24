import yaml
import os
import subprocess

print("1 启动/重启服务")
print("2 结束服务")

print("请输入选项")
choice = input()
choice = int(choice)


def killAll():
    os.system("pkill server_lin")
    os.system("pkill speederv2_")
    os.system("pkill udp2raw_am")


if choice == 1:
    killAll()

    c = 0
    with open("./server.yaml", "r") as f:
        c = yaml.load(f, Loader=yaml.FullLoader)

    ss_port = c["ss_port"]
    udpspeeder_pass = c["udpspeeder_pass"]
    udp2raw_pass = c["udp2raw_pass"]

    if not os.path.exists("log_kcp"):
        os.mknod("log_kcp")

    if not os.path.exists("log_speeder"):
        os.mknod("log_speeder")

    if not os.path.exists("log_udp2raw"):
        os.mknod("log_udp2raw")

    cmdKcp = f"./server_linux_amd64 -t \"127.0.0.1:{ss_port}\" -l \":6999\" -mode fast3 -nocomp -sockbuf 1677217 -dscp 46 2>log_kcp"
    print(cmdKcp)
    subprocess.Popen(cmdKcp, shell=True)

    cmdSpeeder = f"./speederv2_amd64 -s -l 127.0.0.1:7000 -r 127.0.0.1:{ss_port} -k \"{udpspeeder_pass}\" -f 2:2 --timeout 1 >log_speeder"
    print(cmdSpeeder)
    subprocess.Popen(cmdSpeeder, shell=True)

    cmdUdp2raw = f"./udp2raw_amd64_hw_aes -s -l 0.0.0.0:6999 -r 127.0.0.1:7000 -k \"{udp2raw_pass}\" --raw-mode faketcp -a >log_udp2raw"
    print(cmdUdp2raw)
    subprocess.Popen(cmdUdp2raw, shell=True)

if choice == 2:
    killAll()
