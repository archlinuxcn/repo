# Maintainer: stefanwimmer128 <info@stefanwimmer128.xyz>
# Contributor: Damien Flament <damien.flament at gmx dot com>

pkgname='shellspec'
pkgver=0.28.1
pkgrel=3
pkgdesc="BDD style unit testing framework for POSIX compliant shell script"
url="https://shellspec.info"
license=('MIT')
arch=('any')
depends=('sh')
makedepends=('git')
source=("shellspec::git+https://github.com/shellspec/shellspec.git#tag=$pkgver")
sha256sums=('SKIP')

check() {
    cd "shellspec" || return

    # Do not fail on warning sice a bash bug outputs to stderr when not expected https://mail.gnu.org/archive/html/bug-bash/2022-10/msg00073.html
    echo '--no-warning-as-failure' >> .shellspec

    make test
}

package() {
    cd "shellspec" || return

    PREFIX="$pkgdir/usr" make install
    install -m 644 -Dt "$pkgdir/usr/share/licenses/$pkgname" LICENSE
}
