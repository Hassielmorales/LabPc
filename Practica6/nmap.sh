#!/bin/bash
host=$(hostname -l > nmap.txt)

ip=$(ip addr >>nmap.txt)
infor=$(wget -q -O - ipinfo.io/ip >>nmap.txt)

nmap -sL 192.168.0.* >> nmap.txt

base64 nmap.txt >nmap.b6

