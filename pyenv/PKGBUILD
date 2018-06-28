# Maintainer: Chris Down <chris@chrisdown.name>

pkgname=pyenv
pkgver=1.2.5
pkgrel=1
pkgdesc='Simple Python version management'
arch=('any')
url='https://github.com/pyenv/pyenv'
license=('MIT')
optdepends=('mercurial: to install dev builds')
depends=()
source=("https://github.com/pyenv/pyenv/archive/v${pkgver}.zip")
md5sums=('7fbddab1c94a4e07acec18de9558a0a0')

package() {
    mkdir -p "${pkgdir?}"/{opt/pyenv,usr/bin}
    cd "${srcdir?}/$pkgname-$pkgver" || return
    cp -a -- * "$pkgdir"/opt/pyenv
    ln -s /opt/pyenv/libexec/pyenv "$pkgdir/usr/bin/pyenv"

    for bin in pyenv-{,un}install python-build; do
        ln -s /opt/pyenv/plugins/python-build/bin/"$bin" "$pkgdir/usr/bin/$bin"
    done
}
