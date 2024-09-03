# Maintainer: Brett Cornwall <ainola@archlinux.org>
# Contributor: polyzen
# Contributor: Army
# Contributor: Dan Serban
# Contributor: insanum
# Contributor: Thomas Zervogiannis

pkgname=gcalcli
pkgver=4.4.0
pkgrel=2
pkgdesc='Google calendar command line interface'
arch=('any')
url=https://github.com/insanum/gcalcli
license=('MIT')
makedepends=('python-setuptools')
depends=(
    'python-argcomplete'
    'python-dateutil'
    'python-google-api-core'
    'python-google-api-python-client'
    'python-google-auth-oauthlib'
    'python-httplib2'
    'python-parsedatetime'
)
optdepends=(
    'python-vobject: for ics/vcal importing'
)
source=("gcalcli-$pkgver.tar.gz::https://github.com/insanum/gcalcli/archive/v$pkgver.tar.gz")
sha256sums=('ad43ab43c9432a37a7f4d4a15c0d542b45eefc7a133487510ecd6de0ca410bdb')

build() {
    cd "gcalcli-$pkgver"
    python setup.py build
}

# Disabled because it downloads deps via pip. Report this upstream (if
# they're still alive).
#
# check() {
#     cd "gcalcli-$pkgver"
#     python setup.py test
# }

package() {
    cd "gcalcli-$pkgver"
    python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
    install -Dm644 docs/*.{md,png} -t "$pkgdir/usr/share/doc/$pkgname"
    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
