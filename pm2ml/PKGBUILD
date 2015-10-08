#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pm2ml
pkgver=2015.10.8
pkgrel=1
pkgdesc='Generate metalinks for downloading Pacman packages and databases.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/pm2ml"
depends=(python3 pyalpm python3-xcpf)
optdepends=('python3-aur: AUR support' 'aria2: ppl script support.' 'reflector: Reflector support')
backup=(etc/ppl.conf)
source=(
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.10.8.tar.xz
  http://xyne.archlinux.ca/projects/pm2ml/src/pm2ml-2015.10.8.tar.xz.sig
)
sha512sums=(
  662fd59905b0bc8c481d10b6f2daf9685e64e10aeb4130353d70a6b69d760d686eb6b4af5de48f5028f1d8b5fe844c34fb9f643fd4bf4d7df8df82086d81becf
  ff12b9714a41ae81d96cf8ebb1acf3c8af6e9a1f25d1771ad1747c4a47c021b7d7bbe74a564192ae25ca7006e80761c7b6364b023d1db617654f88c793257d54
)
md5sums=(
  cd89cd4301b3fe8c2f4c48bfc987df6d
  11877ff08578d430a806764f453971bc
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
  for foo_ in ppl pplsyu ppls; do
    install -Dm755 "$foo_" "$pkgdir/usr/bin/$foo_"
  done
  install -Dm644 "ppl.conf" "$pkgdir/etc/ppl.conf"
}

# vim: set ts=2 sw=2 et:
