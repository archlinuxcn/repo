# Maintainer: Roald Clark <roaldclark@gmail.com>

pkgname=protoc-gen-dart
pkgver=22.4.0
pkgrel=1
pkgdesc="Protobuf plugin for generating Dart code"
arch=('x86_64')
url="https://pub.dev/packages/protoc_plugin"
license=('BSD-3-Clause')
depends=('glibc')
makedepends=('dart')
options=('!strip')
source=("https://github.com/google/protobuf.dart/archive/protoc_plugin-v${pkgver}.tar.gz")
sha256sums=('f5c5d7a9f5927bda026cfd933f057faeeb2cf8c70b03f11c7c05f8b67538016c')

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

