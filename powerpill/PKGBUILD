#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=powerpill
pkgver=2015.10.18
pkgrel=1
pkgdesc='Pacman wrapper for parallel and segmented downloads.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/powerpill"
depends=(python3 pyalpm 'pm2ml>2012.12.12' reflector aria2 python3-xcpf)
optdepends=('python3-threaded_servers: internal Pacserve support' 'rsync: Rsync download support')
backup=(etc/powerpill/powerpill.json)
source=(
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.10.18.tar.xz
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.10.18.tar.xz.sig
)
sha512sums=(
  d297591293666a66006ea85a4e5bbdb012fc8ebe16c635b73bcefd2814af7100a778450f260a660aa47f3769aae08ea2b5cc5f8359b6898b461439f45914d1b2
  4df04f72c48db9e0b2d5d32f0753aec2b10a00a5720af6f92fe3692ffaecf42ed000e5e7d0109cf30c8f8a8a4c710d039a736d620916a444f88a88be0902d811
)
md5sums=(
  5c4811d33a0d64e9430c34953f0dcd2a
  672f8c4ec233169931a7f23d7f7895b6
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
