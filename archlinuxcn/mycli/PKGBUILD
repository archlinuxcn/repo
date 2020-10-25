# Maintainer: Miodrag Tokić
# Contributor: Yuanji <self@gimo.me>
# Contributor: Aaron Abbott <aabmass at gmail dot com>

pkgname=mycli
pkgver=1.22.2
pkgrel=2
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

source=(
    "$pkgname-$pkgver.tar.gz::https://github.com/dbcli/mycli/archive/v${pkgver}.tar.gz"
    "completion_engine.py.patch"
)
sha256sums=(
    '4427442cf3e66ebbbb480bc5112bdf7e0432c70645f320313e2e0dbf0ae147fb'
    '33f3e60abfe68bc7375dacead9676b3cc4920e1d16c7b57dcf5f474c0c3e6aad'
)

prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    patch -N -p1 -i "$srcdir/completion_engine.py.patch"
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
