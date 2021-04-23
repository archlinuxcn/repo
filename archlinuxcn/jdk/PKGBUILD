# Maintainer : Daniel Bermond <dbermond@archlinux.org>
# Contributor: Det <nimetonmaili g-mail>

pkgbase=jdk
pkgname=('jre' 'jdk')
pkgver=16.0.1
_build=9
_hash=7147401fd7354114ac51ef3e1328291f
_majver="${pkgver%%.*}"
pkgrel=1
pkgdesc='Oracle Java'
arch=('x86_64')
url='https://www.oracle.com/java/'
license=('custom')
source=("https://download.oracle.com/otn-pub/java/jdk/${pkgver}+${_build}/${_hash}/jdk-${pkgver}_linux-x64_bin.tar.gz"
        'java.desktop'
        'jconsole.desktop'
        'jshell.desktop'
        'java_16.png'
        'java_48.png')
sha256sums=('caa0bfc0e9ee52f45c8f8ca803a23f132ef551297c6b9331b091110c5740a9bf'
            '9fc4cd168fd3e0d654093c1b2dd070f627ffae9b7f5c2c0741bac0b5c1ed0635'
            '12b6e632e38e2c2ef54d6b03976290ca649380a89f78b5dae8827423eae52a1b'
            'b2fd5a8f273a103569bf03af6f4ff4d3a5448472abc79b8649cecd0ee9313fc7'
            'd27fec1d74f7a3081c3d175ed184d15383666dc7f02cc0f7126f11549879c6ed'
            '7cf8ca096e6d6e425b3434446b0835537d0fc7fe64b3ccba7a55f7bd86c7e176')

DLAGENTS=('https::/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -b oraclelicense=a -o %o %u')

