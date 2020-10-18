# Contributor: derfenix <derfenix@gmail.com>

pkgname=bpytop
pkgver=1.0.43
pkgrel=1
pkgdesc="Resource monitor that shows usage and stats for processor, memory, disks, network and processes"
arch=('any')
url="https://github.com/aristocratos/bpytop"
license=('Apache')
depends=('python3' 'python-psutil')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/aristocratos/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('9ce2f6a3c4f8738f2695785e18361a7912a2365822d4ab80d61f5fadcd577d41')


package() {
   cd "${srcdir}/${pkgname}-${pkgver}"
   make DESTDIR="${pkgdir}" PREFIX=/usr install
}
