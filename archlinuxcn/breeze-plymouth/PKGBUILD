# Maintainer: Jameson Pugh <imntreal@gmail.com>

pkgname=breeze-plymouth
pkgver=5.21.5
pkgrel=3
pkgdesc="Breeze theme for plymouth"
arch=(any)
url='https://projects.kde.org/breeze-plymouth'
license=(LGPL)
depends=(plymouth)
makedepends=(extra-cmake-modules)
optdepends=(noto-fonts)
source=("http://download.kde.org/stable/plasma/${pkgver}/${pkgname}-${pkgver}.tar.xz"{,.sig}
				'breeze-plymouth.cpiohook')
sha256sums=('f3ad283298c6818a660ab69487695f726ed6582adeb7f4c70195f867eb5e4b66'
            'SKIP'
            'e87418d5694514b6227a0fa81fbc71dfa05d50092a90082a4a4467f4d2d08385')
validpgpkeys=('2D1D5B0588357787DE9EE225EC94D18F7F05997E'  # Jonathan Riddell
              '0AAC775BB6437A8D9AF7A3ACFE0784117FBCE11D'  # Bhushan Shah <bshah@kde.org>
              'D07BD8662C56CB291B316EB2F5675605C74E02CF'  # David Edmundson
              '1FA881591C26B276D7A5518EEAAF29B42A678C20') # Marco Martin <notmart@gmail.com>

prepare() {
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/build"
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  cmake ..
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  make DESTDIR="${pkgdir}" install
	
	install -dm755 "${pkgdir}/etc/initcpio/install"
	install -m644 "${srcdir}/breeze-plymouth.cpiohook" "${pkgdir}/etc/initcpio/install/breeze-plymouth"
}
