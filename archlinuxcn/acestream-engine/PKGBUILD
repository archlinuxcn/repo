# Maintainer: Jonian Guveli <jonian@hardpixel.eu>
# Contributor: Jan Magnus Brevik <janmbrevik@gmail.com>
# Contributor: Rubén Fdes Moreira <tmp-meteque@openmailbox.com>
# Contributor: Sigmund Vestergaard <sigmundv@gmail.com>
# Contributor: MacCyber <jonas.enge@gmail.com>
# Contributor: Doug Newgard <scimmia22@outlook.com>
# Contributor: Jonas Heinrich <onny@project-insanity.org>
# Contributor: Antti Hautaniemi <an7oine@me.com>

_ubuntuver=18.04
pkgname=acestream-engine
pkgver=3.1.49
pkgrel=1
pkgdesc="ACE Stream engine"
arch=("x86_64")
url="http://acestream.org"
license=("unknown")
depends=("openssl-1.0" "net-tools" "python2-setuptools" "python2-xlib" "python2-apsw")
optdepends=("python2-libappindicator: GTK+ gui support")
install="acestream-engine.install"
source=(
  "acestream-engine.service"
  "$pkgname-$pkgver.tar.gz::http://acestream.org/downloads/linux/acestream_${pkgver}_ubuntu_${_ubuntuver}_x86_64.tar.gz"
)
sha256sums=(
  "b9863a9dd3ee6d41d18475f5f539107fe81a573f45ca1cb98013441f955f1af0"
  "d2ed7bdc38f6a47c05da730f7f6f600d48385a7455d922a2688f7112202ee19e"
)

package() {
  mkdir -p "$pkgdir/usr/bin"

  sed -i "/ROOT=/c\ROOT=\/opt\/acestream" "$srcdir/start-engine"

  install -Dm755 "$srcdir/acestreamengine" "$pkgdir/opt/acestream/acestreamengine"
  install -Dm755 "$srcdir/start-engine" "$pkgdir/opt/acestream/start-engine"
  install -Dm644 "$srcdir/acestream-engine.service" "$pkgdir/usr/lib/systemd/system/acestream-engine.service"

  cp -a "$srcdir/acestream.conf" "$pkgdir/opt/acestream/acestream.conf"
  cp -a "$srcdir/data" "$srcdir/lib" "$pkgdir/opt/acestream"

  ln -sf "/opt/acestream/start-engine" "$pkgdir/usr/bin/acestreamengine"
}
