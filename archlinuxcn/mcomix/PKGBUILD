# Maintainer: schuay <jakob.gruber@gmail.com>
# Contributor: Ray Powell <ray_al@xphoniexx.net>

pkgname=mcomix
pkgver=3.1.1
pkgrel=1
pkgdesc="GTK comic book viewer"
arch=('any')
url="https://sourceforge.net/p/mcomix/wiki/Home/"
license=('GPL-2.0-or-later')
depends=('gtk3' 'python-cairo' 'python-gobject' 'python-pillow')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
optdepends=(
  'lhasa: for lha compressed comics'
  'libunrar: for rar compressed comics'
  'p7zip: for 7z compressed comics'
  'python-chardet: for guessing filename encodings in archives'
  'python-pymupdf: for PDF comics'
  'unrar: for rar compressed comics'
  'unzip: for zip compressed comics'
)
source=(
  "https://downloads.sourceforge.net/project/${pkgname}/MComix-${pkgver}/${pkgname}-${pkgver}.tar.gz"
)
sha256sums=('a10aaaed7bc07deb74efde93bf9a8a27e1bcbf1824a0519b264cfee582becef8')

build() {
  cd "${pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl

  # application meta files are no longer copied automatically by the installation process
  cp -a share "$pkgdir/usr"
}
