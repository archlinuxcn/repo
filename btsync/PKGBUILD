# Contributor: Dalton Miller
# Contributor: Kilian Lackhove kilian@lackhove.de
# Contributor: Justin Patera serialhex@gmail.com
# Maintainer: ava1ar <mail(at)ava1ar(dot)me>

pkgname=btsync
pkgver=2.3.8
pkgrel=1
pkgdesc="BitTorrent Sync (Resilio) - automatically sync files via secure, distributed technology"
license=("custom:btsync")
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h')
url="https://www.getsync.com"
install=btsync.install
backup=('etc/btsync.conf')
conflicts=('btsync-1.4')
source=(btsync.service btsync_user.service btsync.conf)
source_arm=("BitTorrent-Sync_arm-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.getsync.com/${pkgver}/linux-arm/BitTorrent-Sync_arm.tar.gz")
source_armv6h=("BitTorrent-Sync_arm-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.getsync.com/${pkgver}/linux-arm/BitTorrent-Sync_arm.tar.gz")
source_armv7h=("BitTorrent-Sync_armhf-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.getsync.com/${pkgver}/linux-armhf/BitTorrent-Sync_armhf.tar.gz")
source_i686=("BitTorrent-Sync_i386-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.getsync.com/${pkgver}/linux-i386/BitTorrent-Sync_i386.tar.gz")
source_x86_64=("BitTorrent-Sync_x64-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.getsync.com/${pkgver}/linux-x64/BitTorrent-Sync_x64.tar.gz")
sha1sums=('05038b03a673dd0207b2758a2e01db5d28c409d1'
          'd30deb7e41ba1d163b4a5e442b8d8118758d312a'
          'bf7d6bd7ffe2d23cce51a51e92fac3b82a7c87bb')
sha1sums_i686=('15dfbe8f2da78c697673b7f2a1ce02df197e4882')
sha1sums_x86_64=('234102dc920441718d2dd61b6f76e67feb62f101')
sha1sums_arm=('364271ab0445e9ccf6a896f48491e9e9ec8d6343')
sha1sums_armv6h=('364271ab0445e9ccf6a896f48491e9e9ec8d6343')
sha1sums_armv7h=('af5716b295c31738fdb0b5ba0076080e407f1b33')

package() {
	# install main binary
	install -Dm755 "${srcdir}"/btsync "${pkgdir}"/usr/bin/btsync

	# generate and install system-wide config
	mkdir -p "${pkgdir}"/etc
	./btsync --dump-sample-config \
		| sed 's:/home/user/\.sync:/var/lib/btsync:' \
		| sed 's:\/\/ "pid_file":  "pid_file":' \
		| sed 's:\/\/ "storage_path":  "storage_path":' \
		> "${pkgdir}"/etc/btsync.conf

	# install systemd config files
	install -Dm644 "${srcdir}"/btsync.service "${pkgdir}"/usr/lib/systemd/system/btsync.service
	install -Dm644 "${srcdir}"/btsync.conf "${pkgdir}"/usr/lib/tmpfiles.d/btsync.conf
	install -Dm644 "${srcdir}"/btsync_user.service "${pkgdir}"/usr/lib/systemd/user/btsync.service

	# install license
	install -Dm644 "${srcdir}"/LICENSE.TXT "${pkgdir}"/usr/share/licenses/${pkgname}/license.txt
}
