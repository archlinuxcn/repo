#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-aur
pkgver=2020
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
  https://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2020.tar.xz
  https://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2020.tar.xz.sig
)
sha512sums=(
  1c95def0c8eecd59e925408c53d737775d39882dcdea66a95fc05377ac02fbc136a700d12c2715b0a59307269881537b6e00fdfd1065fcb835f3319860dd4342
  9e021b93e19ee6e784e4855eca9c521513abc1f82698ed8ae62efc605c5abeddec79f25a4bd6670e3791c2608f36c4b899eb0b8b65118cfbc13f4371476217f7
)
md5sums=(
  d3e079be102786fcc2b9dd3a5c7d5b75
  1b00c893424d99250583b19c93550744
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
