# Contributor: Caleb Maclennan <caleb@alerque.com>
# Contributor: Jacob Mischka <jacob@mischka.me>
# Contributor: Manuel Mazzuola <origin.of@gmail.com>
# Mantainer: Simón Oroño <simonorono@protonmail.com>
# https://aur.archlinux.org/packages/brave-bin/

pkgname=brave-bin
pkgver=0.56.14
pkgrel=1
pkgdesc='Web browser that blocks ads and trackers by default (binary release).'
arch=('x86_64')
url='https://brave.com/download'
license=('custom')
depends=('gtk3' 'gconf' 'nss' 'alsa-lib' 'libxss' 'libgnome-keyring' 'ttf-font')
optdepends=('cups: Printer support'
            'pepper-flash: Adobe Flash support')
provides=("${pkgname-bin}" 'brave-browser')
conflicts=("${pkgname-bin}")
source=("$pkgname-$pkgver.zip::https://github.com/brave/brave-browser/releases/download/v${pkgver}/brave-v${pkgver}-linux-x64.zip"
	"MPL2::https://raw.githubusercontent.com/brave/brave-browser/master/LICENSE"
        "$pkgname.sh"
        "$pkgname.desktop"
        "logo.png")
options=(!strip)
sha512sums=('b0150383510e9f3a2e95952fe19d2def385ca3b72544e82fe0e375402313bd78d5e270f96425bec78fd3c89e4f2bb3dea99c3f80886a327806d1aa0c45f4578b'
            'b8823586fead21247c8208bd842fb5cd32d4cb3ca2a02339ce2baf2c9cb938dfcb8eb7b24c95225ae625cd0ee59fbbd8293393f3ed1a4b45d13ba3f9f62a791f'
            '9b027e4ff5fd8b718b3f3eb2b4a78deccd5f7cfd577943b9d4a2c63031231f3ca8f892fed8c1b4f9f35d148b9656501d0f054719b24d355adcca96bb4975d947'
            '400d345271a3c98be668e4aa08743d707647c92ee35951e937238ac07074119cfdb9601e1934cdf46014bd181b26ab0b568e4cab67c790efe53d029d8b0f9c55'
            'b98aceb1953b3217f7ea1a3b55e11deec6b2725222c8c20e0170ecf266108368fe338b82c64658632985566ad63117ced0b8b2e7698447a46f987836aceba95f')
noextract=("$pkgname-$pkgver.zip")

prepare() {
  mkdir -p brave
  cat $pkgname-$pkgver.zip | bsdtar -xf- -C brave
  chmod +x brave/brave
}

_bsdtardir="brave"

package() {
    install -d -m0755 "$pkgdir/usr/lib"
    cp -a --reflink=auto $_bsdtardir "$pkgdir/usr/lib/$pkgname"

    install -Dm0755 "$pkgname.sh" "$pkgdir/usr/bin/brave"
    install -Dm0644 -t "$pkgdir/usr/share/applications" "$pkgname.desktop"
    install -Dm0644 "logo.png" "$pkgdir/usr/share/pixmaps/brave.png"
    install -Dm0664 -t "$pkgdir/usr/share/licenses/$pkgname" "MPL2"
    mv "$pkgdir/usr/lib/$pkgname/"{LICENSE,LICENSES.chromium.html} "$pkgdir/usr/share/licenses/$pkgname"

    ln -s /usr/lib/PepperFlash "$pkgdir/usr/lib/pepperflashplugin-nonfree"
}
