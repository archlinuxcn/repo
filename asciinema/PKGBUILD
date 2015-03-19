# Maintainer: Marcin Kulik <m@ku1ik.com>

pkgname=asciinema
pkgver=1.0.0
pkgrel=1
pkgdesc="Record and share your terminal sessions, the right way"
arch=('x86_64' 'i686' 'arm')
url="https://asciinema.org/"
license=('GPLv3')
if [ "$CARCH" = "i686" ]; then
  _PKGARCH=386
  sha1sums=('5dcd871492b6ad00eba3525c558ce4da4fea5e7e')
elif [ "$CARCH" = "arm" ]; then
  _PKGARCH=arm
  sha1sums=('039309270cc2823e8e9e5c6414a72725fdc566f1')
else
  _PKGARCH=amd64
  sha1sums=('98b169230f58bb2c53ac818bf22d364febf823a1')
fi
source=("https://github.com/asciinema/asciinema/releases/download/v${pkgver}/${pkgname}-${pkgver}-linux-${_PKGARCH}.tar.gz")

package() {
  cd ${pkgname}-${pkgver}-linux-${_PKGARCH}

  install -Dm755 ${pkgname} "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
