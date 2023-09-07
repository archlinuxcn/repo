# Maintainer: Jonas Bögle <aur@iwr.sh>
# Contributor: Jonathan Duck <duckbrain30@gmail.com>

pkgname=typora
pkgver=1.7.4
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
sha512sums=('3f2a543c17c72b4cd911be1b542599cff5a68b80bbd88868f54d6f5bf94c420ea5791c30ba85d74b780268fc84cdeacfb643b2358981a541d4a608698bbae8b3')

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
