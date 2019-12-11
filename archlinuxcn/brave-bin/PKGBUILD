# Contributor: Caleb Maclennan <caleb@alerque.com>
# Contributor: Jacob Mischka <jacob@mischka.me>
# Contributor: Manuel Mazzuola <origin.of@gmail.com>
# Contributor: Simón Oroño <simonorono@protonmail.com>
# Contributor: now-im <now im 627 @ gmail . com>
# Contributor: Giusy Digital <kurmikon at libero dot it>
# Mantainer: Andrés Rodríguez <hello@andres.codes>
# https://aur.archlinux.org/packages/brave-bin/

pkgname=brave-bin
pkgver=1.1.20
pkgrel=1
epoch=1
pkgdesc="Web browser that blocks ads and trackers by default (binary release)."
arch=("x86_64")
url="https://brave.com/download"
license=("MPL2" "BSD" "custom:chromium")
depends=("gtk3" "nss" "alsa-lib" "libxss" "ttf-font")
optdepends=("cups: Printer support"
            "pepper-flash: Adobe Flash support"
            "libgnome-keyring: Enable GNOME keyring support")
provides=("${pkgname%-bin}" "brave-browser")
conflicts=("${pkgname%-bin}")
source=("$pkgname-$pkgver.zip::https://github.com/brave/brave-browser/releases/download/v${pkgver}/brave-v${pkgver}-linux-x64.zip"
        "$pkgname.sh"
        "brave-browser.desktop"
        "logo.png")
options=(!strip)
sha512sums=("b472daa810174695a7fd3cf6a719b633012b6663071c3de4a953b0a568179cf98931e28e8e0965e4ed404d070c7cdc294792a7522f2ec1ae957e8d69012cf852"
            "2e80e926bba79830cb0e6780d028edfc7a80b5fe81880224c1e2c31329353081f9970ba8755f9003b106a3247b26861f80a3e3ac8731e0bf3c5d515eecca60eb"
            "c21aecaafec43bc1ce1ea3439667efb4c7ea5e54bfa87346a9ae9650de1e90c80174b1610a9216f936f693593816c9585c6be1875b3bd318d067079c06251e92"
            "d7bef52e336bd908d24bf3a084a1fc480831d27a3c80af4c31872465b6a0ce39bdf298e620ae9865526c974465807559cc75610b835e60b4358f65a8a8ff159e")
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
    install -Dm0644 -t "$pkgdir/usr/share/applications" "brave-browser.desktop"
    install -Dm0644 "logo.png" "$pkgdir/usr/share/pixmaps/brave.png"
    LICENSES_DIR="$pkgdir/usr/share/licenses/$pkgname"
    mkdir -p "$LICENSES_DIR"
    mv "$pkgdir/usr/lib/$pkgname/"{LICENSE,LICENSES.chromium.html} "$LICENSES_DIR"
}
