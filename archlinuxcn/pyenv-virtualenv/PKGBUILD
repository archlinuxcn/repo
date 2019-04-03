# Maintainer: Ayrton Araujo <root@ayr-ton.net>
# Co-maintainer: Kevin Del Castillo R. <lans9831@gmail.com>
# Contributor: Nuno Araujo <nuno.araujo@russo79.com>
pkgname=pyenv-virtualenv
pkgver=1.1.5
pkgrel=3
epoch=1
pkgdesc="pyenv plugin to manage virtualenv (a.k.a. python-virtualenv)"
arch=('any')
url="https://github.com/pyenv/pyenv-virtualenv"
license=('MIT')
depends=('pyenv' 'bash')
makedepends=('patch')
source=("https://github.com/pyenv/$pkgname/archive/v$pkgver.tar.gz"
        "fix-symlink-308.patch")
md5sums=('2ebab171a403915d695c383855ac78e4'
         '476790c1f9643d76efbb188b35ed19e0')

prepare() {
  cd "${srcdir?}/$pkgname-$pkgver"

  # Fix issue #308  
  patch -p1 < ../fix-symlink-308.patch
}

package() {
  mkdir -p "${pkgdir?}"/{opt/pyenv/plugins/pyenv-virtualenv,usr/bin}
  cd "${srcdir?}/$pkgname-$pkgver"

  # Intall using the script
  PREFIX="${pkgdir}/opt/pyenv/plugins/pyenv-virtualenv" ./install.sh 

  # Link binaries
  pushd bin &> /dev/null
  for bin in *; do
      ln -s /opt/pyenv/plugins/pyenv-virtualenv/bin/"$bin" "$pkgdir/usr/bin/$bin"
  done
  popd &> /dev/null

  # License
  mkdir -p "$pkgdir"/usr/share/licenses/pyenv-virtualenv
  cp LICENSE "$pkgdir"/usr/share/licenses/pyenv-virtualenv
}

# vim:set sw=2 sts=2 et:
