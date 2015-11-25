#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=powerpill
pkgver=2015.11.21
pkgrel=1
pkgdesc='Pacman wrapper for parallel and segmented downloads.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/powerpill"
depends=(python3 pyalpm 'pm2ml>2012.12.12' reflector aria2 python3-xcpf)
optdepends=('rsync: Rsync download support' 'python3-threaded_servers: internal Pacserve support')
backup=(etc/powerpill/powerpill.json)
source=(
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.11.21.tar.xz
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.11.21.tar.xz.sig
)
sha512sums=(
  1b6586d845e86c7cabf5fd9145a77b921dd646c92426a489d0fc7e0298abcf026463e46079055e19a780b4f381384a27a1e0d20705c16a84f459756cdf208230
  e17fad4df22f7054a2db6a3659a0d1a28551b38ee9c284ca075efb0ae0a47ef50ae7ebe0e07e68795cfa0e2af923c0c042469ac1f4374073863d4f8d2d89afb3
)
md5sums=(
  fdc9d00fad9db431b3f6dfc496473df7
  c8a21ce12868078b1612089187a81093
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
