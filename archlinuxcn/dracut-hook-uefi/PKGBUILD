# Maintainer: Sebastian Wiesner <sebastian@swsnr.de>
# Maintainer: Franklyn Tackitt <franklyn@tackitt.net>
# Maintainer: Kevin Del Castillo <quebin31@gmail.com>

pkgname=dracut-hook-uefi
pkgver=14
pkgrel=3
pkgdesc="Install/remove hooks for dracut unified kernel images for systemd-boot"
url="https://aur.archlinux.org/packages/$pkgname"
arch=('any')
license=('APACHE')
# dracut requires binutils for --uefi support
depends=('dracut' 'binutils')
noextract=()
conflicts=()
source=(
    "dracut-uefi"
    "90-dracut-uefi-install.hook"
    "91-dracut-uefi-remove.hook"
)
sha256sums=('98fd28dce6462bed1d965235a4d3ca44e7cdd83d8349677c17d141f0624ebaf2'
            'b1415197d8ea47a39ff6a4976737559dd2b36bff7f980f06dcca812daf605507'
            '1daaad5f60d89c5198419db7e8a8d7599e9a4e252907437a1dc8f65f2ccd61b8')

package() {
    install -Dm644 "${srcdir}/90-dracut-uefi-install.hook" "${pkgdir}/usr/share/libalpm/hooks/90-dracut-uefi-install.hook"
    install -Dm644 "${srcdir}/91-dracut-uefi-remove.hook" "${pkgdir}/usr/share/libalpm/hooks/91-dracut-uefi-remove.hook"
    install -Dm755 "${srcdir}/dracut-uefi" "${pkgdir}/usr/share/libalpm/scripts/dracut-uefi"
}
