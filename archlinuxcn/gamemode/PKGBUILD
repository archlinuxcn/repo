# Maintainer: Ysblokje <ysblokje at gmail dot com>
pkgname=('gamemode')
pkgver=1.5.1
pkgrel=2
pkgdesc="A daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS"
arch=('x86_64')
url="https://github.com/FeralInteractive/gamemode.git"
license=('BSD 3-Clause License (Revised)')
optdepends=('systemd')
depends=('polkit')
makedepends=('meson' 'ninja' 'pkg-config')
source=("https://github.com/FeralInteractive/gamemode/releases/download/$pkgver/$pkgname-$pkgver.tar.xz"
)
sha256sums=('3a5ea5aafe1b7ec69ac2c054198e9aa6b6fd4dd8ee7a8bcfb71d0b0a40313101'
)

build() {
  meson gamemode-$pkgver build --prefix /usr --libexecdir lib/gamemode -Dwith-pam-group=gamemode -Dwith-systemd-user-unit-dir=/usr/lib/systemd/user
  #meson ${_pkgname} build --prefix /usr -Dwith-systemd-user-unit-dir=/usr/lib/systemd/user -Dwith-pam-group=gamemode
  ninja -C build
}

package() {
  DESTDIR=$pkgdir ninja -C build install
  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" ${pkgname}-${pkgver}/LICENSE.txt
  install -m644 -Dt "${pkgdir}/usr/share/doc/${pkgname}/example" ${pkgname}-${pkgver}/example/gamemode.ini
}

