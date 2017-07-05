#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-aur
pkgver=2017.7
pkgrel=1
pkgdesc='AUR-related modules and helper utilities (aurploader, aurquery, aurtomatic).'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/python3-aur"
depends=(pyalpm python-xdg python3 python3-xcgf python3-xcpf)
optdepends=('curl: Aurploader support' 'git: Clone AUR Git repositories.')
replaces=(aurploader)
conflicts=(aurploader)
provides=(aurploader)
source=(
  http://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2017.7.tar.xz
  http://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2017.7.tar.xz.sig
)
sha512sums=(
  b7274f1df951c79f5f4008fa3bedac66853c7c51d0e305b048d7319952f79dceb4ef38b8f8c3b689a6dae67a551f6a498bcde1d535f998bed8b21bcd0061d541
  2c6cd0ac9d92f9ca16c0003e962afb1304e89265960b50d46012ed4a70e7cd58045bd8d829aa95d4bc01f64de05c182200e33a70aff3b57c8fc935be4472509a
)
md5sums=(
  4b36d653d49c77a7d942677738b770e3
  45454146e5caf7201204f66bec7b2331
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
