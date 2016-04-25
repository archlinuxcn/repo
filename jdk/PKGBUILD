# Maintainer: Det <nimetonmaili g-mail>
# Based on jre: https://aur.archlinux.org/packages/jre/

pkgname=jdk
_major=8
_minor=92
_build=b14
pkgver=${_major}u${_minor}
pkgrel=1
pkgdesc="Oracle Java Development Kit"
arch=('i686' 'x86_64')
url=http://www.oracle.com/technetwork/java/javase/downloads/index.html
license=('custom')
depends=('ca-certificates-java' 'desktop-file-utils' 'hicolor-icon-theme' 'java-environment-common'
         'java-runtime-common' 'libx11' 'libxrender' 'libxslt' 'libxtst' 'shared-mime-info' 'xdg-utils')
optdepends=('alsa-lib: for basic sound support'
            'eclipse: to use "Oracle Java Mission Control" plugins in Eclipse'
            'gtk2: for Gtk+ look and feel (desktop)'
            'ttf-font: fonts')
provides=("java-runtime=$_major" "java-runtime-headless=$_major" "java-web-start=$_major" "java-environment=$_major"
          "java-runtime-jre=$_major" "java-runtime-headless-jre=$_major" "java-web-start-jre=$_major" "java-environment-jdk=$_major"
          "java-openjfx=$_major")

# Variables
DLAGENTS=('http::/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -b oraclelicense=a -o %o %u')
_jname=${pkgname}${_major}
_jvmdir=/usr/lib/jvm/java-$_major-$pkgname

backup=("etc/java-$_jname/amd64/jvm.cfg"
        "etc/java-$_jname/images/cursors/cursors.properties"
        "etc/java-$_jname/management/jmxremote.access"
        "etc/java-$_jname/management/management.properties"
        "etc/java-$_jname/security/java.policy"
        "etc/java-$_jname/security/java.security"
        "etc/java-$_jname/security/javaws.policy"
        "etc/java-$_jname/content-types.properties"
        "etc/java-$_jname/flavormap.properties"
        "etc/java-$_jname/fontconfig.properties.src"
        "etc/java-$_jname/logging.properties"
        "etc/java-$_jname/net.properties"
        "etc/java-$_jname/psfont.properties.ja"
        "etc/java-$_jname/psfontj2d.properties"
        "etc/java-$_jname/sound.properties")
[[ $CARCH = i686 ]] && backup[0]="etc/java-$_jname/i386/jvm.cfg"
options=('!strip') # JDK debug-symbols
install=$pkgname.install
source=("http://download.oracle.com/otn-pub/java/jce/$_major/jce_policy-$_major.zip"
        "jconsole-$_jname.desktop"
        "jmc-$_jname.desktop"
        "jvisualvm-$_jname.desktop"
        "policytool-$_jname.desktop")
source_i686=("http://download.oracle.com/otn-pub/java/jdk/$pkgver-$_build/$pkgname-$pkgver-linux-i586.tar.gz")
source_x86_64=("http://download.oracle.com/otn-pub/java/jdk/$pkgver-$_build/$pkgname-$pkgver-linux-x64.tar.gz")
md5sums=('b3c7031bc65c28c2340302065e7d00d3'
         'b4f0da18e03f7a9623cb073b65dde6c1'
         '8f0ebcead2aecad67fbd12ef8ced1503'
         'a4a21b064ff9f3c3f3fdb95edf5ac6f3'
         '98245ddb13914a74f0cc5a028fffddca')
md5sums_i686=('0f2839ff1066438123dac3404702a3ef')
md5sums_x86_64=('65a1cc17ea362453a6e0eb4f13be76e4')
## Alternative mirror, if your local one is throttled:
#source_x86_64=("http://ftp.wsisiz.edu.pl/pub/pc/pozyteczne%20oprogramowanie/java/$pkgname-$pkgver-linux-x64.gz")

