from lilaclib import *
import subprocess

def pre_build():
    aur_pre_build(maintainers=['staticnull'])

    subprocess.run(["sh", "setffver.sh"])
