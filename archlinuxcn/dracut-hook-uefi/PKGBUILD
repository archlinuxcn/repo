# Maintainer: Sebastian Wiesner <sebastian@swsnr.de>
# Maintainer: Franklyn Tackitt <franklyn@tackitt.net>
# Maintainer: Kevin Del Castillo <quebin31@gmail.com>

pkgname=dracut-hook-uefi
pkgver=17
pkgrel=1
pkgdesc="Install/remove hooks for dracut unified kernel images for systemd-boot"
url="https://github.com/swsnr/dracut-hook-uefi"
arch=('any')
license=('APACHE')
# dracut requires binutils for --uefi support
depends=('dracut' 'binutils')
source=("https://github.com/swsnr/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('2dca141c7ceed8f0b85b04fb8781e440f7e0f263afa7145541deb098c637cd7d')

package() {
    make -C "${srcdir}/${pkgname}-${pkgver}" DESTDIR="${pkgdir}" install
}
