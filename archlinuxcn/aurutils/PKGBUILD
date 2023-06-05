# Maintainer: Alad Wenter <https://github.com/AladW>
# Co-Maintainer: Cedric Girard <cgirard [dot] archlinux [at] valinor [dot] fr>
pkgname=aurutils
pkgver=15.4
pkgrel=1
pkgdesc='helper tools for the arch user repository'
url='https://github.com/AladW/aurutils'
arch=('any')
license=('custom:ISC')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
changelog=aurutils.changelog
install=aurutils.install
sha256sums=('4c1e6cd3c4ee52e81ad46ee4e4a14af7c6dcae450602c68c305b748855e162ac')
depends=('git' 'pacutils' 'curl' 'perl')
optdepends=('bash-completion: bash completion'
            'zsh: zsh completion'
            'devtools: aur-chroot'
            'vifm: default pager'
            'perl-json-xs: faster JSON serialization'
            'ninja: aur-sync ninja support'
            'bat: view-delta example script'
            'git-delta: view-delta example script'
            'python-srcinfo: sync-rebuild example script'
            'python-pyxdg: sync-rebuild example script')

build() {
    cd "$pkgname-$pkgver"
    make AURUTILS_VERSION="$pkgver"
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
