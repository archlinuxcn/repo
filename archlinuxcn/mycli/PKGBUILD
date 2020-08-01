# Maintainer: Miodrag Tokić
# Contributor: Yuanji <self@gimo.me>
# Contributor: Aaron Abbott <aabmass at gmail dot com>

pkgname=mycli
pkgver=1.22.1
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
optdepends=('python-paramiko: SSH support')
options=(!emptydirs)

source=("$pkgname-$pkgver.tar.gz::https://github.com/dbcli/mycli/archive/v${pkgver}.tar.gz")
sha256sums=('52d107105a922de883572b518019477338343d1c7c8618da1c4db2cedb20d912')

prepare() {
    cd "$srcdir/$pkgname-$pkgver"
}

build() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py build
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    install -D -m 644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    python setup.py install --root="$pkgdir" --optimize=1
}
