# Maintainer: Mateen Ulhaq <mulhaq2005+aur at gmail dot com>

pkgbase="python-arxiv"
pkgname=("python-arxiv")
_module="arxiv"
pkgver=2.1.0
pkgrel=1
pkgdesc="Python wrapper for the arXiv API: http://arxiv.org/help/api/"
url="https://github.com/lukasschwab/arxiv.py"
depends=("python" "python-feedparser" "python-requests")
makedepends=("python-setuptools")
license=("MIT")
arch=("any")
source=("https://files.pythonhosted.org/packages/source/${_module::1}/$_module/$_module-$pkgver.tar.gz")
sha256sums=("eb4b1d5ab9dfd66027c344bb324c20be21d56fe15f6ce216ed5b209df747dea8")

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    depends+=()
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
