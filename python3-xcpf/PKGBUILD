#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=python3-xcpf
pkgver=2017.8
pkgrel=1
pkgdesc='Xyne'"'"'s common Pacman functions, for internal use.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/python3-xcpf"
depends=(pyalpm python-xdg python3 python3-memoizedb python3-xcgf)
optdepends=('rsync: Retrieve ABS files via rsync.')
source=(
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.8.tar.xz
  https://xyne.archlinux.ca/projects/python3-xcpf/src/python3-xcpf-2017.8.tar.xz.sig
)
sha512sums=(
  63107173f01216cc1cbb11b9550f91d368388bb7b56ecd04a0085fff9cb02866630c2a139aeb7f019aa88f42dae31a73d1989b52e9c1e4af6c75d58f77a301dc
  102721c9cf4a25b31707705d77d4a7c7256b96eb045533564e87146f945915f75d44ce0e7e67f5476aab8898280c5bf3e8749cfe477a842c5aafe7ea02e6ee76
)
md5sums=(
  ae57a4c2a488de36681c4eaf97639bb3
  af5fcb228ae271ba54dc4ee2137a2d63
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
}

# vim: set ts=2 sw=2 et:
