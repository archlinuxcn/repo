# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Maintainer: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>
# Contributor: Tom < tomgparchaur at gmail dot com >
# Contributor: David Manouchehri <d@32t.ca>

pkgname=dropbox
pkgver=63.4.102
pkgrel=1
pkgdesc="A free service that lets you bring your photos, docs, and videos anywhere and share them easily."
arch=("i686" "x86_64")
url="https://www.dropbox.com"
license=(custom)
depends=("libsm" "libxslt" "libxmu" "libxdamage" "libxrender" "libxxf86vm" "libxcomposite" "fontconfig" "dbus")
optdepends=(
    'ufw-extras: ufw rules for dropbox'
    'perl-file-mimeinfo: opening dropbox folder on some desktop environments'
    'xdg-utils: for "Launch Dropbox Website" and file manager integration'
)
conflicts=("dropbox-experimental")
options=('!strip')

source=("dropbox.png" "dropbox.desktop" "terms.txt" "dropbox.service" "dropbox@.service")
source_i686=("https://clientupdates.dropboxstatic.com/dbx-releng/client/dropbox-lnx.x86-$pkgver.tar.gz")
source_x86_64=("https://clientupdates.dropboxstatic.com/dbx-releng/client/dropbox-lnx.x86_64-$pkgver.tar.gz")

sha256sums=('e7d245f5d1a3d5322614b61400ae2913a8caef44bc86717ff7d8197a15dd7f01'
            '541f2fd2de0d601a08cde7853e404062f542af21e6e7106825b5e68177168e0f'
            '34605b2f36fe6b4bde9b858da3f73ac1505986af57be78bbb1c2c9cf1a611578'
            '6c67a9c8c95c08fafafd2f1d828074b13e3347b05d2e4f4bf4e62746115d7477'
            '98581e65a91ae1f19ed42edcdaaa52e102298b5da0d71b50089393d364474d3d')
sha256sums_i686=('f928b2f9f02c77a5328ec8a62ccfbf0bffc151a0fdb7facf76a27c7199ef2cae')
sha256sums_x86_64=('abbdf116124a958d72181d8835e51ceade55999f9b6a3bc4be36d4ba7e22dc45')

package() {
	if [ "$CARCH" = "x86_64" ]; then
		_source_arch="x86_64"
	else
		_source_arch="x86"
	fi

	install -d "$pkgdir"/opt
	cp -R "$srcdir"/.dropbox-dist/dropbox-lnx.$_source_arch-$pkgver "$pkgdir"/opt/dropbox

	find "$pkgdir"/opt/dropbox/ -type f -exec chmod 644 {} \;
	chmod 755 "$pkgdir"/opt/dropbox/dropboxd
	chmod 755 "$pkgdir"/opt/dropbox/dropbox

	install -d "$pkgdir"/usr/bin
	ln -s ../../opt/dropbox/dropbox "$pkgdir"/usr/bin/dropbox

	install -Dm644 "$srcdir"/dropbox.desktop "$pkgdir"/usr/share/applications/dropbox.desktop
	install -Dm644 "$srcdir"/dropbox.png "$pkgdir"/usr/share/pixmaps/dropbox.png
	install -Dm644 "$srcdir"/terms.txt "$pkgdir"/usr/share/licenses/$pkgname/terms.txt
	install -Dm644 "$srcdir"/dropbox.service "$pkgdir"/usr/lib/systemd/user/dropbox.service
	install -Dm644 "$srcdir"/dropbox@.service "$pkgdir"/usr/lib/systemd/system/dropbox@.service
}
