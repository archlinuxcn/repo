# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Maintainer: Jaroslav Lichtblau <dragonlord at aur dot archlinux dot org>
# Contributor: Andrzej Giniewicz <gginiu at gmail dot com>

pkgbase=python-scikit-image
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
pkgver=0.16.2
pkgrel=1
pkgdesc="Image processing routines for SciPy"
arch=('i686' 'x86_64')
url="http://scikit-image.org/"
license=('BSD')
makedepends=('cython>=0.23.4')
depends=('python-numpy>=1.14' 'python-scipy>=0.19.0' 'python-matplotlib>3.0.0' 'python-networkx>=2.0' 'python-pillow>=4.3.0' 'python-pywavelets>=0.4.0' 'python-imageio>=2.3.0')
optdepends=('python-pyqt5: for imshow(x, fancy=True) and skivi'
            'python-qtpy'
            'freeimage: for reading various types of image file formats'
            'python-pyamg: fast cg_mg mode of random walker segmentation'
            'python-astropy: Provides FITS I/O capability'
            'python-imread: Optional I/O plugin providing most standard formats'
            'python-simpleitk: Optional I/O plugin providing a wide variety of formats. including specialized formats using in medical imaging')
options=('!emptydirs')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('dd7fbd32da74d4e9967dc15845f731f16e7966cee61f5dc0e12e2abb1305068c')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python setup.py build
}

package_python-scikit-image() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}
