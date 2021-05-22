# Maintainer: Fredrick Brennan <copypaste@kittens.ph>
# Maintainer: Pig Monkey <pm@pig-monkey.com>
# Contributor: mutantmonkey <aur@mutantmonkey.in>
# Contributor: Stephan Eisvogel <eisvogel at embinet dot de>
# Contributor: Daniel Reuter <daniel.robin.reuter@googlemail.com>

pkgname=ocrmypdf
pkgver=12.0.2
pkgrel=1
pkgdesc="A tool to add an OCR text layer to scanned PDF files, allowing them to be searched"
url="https://github.com/jbarlow83/OCRmyPDF"
arch=('any')
license=(MPL2)
# NOTICE: The number of dependencies we rely on is *very high*. If the program does not run after an upgrade, make sure all your deps are upgraded, especially AUR deps!
depends=('python' 'python-cffi' 'img2pdf' 'python-pillow>=7.0.0' 'tesseract' 'ghostscript' 'unpaper' 'leptonica' 'pngquant' 'python-pikepdf' 'python-reportlab' 'python-pdfminer' 'python-tqdm' 'python-pluggy' 'python-coloredlogs')

makedepends=('python-setuptools')
optdepends=('jbig2enc: Better compression algorithm; results in smaller PDF files')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('379399f02540afcc20fc483928344055bb41f5be5332c738b4b3d983c50ac85a')

package () {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir/" --optimize=1
  install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE.rst
}

# vim:set ts=2 sw=2 et:
