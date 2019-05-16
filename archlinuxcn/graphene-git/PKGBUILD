# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Lubosz Sarnecki <lubosz@gmail.com>

_realname='graphene'
pkgname="$_realname-git"
pkgver=1.9.2.r1.g5263782
pkgrel=1
pkgdesc='A thin layer of graphic data types'
arch=('i686' 'x86_64')
url='https://github.com/ebassi/graphene/'
depends=('glib2')
makedepends=('git' 'gtk-doc' 'gobject-introspection' 'meson')
provides=("$_realname="$pkgver)
conflicts=("$_realname")
license=('MIT')
source=('git+https://github.com/ebassi/graphene.git')
md5sums=('SKIP')

subver() {
  PREFIX="m4_define(\[graphene_$1_version\], \["
  echo $(grep "$PREFIX" configure.ac | eval sed "'s/$PREFIX//'" | sed 's/\])//')
}

pkgver() {
  cd $_realname
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  arch-meson $_realname build -D gtk_doc=true
  ninja -C build
}

check() {
  meson test -C build
}

package() {
  DESTDIR="$pkgdir" meson install -C build
  install -Dt "$pkgdir/usr/share/licenses/$_realname" -m644 $_realname/LICENSE
  rm -r "$pkgdir"/usr/{lib,share}/installed-tests
}
