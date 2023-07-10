# Maintainer: Bart De Vries <bart at mogwai dot be>
# Contributor: Dan Johansen <strit@manjaro.org>

pkgname=box64
pkgver=0.2.2
pkgrel=1
pkgdesc='Linux Userspace x86_64 Emulator with a twist'
arch=('x86_64' 'aarch64' 'riscv64')
url='https://github.com/ptitSeb/box64'
license=('MIT')
install="box64.install"
depends=('gcc-libs')
makedepends=('git' 'cmake' 'python')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/ptitSeb/${pkgname}/archive/v${pkgver}.tar.gz"
        "box64.install")
sha256sums=('c8aec9540f66c0840253a1214bf622f2593a54e5cc96d7235457a0d0b207d0cc'
            '7e94518dbd11121f150a51b64f4c0ec11f844a83f7b15205d28c1de63de699f2')

build() {
    cd ${pkgname}-${pkgver}
    if [[ $CARCH == "aarch64" ]]; then 
        cmake -B build -S . \
              -DARM_DYNAREC=ON \
              -DCMAKE_BUILD_TYPE=RelWithDebInfo \
              -DCMAKE_INSTALL_PREFIX=/usr
    elif [[ $CARCH == "x86_64" ]]; then
        cmake -B build -S . \
              -DLD80BITS=1 -DNOALIGN=1 \
              -DCMAKE_BUILD_TYPE=RelWithDebInfo \
              -DCMAKE_INSTALL_PREFIX=/usr
    elif [[ $CARCH == "riscv64" ]]; then
        cmake -B build -S . \
              -DRV64=1 \
              -DCMAKE_BUILD_TYPE=RelWithDebInfo \
              -DCMAKE_INSTALL_PREFIX=/usr
    fi
    make -C build
}

package() {
    cd ${pkgname}-${pkgver}/build
    if [[ $CARCH == "aarch64" ]]; then
      make DESTDIR=${pkgdir} install
    elif [[ $CARCH == "x86_64" ]]; then
      install -Dm755 box64 -t "${pkgdir}/usr/bin/"
    elif [[ $CARCH == "riscv64" ]]; then
      make DESTDIR=${pkgdir} install
    fi

    install -Dm644 ../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"

    # Install documentation
    install -d "${pkgdir}/usr/share/doc/${pkgname}/"
    cp -R ../docs/* "${pkgdir}/usr/share/doc/${pkgname}/"
}
