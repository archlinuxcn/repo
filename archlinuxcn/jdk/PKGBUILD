# Maintainer : Daniel Bermond <dbermond@archlinux.org>
# Contributor: Det <nimetonmaili g-mail>

pkgname=jdk
pkgver=14
_build=36
_hash=076bab302c7b4508975440c56f6cc26a
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
sha256sums=('4639bbaecc9cc606f1a4b99fda1efcaefcbf57a7025b3828b095093a6c866afd'
            '4b38647428fc576f423197104a5721c0a07c825196dad426359c78fd19d1f823'
            'b517c7883a81a9951b3b1ddae0427619212808324482b5f02a9b7810328c2ce6'
            '3061d6d325067b6a0e7f900ee699322741b53fd6da200209844edc54530e2bef'
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
    rm "${pkgdir}/${_jvmdir}/bin/"{java,jjs,jpackage,jrunscript,keytool,rmid,rmiregistry}
    
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
    while read -r -d '' _file
    do
        install -D -m644 "$_file" "${pkgdir}/usr/share/${_file%.1}-jdk${_majver}.1"
    done < <(find man/man1 -type f -print0)
    rm "${pkgdir}/usr/share/man/man1/"{java,jjs,jpackage,jrunscript,keytool,rmid,rmiregistry}-jdk"${_majver}".1
    
    # legal/licenses
    cp -a legal/* "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "$pkgname" "${pkgdir}/usr/share/licenses/java${_majver}-${pkgname}"
}
