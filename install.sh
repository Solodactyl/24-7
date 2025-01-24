#!/bin/bash

import os
import random
import string
import time

def display_banner():
    print(r"""
    ███████╗ ██████╗ ██╗      ██████╗     ██████╗ ██╗      █████╗ ██╗   ██╗███████╗
    ██╔════╝██╔═══██╗██║     ██╔═══██╗    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝╚══███╔╝
    ███████╗██║   ██║██║     ██║   ██║    ██████╔╝██║     ███████║ ╚████╔╝   ███╔╝ 
    ╚════██║██║   ██║██║     ██║   ██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝   ███╔╝  
    ███████║╚██████╔╝███████╗╚██████╔╝    ██║     ███████╗██║  ██║   ██║   ███████╗
    ╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝     ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════
                                                       
                              Solo Playz
    """)

# Ensure the script is run with root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root: sudo $0"
  exit 1
fi

# Update and upgrade the system
echo "Updating package list..."
apt update -y
echo "Upgrading packages..."
apt upgrade -y

# Install Docker Compose
echo "Installing Docker Compose..."
apt install docker-compose -y

# Install Neofetch
echo "Installing Neofetch..."
apt install neofetch -y

# Run Neofetch to display system information
echo "Running Neofetch..."
neofetch

echo "All tasks completed successfully!"
