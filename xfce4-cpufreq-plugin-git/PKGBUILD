# Adapted for git by xavery <dkk089@gmail.com>, based on original PKGBUILD by :
# Maintainer: AndyRTR <andyrtr@archlinux.org>
# Contributor: tobias <tobias funnychar archlinux.org>

pkgname=xfce4-cpufreq-plugin-git
_gitname=xfce4-cpufreq-plugin
pkgver=1450.05848bb
pkgrel=1
pkgdesc="CPU frequency plugin for the Xfce4 panel"
arch=('i686' 'x86_64')
license=('GPL2')
url="http://goodies.xfce.org/projects/panel-plugins/xfce4-cpufreq-plugin"
groups=('xfce4-goodies')
depends=('xfce4-panel>=4.7.4' 'libxfcegui4' 'hicolor-icon-theme')
makedepends=('intltool' 'git' 'xfce4-dev-tools' 'autoconf' 'libtool')
provides=('xfce4-cpufreq-plugin')
conflicts=('xfce4-cpufreq-plugin')
options=('!libtool')
install=${_gitname}.install
source=('git://git.xfce.org/panel-plugins/xfce4-cpufreq-plugin'
        ${_gitname}.install)
sha256sums=('SKIP'
            '72645ae7d2dfdc919becbda9e38c2c26e8d8047716fb324e46aa3f2cb3162473')

pkgver() {
  cd ${_gitname}
  git describe --always | sed 's|-|.|g'
}

build() {
  cd ${_gitname}
  mkdir m4
  NOCONFIGURE=1 ./autogen.sh
  ./configure --prefix=/usr \
  --sysconfdir=/etc \
  --libexecdir=/usr/lib \
  --localstatedir=/var \
  --disable-static \
  --disable-debug
  make
}

package() {
  cd ${_gitname}
  make DESTDIR=${pkgdir} install
}
