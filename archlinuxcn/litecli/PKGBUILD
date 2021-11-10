# Maintainer: Andrej Radović <r.andrej@gmail.com>

pkgname=litecli
pkgver=1.6.0
pkgrel=1
pkgdesc="A command-line client for SQLite databases that has auto-completion "\
"and syntax highlighting."
url="https://github.com/dbcli/litecli"
arch=(any)
license=('BSD')
depends=(
  'python'
  'python-click'
  'python-pygments'
  'python-prompt_toolkit'
  'python-sqlparse'
  'python-configobj'
  'python-cli_helpers'
)
makedepends=('python-distribute')
source=(
  $pkgname-$pkgver.zip::https://github.com/dbcli/litecli/archive/v$pkgver.zip
)
provides=('litecli')
conflicts=('litecli-git')
md5sums=('d9504bc2538ba1eb1bc779489e9061b3')

package() {
  cd "$srcdir/${pkgname}-${pkgver}"
  sed -i "s/cli_helpers\[styles\] >= 1.0.1/cli_helpers >= 1.1.0/g" \
    setup.py
  python setup.py install --root="$pkgdir/" --optimize=1
  install -D "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
