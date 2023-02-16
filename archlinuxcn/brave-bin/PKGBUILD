# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Maintainer: José Miguel Sarasola <jmsaraur@gmail.com>
# Contributor: Như Bảo Trương <28810481+nhubaotruong@users.noreply.github.com>
# Contributor: Andrés Rodríguez <hello@andres.codes>
# Contributor: Jacob Mischka <jacob@mischka.me>
# Contributor: Manuel Mazzuola <origin.of@gmail.com>
# Contributor: Simón Oroño <simonorono@protonmail.com>
# Contributor: now-im <now im 627 @ gmail . com>
# Contributor: Giusy Digital <kurmikon at libero dot it>

# Version notes:
# `curl https://brave-browser-downloads.s3.brave.com/latest/release.version`

pkgname=brave-bin
pkgver=1.48.164
pkgrel=1
epoch=1
pkgdesc='Web browser that blocks ads and trackers by default (binary release)'
arch=(x86_64 aarch64)
url=https://brave.com
license=(MPL2 BSD custom:chromium)
depends=(alsa-lib
         gtk3
         libxss
         nss
         ttf-font)
optdepends=('cups: Printer support'
            'libgnome-keyring: Enable GNOME keyring support'
            'libnotify: Native notification support')
provides=("${pkgname%-bin}=$pkgver" 'brave-browser')
conflicts=("${pkgname%-bin}")
options=(!strip)
source=($pkgname.sh brave-browser.desktop)
source_x86_64=(${pkgname}-${pkgver}-x86_64.zip::https://github.com/brave/brave-browser/releases/download/v${pkgver}/brave-browser-${pkgver}-linux-amd64.zip)
source_aarch64=(${pkgname}-${pkgver}-aarch64.zip::https://github.com/brave/brave-browser/releases/download/v${pkgver}/brave-browser-${pkgver}-linux-arm64.zip)

noextract=(${pkgname}-${pkgver}-x86_64.zip ${pkgname}-${pkgver}-aarch64.zip)
sha256sums=('ba7d57a3328c68e6a78e49506af0e238936e823b2f463e8087c20fcf4300232a'
            'c07276b69c7304981525ecb022f92daf7ae125a4fb05ac3442157b50826e257a')
sha256sums_x86_64=('e00c27d0554634153727892626a46665817cf1f698e3192507e134d8c8ed2264')
sha256sums_aarch64=('a75abd716131039c31d8415974c2c0c24e1891dbd2e3bfbf3441b1467ae83556')

prepare() {
	mkdir -p brave
	bsdtar -xf "$pkgname-$pkgver-$CARCH.zip" -C brave
	chmod +x brave/brave
}

package() {
	install -dm0755 "$pkgdir/usr/lib"
	cp -a brave "$pkgdir/usr/lib/$pkgname"

	# allow firejail users to get the suid sandbox working
	chmod 4755 "$pkgdir/usr/lib/brave-bin/chrome-sandbox"

	install -Dm0755 "$pkgname.sh" "$pkgdir/usr/bin/brave"
	install -Dm0644 -t "$pkgdir/usr/share/applications/" "brave-browser.desktop"
	install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" brave/LICENSE
	pushd "$pkgdir/usr/"
	for size in 16x16 24x24 32x32 48x48 64x64 128x128 256x256; do
		install -Dm0644 "lib/$pkgname/product_logo_${size/x*/}.png" \
			"share/icons/hicolor/$size/apps/brave-desktop.png"
	done
}
