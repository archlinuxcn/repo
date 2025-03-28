# Maintainer: Roald Clark <roaldclark@gmail.com>

pkgname=protoc-gen-dart
pkgver=22.0.1
pkgrel=1
pkgdesc="Protobuf plugin for generating Dart code"
arch=('x86_64')
url="https://pub.dev/packages/protoc_plugin"
license=('BSD-3-Clause')
depends=('glibc')
makedepends=('dart')
options=('!strip')
source=("https://github.com/google/protobuf.dart/archive/protoc_plugin-v${pkgver}.tar.gz")
sha256sums=('d41261fc65a396c35ff1ebece519895cd5e528a5629d9fd373b1c1d7a7d2936d')

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

