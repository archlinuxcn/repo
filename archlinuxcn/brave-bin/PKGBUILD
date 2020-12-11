# Contributor: Caleb Maclennan <caleb@alerque.com>
# Contributor: Jacob Mischka <jacob@mischka.me>
# Contributor: Manuel Mazzuola <origin.of@gmail.com>
# Contributor: Simón Oroño <simonorono@protonmail.com>
# Contributor: now-im <now im 627 @ gmail . com>
# Contributor: Giusy Digital <kurmikon at libero dot it>
# Mantainer: Andrés Rodríguez <hello@andres.codes>
# https://aur.archlinux.org/packages/brave-bin/

pkgname=brave-bin
pkgver=1.18.70
pkgrel=1
epoch=1
pkgdesc="Web browser that blocks ads and trackers by default (binary release)."
arch=("x86_64")
url="https://brave.com/download"
license=("MPL2" "BSD" "custom:chromium")
depends=("gtk3" "nss" "alsa-lib" "libxss" "ttf-font")
optdepends=("cups: Printer support"
            "pepper-flash: Adobe Flash support"
            "libgnome-keyring: Enable GNOME keyring support"
            "libnotify: Native notification support")
provides=("${pkgname%-bin}" "brave-browser")
conflicts=("${pkgname%-bin}")
source=("$pkgname-$pkgver.zip::https://github.com/brave/brave-browser/releases/download/v${pkgver}/brave-browser-${pkgver}-linux-amd64.zip"
        "$pkgname.sh"
        "brave-browser.desktop"
        "logo.png")
options=(!strip)
sha512sums=("56967c64ad05f26344ee221d498400bc08a17a7602b9b23fc0a33d75c1db6ed314f6a9529e646a7f0ada871a3721616f63bdcefce24c77e0df1ad17495bdf681"
            "ff99db6b5673846f4ec0daf0ec60535921166f6185131d8d966452452393580f655c421e7ad5889f5a6f6cb3f1e76e7908d711aa003ee37a1ae50774371a8b53"
            "137e14b6ff8faf19fcbfc2adcde73a3fb8f6529e9662c8eed04fc4a891073775c20b79c7149fb617465f53b980a8e46114c1c8eb704be7755da8d22a974761dd"
            "d7bef52e336bd908d24bf3a084a1fc480831d27a3c80af4c31872465b6a0ce39bdf298e620ae9865526c974465807559cc75610b835e60b4358f65a8a8ff159e")
noextract=("$pkgname-$pkgver.zip")

prepare() {
  mkdir -p brave
  bsdtar -xf $pkgname-$pkgver.zip -C brave
  chmod +x brave/brave
}

_bsdtardir="brave"

package() {
    install -d -m0755 "$pkgdir/usr/lib"
    cp -a --reflink=auto $_bsdtardir "$pkgdir/usr/lib/$pkgname"

    # allow firejail users to get the suid sandbox working
    chmod 4755 $pkgdir/usr/lib/brave-bin/chrome-sandbox

    install -Dm0755 "$pkgname.sh" "$pkgdir/usr/bin/brave"
    install -Dm0644 -t "$pkgdir/usr/share/applications" "brave-browser.desktop"
    install -Dm0644 "logo.png" "$pkgdir/usr/share/pixmaps/brave.png"
    LICENSES_DIR="$pkgdir/usr/share/licenses/$pkgname"
    mkdir -p "$LICENSES_DIR"
    if [ -f "$pkgdir/usr/lib/$pkgname/LICENSE" ] && [ -f "$pkgdir/usr/lib/$pkgname/LICENSES.chromium.html" ]; then
      mv "$pkgdir/usr/lib/$pkgname/"{LICENSE,LICENSES.chromium.html} "$LICENSES_DIR"
    fi
}
