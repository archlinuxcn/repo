from lilaclib import *

update_on = [{
  'aur': 'google-cloud-sdk'
}]

build_prefix = 'extra-x86_64'

pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
  single_main()
