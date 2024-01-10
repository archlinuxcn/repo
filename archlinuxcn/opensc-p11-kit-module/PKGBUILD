# Maintainer: Rasmus Moorats <xx@nns.ee>
pkgname=opensc-p11-kit-module
pkgver=1.0.0
pkgrel=2
pkgdesc='OpenSC module configuration for p11-kit'
url='https://github.com/OpenSC/OpenSC'
arch=('any')
license=('Unlicense')
source=('opensc.module')
depends=('opensc' 'libp11-kit')
provides=('opensc-p11-kit-module')
sha256sums=('fea71e2e2c1853bba034106d4eb40646a787ed900fef883e09d38dcb29675db4')

package() {
  cd "$srcdir/"

  install -Dm644 opensc.module "${pkgdir}/usr/share/p11-kit/modules/opensc.module"
}
