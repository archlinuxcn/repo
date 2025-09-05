# Maintainer: WT5A <K5TRP[at]onlyhams[dot]ca>
# Maintainer: Helmut Stult <hst[at]e-mail[dot]de>
# Thanks to the maintainer(s) of chirp-daily
# Contributor: 0b100100 <0b100100 at protonmail dot ch>
# Contributor: Ashley Roll (ash@digitalnemesis.com)
# Contributor: Erez Raviv (erezraviv@gmail.com)

pkgname=chirp-next
pkgver=20250905
pkgrel=1
pkgdesc="GUI tool for programming ham radios"
arch=('any')
url="https://chirpmyradio.com/projects/chirp/wiki/Home"
license=('GPL-3.0-or-later')
depends=('python-pyserial' 'python-requests' 'python-suds'
         'python-yattag' 'python-wxpython' 'python-lark-parser')
optdepends=('hamradio-menus: XDG menus for ham radio software')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
options=(!emptydirs)
conflicts=('chirp' 'chirp-daily')
provides=(chirp)
install=$pkgname.install
source=("${pkgname}-${pkgver}.tar.gz::https://archive.chirpmyradio.com/chirp_next/next-${pkgver}/chirp-${pkgver}.tar.gz")
# Checksums: https://archive.chirpmyradio.com/chirp_next/next-$pkgver/SHA1SUM
sha1sums=('d5c549edbea6ce6f3b93d3d2dba614914396bb97')

# User-Agent override workaround for nitpicky Cloudflare config; see:
# https://wiki.archlinux.org/title/Nonfree_applications_package_guidelines#Custom_DLAGENTS
DLAGENTS=("https::/usr/bin/curl -A 'Mozilla' -fLC - --retry 3 --retry-delay 3 -o %o %u")

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
