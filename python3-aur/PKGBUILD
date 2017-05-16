#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-aur
pkgver=2017.5
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
  http://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2017.5.tar.xz
  http://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2017.5.tar.xz.sig
)
sha512sums=(
  397f0aebe1d7a20208f431092b40b693d7484f47c645abca936b8a6f486252afc29d2e690bf6e6d6ecf256b69481d4f099b87ab91b5bc5282ecdf69851b09fad
  ab4cdc3ac2056402d22d3551274f27bbb0398ba00d34802ca3815c196a0523d26a50dbb503122d91539b00233b8fafc8d57c3c93bbdbd5567ba4adcbde2f3c22
)
md5sums=(
  9aed1bbcb52c963463910998e25c2f4d
  425357d4a59f5b93553ace93f5a2b01f
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
