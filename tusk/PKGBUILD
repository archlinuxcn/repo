# Maintainer: Hugo Barrera <hugo@barrera.io>
# Contributor: liberodark

pkgname=tusk
pkgver=0.11.0
pkgrel=2
pkgdesc="Refined Evernote desktop app"
arch=('x86_64')
url="https://github.com/champloohq/tusk"
license=('MIT')
depends=('xdg-utils')
source=("https://github.com/champloohq/tusk/releases/download/v${pkgver}/tusk_${pkgver}_amd64.deb"
        $pkgname.desktop
        $pkgname.png)
sha512sums=('46a92855835b0155a2ea69d9f9c8644770027959770afdc0de4dade8745bf3d4b4f7b3a21e45ce8a28e7d7603256dc5ebf77491de7bfc9777792a998a3ad56b1'
            '33332116be04baff7111b8b10dfb49511649e6f3a6ee9c63af314ad6571d02d4de369691499b6b34aefda2a871467b4a9a517afb699e6d9ae878a445b10b67f0'
            '46afc3aad7d1a518df8abcebe75d7576c9fda3a10f8b046d9e7399ce76e2035e0c1db5abbedc62ff259d10c16630062d74dca93d42f1c3b5b9787146393b76f4')

package() {
  cd $srcdir
  tar xvf data.tar.xz
  cp -r opt $pkgdir
  install -vDm644 $srcdir/$pkgname.desktop $pkgdir/usr/share/applications/$pkgname.desktop
  install -vDm644 $srcdir/$pkgname.png $pkgdir/usr/share/pixmaps/$pkgname.png

  mkdir -p "$pkgdir/usr/bin/"
  ln -sf "/opt/Tusk/tusk-app" "$pkgdir/usr/bin/tusk-app"
}
