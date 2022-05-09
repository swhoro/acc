#!/bin/bash
# client side

echo "1.启动服务"
echo "2.结束服务"

read -p "请输入选项：" choice

case ${choice} in
1)
  myfile=$(cat now)

  #ip
  ip=$(sed -ne 1p ${myfile})
  port=$(sed -ne 2p ${myfile})

  # get password
  udpspeeder_pass=$(sed -ne 1p config)
  udp2raw_pass=$(sed -ne 2p config)

  IFS="="

  read -a speeder <<<${udpspeeder_pass}
  read -a raw <<<${udp2raw_pass}

  udpspeeder_pass=${speeder[1]}
  udp2raw_pass=${raw[1]}

  # basic information
  echo "配置文件：${myfile}"
  echo "远程地址：${ip}"
  echo "远程端口：${port}"
  echo "udpspeeder密码：${udpspeeder_pass}"
  echo "udp2raw密码：${udp2raw_pass}"

  # log
  if [ ! -e "log_kcp" ]; then
    touch log_kcp
  fi

  if [ ! -e "log_speeder" ]; then
    touch log_speeder
  fi

  if [ ! -e "log_udp2raw" ]; then
    touch log_udp2raw
  fi

  # kcptun
  ./client_linux_amd64 -r "${ip}:${port}" -l ":37092" -mode fast3 -nocomp -sockbuf 1677217 -dscp 46 -autoexpire 900 2>log_kcp &

  # udpspeeder
  ./speederv2_amd64 -c -l 0.0.0.0:37092 -r 127.0.0.1:6999 -k "${udpspeeder_pass}" -f 2:2 --timeout 1 >log_speeder &

  # udp2raw
  ./udp2raw_amd64_hw_aes -c -l 127.0.0.1:6999 -r ${ip}:${port} -k "${udp2raw_pass}" --raw-mode faketcp -a >log_udp2raw &
  ;;

2)
  # kill kcp
  pkill client_lin
  # kill udpspeeder
  pkill speederv2_
  # kill udp2raw
  pkill udp2raw_am
  ;;
esac
