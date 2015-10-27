#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=powerpill
pkgver=2015.10.21
pkgrel=1
pkgdesc='Pacman wrapper for parallel and segmented downloads.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/powerpill"
depends=(python3 pyalpm 'pm2ml>2012.12.12' reflector aria2 python3-xcpf)
optdepends=('rsync: Rsync download support' 'python3-threaded_servers: internal Pacserve support')
backup=(etc/powerpill/powerpill.json)
source=(
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.10.21.tar.xz
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.10.21.tar.xz.sig
)
sha512sums=(
  fa4163ae086ec873951e68c703c1e74022deb47300b1949a4e42646d1bb4e22a81ecdad6e4d2045bc1aae9b93f74fe9d27a1138751ddd8c5fdf42356517e5429
  56cdf31d55d373145970e2117526b14c385788d547e3efa7ba4fea1cc0a6746d628d3aac7b742c434087cfbf4f37676cb181c6ae82b19092f0370b0b79ffd895
)
md5sums=(
  2484ae432f6ef62a925bd15318dee308
  18f87971bfd1a571c9c7b8690b55d395
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
