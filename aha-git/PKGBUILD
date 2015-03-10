_pkgname=aha
pkgname=aha-git
pkgver=0.4.6.1
pkgrel=2
pkgdesc="Ansi HTML Adapter: convert ANSI escape sequences to HTML."
arch=('i686' 'x86_64')
makedepends=('git')
#url="https://github.com/theZiz/aha"
url="http://ziz.delphigl.com/tool_aha.php"
license=('MPL' 'LPGL')
provides=('aha')
conflicts=('aha')

source=('git://github.com/theZiz/aha.git#branch=master')
sha512sums=('SKIP')

pkgver() {
  cd -- "$srcdir/$_pkgname"
#   git log -n1 --pretty=format:%ct
  git describe --tags
}

build() {
  cd -- "$srcdir/$_pkgname"
  make
}

package() {
  cd -- "$srcdir/$_pkgname"
  install -Dm755 "aha" "$pkgdir/usr/bin/aha"
  install -Dm644 "aha.1" "$pkgdir/usr/share/man/man1/aha.1"
}

# vim:set ts=2 sw=2 et: