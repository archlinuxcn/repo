# Maintainer: Trizen <echo dHJpemVuQHByb3Rvbm1haWwuY29tCg== | base64 -d>

pkgname=alsi
pkgver=0.4.8
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
sha256sums=('0eae83cf3ca849a1d309cc1933e8329f24fb31c174587c4306ec665a7654dd8c')

package() {
    cd "$pkgname-$pkgver"
    install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
}
