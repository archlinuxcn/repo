# Maintainer: Lucas Werkmeister <mail@lucaswerkmeister.de>

java_=11
pkgname="jdk${java_}-graalvm-bin"
pkgver=22.2.0
pkgrel=1
pkgdesc="Universal virtual machine for running applications written in a variety of languages (JVM-based, LLVM-based, or other), Java ${java_} version"
arch=('x86_64'
      'aarch64')
url='https://www.graalvm.org/'
license=('custom')
depends=('java-runtime-common'
         'java-environment-common')
makedepends=()
optdepends=("graal-nodejs-jdk${java_}-bin: Node.js component (used to be bundled with this package before the 21.1.0 release)"
            "graaljs-jdk${java_}-bin: JavaScript component (used to be bundled with this package before the 22.2.0 release)"
            "graal-llvm-jdk${java_}-bin: LLVM component (used to be bundled with this package before the 22.2.0 release)"
            "graal-visualvm-jdk${java_}-bin: VisualVM component (used to be bundled with this package before the 22.2.0 release)")
provides=("java-runtime=${java_}"
          "java-environment=${java_}")
options=('staticlibs')
install="$pkgname.install"
source=('graalvm-rebuild-libpolyglot.hook')
sha256sums=('SKIP')
source_x86_64=("https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-${pkgver}/graalvm-ce-java${java_}-linux-amd64-${pkgver}.tar.gz")
source_aarch64=("https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-${pkgver}/graalvm-ce-java${java_}-linux-aarch64-${pkgver}.tar.gz")
sha256sums_x86_64=('882363c75d1b1782a48bbf7dd8b155ab231b0957fd5885941376d90b69f21b9e')
sha256sums_aarch64=('1ab64b35ed2478160bc6725d13ff5a2b9e31676b59ea3aaa9aca7a3a3db47132')

package() {
    cd "graalvm-ce-java${java_}-${pkgver}"
    mkdir -p "$pkgdir/usr/lib/jvm/java-${java_}-graalvm/"
    cp -a -t "$pkgdir/usr/lib/jvm/java-${java_}-graalvm/" *
    install -DTm644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    sed "s/JAVA/${java_}/g" < "../graalvm-rebuild-libpolyglot.hook" > "graalvm-jdk${java_}-rebuild-libpolyglot.hook"
    install -DTm644 "graalvm-jdk${java_}-rebuild-libpolyglot.hook" "$pkgdir/usr/share/libalpm/hooks/graalvm-jdk${java_}-rebuild-libpolyglot.hook"
}
