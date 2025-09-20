# Maintainer: Michal Krenek (Mikos) <m.krenek@gmail.com>
pkgname=libmirisdr4-git
pkgver=r33.fd0452e.1
pkgrel=1
pkgdesc="Support of Mirics MSi001 + MSi2500 SDR devices (yet another flavour of libmirisdr)"
arch=('i686' 'x86_64')
url="https://github.com/f4exb/libmirisdr-4"
license=('GPL')
depends=('libusb>=1.0')
makedepends=('git' 'cmake')
provides=('libmirisdr' 'libmirisdr4' 'libmirisdr-git')
conflicts=('libmirisdr' 'libmirisdr4' 'libmirisdr-git')
source=("${pkgname}::git+https://github.com/f4exb/libmirisdr-4.git")
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/${pkgname}"
    printf "r%s.%s.1" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd "$srcdir/${pkgname}"
    cmake . \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_POLICY_VERSION_MINIMUM=3.5
    make
}

package() {
    cd "$srcdir/${pkgname}"
    make DESTDIR="$pkgdir/" install
    mkdir -p "${pkgdir}/etc/udev/rules.d/"
    cp "$srcdir/${pkgname}/mirisdr.rules" "${pkgdir}/etc/udev/rules.d/99-mirisdr.rules"
}
