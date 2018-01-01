from lilaclib import *

build_prefix = 'archlinuxcn-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build

depends = ['python-llvmlite', 'python-numpy']

if __name__ == '__main__':
  single_main(build_prefix)
