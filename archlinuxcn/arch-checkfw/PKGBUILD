# Maintainer: GalaxySnail <me+aur@glxys.nl>

_pkgname=arch_checkfw
pkgname=arch-checkfw
pkgver=1.1.0
pkgrel=1
pkgdesc="auto detect required firmware packages on Arch Linux"
arch=('any')
license=('GPL-2.0-or-later')
url='https://github.com/GalaxySnail/arch-checkfw'
depends=(
  'python'
  'kmod'
  'pacfiles'
)
makedepends=(
  'git'
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-wheel'
)
#_tag='v1.1.0'
_commit='1372b1c40e2f0f103fc7a4adb520ffa81b9f95ee'
source=("$pkgname::git+$url#commit=$_commit")
sha256sums=('SKIP')

build() {
  cd $pkgname
  python -m build --wheel --no-isolation
}

package() {
  cd $pkgname
  python -m installer --destdir="$pkgdir" dist/$_pkgname-$pkgver-*.whl

  # symlink license file
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "$site_packages/$_pkgname-$pkgver.dist-info/licenses/LICENSE" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
