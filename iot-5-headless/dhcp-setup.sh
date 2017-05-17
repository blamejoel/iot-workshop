#!/bin/bash
sudo apt update
sudo apt install dnsmasq
sudo sed -r '/iface\ eth0\ inet/s/^/#\ /' < /etc/network/interfaces > /tmp/interfaces.tmp && sudo mv /tmp/interfaces.tmp /etc/network/interfaces
