# Maintainer: Jonas Bögle <aur@iwr.sh>
# Contributor: Jonathan Duck <duckbrain30@gmail.com>

pkgname=typora
pkgver=1.7.5
pkgrel=1
pkgdesc="A minimal markdown editor and reader."
arch=('x86_64')
license=('custom:"Copyright (c) 2015 Abner Lee All Rights Reserved."')
url="https://typora.io/"
depends=('gtk3' 'nss' 'alsa-lib')
optdepends=(
	'noto-fonts-emoji: Or some other emoji font to see emojis'
	'pandoc: Import/export for extra file formats')
_filename="${pkgname}_${pkgver}_amd64.deb"
source=("https://typora.io/linux/$_filename")
sha512sums=('35627c94a4f3d11952b3c35d8818832db7ebaf6d3fe534fbdf3f07b67f90ed11b8a128a80a1e898c128a4a568196ee6501eb2e3075a2668a35438903d35b17cb')

package() {
	# unpack archive
	bsdtar -xf data.tar.xz -C "$pkgdir/"
	# remove lintian overrides
	rm -rf "$pkgdir/usr/share/lintian/"
	# move license to correct path
	install -Dm644 "$pkgdir/usr/share/doc/$pkgname/copyright" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	# delete previous copyright path
	rm "$pkgdir/usr/share/doc/$pkgname/copyright"
	# delete doc dir if empty
	rmdir --ignore-fail-on-non-empty "$pkgdir/usr/share/doc/$pkgname" "$pkgdir/usr/share/doc"
	# remove change log from application comment
	sed -i '/Change Log/d' "$pkgdir/usr/share/applications/typora.desktop"
	# fix dir permissions
	find "$pkgdir" -type d -exec chmod 755 {} \;
}
