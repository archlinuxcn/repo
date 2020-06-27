# Maintainer: Bruce Zhang
pkgname=postman
pkgver=7.27.1
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
  "postman.desktop"
  "postman.sh"
)
sha1sums=('35194ee810e13d3a21f224c6d46104fc201631c1'
          '7c00d44372bea7447ee8ef2acb03dcbdd3a9a279')
sha1sums_x86_64=('5906723552bbfb7830c9bcd0560961a22a2b0eb7')

package() {
  cd "$srcdir/Postman/app/resources/app"

  # Install Postman app resource
  find . -type f -exec install -Dm644 {} "$pkgdir/usr/share/postman/app/{}" \;

  # Install bin
  install -Dm755 "$srcdir/postman.sh" "$pkgdir/usr/bin/postman"

  # Install desktop
  install -Dm755 "$srcdir/postman.desktop" "$pkgdir/usr/share/applications/postman.desktop"

  # Install icons & EULA
  install -Dm644 "$srcdir/Postman/app/resources/app/assets/icon.png" "$pkgdir/usr/share/icons/hicolor/128x128/apps/postman.png"
  mkdir -p "$pkgdir/usr/share/licenses/postman"
  echo "https://www.postman.com/licenses/postman-eula/" > "$pkgdir/usr/share/licenses/postman/EULA.txt"
}
