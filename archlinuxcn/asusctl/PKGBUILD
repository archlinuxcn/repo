# Maintainer: Mahdi Sarikhani <mahdisarikhani@outlook.com>
# Contributor: Fabian Bornschein <fabiscafe@archlinux.org>
# Contributor: Static_Rocket

pkgbase=asusctl
pkgname=(asusctl rog-control-center)
pkgver=6.4.0
pkgrel=1
pkgdesc="Daemon and tools to control your ASUS ROG laptop"
arch=('x86_64')
url="https://asus-linux.org"
license=('MPL-2.0')
makedepends=('cargo' 'fontconfig')
source=("${pkgbase}-${pkgver}.tar.gz::https://github.com/OpenGamingCollective/asusctl/archive/${pkgver}.tar.gz")
b2sums=('e90074e904f364386ad661784bd9fc2e929e83ea06ac62fd1d34eb03490cefe8aae3bed2722162f1e8ea5d69248138cb5fd9f90c3a18443d1d8c04cf732b928a')

prepare() {
    cd "${pkgbase}-${pkgver}"
    export RUSTUP_TOOLCHAIN=stable
    cargo fetch --locked --target host-tuple
}

build() {
    cd "${pkgbase}-${pkgver}"
    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    make build
}

package_asusctl() {
    pkgdesc="An utility for Linux to control many aspects of various ASUS laptops"
    depends=('glibc' 'libgcc' 'libusb' 'systemd-libs')
    optdepends=(
        'acpi_call: fan control'
        'asusctltray: tray profile switcher'
        'rog-control-center: graphical user interface for asusctl'
        'supergfxctl: hybrid GPU control'
    )
    install=asusctl.install

    cd "${pkgbase}-${pkgver}"
    make DESTDIR="${pkgdir}" \
        install-asusctl \
        install-asusd \
        install-asusd_user \
        install-asus-shutdown \
        install-data-asusd \
        install-data-asusd_user
}

package_rog-control-center() {
    pkgdesc="Graphical user interface for asusctl"
    depends=('asusctl' 'fontconfig' 'glibc' 'hicolor-icon-theme' 'libgcc' 'systemd-libs')

    cd "${pkgbase}-${pkgver}"
    make DESTDIR="${pkgdir}" \
        install-rog_gui \
        install-data-rog_gui
}
