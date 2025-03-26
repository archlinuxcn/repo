# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=boxbuddy
_app_id=io.github.dvlv.boxbuddyrs
pkgver=2.5.3
pkgrel=1
pkgdesc="A Graphical Interface for Distrobox"
arch=('x86_64')
url="https://www.dvlv.co.uk/BoxBuddyRS"
license=('MIT')
depends=('distrobox' 'libadwaita')
makedepends=('cargo')
source=("$pkgname-$pkgver.tar.gz::https://github.com/Dvlv/BoxBuddyRS/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('c88d36069beb774287eeed6331827b2e06a87c1cd8017d3b4d24a6dd556c8684')

prepare() {
  cd "BoxBuddyRS-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"

  # Correct paths
  sed -i 's|{data_home}/locale|/usr/share/locale|g' src/utils.rs
  sed -i 's|{data_home}/icons|/usr/share/icons|g' src/utils.rs
}

build() {
  cd "BoxBuddyRS-$pkgver"

  # Use system gettext as gettext-sys crate fails with LTO enabled
  export GETTEXT_SYSTEM=true

  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release --all-features
}

check() {
  cd "BoxBuddyRS-$pkgver"
  appstreamcli validate --no-net "${_app_id}.metainfo.xml"
  desktop-file-validate "${_app_id}.desktop"
}

package() {
  cd "BoxBuddyRS-$pkgver"
  install -Dm755 "target/release/$pkgname-rs" -t "$pkgdir/usr/bin/"
  install -Dm644 "${_app_id}.desktop" -t "$pkgdir/usr/share/applications/"
  install -Dm644 "${_app_id}.gschema.xml" -t "$pkgdir/usr/share/glib-2.0/schemas/"
  install -Dm644 "${_app_id}.metainfo.xml" -t "$pkgdir/usr/share/metainfo/"
  install -Dm644 icons/*.svg -t "$pkgdir/usr/share/icons/$pkgname/"
  install -d "$pkgdir/usr/share/icons/hicolor/scalable/apps"
  ln -s "/usr/share/icons/$pkgname/${_app_id}.svg" \
    "$pkgdir/usr/share/icons/hicolor/scalable/apps/"

  pushd po
  for lang in $(ls -d */); do
    install -Dm644 "${lang%%/}/LC_MESSAGES/${pkgname}rs.mo" -t \
      "$pkgdir/usr/share/locale/${lang%%/}/LC_MESSAGES/"
  done
  popd

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