package() {
    cd ${pkgname}1.${_major}.0_${_minor}

    msg2 "Creating directory structure..."
    install -d "$pkgdir"/etc/.java/.systemPrefs
    install -d "$pkgdir"/usr/lib/jvm/java-$_major-$pkgname/bin
    install -d "$pkgdir"/usr/lib/mozilla/plugins
    install -d "$pkgdir"/usr/share/licenses/java$_major-$pkgname

    msg2 "Removing redundancies..."
    rm    db/bin/*.bat
    rm    db/3RDPARTY
    rm    db/LICENSE
    rm -r jre/lib/desktop/icons/HighContrast/
    rm -r jre/lib/desktop/icons/HighContrastInverse/
    rm -r jre/lib/desktop/icons/LowContrast/
    rm    jre/lib/fontconfig.*.bfc
    rm    jre/lib/fontconfig.*.properties.src
    rm -r jre/plugin/
    rm    jre/*.txt
    rm    jre/COPYRIGHT
    rm    jre/LICENSE
    rm    jre/README
    rm    man/ja

    msg2 "Moving contents..."
    mv * "$pkgdir"/$_jvmdir

    # Cd to the new playground
    cd "$pkgdir"/$_jvmdir

    msg2 "Fixing directory structure..."
    # Replace duplicate binaries in bin/ with links to jre/bin/
    for i in $(ls jre/bin/); do
        ln -sf "$_jvmdir/jre/bin/$i" "bin/$i"
    done

    # Suffix .desktops + icons (sun-java.png -> sun-java-$_jname.png)
    for i in $(find jre/lib/desktop/ -type f); do
        rename -- "." "-$_jname." $i
    done

    # Fix .desktop paths
    sed -e "s|Exec=|Exec=$_jvmdir/jre/bin/|" \
        -e "s|.png|-$_jname.png|" \
    -i jre/lib/desktop/applications/*

    # Move .desktops + icons to /usr/share
    mv jre/lib/desktop/* "$pkgdir"/usr/share/
    install -m644 "$srcdir"/*.desktop "$pkgdir"/usr/share/applications/

    # Move confs to /etc and link back to /usr: /usr/lib/jvm/java-$_jname/jre/lib -> /etc
    for new_etc_path in ${backup[@]}; do
        # Old location
        old_usr_path="jre/lib/${new_etc_path#*$_jname/}"

        # Move
        install -Dm644 "$old_usr_path" "$pkgdir/$new_etc_path"
        ln -sf "/$new_etc_path" "$old_usr_path"
    done

    # Link NPAPI plugin
    case "$CARCH" in
        i686)   ln -sf $_jvmdir/jre/lib/i386/libnpjp2.so  "$pkgdir"/usr/lib/mozilla/plugins/libnpjp2-$_jname.so ;;
        x86_64) ln -sf $_jvmdir/jre/lib/amd64/libnpjp2.so "$pkgdir"/usr/lib/mozilla/plugins/libnpjp2-$_jname.so ;;
    esac

    # Replace JKS keystore with 'ca-certificates-java'
    ln -sf /etc/ssl/certs/java/cacerts jre/lib/security/cacerts

    # Suffix man pages
    for i in $(find man/ -type f); do
        mv "$i" "${i/.1}-$_jname.1"
    done

    # Move man pages
    mv man/ja_JP.UTF-8/ man/ja
    mv man/ "$pkgdir"/usr/share

    # Move/link licenses
    mv db/NOTICE COPYRIGHT LICENSE *.txt "$pkgdir"/usr/share/licenses/java$_major-$pkgname/
    ln -sf /usr/share/licenses/java$_major-$pkgname/ "$pkgdir"/usr/share/licenses/$pkgname

    msg2 "Installing Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files..."
    # Replace default "strong", but limited, cryptography to get an "unlimited strength" one for
    # things like 256-bit AES. Enabled by default in OpenJDK:
    # - http://suhothayan.blogspot.com/2012/05/how-to-install-java-cryptography.html
    # - http://www.eyrie.org/~eagle/notes/debian/jce-policy.html
    install -m644 "$srcdir"/UnlimitedJCEPolicyJDK$_major/*.jar jre/lib/security/
    install -Dm644 "$srcdir"/UnlimitedJCEPolicyJDK$_major/README.txt \
                   "$pkgdir"/usr/share/doc/$pkgname/README_-_Java_JCE_Unlimited_Strength.txt

    msg2 "Enabling copy+paste in unsigned applets..."
    # Copy/paste from system clipboard to unsigned Java applets has been disabled since 6u24:
    # - https://blogs.oracle.com/kyle/entry/copy_and_paste_in_java
    # - http://slightlyrandombrokenthoughts.blogspot.com/2011/03/oracle-java-applet-clipboard-injection.html
    _line=$(awk '/permission/{a=NR}; END{print a}' "$pkgdir"/etc/java-$_jname/security/java.policy)
    sed "$_line a\\\\n \
        // (AUR) Allow unsigned applets to read system clipboard, see:\n \
        // - https://blogs.oracle.com/kyle/entry/copy_and_paste_in_java\n \
        // - http://slightlyrandombrokenthoughts.blogspot.com/2011/03/oracle-java-applet-clipboard-injection.html\n \
        permission java.awt.AWTPermission \"accessClipboard\";" \
    -i "$pkgdir"/etc/java-$_jname/security/java.policy
}
