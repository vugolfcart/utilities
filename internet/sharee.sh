#! /bin/sh

route del gw 192.168.1.1
route del default gw 192.168.1.1

echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf

route add default gw 192.168.1.102 # use your own ip