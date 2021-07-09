# Maintainer: <peter at typeblog dot net>

pkgname=firefox-pwa
_pkgname="FirefoxPWA"
pkgdesc='A tool to install, manage and use Progressive Web Apps (PWAs) in Mozilla Firefox. (native component)'
pkgver=0.4.0
pkgrel=2
arch=('x86_64')
url="https://github.com/filips123/FirefoxPWA"
license=('MPL2')
depends=('firefox')
makedepends=('rust' 'cargo')
source=("$pkgname-$pkgver.tar.gz::https://github.com/filips123/FirefoxPWA/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('66150de536d167201addf3df5bd3a485eecc9ff2baeeee37ef39fa9cc5953655')

prepare() {
  cd $srcdir/$_pkgname-$pkgver/native
  sed -i -e "s/^version = .*$/version = \"$pkgver\"/" Cargo.toml
  sed -i -e "s/static DISTRIBUTION_VERSION = .*;/static DISTRIBUTION_VERSION = '$pkgver';/" userchrome/profile/chrome/pwa/chrome.jsm
  # Patch to move runtime install directory inside ~/.local/share
  sed -i -e "s@let directory = .*\$@let directory = PathBuf::from(std::env::var(\"HOME\").unwrap()).join(\".local/share/firefoxpwa/runtime\");@" src/components/runtime.rs
}

build() {
  cd $srcdir/$_pkgname-$pkgver/native
  RUSTUP_TOOLCHAIN=stable cargo build --release --target-dir=target
}

package() {
  cd $srcdir/$_pkgname-$pkgver
  install -Dm755 native/target/release/firefoxpwa $pkgdir/usr/bin/firefoxpwa
  install -Dm755 native/target/release/firefoxpwa-connector $pkgdir/usr/libexec/firefoxpwa-connector
  install -Dm644 native/manifests/linux.json $pkgdir/usr/lib/mozilla/native-messaging-hosts/firefoxpwa.json
  mkdir -p $pkgdir/usr/share/firefoxpwa
  cp -r native/userchrome $pkgdir/usr/share/firefoxpwa/
  chmod -R 755 $pkgdir/usr/share/firefoxpwa
}