package_jre() {
    pkgdesc='Oracle Java Runtime Environment'
    depends=('java-runtime-common' 'ca-certificates-utils' 'freetype2' 'libxtst'
             'libxrender' 'libnet')
    optdepends=('alsa-lib: for basic sound support')
    provides=("java-runtime=${_majver}" "java-runtime-headless=${_majver}"
              "java-runtime-jre=${_majver}" "java-runtime-headless-jre=${_majver}")
    backup=("etc/java-${pkgbase}/management/jmxremote.access"
            "etc/java-${pkgbase}/management/jmxremote.password.template"
            "etc/java-${pkgbase}/management/management.properties"
            "etc/java-${pkgbase}/security/policy/limited/default_US_export.policy"
            "etc/java-${pkgbase}/security/policy/limited/default_local.policy"
            "etc/java-${pkgbase}/security/policy/limited/exempt_local.policy"
            "etc/java-${pkgbase}/security/policy/unlimited/default_US_export.policy"
            "etc/java-${pkgbase}/security/policy/unlimited/default_local.policy"
            "etc/java-${pkgbase}/security/policy/README.txt"
            "etc/java-${pkgbase}/security/java.policy"
            "etc/java-${pkgbase}/security/java.security"
            "etc/java-${pkgbase}/logging.properties"
            "etc/java-${pkgbase}/net.properties"
            "etc/java-${pkgbase}/sound.properties")
    install=jre.install
    
    cd "jdk-${pkgver}"
    local _jvmdir="/usr/lib/jvm/java-${_majver}-jdk"
    
    install -d -m755 "${pkgdir}/etc"
    install -d -m755 "${pkgdir}/${_jvmdir}"
    install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}"
    
    # conf
    cp -a conf "${pkgdir}/etc/java-${pkgbase}"
    ln -s "../../../../etc/java-${pkgbase}" "${pkgdir}/${_jvmdir}/conf"
    
    # bin
    install -D -m755 bin/{java,jpackage,jrunscript} -t "${pkgdir}/${_jvmdir}/bin"
    install -D -m755 bin/{keytool,rmid,rmiregistry}     -t "${pkgdir}/${_jvmdir}/bin"
    
    # libs
    cp -a lib "${pkgdir}/${_jvmdir}"
    rm -r "${pkgdir}/${_jvmdir}/lib/jfr"
    rm "${pkgdir}/${_jvmdir}/lib/"{ct.sym,libattach.so,libsaproc.so,src.zip}
    
    # man pages
    local _file
    for _file in man/man1/{java,jpackage,jrunscript,keytool,rmid,rmiregistry}.1
    do
        install -D -m644 "$_file" "${pkgdir}/usr/share/${_file%.1}-jdk${_majver}.1"
    done
    
    install -D -m644 release -t "${pkgdir}/${_jvmdir}"
    
    # replace JKS keystore with ca-certificates-utils
    rm "${pkgdir}${_jvmdir}/lib/security/cacerts"
    ln -s /etc/ssl/certs/java/cacerts "${pkgdir}${_jvmdir}/lib/security/cacerts"
    
    # legal/licenses
    cp -a legal/* "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "$pkgname" "${pkgdir}/usr/share/licenses/java-${pkgname}"
    ln -s "../../../share/licenses/${pkgname}" "${pkgdir}/${_jvmdir}/legal"
}

package_jdk() {
    pkgdesc='Oracle Java Development Kit'
    depends=('java-environment-common' "jre>=${_majver}" "jre<$((_majver + 1))" 'zlib' 'hicolor-icon-theme')
    provides=("java-environment=${_majver}" "java-environment-jdk=${_majver}")
    install=jdk.install
    
    cd "jdk-${pkgver}"
    local _jvmdir="/usr/lib/jvm/java-${_majver}-${pkgname}"
    
    install -d -m755 "${pkgdir}/${_jvmdir}"
    install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}"
    
    # bin
    cp -a bin "${pkgdir}/${_jvmdir}"
    rm "${pkgdir}/${_jvmdir}/bin/"{java,jpackage,jrunscript,keytool,rmid,rmiregistry}
    
    # libs
    install -D -m644 lib/ct.sym       -t "${pkgdir}/${_jvmdir}/lib"
    install -D -m644 lib/libattach.so -t "${pkgdir}/${_jvmdir}/lib"
    install -D -m644 lib/libsaproc.so -t "${pkgdir}/${_jvmdir}/lib"
    cp -a lib/jfr "${pkgdir}/${_jvmdir}/lib"
    
    cp -a include "${pkgdir}/${_jvmdir}"
    cp -a jmods   "${pkgdir}/${_jvmdir}"
    
    install -D -m644 lib/src.zip -t "${pkgdir}/${_jvmdir}/lib"
    
    # desktop and icons
    install -D -m644 "${srcdir}/java.desktop"     "${pkgdir}/usr/share/applications/java-java-jdk.desktop"
    install -D -m644 "${srcdir}/jconsole.desktop" "${pkgdir}/usr/share/applications/jconsole-java-jdk.desktop"
    install -D -m644 "${srcdir}/jshell.desktop"   "${pkgdir}/usr/share/applications/jshell-java-jdk.desktop"
    install -D -m644 "${srcdir}/java_16.png" "${pkgdir}/usr/share/icons/hicolor/16x16/apps/java-jdk.png"
    install -D -m644 "${srcdir}/java_48.png" "${pkgdir}/usr/share/icons/hicolor/48x48/apps/java-jdk.png"
    
    # man pages
    local _file
    while read -r -d '' _file
    do
        install -D -m644 "$_file" "${pkgdir}/usr/share/${_file%.1}-jdk${_majver}.1"
    done < <(find man/man1 -type f -print0)
    rm "${pkgdir}/usr/share/man/man1/"{java,jpackage,jrunscript,keytool,rmid,rmiregistry}-jdk"${_majver}".1
    
    # legal/licenses
    cp -a legal/* "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "$pkgname" "${pkgdir}/usr/share/licenses/java-${pkgname}"
}
