# Maintainer: Justin Patera serialhex@gmail.com
# Contrib Repo: https://github.com/serialhex/bittorrent-sync
#
# Contributor: Dalton Miller
# Contributor: Kilian Lackhove kilian@lackhove.de
# Contributor: Emil Lundberg <lundberg.emil@gmail.com>

pkgname=bittorrent-sync
pkgver=1.1.70
pkgrel=2
pkgdesc="BitTorrent Sync - automatically sync files via secure, distributed technology"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h')
url="http://labs.bittorrent.com/experiments/sync.html"
license=('custom:bittorrent')
backup=("etc/btsync.conf")
install="${pkgname}.install"
source=("${pkgname}.install"
	"btsync.service"
	"btsync@.service"
	"btsync-makeconfig.sh"
	"btsync-wrapper.sh"
	"btsync.conf.doc"
	"terms-of-use.html::http://www.bittorrent.com/legal/terms-of-use"
	"privacy-policy.html::http://www.bittorrent.com/legal/privacy"
	)
sha256sums=('70189cc836ed0fd42496dad5ae586e31f65b87efb6f9182061049c1ff271133d'
	    'f51c4e95b141a6ff6118fcbd26451d6887181bf27ee966f9beeda4bec9014261'
	    '3d7d58815921c65e3d36beb739e5aaef513945ee713d3f4629e29d3af798efd5'
	    '551f73b0400427679e3854fa0d043859e00ac38168d6658d27a1306443f2c5d9'
	    'b45a32bcd0807d2df6e79593d20beb43febbfa6fd83373f9e1a5a7f8571e037e'
	    'de4f2a124d56ddbaec23535a250dbe9001606f47b74f3c3c97056107b21c7f6e'
	    'SKIP'
	    'SKIP'
	    )

if [ "$CARCH" == x86_64 ]; then
	source+=("http://syncapp.bittorrent.com/$pkgver/btsync_x64-$pkgver.tar.gz")
	sha256sums+=('7197ac1a23ff593b1cc6ef124cb2555376aac4637f368483ed2e0d5230b3dec2')
elif [ "$CARCH" == i686 ]; then
	source+=("http://syncapp.bittorrent.com/$pkgver/btsync_i386-$pkgver.tar.gz")
        sha256sums+=('25161852b8eaddf50ae385771f79bac47818467bc5cabc539a64d985e8af4dc6')
elif [ "$CARCH" == arm ] || [ "$CARCH" == armv6h ] || [ "$CARCH" == armv7h ]; then
        source+=("http://syncapp.bittorrent.com/$pkgver/btsync_arm-$pkgver.tar.gz")
        sha256sums+=('d79b3cf1881fcab95614693569c950d07dd93ffb70cefd901963dec54b75a05b')
fi

build() {
	cd "${srcdir}"
	./btsync-makeconfig.sh --storage-path /var/lib/btsync --login admin --device-name $HOSTNAME > btsync.conf
}

package() {
	cd "${srcdir}"

        install -D -m 644 LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.TXT"
        install -D -m 644 terms-of-use.html "${pkgdir}/usr/share/licenses/${pkgname}/terms-of-use.html"
        install -D -m 644 privacy-policy.html "${pkgdir}/usr/share/licenses/${pkgname}/privacy-policy.html"

	install -D -m 644 btsync.conf "${pkgdir}/etc/btsync.conf"
	install -D -m 644 btsync.conf.doc "${pkgdir}/usr/share/${pkgname}/btsync.conf.doc"
	install -D -m 755 btsync-makeconfig.sh "${pkgdir}/usr/share/${pkgname}/btsync-makeconfig.sh"

	install -D -m 755 btsync "${pkgdir}/usr/bin/btsync"
	install -D -m 755 btsync-wrapper.sh "${pkgdir}/usr/bin/btsync-wrapper"

	install -D -m 644 btsync.service "${pkgdir}/usr/lib/systemd/system/btsync.service"
	install -D -m 644 btsync@.service "${pkgdir}/usr/lib/systemd/system/btsync@.service"

}
