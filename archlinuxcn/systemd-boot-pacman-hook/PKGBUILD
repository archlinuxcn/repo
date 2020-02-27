# Maintainer: Federico Di Pierro <nierro92@gmail.com>

pkgname=systemd-boot-pacman-hook
pkgver=2
pkgrel=1
pkgdesc="Pacman hook to upgrade systemd-boot after systemd upgrade."
arch=("any")
license=("GPL")
depends=('systemd')
source=(systemd-boot.hook)
md5sums=("13c7893e3e8b34479c42795d8f9e1ad3")

package() {
    install -m755 -d "${pkgdir}/usr/share/libalpm/hooks"
    install -m644 "${srcdir}/systemd-boot.hook" "${pkgdir}/usr/share/libalpm/hooks/systemd-boot.hook"
}
