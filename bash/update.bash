#!/usr/bin/zsh

sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt clean -y

# print -P "\n%F{green}System updates and upgrades completed successfully.%f\n"
print -P "\n%F{cyan}System updates and upgrades completed successfully.%f\n"
