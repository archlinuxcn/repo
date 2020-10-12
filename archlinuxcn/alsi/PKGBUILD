# Maintainer: Trizen <echo dHJpemVuQHByb3Rvbm1haWwuY29tCg== | base64 -d>

pkgname=alsi
pkgver=0.4.9
pkgrel=1
pkgdesc="ALSI: a configurable system information tool for Arch Linux."
url="https://github.com/trizen/${pkgname}"
arch=('any')
license=('GPLv3')
depends=(
    'perl>=5.14.2'
    'perl-data-dump'
    )
optdepends=(
    'scrot: for taking screenshots.'
    )
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/trizen/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('a49d25116af03b94823b78fac9c1c5a7254c7928f7e6adae08403f4739aebeef')

package() {
    cd "$pkgname-$pkgver"
    install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
}
