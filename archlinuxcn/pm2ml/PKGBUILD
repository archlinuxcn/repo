#Maintainer: Xyne <gro xunilhcra enyx, backwards>
pkgname=pm2ml
pkgver=2021.11.20.1
pkgrel=4
pkgdesc='Generate metalinks for downloading Pacman packages and databases.'
arch=(any)
license=(GPL)
url="https://xyne.dev/projects/pm2ml"
depends=(pyalpm python3 python3-xcgf python3-xcpf)
optdepends=('aria2: ppl script support.' 'python3-aur: AUR support' 'reflector: Reflector support')
backup=(etc/ppl.conf)
source=(
  https://xyne.dev/projects/pm2ml/src/pm2ml-2021.11.20.1.tar.xz
  https://xyne.dev/projects/pm2ml/src/pm2ml-2021.11.20.1.tar.xz.sig
)
sha512sums=(
  293cc288509ffc57c232e67e6c99e5de57a259440705ee239b1741f07f39cbdafbc8fa0e17cc9c3d22cf544fcebd3f46c4811e00070d9f0865ea687288dcab07
  e2f384bc6eb32aeba8d8a533e200aa9d307a50680fc95cecaefdba0143446ea13716b7a2eea7079a3fba78cb1cb613c93a9b6265c2dc07f5cafab51747979d5d
)
md5sums=(
  e03e44428baec1cbdc24561843ad67da
  dd861a7b1bef4d6b4b9f93a313d688fc
)
validpgpkeys=('D89FAAEB4CECAFD199A2F5E612C6F735F7A9A519')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  for foo_ in ppl pplsyu ppls; do
    install -Dm755 "$foo_" "$pkgdir/usr/bin/$foo_"
  done
  install -Dm644 "ppl.conf" "$pkgdir/etc/ppl.conf"
}

# vim: set ts=2 sw=2 et:
