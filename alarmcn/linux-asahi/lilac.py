#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    run_cmd(["sh", "-c", 'curl -L -sSO https://github.com/AsahiLinux/PKGBUILDs/archive/refs/heads/main.zip'])
    run_cmd(['unzip', 'main.zip'])
    run_cmd(["sh", "-c", 'mv PKGBUILDs-main/linux-asahi/* .'])
    run_cmd(['rm', '-rf', 'PKGBUILDs-main/', 'main.zip'])
    run_cmd(["updpkgsums"])

def post_build():
    git_pkgbuild_commit()
