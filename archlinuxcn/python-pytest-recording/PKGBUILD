# Maintainer: Gesh <gesh@gesh.uni.cx>
# Contributor: Achmad Fathoni<fathoni.id(at)gmail.com>

pkgname=python-pytest-recording
pkgver=0.13.2
pkgrel=3
_name=${pkgname#python-}
_name="${_name//-/_}"
_src_folder="${_name}-${pkgver}"
pkgdesc='Pytest plugin to record network interactions with VCR.py'
arch=('any')
url="https://pypi.org/project/${_name}"
license=('MIT')
depends=(python 'python-vcrpy>=7.0.0' python-pytest)
makedepends=(python-build python-installer python-hatchling)
optdepends=(
    'python-pycurl: Block pycurl-based network connections'
)
checkdepends=(python-coverage python-pytest-httpbin python-pytest-mock python-requests python-werkzeug)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('000c3babbb466681457fd65b723427c1779a0c6c17d9e381c3142a701e124877')

build() {
    cd "${srcdir}/${_src_folder}"
    python -m build --wheel --no-isolation

    python -m installer --destdir=tmp_install dist/*.whl
}

check() {
    cd "${srcdir}/${_src_folder}"

    local _site_packages
    _site_packages="$(python -c 'import site; print(site.getsitepackages()[0])')"
    export PYTHONPATH="$PWD/tmp_install/$_site_packages"

    python -m pytest
}

package() {
    cd "${srcdir}/${_src_folder}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
