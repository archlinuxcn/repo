# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: Det <nimetonmaili g-mail>

pkgname=jdk
pkgver=11.0.2
_build=9
_hash=f51449fcd52f4d52b93a989c5c56ed3c
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
sha256sums=('7b4fd8ffcf53e9ff699d964a80e4abf9706b5bdb5644a765c2b96f99e3a2cdc8'
            '1052634cdcbf50ca14b864b58f3afa53de1706bdc9c593667c29974146212c54'
            '9a84d1b4dd969e867b2dbb6df0d0c44814729e0f1d0c61ab6c54d676eae83b3b'
            '73d686fd6e478a887a51451d7ada7c045f31ce299f65f45e50a793820ee99d85'
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
    
    # legal/licenses
    cp -a legal/* "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "$pkgname" "${pkgdir}/usr/share/licenses/java${_majver}-${pkgname}"
}
