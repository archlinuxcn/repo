# Maintainer: Ariel AxionL <axionl@aosc.io>

pkgname=('zafiro-icon-theme')
pkgver=0.7.4
pkgrel=2
pkgdesc="A icon pack flat with light colors."
arch=('any')
url="https://github.com/zayronxio/Zafiro-icons"
license=('Artistic2.0')
source=("https://github.com/zayronxio/Zafiro-icons/archive/v$pkgver.tar.gz")
sha256sums=('c6e1f37a6bf0c3e0d06d7e4f8472cbe63e8e265c5d3a68cd5ccee58ad39d6a69')

package() {
  install -dm 755 $pkgdir/usr/share/icons
  dir=$srcdir/Zafiro-icons-$pkgver
  install -Dm644 $dir/LICENSE.md $pkgdir/usr/share/licenses/$pkgname/LICENSE

  cp -dr --no-preserve='ownership' $dir $pkgdir/usr/share/icons/$pkgname
}

# vim: ts=2 sw=2 et:
