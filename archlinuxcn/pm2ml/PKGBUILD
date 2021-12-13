#Maintainer: Xyne <gro xunilhcra enyx, backwards>
pkgname=pm2ml
pkgver=2021.11.20.1
pkgrel=2
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
  8c651bd924f2d77260addfb8674a18cf45b3b319aecd6dba905509a8fe5493c381e361d9f91aade5537efc8ca022d47fe2c687235cad4b91434c4f8a5d441067
)
md5sums=(
  e03e44428baec1cbdc24561843ad67da
  c281d715d8c56418a2f9bbff91357900
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

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
