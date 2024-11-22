# Maintainer: WT5A <K5TRP[at]onlyhams[dot]ca>
# Maintainer: Helmut Stult <hst[at]e-mail[dot]de>
# Thanks to the maintainer(s) of chirp-daily
# Contributor: 0b100100 <0b100100 at protonmail dot ch>
# Contributor: Ashley Roll (ash@digitalnemesis.com)
# Contributor: Erez Raviv (erezraviv@gmail.com)

pkgname=chirp-next
pkgver=20241122
pkgrel=1
pkgdesc="GUI tool for programming ham radios, built from chirp-next"
arch=('any')
url="https://chirpmyradio.com/projects/chirp/wiki/Home"
license=('GPL-3.0-or-later')
depends=('python-six' 'python-pyserial' 'python-future' 'python-requests' 'python-suds' 'python-yattag' 'python-wxpython')
optdepends=('hamradio-menus: XDG menus for ham radio software')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
options=(!emptydirs)
conflicts=('chirp' 'chirp-daily')
provides=(chirp)
install=$pkgname.install
source=("${pkgname}-${pkgver}.tar.gz::https://archive.chirpmyradio.com/chirp_next/next-${pkgver}/chirp-${pkgver}.tar.gz")
# Checksums: https://archive.chirpmyradio.com/chirp_next/next-$pkgver/SHA1SUM
sha1sums=('0030dec600b48644c4c09f125f754e41eb3fcd7e')

build() {
    cd "chirp-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
  _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cd "chirp-$pkgver"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -D -m644 "${srcdir}/chirp-${pkgver}/chirp/share/chirpw.1" "${pkgdir}/usr/share/man/man1/chirp.1"
  install -D -m644 "${srcdir}/chirp-${pkgver}/chirp/share/chirp.desktop" "${pkgdir}/usr/share/applications/chirp.desktop"
  install -D -m644 "${srcdir}/chirp-${pkgver}/chirp/share/chirp.png" "${pkgdir}/usr/share/pixmaps/chirp.png"
  cp -dr --preserve=mode,timestamp "${srcdir}/chirp-${pkgver}/chirp/locale/" "${pkgdir}${_site_packages}/chirp/locale"
}
