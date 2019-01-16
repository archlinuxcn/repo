# Maintainer: Jianqiu Zhang <void001@archlinuxcn.org>

pkgname=ssf2fcitx-git
pkgver=79c151d
pkgrel=1
pkgdesc="Automagically convert your favorite sogou-pinyin skin to fcitx skin"
#epoch=0
arch=('x86_64')
url="https://github.com/VOID001/ssf2fcitx"
license=(GPL3)
groups=()
depends=(qt5-base)
makedepends=(git cmake qt5-base wget)
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
changelog=
source=($pkgname-$pkgver::git+https://github.com/VOID001/ssf2fcitx)
md5sums=('SKIP')

check()
{
  echo "Nothing to do"
}

prepare()
{
  echo "Nothing to do"
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr ..
  make 
}

package() {
  cd "$srcdir/$pkgname-$pkgver/build"
  make test
  make DESTDIR="$pkgdir/" install
}

# vim:set ts=2 sw=2 et:

