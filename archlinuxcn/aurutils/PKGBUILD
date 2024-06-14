# Maintainer: Alad Wenter <https://github.com/AladW>
# Co-Maintainer: Cedric Girard <cgirard [dot] archlinux [at] valinor [dot] fr>
# Co-Maintainer: zoorat <zoorat [at] protonmail [dot] com>

pkgname=aurutils
pkgver=19.7
pkgrel=1
pkgdesc='helper tools for the arch user repository'
url='https://github.com/AladW/aurutils'
arch=('any')
license=('ISC')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
changelog=aurutils.changelog
install=aurutils.install
sha256sums=('f92243f4350a8ccc63ef731d84dc26a56fff3c4a1dd456099f9194ca22ceba90')
depends=('git' 'pacutils' 'curl' 'perl' 'perl-json-xs' 'bash')
optdepends=('bash-completion: bash completion'
            'zsh: zsh completion'
            'devtools: aur-chroot'
            'vifm: default pager'
            'ninja: aur-sync ninja support'
            'bat: view-delta example script'
            'git-delta: view-delta example script'
            'python-srcinfo: sync-rebuild example script')

build() {
    cd "$pkgname-$pkgver"
    make AURUTILS_VERSION="$pkgver"
}

package() {
    cd "$pkgname-$pkgver"
    make AURUTILS_VERSION="$pkgver" PREFIX=/usr ETCDIR=/etc DESTDIR="$pkgdir" install
}
