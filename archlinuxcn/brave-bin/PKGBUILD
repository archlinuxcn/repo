# Contributor: Caleb Maclennan <caleb@alerque.com>
# Contributor: Jacob Mischka <jacob@mischka.me>
# Contributor: Manuel Mazzuola <origin.of@gmail.com>
# Contributor: Simón Oroño <simonorono@protonmail.com>
# Contributor: now-im <now im 627 @ gmail . com>
# Contributor: Giusy Digital <kurmikon at libero dot it>
# Mantainer: Andrés Rodríguez <hello@andres.codes>
# https://aur.archlinux.org/packages/brave-bin/

pkgname=brave-bin
pkgver=1.13.82
pkgrel=2
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
        "$pkgname-$pkgver.deb::https://github.com/brave/brave-browser/releases/download/v${pkgver}/brave-browser_${pkgver}_amd64.deb"
        "$pkgname.sh"
        "brave-browser.desktop"
        "logo.png")
options=(!strip)
sha512sums=("c323a38de39e1142566461931fb73237b70e240d758048e2af781b6d112deee72b2dc1f2fbd5b5b2338690e876f579dfbe9aa69d4eb90ca39973432ed62711a8"
            "c9de2a2b4349adc070029661e57035511315384fa3bb36713eb482f6df5c00120635a4478506e63fe15a20bf46fddbf7f6b1b43b0c32f432a6ee9020587939c4"
            "2e80e926bba79830cb0e6780d028edfc7a80b5fe81880224c1e2c31329353081f9970ba8755f9003b106a3247b26861f80a3e3ac8731e0bf3c5d515eecca60eb"
            "137e14b6ff8faf19fcbfc2adcde73a3fb8f6529e9662c8eed04fc4a891073775c20b79c7149fb617465f53b980a8e46114c1c8eb704be7755da8d22a974761dd"
            "d7bef52e336bd908d24bf3a084a1fc480831d27a3c80af4c31872465b6a0ce39bdf298e620ae9865526c974465807559cc75610b835e60b4358f65a8a8ff159e")
noextract=("$pkgname-$pkgver.zip")

prepare() {
  mkdir -p brave
  cat $pkgname-$pkgver.zip | bsdtar -xf- -C brave
  chmod +x brave/brave

  ar x "${pkgname}-${pkgver}.deb"
  tar xvJf data.tar.xz
}

_bsdtardir="brave"

package() {
    install -d -m0755 "$pkgdir/usr/lib"
    cp -a --reflink=auto $_bsdtardir "$pkgdir/usr/lib/$pkgname"
    cp ./opt/brave.com/brave/lib{EGL,GLESv2}.so "$pkgdir/usr/lib/$pkgname"

    install -Dm0755 "$pkgname.sh" "$pkgdir/usr/bin/brave"
    install -Dm0644 -t "$pkgdir/usr/share/applications" "brave-browser.desktop"
    install -Dm0644 "logo.png" "$pkgdir/usr/share/pixmaps/brave.png"
    LICENSES_DIR="$pkgdir/usr/share/licenses/$pkgname"
    mkdir -p "$LICENSES_DIR"
    if [ -f "$pkgdir/usr/lib/$pkgname/LICENSE" ] && [ -f "$pkgdir/usr/lib/$pkgname/LICENSES.chromium.html" ]; then
      mv "$pkgdir/usr/lib/$pkgname/"{LICENSE,LICENSES.chromium.html} "$LICENSES_DIR"
    fi
}
