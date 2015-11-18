#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=powerpill
pkgver=2015.11.15
pkgrel=1
pkgdesc='Pacman wrapper for parallel and segmented downloads.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/powerpill"
depends=(python3 pyalpm 'pm2ml>2012.12.12' reflector aria2 python3-xcpf)
optdepends=('python3-threaded_servers: internal Pacserve support' 'rsync: Rsync download support')
backup=(etc/powerpill/powerpill.json)
source=(
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.11.15.tar.xz
  http://xyne.archlinux.ca/projects/powerpill/src/powerpill-2015.11.15.tar.xz.sig
)
sha512sums=(
  389d2a15cc8a213b5017cf149d75a5ec1ee6190c0e313594aad9f87e6ebdbd291786f520f3241d68e60727df0ece278a99718101154f10767abd8046fcd972c3
  7befa81eec7f569be05513f34bec98d31fb912fbacc0c3a43e489f401624895f1b50a45823e20cfcd741bdd9bbb366c74dc8f750a9ed3fb825b6df519794ced4
)
md5sums=(
  12ab71f8b591b07c49294723cb2e6dce
  bad8375e41db24b463ded2daef04b3f2
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
