# Maintainer: Peter Cai <peter at typeblog dot net>
# Contributor: TheFool <rn6l05d28@relay.firefox.com>

pkgname=firefox-pwa
_pkgname="FirefoxPWA"
pkgdesc='A tool to install, manage and use Progressive Web Apps (PWAs) in Mozilla Firefox. (native component)'
pkgver=0.4.1
pkgrel=1
arch=('x86_64')
url="https://github.com/filips123/FirefoxPWA"
license=('MPL2')
provides=('firefoxpwa')
conflicts=('firefoxpwa')
depends=('firefox')
makedepends=('rust' 'cargo')
install=firefox-pwa.install
source=("$pkgname-$pkgver.tar.gz::https://github.com/filips123/FirefoxPWA/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('5d8b61c3d831063a0ba4b3ffc78e10f3513c3269af4833b51bc7ab1a818becd4')

prepare() {
  cd $srcdir/$_pkgname-$pkgver/native
  sed -i -e "s/^version = .*$/version = \"$pkgver\"/" Cargo.toml
  sed -i -e "s/static DISTRIBUTION_VERSION = .*;/static DISTRIBUTION_VERSION = '$pkgver';/" userchrome/profile/chrome/pwa/chrome.jsm
  # Patch to move runtime install directory inside ~/.local/share
  sed -i -e "s@let directory = .*\$@let directory = PathBuf::from(std::env::var(\"HOME\").unwrap()).join(\".local/share/firefoxpwa/runtime\");@" src/components/runtime.rs
  # We don't use libexec on Arch
  sed -i "s@/usr/libexec/firefoxpwa-connector@/usr/lib/firefoxpwa/firefoxpwa-connector@g" manifests/linux.json
}

build() {
  cd $srcdir/$_pkgname-$pkgver/native
  RUSTUP_TOOLCHAIN=stable cargo build --release --target-dir=target
}

package() {
  cd $srcdir/$_pkgname-$pkgver
  install -Dm755 native/target/release/firefoxpwa $pkgdir/usr/bin/firefoxpwa
  install -Dm755 native/target/release/firefoxpwa-connector $pkgdir/usr/lib/firefoxpwa/firefoxpwa-connector
  install -Dm644 native/manifests/linux.json $pkgdir/usr/lib/mozilla/native-messaging-hosts/firefoxpwa.json
  mkdir -p $pkgdir/usr/share/firefoxpwa
  cp -r native/userchrome $pkgdir/usr/share/firefoxpwa/
  chmod -R 755 $pkgdir/usr/share/firefoxpwa
}
