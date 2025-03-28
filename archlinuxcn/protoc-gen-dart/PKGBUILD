# Maintainer: Roald Clark <roaldclark@gmail.com>

pkgname=protoc-gen-dart
pkgver=22.0.0
pkgrel=1
pkgdesc="Protobuf plugin for generating Dart code"
arch=('x86_64')
url="https://pub.dev/packages/protoc_plugin"
license=('BSD-3-Clause')
depends=('glibc')
makedepends=('dart')
options=('!strip')
source=("https://github.com/google/protobuf.dart/archive/protoc_plugin-v${pkgver}.tar.gz")
sha256sums=('be04810fbcec24aa04c6b8f36a8f4ca30c95ce16ad3199111b6302e66b8ec99b')

prepare() {
    cd "${srcdir}/protobuf.dart-protoc_plugin-v${pkgver}/protoc_plugin"
    # disable analytics
    dart --disable-analytics
    # download dependencies
    dart pub get
}

build() {
    cd "${srcdir}/protobuf.dart-protoc_plugin-v${pkgver}/protoc_plugin"
    dart compile exe bin/protoc_plugin.dart -o protoc-gen-dart
}

package() {
    cd "${srcdir}/protobuf.dart-protoc_plugin-v${pkgver}/protoc_plugin"
    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
    install -Dm755 protoc-gen-dart -t "$pkgdir/usr/bin/"
}

