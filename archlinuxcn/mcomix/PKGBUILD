# Maintainer: schuay <jakob.gruber@gmail.com>
# Contributor: Ray Powell <ray_al@xphoniexx.net>

pkgname=mcomix
pkgver=3.2.0
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
sha256sums=('a332b3e436e2cbcc001e5d8b3579831d562309110c3d14b1012f8ba7fa04e917')

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
