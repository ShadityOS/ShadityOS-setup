#!/bin/bash
# Add it to the autostart option in your desktop environment's settings along with the setup.py script

FLAG="/var/log/firstboot.log"

if [ ! -f $FLAG ]; then
   x-terminal-emulator -e python3 setup.py
   touch $FLAG
   echo "Rebooting..."
   reboot
fi
