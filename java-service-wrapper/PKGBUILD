# Maintainer: skydrome <skydrome@i2pmail.org>
# Contributor: Artyom Olshevskiy <siasia@siasia>

pkgname='java-service-wrapper'
pkgver=3.5.34
pkgrel=1
pkgdesc="Enables a Java Application to be run as a Windows Service or Unix Daemon"
url="https://wrapper.tanukisoftware.com/doc/english/introduction.html"
arch=('i686' 'x86_64' 'aarch64' 'armv6h' 'armv7h')
license=('GPL2')
conflicts=('java-service-wrapper-bin')
makedepends=('apache-ant' 'java-environment>=7')
source=("https://wrapper.tanukisoftware.com/download/${pkgver}/wrapper_${pkgver}_src.tar.gz")
sha256sums=('d5c8f2530bba5ac5d938b25ccd2aee30f577e518098ae964d25be41fe06d3db6')

prepare() {
    sed -i "${srcdir}/wrapper_${pkgver}_src/build.xml" \
        -e "s:value=\"1.4\":value=\"1.7\":"

    # Prevent building the testsuite on the x64, this requires the cunit pkg
    # from the AUR, its a pain and useless to keep it a build-dep
    sed -i "${srcdir}/wrapper_${pkgver}_src/src/c/Makefile-linux-x86"*.make \
        -e "s|all: .*|all: init wrapper libwrapper.so|"
}

build() {
    cd "${srcdir}/wrapper_${pkgver}_src"
    source /etc/profile.d/apache-ant.sh
    source /etc/profile.d/jre.sh
    export JAVA_HOME="${JAVA_HOME:-/usr/lib/jvm/default}"

    [[ "$CARCH" = @(x86_64|aarch64) ]] && _bits=64 || _bits=32
    ant -Dbits=${_bits} -Dos.arch="$(uname -m)" jar compile-c-unix
}

package() {
    cd "${srcdir}/wrapper_${pkgver}_src"
    install -Dm755 bin/wrapper       "${pkgdir}/usr/bin/java-service-wrapper"
    install -Dm644 lib/libwrapper.so "${pkgdir}/usr/lib/java-service-wrapper/libwrapper.so"
    install -Dm644 lib/wrapper.jar   "${pkgdir}/usr/share/java/wrapper-${pkgver}.jar"
    install -Dm644 doc/wrapper-community-license*.txt "${pkgdir}/usr/share/licenses/java-service-wrapper/LICENSE"
    ln -s /usr/share/java/wrapper-${pkgver}.jar "${pkgdir}/usr/share/java/wrapper.jar"
}
