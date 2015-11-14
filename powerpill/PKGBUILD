#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=powerpill
pkgver=2015.11
pkgrel=1
pkgdesc='Pacman wrapper for parallel and segmented downloads.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/powerpill"
depends=(python3 pyalpm 'pm2ml>2012.12.12' reflector aria2 python3-xcpf)
optdepends=('python3-threaded_servers: internal Pacserve support' 'rsync: Rsync download support')
backup=(etc/powerpill/powerpill.json)
source=(
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.11.tar.xz
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.11.tar.xz.sig
)
sha512sums=(
  3df084c43dc72fdf971514132e8b1e8f184ba0a965b9c811483659083a282c73f3da27358c66bb83550db4fc08cabe28b7de70ea25298dced9f10bd30a80a040
  a738143a83d0e0e2ebddf854850599ded3008c211916a183db152db303ca529beda917d6004d2aa17d9497c45423bc7df5cf95f8ad4f47663722471b842a5246
)
md5sums=(
  200f14ce26ed01ac2d66635c28de8069
  6cd249e0f47eb5a1e3c09d71631a403b
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
