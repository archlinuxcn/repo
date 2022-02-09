# Maintainer: Padraic Fanning <fanninpm at miamioh dot edu>
# Contributor: Yufan You <ouuansteve at gmail>

pkgname=lean-community
_pkgname=lean
pkgver=3.39.1
pkgrel=1
pkgdesc='Lean Theorem Prover, maintained by the Lean community'
arch=('x86_64' 'i386')
url="https://github.com/leanprover-community/lean"
license=('Apache')
makedepends=('cmake' 'ninja' 'python')
optdepends=('python-mathlibtools')
conflicts=('lean-bin' 'lean-git' 'lean3-bin' 'lean2-git')
source=("$pkgname-$pkgver.tar.gz::https://github.com/leanprover-community/lean/archive/v$pkgver.tar.gz")
sha256sums=('7a4179dbfe90317ad19a7fde76dfd38fb0f2ed24e08208b1ebee6b98b8396063')

build() {
  cd "$_pkgname-$pkgver"
  mkdir build
  cd build
  cmake ../src -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -G Ninja
  ninja
}

package() {
  cd "$_pkgname-$pkgver"/build
  DESTDIR="$pkgdir" ninja install
}
