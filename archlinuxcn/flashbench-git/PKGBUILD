# Maintainer: lestb <tkhdlstfl dot l plus aur at gmail dot com>
# Contributor: Marti Raudsepp <marti@juffo.org>
# Package Repository: https://github.com/mij-aur-packages/flashbench-git

pkgname=flashbench-git
pkgver=r62.2e30b19
pkgrel=1
pkgdesc="Tool for benchmarking and classifying flash memory drives"
arch=(i686 x86_64)
license=('GPL2')
url="https://lwn.net/SubscriberLink/428584/354d16fe00c90072/"
replaces=('flashbench')
provides=('flashbench')
conflicts=('flashbench')
source=('git+https://git.linaro.org/people/arnd.bergmann/flashbench.git')
md5sums=('SKIP')

pkgver() {
  cd "${srcdir}/flashbench"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "${srcdir}/flashbench"
  make
}

package() {
  cd "${srcdir}/flashbench"
  mkdir -p "${pkgdir}/usr/bin"
  install -m755 flashbench erase "${pkgdir}/usr/bin/"
}
