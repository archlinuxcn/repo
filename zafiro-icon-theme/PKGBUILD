# Maintainer: Ariel AxionL <axionl@aosc.io>

pkgname=('zafiro-icon-theme')
pkgver=0.8.2
pkgrel=1
pkgdesc="A icon pack flat with light colors."
arch=('any')
url="https://github.com/zayronxio/Zafiro-icons"
license=('Artistic2.0')
source=("https://github.com/zayronxio/Zafiro-icons/archive/v$pkgver.tar.gz")
sha256sums=('6150f7eb0f69438fd0d41c0b63277b7346d67fba49a6c0ba3380520d3bab0788')

package() {
  install -dm 755 $pkgdir/usr/share/icons
  dir=$srcdir/Zafiro-icons-$pkgver
  install -Dm644 $dir/LICENSE.md $pkgdir/usr/share/licenses/$pkgname/LICENSE

  cp -dr --no-preserve='ownership' $dir $pkgdir/usr/share/icons/$pkgname
}

# vim: ts=2 sw=2 et:
