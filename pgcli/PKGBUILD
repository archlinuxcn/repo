# Maintainer: asm0dey <pavel.finkelshtein+AUR@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>

pkgname=pgcli
pkgver=2.0.1
pkgrel=7
pkgdesc="a command line interface for Postgres with auto-completion and syntax highlighting"
url="http://pgcli.com/"
arch=(any)
license=('BSD')
depends=('python' 'python-sqlparse' 'python-psycopg2' 'python-click' 'python-prompt_toolkit' 'python-humanize>=0.5.1' 'python-configobj>=5.0.6' 'python-pgspecial>=1.11.2' 'python-setproctitle' 'python-cli_helpers>=1.0.1' 'python-keyring' 'python-dbus' 'python-pygments')
makedepends=('python-distribute')
source=($pkgname-$pkgver.zip::https://github.com/dbcli/pgcli/archive/v$pkgver.zip)
provides=('pgcli')
conflicts=('pgcli-git')
md5sums=('254822a27692a1951e6b2de95221606e')

package() {
    cd "$srcdir/pgcli-${pkgver}"
    python setup.py install --root="$pkgdir/" --optimize=1
    mkdir -p "$pkgdir/usr/share/licenses/$pkgname"
    cp LICENSE.txt "$_/LICENSE"
}
