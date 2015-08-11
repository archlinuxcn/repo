# Maintainer: farseerfc <farseerfc@archlinuxcn.org>
# Contributor: Tom Li <biergaizi@member.fsf.org>

pkgname=python-rpweibo
pkgver=0.02.2
_pkgver=0.02.2
pkgrel=2
pkgdesc="A Weibo API wrapper based on cURL + Python."
arch=('any')
url="https://github.com/WeCase/rpweibo"
license=('LGPL3')
depends=('python' 'python-pycurl' 'python-rsa')
source=("rpweibo-${_pkgver}.tar.gz::https://github.com/WeCase/rpweibo/archive/${_pkgver}.tar.gz")
md5sums=('f836fb884b624b4462d0a39c449ad181')

package() {
  cd "$srcdir/rpweibo-${_pkgver}"
  python setup.py install --root="$pkgdir/" --optimize=1
}
