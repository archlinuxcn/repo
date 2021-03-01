# Maintainer: João Figueiredo <jf.mundox@gmail.com>
# Contributor: Jan de Groot <jan@archlinux.org>

pkgname=gconf
pkgver=3.2.6+11+g07808097
pkgrel=10
pkgdesc="An obsolete configuration database system"
url="https://projects-old.gnome.org/gconf/"
arch=($CARCH)
license=(LGPL)
depends=(libxml2 polkit libldap dbus-glib python)
makedepends=(git intltool gtk-doc gobject-introspection gnome-common)
install=gconf.install
_commit=0780809731c8ab1c364202b1900d3df106b28626 # The latest and last commit, dug out from deep within the waves of time...
source=("git+https://gitlab.gnome.org/Archive/gconf.git#commit=$_commit"
        01_xml-gettext-domain.patch gconf-reload.patch
        gconf-merge-schema gconfpkg gconf-{install,remove}.hook)
sha256sums=('SKIP'
            'c883dec2b96978874a53700cfe7f26f24f8296767203e970bc6402b4b9945eb8'
            '567b78d8b4b4bbcb77c5f134d57bc503c34867fcc6341c0b01716bcaa4a21694'
            'ee6b6e6f4975dad13a8c45f1c1f0547a99373bdecdcd6604bfc12965c328a028'
            'bf1928718caa5df2b9e54a13cfd0f15a8fe0e09e86b84385ce023616a114e898'
            '2732b2a6b187c5620105a036bde12edee99669605f70cbde56fe5f39619c3dc0'
            '436a65ff290095bc3d35d7d6297cf4d647f61e9f9922cea7ef9f1e251b447ff7')

prepare() {
  cd $pkgname

  # Patch from fedora - reloads gconf after installing schemas
  patch -Np1 -i ../gconf-reload.patch

  # http://bugzilla.gnome.org/show_bug.cgi?id=568845
  patch -Np1 -i ../01_xml-gettext-domain.patch

  # The following line copied from Fedora
  # https://src.fedoraproject.org/rpms/GConf2/blob/70ed26d67b563d858a84505622d11f41879a6b37/f/GConf2.spec#_90
  2to3 --write --nobackup gsettings/gsettings-schema-convert

  sed -i '1s|#!/usr/bin/env python$|#!/usr/bin/python|' gsettings/gsettings-schema-convert

  NOCONFIGURE=1 ./autogen.sh
}

build() {
  cd $pkgname
  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var \
    --libexecdir=/usr/lib \
    --enable-defaults-service \
    --disable-gtk-doc \
    --disable-static \
    --disable-orbit
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

check() {
  cd $pkgname
  make check
}

package() {
  DESTDIR="$pkgdir" make -C $pkgname install

  install -d "$pkgdir/etc/gconf/gconf.xml.system"
  install -D gconf-merge-schema gconfpkg -t "$pkgdir/usr/bin"
  install -Dm644 ./*.hook -t "$pkgdir/usr/share/libalpm/hooks"

  # fix dbus policy location - --with-dbusdir doesn't work
  install -Dm644 "$pkgdir/etc/dbus-1/system.d/org.gnome.GConf.Defaults.conf" -t "$pkgdir/usr/share/dbus-1/system.d"
  rm -rf "$pkgdir/etc/dbus-1/"
}
