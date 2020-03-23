# $Id: PKGBUILD 226039 2017-04-27 13:52:30Z felixonmars $
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: csslayer <wengxt AT gmail com>

_SPELL_EN_DICT_VER='20121020' # defined in upstream src/modules/spell/dict/CMakeLists.txt
_SPELL_EN_DICT_SHA256='c44a5d7847925eea9e4d2d04748d442cd28dd9299a0b572ef7d91eac4f5a6ceb'

_pkgname=fcitx5
pkgname=${_pkgname}-git
pkgver=r478.c123909
pkgrel=1
pkgdesc="Next generation of fcitx"
arch=('i686' 'x86_64')
url="https://github.com/fcitx/fcitx5"
license=('GPL')
depends=('cairo' 'enchant' 'iso-codes' 'libgl' 'libxkbcommon-x11' 'pango' 'systemd' 'wayland'
         'wayland-protocols' 'xcb-imdkit-git' 'xcb-util-wm' 'libxkbfile'
    	 'fmt' 'libxkbfile' 'gdk-pixbuf2' 'cldr-emoji-annotation')
makedepends=('extra-cmake-modules' 'git')
provides=($_pkgname)
conflicts=($_pkgname)

source=("git+$url.git"
	"en_dict-${_SPELL_EN_DICT_VER}.tar.gz::http://download.fcitx-im.org/data/en_dict-${_SPELL_EN_DICT_VER}.tar.gz")
sha256sums=('SKIP' "${_SPELL_EN_DICT_SHA256}")

pkgver() {
  cd fcitx5
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd fcitx5/src/modules/spell/dict
  cp $srcdir/en_dict-${_SPELL_EN_DICT_VER}.tar.gz .
}

build(){
  cd fcitx5

  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=/usr/lib .
  make
}

package() {
  cd fcitx5
  make DESTDIR="$pkgdir" install
}
