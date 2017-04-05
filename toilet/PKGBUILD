# Maintainer:  Eric Bailey <nerflad@gmail.com>
# Contributor: Johnathan Jenkins <twodopeshaggy@gmail.com>
# Contributor: Christian Neukirchen <chneukirchen@gmail.com>
# Contributor: bl4ckb1t <bl4ckb1t@gmail.com>
pkgname=toilet
pkgver=0.3.3eb9d58
pkgrel=2
pkgdesc="free replacement for the FIGlet utility."
arch=('i686' 'x86_64')
url="https://github.com/cacalabs/toilet"
license=('custom:WTFPL')
makedepends=('git')
depends=('libcaca')
source=('git://github.com/cacalabs/toilet.git')
sha256sums=('SKIP')
_upstreamver=0.3
_gitname=toilet

pkgver() {
    cd "$_gitname"
    git log --oneline | awk '{print $1}' | head -n 1 | sed '1s/^/'$_upstreamver'./'
}

build() {
  cd "$_gitname"
  ./bootstrap
  ./configure --prefix=/usr
  make
}

package() {
  cd "$_gitname"
  make DESTDIR="$pkgdir" install
  install -Dm644 COPYING "$pkgdir"/usr/share/licenses/${pkgname}/COPYING
}
