#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-aur
pkgver=2018.8
pkgrel=4
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
  https://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2018.8.tar.xz
  https://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2018.8.tar.xz.sig
)
sha512sums=(
  91327fbb8ea85ffa757e9c6e5eac2b726826b266e2ef104291d6f1f7eae5b7cce2564fc9ebf8689eea262f675a6df2cb38efe717f21f607aeb6042bc2361a610
  ad3a8c506220c594ab6eb0dbcb6adef09e1659ee39325414e45debfbc9b482022e8006861c511458a81fa9e2b145d7fa088b35cebc76806bbf2cd804395e6865
)
md5sums=(
  bec3b4e2d7b655f89417f52a09f63439
  354ee94fc3f8e75d2772ab0939da3660
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  for aurfoo in aur*
  do
    if [[ -x $aurfoo ]]
    then
      install -Dm755 "$aurfoo" "$pkgdir/usr/bin/$aurfoo"
    fi
  done
}


# vim: set ts=2 sw=2 et:
