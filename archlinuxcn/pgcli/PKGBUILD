# Maintainer: asm0dey <pavel.finkelshtein+AUR@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>

pkgname=pgcli
pkgver=2.2.0
pkgrel=1
pkgdesc="a command line interface for Postgres with auto-completion and syntax highlighting"
url="http://pgcli.com/"
arch=(any)
license=('BSD')
depends=('python' 'python-sqlparse>=0.3.0' 'python-psycopg2' 'python-click' 'python-prompt_toolkit' 'python-humanize>=0.5.1' 'python-configobj>=5.0.6' 'python-pgspecial>=1.11.5' 'python-setproctitle' 'python-cli_helpers>=1.2.0' 'python-keyring' 'python-dbus' 'python-pygments')
makedepends=('python-distribute')
source=($pkgname-$pkgver.zip::https://github.com/dbcli/pgcli/archive/v$pkgver.zip)
provides=('pgcli')
conflicts=('pgcli-git')
md5sums=('54be939f8664d5ba8687be2f3b698e9b')

package() {
    cd "$srcdir/pgcli-${pkgver}"
    sed -i -e "s/prompt_toolkit>=2.0.6,<3.0.0/prompt_toolkit>=2.0.6/g" setup.py
    python setup.py install --root="$pkgdir/" --optimize=1
    mkdir -p "$pkgdir/usr/share/licenses/$pkgname"
    cp LICENSE.txt "$_/LICENSE"
}
