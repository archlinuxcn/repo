# Maintainer: Markus Schanz <coksnuss@googlemail.com>
pkgname=pacman-boot-backup-hook
pkgver=1.7
pkgrel=1
pkgdesc="Pacman hook that creates a copy of the /boot directory prior and post to upgrades of the systemd package or when mkinitcpio is triggered."
arch=('any')
backup=(etc/pacman-boot-backup.conf)
license=('MIT')
changelog=CHANGELOG

source=('LICENSE'
        'backup-boot-partition'
        '50_bootbackup.hook'
        'uu_bootbackup.hook'
        'pacman-boot-backup.conf')
sha256sums=('c70e605b0f57a2e4a20f76ff77935cb3bfce4adcf8b654aba4ef4e5103b431f2'
            '2445f388b4bc94382d25e01175babc804821090706d9ac69b5fadfbf5c60d5a9'
            'bfdb5d9f83f1cd9d9a427cb302883b4ddfa53e4e39e45c3006066baf5b84ce81'
            'a4b17a1dddaa6516258431fa67ecf236a128d3c7d640598423e13b2404e14e31'
            '1cefb346964c3aa4db829bffa788c39839f7a0959f294c91cdb43ae591c8472d')

package() {
	install -m 0755 -d $pkgdir/usr/share/licenses/$pkgname
	install -m 0644 $srcdir/LICENSE $pkgdir/usr/share/licenses/$pkgname

	install -m 0755 -d $pkgdir/etc
	install -m 0644 $srcdir/pacman-boot-backup.conf $pkgdir/etc

	install -m 0755 -d $pkgdir/usr/share/libalpm/hooks
	install -m 0644 $srcdir/50_bootbackup.hook $pkgdir/usr/share/libalpm/hooks
	install -m 0644 $srcdir/uu_bootbackup.hook $pkgdir/usr/share/libalpm/hooks

	install -m 0755 -d $pkgdir/usr/share/libalpm/scripts
	install -m 0755 $srcdir/backup-boot-partition $pkgdir/usr/share/libalpm/scripts
}
