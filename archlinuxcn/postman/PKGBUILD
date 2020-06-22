# Maintainer: Bruce Zhang
pkgname=postman
pkgver=7.27.0
pkgrel=1
pkgdesc='Build, test, and document your APIs faster'
arch=('x86_64')
url='https://www.getpostman.com/downloads/'
license=('custom:Postman EULA')
depends=('electron7')
provides=('postman')
conflicts=('postman-bin')
options=('!strip')
source_x86_64=(
  "$pkgname-$pkgver-x86_64.orig.tar.gz::https://dl.pstmn.io/download/version/$pkgver/linux64"
)
source=(
  "EULA.html::https://www.postman.com/licenses/postman-eula/"
  "postman.desktop"
  "postman.sh"
)
sha1sums=('bf9869d5f1743437a41dd439ab632455b3c39083'
          '35194ee810e13d3a21f224c6d46104fc201631c1'
          '7c00d44372bea7447ee8ef2acb03dcbdd3a9a279')
sha1sums_x86_64=('4984975019591580adf44242526549fe914cf51c')

package() {
  cd "$srcdir/Postman/app/resources/app"

  # Install Postman app resource
  find . -type f -exec install -Dm644 {} "$pkgdir/usr/share/postman/app/{}" \;

  # Install bin
  install -Dm755 "$srcdir/postman.sh" "$pkgdir/usr/bin/postman"

  # Install desktop
  install -Dm755 "$srcdir/postman.desktop" "$pkgdir/usr/share/applications/postman.desktop"

  # Install icons & eula
  install -Dm644 "$srcdir/Postman/app/resources/app/assets/icon.png" "$pkgdir/usr/share/icons/hicolor/128x128/apps/postman.png"
  install -Dm644 "$srcdir/EULA.html" "$pkgdir/usr/share/licenses/postman/EULA.html"
}
