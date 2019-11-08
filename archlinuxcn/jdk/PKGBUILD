# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: Det <nimetonmaili g-mail>

pkgname=jdk
pkgver=13.0.1
_build=9
_hash=cec27d702aa74d5a8630c65ae61e4305
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
sha256sums=('593f25d35493ec3edc1af341dc5ad1aad455aef1fdb7e596af56df754625a09d'
            '91c70275116cdfea1a0459fe76dd0d916bfecd12faafb8fd1bcf9b7306e85cb6'
            'b9ad3acc8ba7ead6e8374f590588bb136d3a0e6d80e80a048d75ff63ca2325d0'
            '34f05e1ce1a33ec65d94388428ccbad2a441460f9cc7b42a69dbc75255ec92bf'
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
    while read -r -d '' _file
    do
        install -D -m644 "$_file" "${pkgdir}/usr/share/${_file%.1}-jdk${_majver}.1"
    done < <(find man/man1 -type f -print0)
    rm "${pkgdir}/usr/share/man/man1/"{java,jjs,jrunscript,keytool,pack200}-jdk"${_majver}".1
    rm "${pkgdir}/usr/share/man/man1/"{rmid,rmiregistry,unpack200}-jdk"${_majver}".1
    
    # legal/licenses
    cp -a legal/* "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "$pkgname" "${pkgdir}/usr/share/licenses/java${_majver}-${pkgname}"
}
