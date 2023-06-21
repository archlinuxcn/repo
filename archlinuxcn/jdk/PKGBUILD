# Maintainer : Daniel Bermond <dbermond@archlinux.org>
# Contributor: Det <nimetonmaili g-mail>

pkgbase=jdk
pkgname=('jre' 'jdk' 'jdk-doc')
pkgver=20.0.1
_build=9
_hash=b4887098932d415489976708ad6d1a4b
_majver="${pkgver%%.*}"
pkgrel=1
pkgdesc='Oracle Java'
arch=('x86_64')
url='https://www.oracle.com/java/'
license=('custom')
makedepends=('python-html2text')
source=("https://download.oracle.com/java/${_majver}/archive/jdk-${pkgver}_linux-x64_bin.tar.gz"
        "https://download.oracle.com/otn_software/java/jdk/${pkgver}+${_build}/${_hash}/jdk-${pkgver}_doc-all.zip"
        "jdk-${_majver}_doc-license.html"::"https://download.oracle.com/otndocs/jcp/java_se-${_majver}-final-spec/license.html"
        'java.desktop'
        'jconsole.desktop'
        'jshell.desktop'
        'java_16.png'
        'java_48.png'
        'LICENSE')
noextract=("jdk-${pkgver}_doc-all.zip")
sha256sums=('bb118683feb4d66476198c8176a9845a9125bf5b303089b56b4b59ff9a544ccf'
            '36f9fa700951cb53373554be69337294ab92269f45ddce66db8c9575fbf94a8f'
            'b5703ac13aa6ff7c8323b090a2996adc262895b6fcba6264262db3ac4789aec9'
            'def8848024c91d814e5f43a10d091c9d30917ab74b5098a7c22a5993e2f67370'
            '8a95581b09260cd67a26518b6a8282f3e67396b19a66d4e5f32f8285fca096be'
            'b51dda29ac5b8a0d3386354010ccaae1de628c462d1f6bde3cfc28729b24ae0c'
            'd27fec1d74f7a3081c3d175ed184d15383666dc7f02cc0f7126f11549879c6ed'
            '7cf8ca096e6d6e425b3434446b0835537d0fc7fe64b3ccba7a55f7bd86c7e176'
            '20becfcac0bdeaa29a76e6966d727f8cc79381354cbd5d530cdec823954df19f')

DLAGENTS=('https::/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -b oraclelicense=a -o %o %u')

prepare() {
    mkdir -p "jdk-doc-${pkgver}"
    bsdtar -x -f "jdk-${pkgver}_doc-all.zip" -C "jdk-doc-${pkgver}" --strip-components='1'
    html2text "jdk-${_majver}_doc-license.html" > LICENSE-doc
}

package_jre() {
    pkgdesc+=' Runtime Environment'
    depends=('java-runtime-common' 'ca-certificates-utils' 'freetype2' 'libx11' 'libxext'
             'libxi' 'libxtst' 'libxrender')
    optdepends=('alsa-lib: for basic sound support'
                'gtk2: for the Gtk+ 2 look and feel - desktop usage'
                'gtk3: for the Gtk+ 3 look and feel - desktop usage')
    provides=("java-runtime=${_majver}" "java-runtime-jdk${_majver}"
              "jre${_majver}-jdk=${pkgver}-${pkgrel}"
              "java-runtime-headless=${_majver}" "java-runtime-headless-jdk=${_majver}"
              "jre${_majver}-jdk-headless="${pkgver}-${pkgrel})
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
    install -D -m755 bin/{java,jfr,jrunscript,jwebserver} -t "${pkgdir}/${_jvmdir}/bin"
    install -D -m755 bin/{keytool,rmiregistry} -t "${pkgdir}/${_jvmdir}/bin"
    
    # libs
    cp -a lib "${pkgdir}/${_jvmdir}"
    rm "${pkgdir}/${_jvmdir}/lib/"{ct.sym,libattach.so,libsaproc.so,src.zip}
    
    # man pages
    local _file
    for _file in man/man1/{java,jfr,jrunscript,keytool,rmiregistry}.1
    do
        install -D -m644 "$_file" "${pkgdir}/usr/share/${_file%.1}-jdk${_majver}.1"
    done
    
    install -D -m644 release -t "${pkgdir}/${_jvmdir}"
    
    # link JKS keystore from ca-certificates-utils
    rm "${pkgdir}/${_jvmdir}/lib/security/cacerts"
    ln -s /etc/ssl/certs/java/cacerts "${pkgdir}${_jvmdir}/lib/security/cacerts"
    
    # legal/licenses
    cp -a legal/* "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "$pkgname" "${pkgdir}/usr/share/licenses/java-${pkgname}"
    ln -s "../../../share/licenses/${pkgname}" "${pkgdir}/${_jvmdir}/legal"
    install -D -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_jdk() {
    pkgdesc+=' Development Kit'
    depends=('java-environment-common' "jre=${pkgver}-${pkgrel}" 'zlib'
             'hicolor-icon-theme')
    provides=("java-environment=${_majver}" "java-environment-jdk=${_majver}"
              "jdk${_majver}-jdk=${pkgver}-${pkgrel}")
    install=jdk.install
    
    cd "jdk-${pkgver}"
    local _jvmdir="/usr/lib/jvm/java-${_majver}-${pkgname}"
    
    install -d -m755 "${pkgdir}/${_jvmdir}"
    install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}"
    
    # bin
    cp -a bin "${pkgdir}/${_jvmdir}"
    rm "${pkgdir}/${_jvmdir}/bin/"{java,jfr,jrunscript,keytool,rmiregistry,jwebserver}
    
    # libs
    install -D -m644 lib/ct.sym       -t "${pkgdir}/${_jvmdir}/lib"
    install -D -m644 lib/libattach.so -t "${pkgdir}/${_jvmdir}/lib"
    install -D -m644 lib/libsaproc.so -t "${pkgdir}/${_jvmdir}/lib"
    
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
    rm "${pkgdir}/usr/share/man/man1/"{java,jfr,jrunscript,keytool,rmiregistry}-jdk"${_majver}".1
    
    # legal/licenses
    cp -a legal/* "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "$pkgname" "${pkgdir}/usr/share/licenses/java-${pkgname}"
    install -D -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_jdk-doc() {
    pkgdesc+=' documentation'
    arch=('any')
    
    install -d -m755 "${pkgdir}/usr/share"/{doc,licenses}
    cp -dr --no-preserve='ownership' "jdk-doc-${pkgver}" "${pkgdir}/usr/share/doc/java-jdk"
    mv "${pkgdir}/usr/share/doc/java-jdk/legal" "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 LICENSE-doc "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    ln -s "../../licenses/${pkgname}" "${pkgdir}/usr/share/doc/java-jdk/legal"
}
