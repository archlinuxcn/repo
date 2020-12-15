#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-aur
pkgver=2020.12.15
pkgrel=3
pkgdesc='AUR-related modules and helper utilities (aurploader, aurquery, aurtomatic).'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/python3-aur"
depends=(pyalpm python-xdg python3 python3-xcgf python3-xcpf)
optdepends=('curl: Aurploader support' 'git: Clone AUR Git repositories.')
replaces=(aurploader)
conflicts=(aurploader)
provides=(aurploader)
source=(
  https://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2020.12.15.tar.xz
  https://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2020.12.15.tar.xz.sig
)
sha512sums=(
  05cba4c05937b8722b061fb24a32548c6f04fa04966449fd238eb991bea2ed30905ae60567802922810ebba87febfeb0d5c4b34a27e63e33dbda764bbafa17aa
  2676a6b1ba8a383cade9065ba1c5d82ab445fe1bb1e0dcd7e103967a65f7d39fee9a8b101a7e2ee7b89e38f97dad3bca6e88784539e3717ffd15dc5935f40d33
)
md5sums=(
  bf033724fee5dcfc13634cbd3aa833f3
  24d339085b082c49a6078d7483a13c9d
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}


# vim: set ts=2 sw=2 et:
