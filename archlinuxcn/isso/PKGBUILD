_pkgname=isso
pkgname=isso
pkgver=0.12.2
pkgrel=2
pkgdesc="lightweight Disqus alternative"
arch=('any')
url="https://github.com/posativ/isso/"
license=('MIT')
depends=('python' 'python-bleach' 'python-jinja' 'python-werkzeug' 'python-html5lib' 'python-misaka' 'python-itsdangerous' 'python-six' 'python-cffi' 'sqlite' 'python-setuptools')
_name=${pkgname#python-}
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_pkgname}-${pkgver}.tar.gz")
md5sums=('d5eeccd40e981b3fa42580c971cb6414')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
