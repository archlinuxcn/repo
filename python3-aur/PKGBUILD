#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-aur
pkgver=2018
pkgrel=1
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
  https://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2018.tar.xz
  https://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2018.tar.xz.sig
)
sha512sums=(
  06586fca8a142b72cd248409ce3b1c704b86e1d27ccb1eaeb1f827bbdb875be99257c3b145742737a58d79ceff3339bedef7ff4d0620912f40d90c848dfd6fab
  6a61124d7fccb7237d32e0b400bd7bb9a95d0da562727936594f3e00d9c9116b548a4085e702181fdebd5b7528572133543ed428fd6b51e8d71a906d19a7592f
)
md5sums=(
  bd81004280d0700f4dff01dd4414db72
  e4450a7bd8356fa31bfa726839e996fd
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
