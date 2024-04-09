# Maintainer: Carl Smedstad <carl.smedstad at protonmail dot com>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Mufeed Ali <fushinari@protonmail.com>
# Contributor: lastweakness <lastweakness@tuta.io>

pkgname=python-cloudscraper
_name=${pkgname#python-}
pkgver=1.2.71
pkgrel=2
pkgdesc="Python module to bypass Cloudflare's anti-bot page"
arch=(any)
url="https://github.com/VeNoMouS/cloudscraper"
license=(MIT)
depends=(
  python
  python-brotli
  python-pyparsing
  python-requests
  python-requests-toolbelt
  python-urllib3
)
optdepends=(
  'nodejs: alternative interpreter/solver'
  'python-js2py: alternative interpreter/solver'
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
checkdepends=(
  nodejs
  python-js2py
  python-pytest
  python-responses
)

_commit=cbb3c0ea31597a3c94760d9edf648a77510da8ac
source=("$pkgname-$_commit.tar.gz::$url/archive/$_commit.tar.gz")
sha256sums=('045c8f6e87697d0684997a61315883c968974a1a0a2bc7ee470c1e63ceab23fc')

_archive="$_name-$_commit"

build() {
  cd "$_archive"

  python -m build --wheel --no-isolation
}

check() {
  cd "$_archive"

  pytest \
    --deselect tests/test_cloudscraper.py::TestCloudScraper::test_bad_interpreter_js_challenge1_16_05_2020 \
    --deselect tests/test_cloudscraper.py::TestCloudScraper::test_bad_solve_js_challenge1_16_05_2020 \
    --deselect tests/test_cloudscraper.py::TestCloudScraper::test_Captcha_challenge_12_12_2019 \
    --deselect tests/test_cloudscraper.py::TestCloudScraper::test_reCaptcha_providers
}

package() {
  cd "$_archive"

  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE
}
