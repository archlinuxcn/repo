# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

# TODO(oldherl): this package bundles tcl/tk sources
# Should we remove it and use Arch dependencies some day?
def pre_build():
    aur_pre_build(maintainers='ydallilar')
    add_depends(['libxml2', 'libx11', 'desktop-file-utils'])

#post_build = aur_post_build

#if __name__ == '__main__':
#  single_main(build_prefix)


