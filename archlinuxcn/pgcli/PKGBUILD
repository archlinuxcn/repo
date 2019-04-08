# Maintainer: asm0dey <pavel.finkelshtein+AUR@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>

pkgname=pgcli
pkgver=2.1.0
pkgrel=2
pkgdesc="a command line interface for Postgres with auto-completion and syntax highlighting"
url="http://pgcli.com/"
arch=(any)
license=('BSD')
depends=('python' 'python-sqlparse' 'python-psycopg2' 'python-click' 'python-prompt_toolkit' 'python-humanize>=0.5.1' 'python-configobj>=5.0.6' 'python-pgspecial>=1.11.5' 'python-setproctitle' 'python-cli_helpers>=1.0.1' 'python-keyring' 'python-dbus' 'python-pygments')
makedepends=('python-distribute')
source=($pkgname-$pkgver.zip::https://github.com/dbcli/pgcli/archive/v$pkgver.zip)
provides=('pgcli')
conflicts=('pgcli-git')
md5sums=('92e6d5b977a0c687ed0d5710db975a41')

package() {
    cd "$srcdir/pgcli-${pkgver}"
    python setup.py install --root="$pkgdir/" --optimize=1
    mkdir -p "$pkgdir/usr/share/licenses/$pkgname"
    cp LICENSE.txt "$_/LICENSE"
}
