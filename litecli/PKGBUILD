# Maintainer: Andrej Radović <r.andrej@gmail.com>

pkgname=litecli
pkgver=0.0.3
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
md5sums=('976766def2012b1eee80dfcf703597b5')

package() {
    cd "$srcdir/${pkgname}-${pkgver}"
    python setup.py install --root="$pkgdir/" --optimize=1
    install -D "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
