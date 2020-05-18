# Maintainer: Salamandar <felix@piedallu.me>

pkgname=ninja-samurai
pkgver=1.0
pkgrel=1
pkgdesc='Compatibility package to use Samurai instead of Ninja Build'
arch=('any')
url='https://github.com/Salamandar/ninja-samurai'
license=(GPL)
depends=('samurai')
provides=('ninja')
conflicts=('ninja')

source=()
md5sums=()

package() {
    install -d "$pkgdir/usr/bin"
    ln -s samu "$pkgdir/usr/bin/ninja"
}
