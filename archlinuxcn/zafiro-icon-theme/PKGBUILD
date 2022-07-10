# Maintainer: Ariel AxionL <axionl@aosc.io>

pkgname=('zafiro-icon-theme')
pkgver=1.3
pkgrel=1
pkgdesc="A icon pack flat with light colors."
arch=('any')
url="https://github.com/zayronxio/Zafiro-icons"
license=('GPL3')
source=("https://github.com/zayronxio/Zafiro-icons/archive/$pkgver.tar.gz")
sha256sums=('d4e81453d050ae07b157c65e388e748639a711afc1a6d1b033bdfdd90230ecb7')

package() {
  install -dm 755 $pkgdir/usr/share/icons
  dir=$srcdir/Zafiro-icons-$pkgver
  install -Dm644 $dir/LICENSE.md $pkgdir/usr/share/licenses/$pkgname/LICENSE

  cp -dr --no-preserve='ownership' $dir $pkgdir/usr/share/icons/$pkgname
}

# vim: ts=2 sw=2 et:
