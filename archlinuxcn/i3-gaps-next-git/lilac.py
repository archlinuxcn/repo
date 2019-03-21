#!/usr/bin/python3

from lilaclib import *

#  PATCH = r"""
#  diff --git a/archlinuxcn/i3-gaps-next-git/PKGBUILD b/archlinuxcn/i3-gaps-next-git/PKGBUILD
#  index 5c4c197f7..c399b212a 100644
#  --- a/archlinuxcn/i3-gaps-next-git/PKGBUILD
#  +++ b/archlinuxcn/i3-gaps-next-git/PKGBUILD
#  @@ -31,6 +31,50 @@ pkgver() {
#     git describe --long | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
#   }
#
#  +prepare() {
#  +  cd "$srcdir/$_gitname"
#  +  # apply patch from:  https://github.com/i3/i3/issues/3652
#  +  # see also https://aur.archlinux.org/packages/i3-gaps-next-git
#  +  patch -F5 -Np1 <<'EOF'
#  +diff --git a/Makefile.am b/Makefile.am
#  +index ee71b7f2..79201b98 100644
#  +--- a/Makefile.am
#  ++++ b/Makefile.am
#  +@@ -277,6 +277,8 @@ i3_LDADD = \
#  +
#  + libi3_CFLAGS = \
#  +    $(AM_CFLAGS) \
#  ++   $(GLIB2_CFLAGS) \
#  ++   $(GOBJECT2_CFLAGS) \
#  +    $(XCB_CFLAGS) \
#  +    $(XCB_UTIL_CFLAGS) \
#  +    $(XCB_UTIL_XRM_CFLAGS) \
#  +@@ -285,6 +287,8 @@ libi3_CFLAGS = \
#  +
#  + libi3_LIBS = \
#  +    $(top_builddir)/libi3.a \
#  ++   $(GLIB2_LIBS) \
#  ++   $(GOBJECT2_LIBS) \
#  +    $(XCB_LIBS) \
#  +    $(XCB_UTIL_LIBS) \
#  +    $(XCB_UTIL_XRM_LIBS) \
#  +diff --git a/configure.ac b/configure.ac
#  +index 6088699d..556b4be3 100644
#  +--- a/configure.ac
#  ++++ b/configure.ac
#  +@@ -101,6 +101,8 @@ PKG_CHECK_MODULES([XKBCOMMON], [xkbcommon xkbcommon-x11])
#  + PKG_CHECK_MODULES([YAJL], [yajl])
#  + PKG_CHECK_MODULES([LIBPCRE], [libpcre >= 8.10])
#  + PKG_CHECK_MODULES([PANGOCAIRO], [cairo >= 1.14.4 pangocairo])
#  ++PKG_CHECK_MODULES([GLIB2], [glib-2.0])
#  ++PKG_CHECK_MODULES([GOBJECT2], [gobject-2.0])
#  +
#  + # Checks for programs.
#  + AC_PROG_AWK
#  +EOF
#  +
#  +}
#  +
#   build() {
#     cd "$_gitname"
#
#  """
#
#  import subprocess
#
#  def apply_patch(filename, patch):
#      patch_proc = subprocess.Popen(["patch", "-Np3", filename], stdin=subprocess.PIPE)
#      patch_proc.communicate(patch.encode('utf-8'))
#
#  def pre_build():
#      aur_pre_build()
#      apply_patch("PKGBUILD", PATCH)
#
#  if __name__=="__main__":
#      single_main("extra-x86_64")
