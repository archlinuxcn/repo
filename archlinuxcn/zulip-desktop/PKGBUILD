# Maintainer: Eric Engestrom <aur [at] engestrom [dot] ch>
# Maintainer: Jean Lucas <jean@4ray.co>
# Maintainer: AI5C <ai5c@ai5c.com>
# Contributor: kaptoxic <kaptoxic at yahoo dot com>
# Contributor: Matthew Avant <matthew dot avant at gmail dot com>
# Contributor: Rose Ames <rose at happyspork dot com>

pkgname=zulip-desktop
pkgver=5.6.0
pkgrel=1
pkgdesc='Real-time team chat based on the email threading model'
arch=(i686 x86_64)
url=https://zulipchat.com
license=(Apache)
depends=(libxkbfile gtk3 libxss nss)
makedepends=(npm python2)
source=($pkgname-$pkgver.tar.gz::https://github.com/zulip/$pkgname/archive/v$pkgver.tar.gz
        $pkgname.desktop)
sha512sums=('5ee0bb198bb46c063af0f1e24ca531cfafe7928fd68aa2f43f1b90bbe81b4c5128bf6b7b2f61357dc53a0606ba9e45794bf83920e3d44f3c70db8828d8b160d8'
            '7696a6874d17957f99452452723ae1a6b32b6814b018361a71ed1fe0191e1c6da6f3ad693e2e279615e74f687c380ff2f6dab8b69fcd82476e8f33b56a6b4cb5')

build() {
  cd $pkgname-$pkgver
  npm i
  npm run pack
}

package() {
  cd $pkgname-$pkgver

  install -d "$pkgdir"/usr/{lib,bin}
  cp -a dist/linux-unpacked "$pkgdir"/usr/lib/$pkgname
  ln -s /usr/lib/$pkgname/zulip "$pkgdir"/usr/bin

  install -Dm 644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname

  install -Dm 644 ../$pkgname.desktop -t "$pkgdir"/usr/share/applications
  for i in 16 24 32 48 64 96 128 256 512; do
    install -Dm 644 build/icons/${i}x${i}.png \
      "$pkgdir"/usr/share/icons/hicolor/${i}x${i}/apps/zulip.png
  done
}
