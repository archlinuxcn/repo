# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=boxbuddy
_app_id=io.github.dvlv.boxbuddyrs
pkgver=2.2.12
pkgrel=1
pkgdesc="A Graphical Interface for Distrobox"
arch=('x86_64')
url="https://github.com/Dvlv/BoxBuddyRS"
license=('MIT')
depends=('distrobox' 'libadwaita')
makedepends=('cargo')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('1b2495d4525f2ebddc0cef72d424957a67c24953a9da2fed4423aac9cac53a58')

prepare() {
  cd "BoxBuddyRS-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
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
  install -Dm644 "icons/${_app_id}.svg" -t \
    "$pkgdir/usr/share/icons/hicolor/scalable/apps/"
  install -Dm644 icons/build-alt-{symbolic,symbolic-light}.svg -t \
    "$pkgdir/usr/share/icons/hicolor/symbolic/apps/"

  for lang in de_DE el es fr_FR hi it_IT nl_NL pt_BR ru_RU uk_UA zh_CN zh_TW; do
    install -Dm644 "po/${lang}/LC_MESSAGES/${pkgname}rs.mo" -t \
      "$pkgdir/usr/share/locale/${lang}/LC_MESSAGES/"
  done

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
