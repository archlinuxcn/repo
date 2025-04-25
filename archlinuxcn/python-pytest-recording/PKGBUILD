# Maintainer: Gesh <gesh@gesh.uni.cx>
# Contributor: Achmad Fathoni<fathoni.id(at)gmail.com>

pkgname=python-pytest-recording
_pkgname=${pkgname#python-}
pkgver=0.13.2
pkgrel=7
pkgdesc='Pytest plugin to record network interactions with VCR.py'
arch=('any')
url="https://pypi.org/project/${_pkgname//-/_}"
_url='https://github.com/kiwicom/pytest-recording'
license=('MIT')
depends=(python 'python-vcrpy>=7.0.0' python-pytest)
makedepends=(python-build python-installer python-hatchling)
optdepends=(
    'python-pycurl: Block pycurl-based network connections'
)
checkdepends=(
    python-coverage
    python-pytest
    python-pytest-httpbin
    python-pytest-mock
    python-requests
    python-werkzeug
)
source=("$pkgname-$pkgver::${_url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('979a7849e758ed1d6ba17056533c75ac901f30a420d8229342bf4c5043cb86fb')

build() {
    cd "$_pkgname-$pkgver"
    python -m build --wheel --no-isolation

    python -m installer --destdir=tmp_install dist/*.whl
}

check() {
    cd "$_pkgname-$pkgver"

    local _site_packages
    _site_packages="$(python -c 'import site; print(site.getsitepackages()[0])')"
    export PYTHONPATH="$PWD/tmp_install/$_site_packages"

    export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
    # Can't pass these via -p for some reason, see
    # https://github.com/pytest-dev/pytest/issues/13388
    export PYTEST_PLUGINS=pytest_httpbin.plugin,pytest_mock,pytest_recording.plugin
    python -m pytest
}

package() {
    cd "$_pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
