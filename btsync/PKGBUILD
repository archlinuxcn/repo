# Contributor: Dalton Miller
# Contributor: Kilian Lackhove kilian@lackhove.de
# Contributor: Justin Patera serialhex@gmail.com
# Maintainer: ava1ar <mail(at)ava1ar(dot)me>

pkgname=btsync
pkgver=2.0.125
pkgrel=1
pkgdesc="BitTorrent Sync - automatically sync files via secure, distributed technology"
license=("custom:btsync")
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h')
url="http://www.bittorrent.com/sync"
install=btsync.install
backup=('etc/btsync.conf')
optdepends=("btsync-autoconfig: Auto-create users' config files if needed") 
conflicts=('btsync-1.4')
source=(btsync.service btsync_user.service btsync.conf)
source_arm=("https://download-cdn.getsyncapp.com/${pkgver}/linux-arm/BitTorrent-Sync_arm.tar.gz")
source_armv6h=("https://download-cdn.getsyncapp.com/${pkgver}/linux-arm/BitTorrent-Sync_arm.tar.gz")
source_armv7h=("https://download-cdn.getsyncapp.com/${pkgver}/linux-arm/BitTorrent-Sync_arm.tar.gz")
source_i686=("https://download-cdn.getsyncapp.com/${pkgver}/linux-i386/BitTorrent-Sync_i386.tar.gz")
source_x86_64=("https://download-cdn.getsyncapp.com/${pkgver}/linux-x64/BitTorrent-Sync_x64.tar.gz")
sha1sums=('05038b03a673dd0207b2758a2e01db5d28c409d1'
          'd30deb7e41ba1d163b4a5e442b8d8118758d312a'
          'bf7d6bd7ffe2d23cce51a51e92fac3b82a7c87bb')
sha1sums_i686=('fcc2558b4d28fe1484abd7814b836b3bd0bed973')
sha1sums_x86_64=('b6b9feb60eca811b4f4b4f5e717079b6ded82134')
sha1sums_arm=('6f6cae12db626aeb62ae7b8a38649bdaf3baef39')
sha1sums_armv6h=('6f6cae12db626aeb62ae7b8a38649bdaf3baef39')
sha1sums_armv7h=('6f6cae12db626aeb62ae7b8a38649bdaf3baef39')

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
