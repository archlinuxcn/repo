#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Aleksana', 'q234rty'])
    add_depends(['libdisplay-info.so', 'libhyprlang.so'])
    add_replaces(['hyprland-nvidia-hidpi-git'])
