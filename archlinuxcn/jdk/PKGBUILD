# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: Det <nimetonmaili g-mail>

pkgname=jdk
pkgver=12.0.1
_build=12
_hash=69cfe15208a647278a19ef0990eea691
_majver="${pkgver%%.*}"
_next="$((_majver + 1))"
pkgrel=1
pkgdesc='Oracle Java Development Kit'
arch=('x86_64')
url='https://www.oracle.com/java/'
license=('custom')
depends=('java-environment-common' "jre>=${_majver}" "jre<${_next}" 'zlib' 'hicolor-icon-theme')
provides=("java-environment=${_majver}" "java-environment-jdk=${_majver}")
install="${pkgname}.install"
source=("https://download.oracle.com/otn-pub/java/jdk/${pkgver}+${_build}/${_hash}/${pkgname}-${pkgver}_linux-x64_bin.tar.gz"
        'java.desktop'
        'jconsole.desktop'
        'jshell.desktop'
        'java_16.png'
        'java_48.png')
sha256sums=('9fd6dcdaf2cfca7da59e39b009a0f5bcd53bec2fb16105f7ca8d689cdab68d75'
            '7b348c5f6b6ce7df7f849a90f0bdbbdb5a2d6236ec05e96e0b160755cf87fd69'
            '74d52ebc46e1d6b104130c04209a9cf318163de022034239042a1981a6ffd60f'
            'd207bb3f4a55e329546d084d8b82b6c217177ff11ebcc85e6420b14b011b3cd1'
            'd27fec1d74f7a3081c3d175ed184d15383666dc7f02cc0f7126f11549879c6ed'
            '7cf8ca096e6d6e425b3434446b0835537d0fc7fe64b3ccba7a55f7bd86c7e176')
            
DLAGENTS=('https::/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -b oraclelicense=a -o %o %u')

package() {
    cd "jdk-${pkgver}"
    
    local _jvmdir="/usr/lib/jvm/java-${_majver}-${pkgname}"
    
    install -d -m755 "${pkgdir}/${_jvmdir}"
    install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}"
    
    # bin
    cp -a bin "${pkgdir}/${_jvmdir}"
    rm "${pkgdir}/${_jvmdir}/bin/"{java,jjs,jrunscript,keytool,pack200}
    rm "${pkgdir}/${_jvmdir}/bin/"{rmid,rmiregistry,unpack200}
    
    # libs
    install -D -m644 lib/ct.sym       -t "${pkgdir}/${_jvmdir}/lib"
    install -D -m644 lib/libattach.so -t "${pkgdir}/${_jvmdir}/lib"
    install -D -m644 lib/libsaproc.so -t "${pkgdir}/${_jvmdir}/lib"
    cp -a lib/jfr "${pkgdir}/${_jvmdir}/lib"
    
    cp -a include "${pkgdir}/${_jvmdir}"
    cp -a jmods   "${pkgdir}/${_jvmdir}"
    
    install -D -m644 lib/src.zip -t "${pkgdir}/${_jvmdir}/lib"
    
    # desktop and icons
    install -D -m644 "${srcdir}/java.desktop"     "${pkgdir}/usr/share/applications/java-java${_majver}-jdk.desktop"
    install -D -m644 "${srcdir}/jconsole.desktop" "${pkgdir}/usr/share/applications/jconsole-java${_majver}-jdk.desktop"
    install -D -m644 "${srcdir}/jshell.desktop"   "${pkgdir}/usr/share/applications/jshell-java${_majver}-jdk.desktop"
    install -D -m644 "${srcdir}/java_16.png" "${pkgdir}/usr/share/icons/hicolor/16x16/apps/java${_majver}-jdk.png"
    install -D -m644 "${srcdir}/java_48.png" "${pkgdir}/usr/share/icons/hicolor/48x48/apps/java${_majver}-jdk.png"
    
    # man pages
    local _file
    for _file in man/man1/*
    do
        install -D -m644 "$_file" "${pkgdir}/usr/share/${_file%.1}-jdk${_majver}.1"
    done
    rm "${pkgdir}/usr/share/man/man1/"{java,jjs,jrunscript,keytool,pack200}-jdk"${_majver}".1
    rm "${pkgdir}/usr/share/man/man1/"{rmid,rmiregistry,unpack200}-jdk"${_majver}".1
    
    # legal/licenses
    cp -a legal/* "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "$pkgname" "${pkgdir}/usr/share/licenses/java${_majver}-${pkgname}"
}
