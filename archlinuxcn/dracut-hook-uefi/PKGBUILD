# Maintainer: Sebastian Wiesner <sebastian@swsnr.de>
# Maintainer: Franklyn Tackitt <franklyn@tackitt.net>
# Maintainer: Kevin Del Castillo <quebin31@gmail.com>

pkgname=dracut-hook-uefi
pkgver=16
pkgrel=1
pkgdesc="Install/remove hooks for dracut unified kernel images for systemd-boot"
url="https://github.com/swsnr/dracut-hook-uefi"
arch=('any')
license=('APACHE')
# dracut requires binutils for --uefi support
depends=('dracut' 'binutils')
source=("https://github.com/swsnr/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('3b2946ce3af2c61c1197a3a1d654204f82b95ff83a7c625e1410cad87dd06935')

package() {
    make -C "${srcdir}/${pkgname}-${pkgver}" DESTDIR="${pkgdir}" install
}
