# $Id: PKGBUILD 220461 2014-08-20 20:42:53Z heftig $
# Maintainer : GI_Jack <iamjacksemail@hackermail.com>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Jason Chu <jchu@xentac.net>

# It should be noted that the tox developers think this package might break other openal
# installs, use with caution
# adds echo cancelation and a few other tox specific features.
# Contact NikolaiToryzin on Freenode IRC for questions

_pkgname=openal
pkgname=openal-soft-tox
pkgver=r3453.b80570b
pkgrel=2
pkgdesc="A cross-platform 3D audio library(patched for tox.im)"
arch=(i686 x86_64)
url="https://github.com/irungentoo/openal-soft-tox"
license=(LGPL)
depends=(glibc)
conflicts=$_pkgname
provides=$_pkgname
makedepends=(alsa-lib pkgconfig cmake libpulse qt4 fluidsynth portaudio git)
optdepends=('qt4: alsoft-config GUI Configurator'
            'fluidsynth: MIDI rendering')
source=($_pkgname::git+https://github.com/irungentoo/openal-soft-tox.git)
md5sums=('SKIP')

build() {
  cd $_pkgname/build
  cmake -D CMAKE_INSTALL_PREFIX=/usr -D CMAKE_BUILD_TYPE=Release ..
  make
}
pkgver() {
  cd $_pkgname
  printf 'r%s.%s' "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}
package() {
  cd $_pkgname
  make -C build DESTDIR="$pkgdir/" install
  install -m644 -t "$pkgdir/usr/share/openal" env-vars.txt hrtf.txt
}
