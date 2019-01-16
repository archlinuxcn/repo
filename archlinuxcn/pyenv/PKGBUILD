# Maintainer: Chris Down <chris@chrisdown.name>

pkgname=pyenv
pkgver=1.2.8
pkgrel=1
pkgdesc='Simple Python version management'
arch=('any')
url='https://github.com/pyenv/pyenv'
license=('MIT')
optdepends=('mercurial: to install dev builds')
depends=()
source=("https://github.com/pyenv/pyenv/archive/v${pkgver}.zip")
md5sums=('7f545255193b1d5de610adcca548168b')

package() {
    mkdir -p "${pkgdir?}"/{opt/pyenv,usr/bin}
    cd "${srcdir?}/$pkgname-$pkgver" || return
    cp -a -- * "$pkgdir"/opt/pyenv
    ln -s /opt/pyenv/libexec/pyenv "$pkgdir/usr/bin/pyenv"

    for bin in pyenv-{,un}install python-build; do
        ln -s /opt/pyenv/plugins/python-build/bin/"$bin" "$pkgdir/usr/bin/$bin"
    done
}
