#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=powerpill
pkgver=2016.1
pkgrel=1
pkgdesc='Pacman wrapper for parallel and segmented downloads.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/powerpill"
depends=(aria2 'pm2ml>2012.12.12' pyalpm python3 python3-xcgf python3-xcpf reflector)
optdepends=('python3-threaded_servers: internal Pacserve support' 'rsync: Rsync download support')
backup=(etc/powerpill/powerpill.json)
source=(
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2016.1.tar.xz
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2016.1.tar.xz.sig
)
sha512sums=(
  21a6c46c77c21eeaaca5e1118b0b1548696b7313073d39df23a95a0ddfecfbefc633abcf09e8aabc66f8b4b7a9ed6e3a32d4bca940fec81c18bb3fbacc1464c6
  95f5c3552b60995625e35d5bc84e18ca3a3afdcdff9317c79f5005c9c4ddc9e9bca6494d969e1ac6fc04668471149ad31098953363debb4a226a143671c35e9d
)
md5sums=(
  120e7ff09456b1a9f25d42b749b22a99
  f6b23ff2dfbf2e2c7f091671a85b57aa
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm755 "powerpill" "$pkgdir/usr/bin/powerpill"
  install -Dm644 "powerpill.json" "$pkgdir/etc/powerpill/powerpill.json"
  install -Dm644 "man/powerpill.json.1.gz" "$pkgdir/usr/share/man/man1/powerpill.json.1.gz"
  install -Dm644 "powerpill-bash-completion.sh" "$pkgdir/usr/share/bash-completion/completions/powerpill"
}

# vim: set ts=2 sw=2 et:
