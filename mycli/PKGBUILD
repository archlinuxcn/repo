# Maintainer: Miodrag Tokić
# Contributor: Aaron Abbott <aabmass at gmail dot com>

pkgname=mycli
pkgver=1.18.0
pkgrel=1
pkgdesc='A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting'
arch=('any')
url='https://github.com/dbcli/mycli'
license=('BSD')
depends=(
    'python'
    'python-click'
    'python-configobj'
    'python-cryptography'
    'python-prompt_toolkit'
    'python-pygments'
    'python-pymysql'
    'python-sqlparse'
    'python-cli_helpers'
)
makedepends=('python-setuptools')
options=(!emptydirs)

source=("$pkgname-$pkgver.tar.gz::https://github.com/dbcli/mycli/archive/v${pkgver}.tar.gz")
sha256sums=('bef5869fb56074fdead4f5eb0d06fd64100dde0d274720196383ecbe74e6890e')

build() {
    cd "$srcdir/$pkgname-$pkgver"

    python setup.py build
}

package() {
    cd "$srcdir/$pkgname-$pkgver"

    install -D -m 644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    python setup.py install --root="$pkgdir" --optimize=1
}
