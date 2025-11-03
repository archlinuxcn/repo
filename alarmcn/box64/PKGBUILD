# Maintainer: Bart De Vries <bart at mogwai dot be>
# Contributor: Dan Johansen <strit@manjaro.org>

pkgname=box64
pkgver=0.3.8
pkgrel=2
pkgdesc='Linux Userspace x86_64 Emulator with a twist'
arch=('x86_64' 'aarch64' 'riscv64' 'powerpc64le')
url='https://github.com/ptitSeb/box64'
license=('MIT')
install="box64.install"
depends=('gcc-libs')
makedepends=('git' 'cmake' 'python')
options=('!strip')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/ptitSeb/${pkgname}/archive/v${pkgver}.tar.gz"
        "box64.install")
sha256sums=('db968457550ca86a35297bb458a1c0126d533e1607be15f6b285964ee7ea1098'
            '7e94518dbd11121f150a51b64f4c0ec11f844a83f7b15205d28c1de63de699f2')

build() {
    cd ${pkgname}-${pkgver}
    if [[ $CARCH == "aarch64" ]]; then
        name="$(LC_ALL=C lscpu | grep Model)"
        exargs=""
        if [ -n "$(echo $name | grep RK3588)" ]; then
              exargs="-DRK3588=1"
        elif [ -n "$(echo $name | grep RK3399)" ]; then
              exargs="-DRK3399=1"
        elif [ -n "$(echo $name | grep 'Cortex-A53')" ]; then
              exargs="-DRPI3ARM64=1"
        elif [ -n "$(echo $name | grep 'Cortex-A72')" ]; then
              exargs="-DRPI4ARM64=1"
        elif [ -n "$(echo $name | grep 'Cortex-A76')" ]; then
              exargs="-DRPI5ARM64=1"
        fi
        cmake -B build -S . \
              $exargs \
              -DARM_DYNAREC=ON \
              -DCMAKE_BUILD_TYPE=RelWithDebInfo \
              -DCMAKE_INSTALL_PREFIX=/usr
    elif [[ $CARCH == "x86_64" ]]; then
        cmake -B build -S . \
              -DLD80BITS=1 -DNOALIGN=1 \
              -DCMAKE_BUILD_TYPE=RelWithDebInfo \
              -DCMAKE_INSTALL_PREFIX=/usr
    elif [[ $CARCH == "powerpc64le" ]]; then
        cmake -B build -S . \
              -DPPC64LE=1 \
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
    elif [[ $CARCH == "powerpc64le" ]]; then
      make DESTDIR=${pkgdir} install
    elif [[ $CARCH == "riscv64" ]]; then
      make DESTDIR=${pkgdir} install
    fi

    install -Dm644 ../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"

    # Install documentation
    install -d "${pkgdir}/usr/share/doc/${pkgname}/"
    cp -R ../docs/* "${pkgdir}/usr/share/doc/${pkgname}/"
}
