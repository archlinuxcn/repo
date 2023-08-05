# Maintainer: Christian Boxdörfer <christian.boxdoerfer@posteo.de>
pkgname=fsearch
_gitname=fsearch
pkgver=0.2.3
pkgrel=1
pkgdesc="A fast graphical file search utility."
arch=('i686' 'x86_64')
url="https://cboxdoerfer.github.io/fsearch"
license=('GPL2')
depends=('gtk3' 'icu' 'pcre2')
makedepends=('git' 'meson')
conflicts=('fsearch-git')
source=("$pkgname-$pkgver.tar.gz"::"https://github.com/cboxdoerfer/fsearch/archive/$pkgver.tar.gz")
sha256sums=('b3c576bf1230da7c374d00bb32d72686b940b4dee80d941495acfdd5437bf117')

build() {
    arch-meson $pkgname-$pkgver build \
        --buildtype release \
        -Dchannel=AUR-stable
    meson compile -C build
}

check() {
    meson test -C build
}

package() {
    DESTDIR="$pkgdir" meson install -C build
}
