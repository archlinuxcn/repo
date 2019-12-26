# Maintainer: xiretza <xiretza+aur@gmail.com>
# Contributor: Arthur Țițeică arthur.titeica/gmail/com
# Contributor: rockerzz <rockerzz@gmail.com>

pkgname=log4c
pkgver=1.2.4
pkgrel=2
pkgdesc='Logging FrameWork for C, as Log4j or Log4Cpp'
url='http://log4c.sourceforge.net/'
arch=('i686' 'x86_64')
license=('LGPL')
depends=('expat')
source=("http://prdownloads.sourceforge.net/${pkgname}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('5991020192f52cc40fa852fbf6bbf5bd5db5d5d00aa9905c67f6f0eadeed48ea')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr \
              --sysconfdir=/etc/log4c
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="${pkgdir}" install
}

