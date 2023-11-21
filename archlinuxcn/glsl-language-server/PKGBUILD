# Maintainer: Sven-Hendrik Haase <svenstaro@archlinux.org>
pkgname=glsl-language-server
pkgver=0.5.0
pkgrel=1
pkgdesc="A language server implementation for GLSL"
arch=('x86_64')
url="https://github.com/svenstaro/glsl-language-server"
license=(MIT)
depends=('gcc-libs' 'glibc')
makedepends=('cmake' 'git' 'ninja' 'python')
source=(git+https://github.com/svenstaro/glsl-language-server#tag=$pkgver)
sha512sums=('SKIP')

prepare() {
  cd "$pkgname"

  git submodule update --init
}

build() {
  cd "$pkgname"

  cmake \
    -Bbuild \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX=/usr
  ninja -C build
}

package() {
  cd "$pkgname"

  DESTDIR="$pkgdir/" ninja -C build install
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

# vim:set ts=2 sw=2 et:
