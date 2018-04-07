# Maintainer: Chris Down <chris@chrisdown.name>

pkgname=pyenv
pkgver=1.2.3
pkgrel=1
pkgdesc='Simple Python version management'
arch=('any')
url='https://github.com/pyenv/pyenv'
license=('MIT')
optdepends=('mercurial: to install dev builds')
depends=()
source=("https://github.com/pyenv/pyenv/archive/v${pkgver}.zip")
md5sums=('eef5143505aa856fcc7b64523a8975df')

package() {
    mkdir -p "${pkgdir?}"/{opt/pyenv,usr/bin}
    cd "${srcdir?}/$pkgname-$pkgver" || return
    cp -a -- * "$pkgdir"/opt/pyenv
    ln -s /opt/pyenv/libexec/pyenv "$pkgdir/usr/bin/pyenv"

    for bin in pyenv-{,un}install python-build; do
        ln -s /opt/pyenv/plugins/python-build/bin/"$bin" "$pkgdir/usr/bin/$bin"
    done
}
