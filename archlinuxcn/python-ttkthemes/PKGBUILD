# Maintainer: Juliette Monsel <j_4321 at protonmail dot com>
pkgname=('python-ttkthemes')
pkgver=3.2.2
pkgrel=1
pkgdesc="Group of themes for the ttk extenstions for Tkinter "
_name=ttkthemes
arch=('any')
url="https://github.com/TkinterEP/ttkthemes"
license=('GPL3')
source=("${pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha512sums=('620baa326d1e37913c0f052c3e748eaf4d08f3ca99d861730a69258789f9a76707a20c5229d9c13f6fe6f7208035ed54f6dc14c6eb5f548a38a171229c24be56')
makedepends=('python-setuptools')
depends=('tk' 'python-pillow')

build() {
    cd "$srcdir/$_name-${pkgver}"
    python setup.py build
}

package() {
    cd "$srcdir/$_name-${pkgver}"
    python setup.py install --root="$pkgdir/" --prefix=/usr --optimize=1 --skip-build
}
