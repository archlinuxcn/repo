# Maintainer: Brett Cornwall <ainola@archlinux.org>
# Contributor: polyzen
# Contributor: Army
# Contributor: Dan Serban
# Contributor: insanum
# Contributor: Thomas Zervogiannis

pkgname=gcalcli
pkgver=4.5.0
pkgrel=2
pkgdesc='Google calendar command line interface'
arch=('any')
url=https://github.com/insanum/gcalcli
license=('MIT')
makedepends=('python-setuptools')
depends=(
    'python-argcomplete'
    'python-babel'
    'python-dateutil'
    'python-google-api-core'
    'python-google-api-python-client'
    'python-google-auth-oauthlib'
    'python-httplib2'
    'python-parsedatetime'
    'python-truststore'
)
optdepends=(
    'python-vobject: for ics/vcal importing'
)
source=("gcalcli-$pkgver.tar.gz::https://github.com/insanum/gcalcli/archive/v$pkgver.tar.gz")
sha256sums=('db906fde41236a5563af58d359f5b35ba586a4ad4c6cf2646dd6ba976857c1e3')

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
