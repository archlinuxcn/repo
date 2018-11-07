# Maintainer: Ingo Bürk <admin at airblader dot de>
# Contributor: Vivien Didelot <vivien+aur@didelot.org>
pkgname=i3blocks-gaps-git
_pkgname=i3blocks-gaps
pkgver=1.4.r40.g2d91d2c
pkgrel=2
pkgdesc='Define blocks for your i3bar status line'
arch=('i686' 'x86_64')
url="https://github.com/Airblader/$_pkgname"
license=('GPL3')
makedepends=('git' 'pandoc')
optdepends=('acpi: For example battery script'
            'bc: For bandwidth script'
            'lm_sensors: For temperature script'
            'sysstat: For example cpu_usage script'
            'alsa-utils: For default volume script'
            'playerctl: For mediaplayer contrib script'
            'openvpn: For openvpn contrib script')
provides=("i3blocks")
conflicts=("i3blocks" "i3blocks-git")
source=("git+https://github.com/Airblader/$_pkgname")
sha256sums=('SKIP')

pkgver () {
  cd "$srcdir/$_pkgname"
  git describe --long | sed -r 's/([^-]*-g)/r\1/;s/-/./g'
}

build () {
  make -C "$srcdir/$_pkgname" clean
  make -C "$srcdir/$_pkgname" PREFIX=/usr
}

package () {
  make -C "$srcdir/$_pkgname" DESTDIR="$pkgdir" PREFIX=/usr LIBEXECDIR=/usr/lib install
}

# vim: et ts=2 sw=2
