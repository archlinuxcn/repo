# Maintainer: Ariel AxionL <axionl@aosc.io>

pkgname=('zafiro-icon-theme')
pkgver=1.0
pkgrel=4
pkgdesc="A icon pack flat with light colors."
arch=('any')
url="https://github.com/zayronxio/Zafiro-icons"
license=('GPL3')
source=("https://github.com/zayronxio/Zafiro-icons/archive/$pkgver.tar.gz")
sha256sums=('9824bff36a6374d5a3967932a4fe2de00fecf1370dda148944b0bfc2abcc2ae8')

package() {
  install -dm 755 $pkgdir/usr/share/icons
  dir=$srcdir/Zafiro-icons-$pkgver
  install -Dm644 $dir/LICENSE.md $pkgdir/usr/share/licenses/$pkgname/LICENSE

  cp -dr --no-preserve='ownership' $dir $pkgdir/usr/share/icons/$pkgname
}

# vim: ts=2 sw=2 et:
