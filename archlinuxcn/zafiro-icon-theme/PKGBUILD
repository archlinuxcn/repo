# Maintainer: Ariel AxionL <axionl@aosc.io>

pkgname=('zafiro-icon-theme')
pkgver=0.8.4
pkgrel=1
pkgdesc="A icon pack flat with light colors."
arch=('any')
url="https://github.com/zayronxio/Zafiro-icons"
license=('Artistic2.0')
source=("https://github.com/zayronxio/Zafiro-icons/archive/v$pkgver.tar.gz")
sha256sums=('a01375ca5b03dba0f8a2729cfa0968ffcaf28250edd17bd254f068cbacfd007f')

package() {
  install -dm 755 $pkgdir/usr/share/icons
  dir=$srcdir/Zafiro-icons-$pkgver
  install -Dm644 $dir/LICENSE.md $pkgdir/usr/share/licenses/$pkgname/LICENSE

  cp -dr --no-preserve='ownership' $dir $pkgdir/usr/share/icons/$pkgname
}

# vim: ts=2 sw=2 et:
