# Maintainer: Fredrick Brennan <copypaste@kittens.ph>
# Maintainer: Pig Monkey <pm@pig-monkey.com>
# Contributor: mutantmonkey <aur@mutantmonkey.in>
# Contributor: Stephan Eisvogel <eisvogel at embinet dot de>
# Contributor: Daniel Reuter <daniel.robin.reuter@googlemail.com>

pkgname=ocrmypdf
pkgver=16.1.0
pkgrel=1
pkgdesc="A tool to add an OCR text layer to scanned PDF files, allowing them to be searched"
url="https://github.com/ocrmypdf/OCRmyPDF"
arch=('any')
license=(MPL2)
# NOTICE: The number of dependencies we rely on is *very high*. If the program does not run after an upgrade, make sure all your deps are upgraded, especially AUR deps!
depends=('python>=3.9' 'img2pdf' 'python-pillow' 'tesseract' 'ghostscript' 'unpaper' 'pngquant' 'python-pikepdf' 'python-reportlab' 'python-pdfminer' 'python-tqdm' 'python-pluggy' 'python-rich' 'python-importlib_resources' 'python-packaging')

makedepends=('python-setuptools-scm>=7.0.5' 'python-build' 'python-installer' 'python-wheel')
optdepends=('jbig2enc: Better compression algorithm; results in smaller PDF files')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('e1e63a14b64320b17dd41fe193a530e679d62b2565e00abf33a28f527ca1c37d')
install="${pkgname}.install"

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE.rst
}

# vim:set ts=2 sw=2 et:
