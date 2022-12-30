# $Id: PKGBUILD 226039 2017-04-27 13:52:30Z felixonmars $
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: csslayer <wengxt AT gmail com>

_SPELL_EN_DICT_VER='20121020' # defined in upstream src/modules/spell/dict/CMakeLists.txt
_SPELL_EN_DICT_SHA256='c44a5d7847925eea9e4d2d04748d442cd28dd9299a0b572ef7d91eac4f5a6ceb'

_pkgname=fcitx5
pkgname=${_pkgname}-git
pkgver=5.0.21.r16.g22454ff
pkgrel=1
pkgdesc="Next generation of fcitx"
arch=('i686' 'x86_64')
url="https://github.com/fcitx/fcitx5"
license=('GPL')
depends=('cairo' 'enchant' 'iso-codes' 'libgl' 'libxkbcommon-x11' 'pango' 'systemd' 'wayland'
         'wayland-protocols' 'xcb-imdkit-git' 'xcb-util-wm' 'libxkbfile' 'fmt' 'gdk-pixbuf2')
makedepends=('extra-cmake-modules' 'git' 'ninja')
provides=($_pkgname)
conflicts=($_pkgname)

source=("git+$url.git"
	"en_dict-${_SPELL_EN_DICT_VER}.tar.gz::http://download.fcitx-im.org/data/en_dict-${_SPELL_EN_DICT_VER}.tar.gz")
sha256sums=('SKIP' "${_SPELL_EN_DICT_SHA256}")

pkgver() {
  cd fcitx5
  git describe --long | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd fcitx5/src/modules/spell
  cp $srcdir/en_dict-${_SPELL_EN_DICT_VER}.tar.gz .
}

build(){
  cd fcitx5

  cmake -GNinja -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=/usr/lib -DCMAKE_INSTALL_LIBEXECDIR=/usr/lib -DCMAKE_INSTALL_SYSCONFDIR=/etc .
  ninja
}

check(){
  cd fcitx5
  ninja test
}

package() {
  cd fcitx5
  DESTDIR="$pkgdir" ninja install
}
