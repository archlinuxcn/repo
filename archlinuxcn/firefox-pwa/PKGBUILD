# Maintainer: filips <projects at filips dot si>
# Maintainer: Peter Cai <peter at typeblog dot net>
# Contributor: TheFool <rn6l05d28@relay.firefox.com>

# This file is automatically updated/generated on every package release
# Any changes made directly to the AUR repository will be overwritten
# Please contribute changes to the main GitHub repository instead
# See: https://github.com/filips123/FirefoxPWA/blob/main/native/packages/aur/firefox-pwa/PKGBUILD

_pkgname="FirefoxPWA"
pkgname="firefox-pwa"
pkgdesc="A tool to install, manage and use Progressive Web Apps (PWAs) in Mozilla Firefox (native component)"
pkgver="1.1.0"
pkgrel=1
url="https://github.com/filips123/FirefoxPWA"
arch=("x86_64" "i686")
license=("MPL2")

makedepends=("rust" "cargo")
optdepends=("firefox: Support for browser extension")
install=package.install

source=("$pkgname-$pkgver.tar.gz::https://github.com/filips123/FirefoxPWA/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('e3a18c742cc44d0ffde698753182733da75bfe9a2e331efddeb133c479108328')
b2sums=('379263387c9ebefe44173d3159ebc1ec31c5363437e51d0001aee8ad7f97745a3ed901f825829ce1e6ed2f143ef4ae352e88e04b038c9eb84fe0693e6af8f31c')

prepare() {
    cd $srcdir/$_pkgname-$pkgver/native/

    # Set the correct version in source files
    sed -i "s/version = \"0.0.0\"/version = \"$pkgver\"/g" Cargo.toml
    sed -i "s/DISTRIBUTION_VERSION = '0.0.0'/DISTRIBUTION_VERSION = '$pkgver'/g" userchrome/profile/chrome/pwa/chrome.jsm

    # We don't use libexec on Arch
    sed -i "s@/usr/libexec/firefoxpwa-connector@/usr/lib/firefoxpwa/firefoxpwa-connector@g" manifests/linux.json
}

build() {
    cd $srcdir/$_pkgname-$pkgver/native/
    RUSTUP_TOOLCHAIN=stable cargo build --release
}

check() {
    cd $srcdir/$_pkgname-$pkgver/native/
    [ "$(./target/release/firefoxpwa --version)" == "firefoxpwa $pkgver" ]
}

package() {
    cd $srcdir/$_pkgname-$pkgver/native/

    # Executables
    install -Dm755 target/release/firefoxpwa $pkgdir/usr/bin/firefoxpwa
    install -Dm755 target/release/firefoxpwa-connector $pkgdir/usr/lib/firefoxpwa/firefoxpwa-connector

    # Manifest
    install -Dm644 manifests/linux.json $pkgdir/usr/lib/mozilla/native-messaging-hosts/firefoxpwa.json

    # Completions
    install -Dm755 target/release/completions/firefoxpwa.bash $pkgdir/usr/share/bash-completion/completions/firefoxpwa
    install -Dm755 target/release/completions/firefoxpwa.fish $pkgdir/usr/share/fish/completions/firefoxpwa.fish
    install -Dm755 target/release/completions/_firefoxpwa $pkgdir/usr/share/zsh/vendor-completions/_firefoxpwa

    # Documentation
    install -Dm644 ../README.md $pkgdir/usr/share/doc/firefoxpwa/README.md
    install -Dm644 ../native/README.md $pkgdir/usr/share/doc/firefoxpwa/README-NATIVE.md
    install -Dm644 ../extension/README.md $pkgdir/usr/share/doc/firefoxpwa/README-EXTENSION.md
    install -Dm644 packages/debian/copyright $pkgdir/usr/share/doc/firefoxpwa/copyright

    # UserChrome
    mkdir -p $pkgdir/usr/share/firefoxpwa/userchrome/
    cp -r userchrome/* $pkgdir/usr/share/firefoxpwa/userchrome/
}
