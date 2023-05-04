#Maintainer: Xyne <gro xunilhcra enyx, backwards>
pkgname=python3-aur
pkgver=2021.11.20.1
pkgrel=4
pkgdesc='AUR-related modules and helper utilities (aurploader, aurquery, aurtomatic).'
arch=(any)
license=(GPL)
url="https://xyne.dev/projects/python3-aur"
depends=(pyalpm python-pyxdg python3 python3-xcgf python3-xcpf)
optdepends=('curl: Aurploader support' 'git: Clone AUR Git repositories.')
replaces=(aurploader)
conflicts=(aurploader)
provides=(aurploader)
source=(
  https://xyne.dev/projects/python3-aur/src/python3-aur-2021.11.20.1.tar.xz
  https://xyne.dev/projects/python3-aur/src/python3-aur-2021.11.20.1.tar.xz.sig
)
sha512sums=(
  3224921db2fceb34d709d42ca4551419960749130a9a7b09584547257fb00c3eab1b30a335526670e0427f5ae06d641f80c6bad71def5869abf29116ed5bbc64
  cd1ed420aa8ba4948301007cc114f738c177c293731979c32a58c1fc5b131adbfc5c70482a2d98137c48a4654159f2e842061f300e97c0e06decfff2bcdcca55
)
md5sums=(
  5d42d70c86aa9c717d92065d63c38d43
  e002ab0bf32ae781eb45b31cf3275834
)
validpgpkeys=('D89FAAEB4CECAFD199A2F5E612C6F735F7A9A519')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}


# vim: set ts=2 sw=2 et:
