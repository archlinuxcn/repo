import subprocess
from lilaclib import aur_post_build, git_add_files


def post_build():
    package_list = '\n'.join(subprocess.check_output([
        'bash', '-c', 'source PKGBUILD; echo ${pkgname[@]}',
    ]).decode('utf-8').strip().split(' '))
    with open('package.list', 'w') as f:
        f.write(package_list)
    git_add_files('package.list')  # aur_post_build() will commit it

    aur_post_build()
