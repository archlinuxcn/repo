# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-x-wr-timezone
_name=${pkgname#python-}
pkgver=0.0.7
pkgrel=1
pkgdesc="Handling of non-standard X-WR-TIMEZONE icalendar property in Python and Command Line"
arch=('any')
url="https://github.com/niccokunzmann/x-wr-timezone"
license=('LGPL-3.0-or-later')
depends=('python-icalendar' 'python-pytz')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
checkdepends=('python-pygments' 'python-pytest' 'python-pytest-cov' 'python-restructuredtext_lint')
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('d4ce744636f29e39d816837827af8365187c90ca9d1a1ab80f82874584c80eea')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

#check() {
#  cd "$_name-$pkgver"
#  coverage run -m pytest --x-wr-timezone=all
#}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
