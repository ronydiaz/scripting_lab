#!/bin/bash

echo "Updating system packages..."
sudo apt update -y && sudo apt upgrade -y

echo "Clean up..."
sudo apt autoremove -y
sudo apt clean

echo "System has been updated and clean up"


