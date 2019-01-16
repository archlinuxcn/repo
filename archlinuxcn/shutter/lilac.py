# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'
#pre_build = aur_pre_build
#post_build = aur_post_build

depends = ["orbit2", ("libgnome", "libgnome-data"), "gnome-vfs-nosmb", "libbonobo", "libgnome", "libbonoboui", "gnome-perl", "perl-gnome2-wnck", "perl-gtk2-imageview", "perl-gtk2-unique", "perl-json-maybexs"]

if __name__ == '__main__':
      single_main(build_prefix)
