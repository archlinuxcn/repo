#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=powerpill
pkgver=2015
pkgrel=1
pkgdesc='Pacman wrapper for parallel and segmented downloads.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/powerpill"
depends=(python3 pyalpm 'pm2ml>2012.12.12' reflector aria2)
optdepends=('rsync: Rsync download support' 'python3-threaded_servers: internal Pacserve support')
backup=(etc/powerpill/powerpill.json)
source=(
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.tar.xz
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.tar.xz.sig
)
sha512sums=(
  958ebecc548e767e0d84e4e315cfc0b52259e9ce715cbf29829b62619e7f90a1f4d2d9b66c003a9be7f19ccc0e1a54dd7d6b7ca2a245a216dd2cf50af2f431c6
  9f6b01344ec9cc02beae0816de38b4ded32181503805c623e82f9264aa84467432d3f64107095fa5b316daba70e6df9e2a53af47cdb314cdf229815fd73af8b1
)
md5sums=(
  32722e5ae4cb1c9fd9d245632313b09c
  5dd26bd9b3dfd6e0b918c5c9ff253f14
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "powerpill.json" "$pkgdir/etc/powerpill/powerpill.json"
  install -Dm644 "man/powerpill.json.1.gz" "$pkgdir/usr/share/man/man1/powerpill.json.1.gz"
  install -Dm644 "powerpill-bash-completion.sh" "$pkgdir/usr/share/bash-completion/completions/powerpill"
}

# vim: set ts=2 sw=2 et:
