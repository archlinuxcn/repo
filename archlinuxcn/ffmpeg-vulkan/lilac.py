from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
    g.files = download_official_pkgbuild('ffmpeg')
    for line in edit_file('PKGBUILD'):
        if 'pkgname=' in line:
            line = 'pkgname=ffmpeg-vulkan'
        elif 'provides=' in line:
            line = line.replace('(','(ffmpeg')
        elif 'depends=' in line and 'makedepends' not in line and 'optdepends' not in line:
            print(line)
            print('vulkan-icd-loader')
            print('glslang')
            print('spirv-tools')
            continue
        elif 'makedepends=' in line:
            print(line)
            print('vulkan-headers')
            continue
        elif 'source=' in line:
            print("conflicts=(ffmpeg)")
        elif './configure' in line:
            print(line)
            print("--enable-vulkan \\")
            print("--enable-libglslang \\")
            continue

        print(line)

def post_build():
    git_add_files(g.files)
    git_commit()

