#Maintainer: Xyne <gro xunilhcra enyx, backwards>
pkgname=python3-aur
pkgver=2021.11.20.1
pkgrel=2
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
  8a1a379c570ad0871be150bfe87ff659436f9cee4944805c0cb70630aba7f3c0bc797a590ccab2951fce84f09c5fc0e3eda8764bf5bb1b37b06080aa7bfbe38e
)
md5sums=(
  5d42d70c86aa9c717d92065d63c38d43
  ddb7ac1121dccf06f8a33d2633873c0b
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}


# vim: set ts=2 sw=2 et:
