#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=powerpill
pkgver=2015.10.6.4
pkgrel=1
pkgdesc='Pacman wrapper for parallel and segmented downloads.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/powerpill"
depends=(python3 pyalpm 'pm2ml>2012.12.12' reflector aria2 python3-xcpf)
optdepends=('python3-threaded_servers: internal Pacserve support' 'rsync: Rsync download support')
backup=(etc/powerpill/powerpill.json)
source=(
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.10.6.4.tar.xz
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.10.6.4.tar.xz.sig
)
sha512sums=(
  000770db002efeda02098e43bbcabc517ce3886e78b33c58cd18b45a4c479aba0349d4dc563381c0eb9f6dabea454a9fde38ba7d39b6d1cdfa9188d15d1b05dc
  f47add3f818b7d0906adb8d33485385ca9f8e77d5c69648d35a5bf6ed412816af384b58d30f0b0d93af40a64fbfd44a26fc784e2fc92d725b7e2082deac14bfd
)
md5sums=(
  cfec5dd24b534874ef614fea7c66c6e5
  80565b3151b6fef7b947ab40ccb0654b
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
