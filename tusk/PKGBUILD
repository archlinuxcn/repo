# Maintainer: liberodark

pkgname=tusk
pkgver=0.9.2
pkgrel=1
pkgdesc="Refined Evernote desktop app"
arch=('x86_64')
url="https://github.com/champloohq/tusk"
license=('MIT')
depends=('xdg-utils')
source_x86_64=("https://github.com/champloohq/tusk/releases/download/v${pkgver}/tusk_${pkgver}_amd64.deb")
source=($pkgname.desktop
        $pkgname.png)
sha512sums=('33332116be04baff7111b8b10dfb49511649e6f3a6ee9c63af314ad6571d02d4de369691499b6b34aefda2a871467b4a9a517afb699e6d9ae878a445b10b67f0'
         '46afc3aad7d1a518df8abcebe75d7576c9fda3a10f8b046d9e7399ce76e2035e0c1db5abbedc62ff259d10c16630062d74dca93d42f1c3b5b9787146393b76f4')
sha512sums_x86_64=('6261ad9bb46a6ac1b00cc617c5226a8e84b0c35cbaabeb5ef4994415908007ad227d089836b31efe6cc5d431069e006f1a6b56dd2ffd4d8fc6c4e4cab05953ba')
        
package() {
  cd $srcdir
  tar xvf data.tar.xz
  cp -r opt $pkgdir
  install -vDm644 $srcdir/$pkgname.desktop $pkgdir/usr/share/applications/$pkgname.desktop
  install -vDm644 $srcdir/$pkgname.png $pkgdir/usr/share/pixmaps/$pkgname.png
}
