# Maintainer: Drew Metzger <aur at unexceptional dot net>

pkgname=greatfet-git
pkgver=2024.0.4
pkgrel=1
pkgdesc="GreatFET firmware and host software"
arch=('any')
url="https://github.com/greatscottgadgets/greatfet"
license=(BSD)
depends=(
  'ipython'
  'python-pyusb'
  'python-future'
  'python-pygreat'
  'python-cmsis-svd-git'
  'python-pyfwup'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-pyproject-patcher'
  'python-setuptools'
  'python-wheel'
)
provides=('greatfet')
source=("git+${url}")
sha1sums=('SKIP')
install=greatfet-git.install
_gitname=greatfet

pkgver() {
  cd $_gitname
  echo $(git describe --always --tags $(git rev-list --tags --max-count=1) | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g')
}

prepare() {
  # since the latest release is outside of the main branch for some reason...
  cd $_gitname
  git checkout --quiet "v${pkgver}"

  echo >&2 'Pinning version number'
  export pkgver
  python << 'EOF'
from pyproject_patcher import patch_in_place
with patch_in_place('host/pyproject.toml') as toml:
    toml.set_project_version_from_env('pkgver')
    toml.tools.setuptools_git_versioning.remove()
EOF
}

build() {
  python -m build --wheel --no-isolation "${_gitname}/host"
}

package() {
  install -D -m644 "${srcdir}/${_gitname}/host/util/54-greatfet.rules" "${pkgdir}/usr/lib/udev/rules.d/54-greatfet.rules"
  python -I -m installer --destdir="${pkgdir}" $srcdir/$_gitname/host/dist/*.whl
}

# vim:set ts=2 sw=2 et:
