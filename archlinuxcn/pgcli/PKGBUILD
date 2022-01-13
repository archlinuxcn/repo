# Maintainer: a821
# Contributor: asm0dey <pavel.finkelshtein+AUR@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>

pkgname=pgcli
pkgver=3.3.0
pkgrel=2
pkgdesc="a command line interface for Postgres with auto-completion and syntax highlighting"
url="http://pgcli.com/"
arch=(any)
license=('BSD')
depends=('python-sqlparse' 'python-psycopg2' 'python-click' 'python-prompt_toolkit'
         'python-configobj' 'python-pgspecial' 'python-setproctitle' 'python-cli_helpers'
         'python-keyring' 'python-pygments' 'python-pendulum')
makedepends=('python-setuptools')
source=($pkgname-$pkgver.tar.gz::https://github.com/dbcli/pgcli/archive/v$pkgver.tar.gz)
sha256sums=('e6fefd9f77a060d5c2de30769022172f75df9cffd94b9d0593ed876ec3600e99')

prepare() {
    # remove pinned pygment version
    sed -i 's/,<=2.11.1//' "pgcli-${pkgver}/setup.py"
}

package() {
    cd "pgcli-${pkgver}"
    python setup.py install --root="$pkgdir/" --optimize=1
    install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
