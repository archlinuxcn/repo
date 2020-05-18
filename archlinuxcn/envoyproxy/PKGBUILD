# Maintainer: kXuan <kxuanobj@gmail.com>

pkgname=envoyproxy
pkgver=1.14.1
pkgrel=1
pkgdesc="A high performance, open source, general RPC framework that puts mobile and HTTP/2 first."
arch=('i686' 'x86_64')
url='https://envoyproxy.io'
license=('Apache2')
makedepends=(
    'bazel'
    'cmake'
    'git'
    'go'
    'java-environment-openjdk'
    'ninja'
    'perl'
    'python'
)
source=(
    "https://github.com/$pkgname/envoy/archive/v$pkgver.tar.gz"
)
sha512sums=('0d68a15f7eb5a16a26a093a993132d57941931963f06845d3ba489505f18a9a7d82c809c38c6552ef01bc542ee715152b964f1dcf6b69951c3d9bbe6b3f3af20'
)

prepare() {
  cd "envoy-$pkgver"
  go get github.com/bazelbuild/buildtools/buildifier
  bazel --version | cut -d\  -f2 > .bazelversion
  # The commit id of $pkgver
  echo "3504d40f752eb5c20bc2883053547717bcb92fd8" > SOURCE_VERSION
}

build() {
  cd "envoy-$pkgver"

  bazel build --verbose_failures --workspace_status_command bazel/get_workspace_status -c opt //source/exe:envoy-static
}

package() {
  cd "envoy-$pkgver"

  install -Dm755 bazel-bin/source/exe/envoy-static "$pkgdir"/usr/bin/envoy
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
