# Maintainer: Xuanwo <xuanwo@archlinuxcn.org>
pkgname=tikv
pkgver=2.1.2
pkgrel=1
pkgdesc='Distributed transactional key-value database, originally created to complement TiDB'
makedepends=('go' 'make' 'rustup' 'awk' 'cmake' 'gcc')
arch=('x86_64')
url='https://github.com/tikv/tikv'
license=('Apache')
provides=('tikv-server')
backup=(etc/tikv/tikv.toml)
depends=('tikv-pd')
source=(tikv-${pkgver}.tar.gz::https://github.com/tikv/tikv/archive/v${pkgver}.tar.gz
        tikv.service
        tikv-sysusers.conf
        tikv-tmpfiles.conf
        tikv.toml)
sha256sums=('f2094871aa8c66337befef9e723677106d52f736ff2913246081b02725dbce0b'
            '870b8eaf83bc0d22b05b0f3a7890660e483cf77bb1d84bc50ad04fb23068cd8c'
            '744b252e29099b0099dc41e30bc3badd33b3d661c7126af8044faa4fc2df8927'
            '935291bac6a216c6f880df9bfaec8900266413bb202ac483e79f291e1f28e9f1'
            '248790d756d15322ed7af13f30525744c472190ac68a26b486c5eed24427abdf')

prepare() {
    cd tikv-${pkgver}
    rustup component add rustfmt-preview
}

build() {
    cd tikv-${pkgver}
    cargo build --release --features "portable sse no-fail"
}

package() {
  # Install binary
  install -Dm755 "$srcdir/tikv-${pkgver}/target/release/tikv-ctl" "$pkgdir/usr/bin/tikv-ctl"
  install -Dm755 "$srcdir/tikv-${pkgver}/target/release/tikv-server" "$pkgdir/usr/bin/tikv-server"
  install -Dm755 "$srcdir/tikv-${pkgver}/target/release/tikv-importer" "$pkgdir/usr/bin/tikv-importer"
  # Install systemd service
  install -Dm644 "$srcdir/tikv.service" "$pkgdir/usr/lib/systemd/system/tikv.service"
  # Install sysusers
  install -Dm644 "$srcdir/tikv-sysusers.conf" "$pkgdir/usr/lib/sysusers.d/tikv.conf"
  # Install tmpfiles
  install -Dm644 "$srcdir/tikv-tmpfiles.conf" "$pkgdir/usr/lib/tmpfiles.d/tikv.conf"
  # Install default config
  install -Dm644 tikv.toml "$pkgdir/etc/tikv/tikv.toml"
}

# vim: ft=sh syn=sh et
