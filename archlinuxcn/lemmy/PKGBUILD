# Maintainer: George Rawlinson <grawlinson@archlinux.org>

pkgname=lemmy
pkgver=0.18.3
pkgrel=3
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
optdepends=(
  'lemmy-ui: for the web app'
  'pict-rs: for image hosting backend'
)
backup=('etc/lemmy/lemmy.hjson')
options=('!lto')
_commit='9ef4da19fc12c9d6963e1d1746dad44bdb40407c'
source=(
  "$pkgname::git+https://github.com/LemmyNet/lemmy.git#commit=$_commit"
  'git+https://github.com/LemmyNet/lemmy-translations.git'
  'systemd.service'
  'sysusers.conf'
  'tmpfiles.conf'
)
b2sums=('SKIP'
        'SKIP'
        'cb348364c053a525b55c026af5046ca7cd029dc6a890fa2621578e03e12462c85c31e268977d1e40fdd0945e8ea9b1355bc40fc03741a3792a07a7a814efd750'
        'f736c1415e98be9f69451d49fca3c7804dd05ef1b3d7537b787dbd004094662346605911377bf63260d3fa90eeed2a075e3b890b5496995a3f9e4a99792d8389'
        'f57297e6a82193b192dfee8d506751375a2487bbf644d15a7deaa019891dd53fcb5e1268c09ae805605cd68097ee006e62887dce2564beb7a2736b7769217650')

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
  # systemd integration
  install -vDm644 systemd.service "$pkgdir/usr/lib/systemd/system/lemmy.service"
  install -vDm644 sysusers.conf "$pkgdir/usr/lib/sysusers.d/lemmy.conf"
  install -vDm644 tmpfiles.conf "$pkgdir/usr/lib/tmpfiles.d/lemmy.conf"
  install -vDm644 "$pkgname/config/config.hjson" "$pkgdir/etc/lemmy/lemmy.hjson"

  cd "$pkgname"

  # binary
  install -vDm755 -t "$pkgdir/usr/bin" target/release/lemmy_server
}
