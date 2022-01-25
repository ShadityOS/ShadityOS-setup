#!/bin/bash

FLAG="/var/log/firstboot.log"

if [ ! -f $FLAG ]; then
   echo "This is the first boot"
   x-terminal-emulator -e python3 setup.py
   touch $FLAG
   echo "Rebooting..."
   reboot
fi
