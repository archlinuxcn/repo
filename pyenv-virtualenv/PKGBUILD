# Maintainer: Ayrton Araujo <root@ayr-ton.net>
# Contributor: Nuno Araujo <nuno.araujo@russo79.com>
pkgname=pyenv-virtualenv
pkgver=1.1.3
pkgrel=2
epoch=1
pkgdesc="pyenv plugin to manage virtualenv (a.k.a. python-virtualenv)"
arch=('any')
url="https://github.com/pyenv/pyenv-virtualenv"
license=('MIT')
depends=('pyenv' 'bash')
source=("https://github.com/pyenv/$pkgname/archive/v$pkgver.tar.gz")
md5sums=('49305063e18108959b2c2a43f9c1d813')

package() {
  mkdir -p "${pkgdir?}"/{opt/pyenv/plugins/pyenv-virtualenv,usr/bin}
  cd "${srcdir?}/$pkgname-$pkgver"
  cp -a -- * "$pkgdir"/opt/pyenv/plugins/pyenv-virtualenv

  for bin in $pkgdir/opt/pyenv/plugins/pyenv-virtualenv/bin/*; do
	  ln -s /opt/pyenv/plugins/pyenv-virtualenv/bin/"$(basename $bin)" "$pkgdir/usr/bin/$(basename $bin)"
  done

  # License
  mkdir -p "$pkgdir"/usr/share/licenses/pyenv-virtualenv
  cp LICENSE "$pkgdir"/usr/share/licenses/pyenv-virtualenv
}

