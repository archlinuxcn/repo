# Maintainer: Sergey Shatunov <me@aur.rocks>

pkgname=dracut-ukify
pkgver=11
pkgrel=1
pkgdesc="Integration layer for dracut and systemd's ukify tool for Arch Linux"
url="https://aur.archlinux.org/packages/dracut-ukify"
arch=(any)
license=('MIT')
depends=(dracut 'systemd-ukify>=254')
optdepends=(
	'sbsigntools: secureboot support'
)
source=('10-dracut-ukify-pre-install.hook'
        '60-dracut-ukify-remove.hook'
        '90-dracut-ukify-dkms-remove.hook'
        '90-dracut-ukify-install.hook'
        'dracut-ukify'
        'dracut-ukify.conf')
sha256sums=('c1be3eaf920282c15fba17e22be3d38c407a1b2c502028677950978286a85585'
            '2cebdc72aa91cb9f6ed94bcfacfd827973409c1a366c68aa646665de31ef629b'
            'd96d34365c49fe1b5295c304fdc84bd4e6a74302dda3da9bb62220c891dea4fd'
            '4efc18bb4bf68b67aa7e7422484082e956e0cbb04404c8273bc27d1d2f4a04c9'
            'c8215f9e2e5e6ac00c929e010905220eeecdf9382f8f0de1521dfa664358a449'
            'd6a7ac3a97fccdfd47e9bd72699130c6ac5b6a8ce791c7eaea5f1e29d54f8772')
backup=(etc/dracut-ukify.conf)
provides=(dracut-hook)
conflicts=(dracut-hook-uefi dracut-uefi-hook)

package() {
  install -Dm644 "${srcdir}/10-dracut-ukify-pre-install.hook" "${pkgdir}/usr/share/libalpm/hooks/10-dracut-ukify-pre-install.hook"
  install -Dm644 "${srcdir}/60-dracut-ukify-remove.hook"      "${pkgdir}/usr/share/libalpm/hooks/60-dracut-ukify-remove.hook"
  install -Dm644 "${srcdir}/90-dracut-ukify-dkms-remove.hook" "${pkgdir}/usr/share/libalpm/hooks/90-dracut-ukify-dkms-remove.hook"
  install -Dm644 "${srcdir}/90-dracut-ukify-install.hook"     "${pkgdir}/usr/share/libalpm/hooks/90-dracut-ukify-install.hook"
  install -Dm755 "${srcdir}/dracut-ukify"                     "${pkgdir}/usr/bin/dracut-ukify"
  install -Dm644 "${srcdir}/dracut-ukify.conf"                "${pkgdir}/etc/dracut-ukify.conf"
}
