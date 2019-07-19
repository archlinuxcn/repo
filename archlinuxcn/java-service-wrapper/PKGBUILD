# Maintainer: skydrome <skydrome@i2pmail.org>
# Contributor: Artyom Olshevskiy <siasia@siasia>

pkgname=java-service-wrapper
pkgver=3.5.40
pkgrel=1
pkgdesc="Enables a Java Application to be run as a Windows Service or Unix Daemon"
url="https://wrapper.tanukisoftware.com/doc/english/introduction.html"
arch=('i686' 'x86_64' 'aarch64' 'armv6h' 'armv7h')
license=('GPL2' 'custom:tanuki-community')
makedepends=('apache-ant' 'java-environment>=8')
source=("https://wrapper.tanukisoftware.com/download/${pkgver}/wrapper_${pkgver}_src.tar.gz"
        'java10.patch')
sha256sums=('8f8020ff193a8be4fe78395535f1aba9a3faee9e38de017f08980d92248329f0'
            '75ad8377c824d3fcd03b919c5744706b74fec5a35c32fe7d1f76f4cc8c1f9b98')

prepare() {
    cd "wrapper_${pkgver}_src"

    _ver=$(javac -version 2>&1 |awk '{print $2}')
    #msg "Detected Java $_ver"
    [[ "$_ver" =~ ^1[0-4]\. ]] &&
        patch -Np0 -i "$srcdir/java10.patch"

    # Prevent building the testsuite on the x64, this requires the cunit pkg
    # from the AUR, its a pain and useless to keep it a build-dep
    sed -i "src/c/Makefile-linux-x86"*.make \
        -e "s|all: .*|all: init wrapper libwrapper.so|"
}

build() {
    cd "wrapper_${pkgver}_src"
    export ANT_HOME=/usr/share/ant
    export ANT_OPTS="-Dfile.encoding=UTF-8"
    export JAVA_HOME="${JAVA_HOME:-/usr/lib/jvm/default}"

    [[ "$(javac -version 2>&1 |awk '{print $2}')" =~ ^1[0-4]\. ]] &&
                                          _target=11  || _target=8
    [[ "$CARCH" = @(x86_64|aarch64) ]] && _bits=64    || _bits=32
    [[ "$CARCH" = arm*              ]] && _arch=armhf || _arch=x86

    ant -Dbits="$_bits" -Ddist.arch="$_arch" -Djavac.target.version="$_target" \
        jar compile-c-unix
}

package() {
    cd "wrapper_${pkgver}_src"
    install -Dm755 bin/wrapper       "${pkgdir}/usr/bin/java-service-wrapper"
    install -Dm644 lib/libwrapper.so "${pkgdir}/usr/lib/java-service-wrapper/libwrapper.so"
    install -Dm644 lib/wrapper.jar   "${pkgdir}/usr/share/java/wrapper-${pkgver}.jar"
    install -Dm644 doc/wrapper-community-license*.txt "${pkgdir}/usr/share/licenses/java-service-wrapper/LICENSE"
    ln -s /usr/share/java/wrapper-${pkgver}.jar "${pkgdir}/usr/share/java/wrapper.jar"
}
