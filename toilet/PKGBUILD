# Maintainer:  Eric Bailey <nerflad@gmail.com>
# Contributor: Johnathan Jenkins <twodopeshaggy@gmail.com>
# Contributor: Christian Neukirchen <chneukirchen@gmail.com>
# Contributor: bl4ckb1t <bl4ckb1t@gmail.com>
pkgname=toilet
pkgver=0.3.r155.3eb9d58
pkgrel=1
pkgdesc="free replacement for the FIGlet utility."
arch=('i686' 'x86_64')
url="https://github.com/cacalabs/toilet"
license=('custom:WTFPL')
depends=('libcaca')
source=('https://github.com/cacalabs/toilet/archive/master.tar.gz')
sha256sums=('294e6992accafd407fa43892f445137e81a7a0b1c8610b76928d1bab6b5c1fec')

build() {
    cd $pkgname-master
    ./bootstrap
    ./configure --prefix=/usr
    make
}

package() {
    cd $pkgname-master
    make DESTDIR="$pkgdir" install
    install -Dm644 COPYING "$pkgdir"/usr/share/licenses/${pkgname}/COPYING
}
