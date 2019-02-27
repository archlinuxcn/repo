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
pkgver=3.1.35
pkgrel=1
pkgdesc="ACE Stream engine"
arch=("x86_64")
url="http://acestream.org"
license=("unknown")
depends=("openssl-1.0" "net-tools" "python2-setuptools" "python2-xlib" "python2-apsw" "python2-lxml" "python2-typing")
optdepends=("python2-libappindicator: GTK+ gui support")
install="acestream-engine.install"
source=(
  "acestream-engine.service"
  "$pkgname-$pkgver.tar.gz::http://acestream.org/downloads/linux-beta/acestream_${pkgver}_ubuntu_${_ubuntuver}_x86_64.tar.gz"
  "python2-m2crypto-0.24.0.tar.xz::https://archive.archlinux.org/packages/p/python2-m2crypto/python2-m2crypto-0.24.0-4-x86_64.pkg.tar.xz"
)
sha256sums=(
  "b9863a9dd3ee6d41d18475f5f539107fe81a573f45ca1cb98013441f955f1af0"
  "c20f427e635238857eb2c2a8402e3d90690c252f7f187d295fbc038f2a2be001"
  "177c22681be64a7533b3303652da8724aa20edcbead87be90765bc5040f4cff5"
)

package() {
  mkdir -p "$pkgdir/usr/bin"

  sed -i "/ROOT=/c\ROOT=\/opt\/acestream" "$srcdir/start-engine"

  install -Dm755 "$srcdir/acestreamengine" "$pkgdir/opt/acestream/acestreamengine"
  install -Dm755 "$srcdir/start-engine" "$pkgdir/opt/acestream/start-engine"
  install -Dm644 "$srcdir/acestream-engine.service" "$pkgdir/usr/lib/systemd/system/acestream-engine.service"

  cp -a "$srcdir/acestream.conf" "$pkgdir/opt/acestream/acestream.conf"
  cp -a "$srcdir/data" "$srcdir/lib" "$pkgdir/opt/acestream"
  cp -a "$srcdir/usr/lib/python2.7/site-packages/M2Crypto" "$pkgdir/opt/acestream/lib"

  rm "$pkgdir/opt/acestream/lib/m2crypto.egg"
  rm "$pkgdir/opt/acestream/lib/lxml-3.7.2-py2.7-linux-x86_64.egg"

  ln -sf "/opt/acestream/start-engine" "$pkgdir/usr/bin/acestreamengine"
}
