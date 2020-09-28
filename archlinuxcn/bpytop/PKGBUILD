# Contributor: derfenix <derfenix@gmail.com>

pkgname=bpytop
pkgver=1.0.39
pkgrel=1
pkgdesc="Resource monitor that shows usage and stats for processor, memory, disks, network and processes"
arch=('any')
url="https://github.com/aristocratos/bpytop"
license=('Apache')
depends=('python3' 'python-psutil')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/aristocratos/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('d7fdbd1acf9fdd1afc5b6f396fad85dff8dd90455c694bc2a2da32d639f2c45f')


package() {
   cd "${srcdir}/${pkgname}-${pkgver}"
   make DESTDIR="${pkgdir}" PREFIX=/usr install
}
