# Maintainer: George Rawlinson <grawlinson@archlinux.org>

pkgname=lemmy
pkgver=0.18.2
pkgrel=1
pkgdesc='A link aggregator for the fediverse'
arch=('x86_64')
url='https://join-lemmy.org'
license=('AGPL3')
depends=(
  'gcc-libs'
  'openssl'
  'postgresql-libs'
  'imagemagick'
  'ffmpeg'
  'perl-image-exiftool'
)
makedepends=('git' 'rust' 'protobuf')
optdepends=('lemmy-ui: for the web app')
options=('!lto')
_commit='69a7181a29ea01672c61e0190e68b632dfcaf232'
source=(
  "$pkgname::git+https://github.com/LemmyNet/lemmy.git#commit=$_commit"
  'git+https://github.com/LemmyNet/lemmy-translations.git'
)
b2sums=('SKIP' 'SKIP')

pkgver() {
  cd "$pkgname"
  git describe --tags | sed 's/^v//'
}

prepare() {
  cd "$pkgname"

  # setup submodules
  git submodule init
  git config submodule.crates/utils/translations.url ../lemmy-translations
  git -c protocol.file.allow=always submodule update

  # set version
  sed -i "s/unknown version/$pkgver/" crates/utils/src/version.rs

  # download dependencies
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$pkgname"

  cargo build --frozen --release
}

package() {
  cd "$pkgname"

  # binary
  install -vDm755 -t "$pkgdir/usr/bin" target/release/lemmy_server
}
