# Maintainer: Anton Hvornum <torxed@archlinux.org>
# Maintainer: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor: Ingo Meyer <i.meyer@fz-juelich.de>
# Contributor: Shresth Paul <shresthpaul133@gmail.com>

# importlib_metadata is a false positive warning from namcap due to
# backwards compatability import of the script entrypoint.

# python-setuptools is also a false positive due to a third-level
# backwards compatability attempt in script entrypoint.

pkgname=python-simple-term-menu
pkgver=1.6.6
pkgrel=3
pkgdesc='A Python package which creates simple interactive menus on the command line.'
arch=('any')
url='https://github.com/IngoMeyer441/simple-term-menu'
license=('MIT')
depends=('python')
makedepends=(
  'python-setuptools'
)
checkdepends=()
optdepends=()
source=("https://files.pythonhosted.org/packages/d8/80/f0f10b4045628645a841d3d98b584a8699005ee03a211fc7c45f6c6f0e99/simple_term_menu-1.6.6.tar.gz")
sha256sums=('9813d36f5749d62d200a5599b1ec88469c71378312adc084c00c00bfbb383893')

# Optional but cleaner
_srcname="simple_term_menu"

pkgver() {
  echo "$pkgver"
}

build() {
  cd "$_srcname-$pkgver"
  python setup.py build
}

package() {
  cd "${srcdir}/${_srcname}-${pkgver}" || return
  python setup.py install --optimize=1 \
                          --prefix=/usr \
                          --root="${pkgdir}" \
                          --skip-build

  install -vDm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
