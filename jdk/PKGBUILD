# Maintainer: Det <nimetonmaili g-mail>

pkgname=jdk
pkgver=9.0.1
_major=${pkgver/.*}
_build=11
pkgrel=1
pkgdesc="Oracle Java Development Kit"
arch=('x86_64')
url="http://www.oracle.com/technetwork/java/javase/downloads/index.html"
license=('custom:Oracle')
depends=('ca-certificates-java' 'hicolor-icon-theme' 'java-environment-common' 'java-runtime-common' 'nss' 'xdg-utils')
optdepends=('alsa-lib: for basic sound support'
            'eclipse-java: to use "Oracle Java Mission Control" plugins in Eclipse'
            'gtk2: for Gtk+ look and feel (desktop)')
provides=("java-runtime=$_major" "java-runtime-headless=$_major" "java-web-start=$_major" "java-environment=$_major"
          "java-runtime-jre=$_major" "java-runtime-headless-jre=$_major" "java-web-start-jre=$_major" "java-environment-jdk=$_major"
          "java-openjfx=$_major")
conflicts=("java-runtime-jre=$_major" "java-environment-jdk=$_major")

# Variables
DLAGENTS=('http::/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -b oraclelicense=a -o %o %u')
_jname=${pkgname}${_major}
_jvmdir=/usr/lib/jvm/java-$_major-$pkgname
 
backup=("etc/java-$_jname/management/jmxremote.access"
        "etc/java-$_jname/management/management.properties"
        "etc/java-$_jname/security/java.policy"
        "etc/java-$_jname/security/java.security"
        "etc/java-$_jname/security/javaws.policy"
        "etc/java-$_jname/fontconfig.properties.src"
        "etc/java-$_jname/logging.properties"
        "etc/java-$_jname/net.properties"
        "etc/java-$_jname/psfont.properties.ja"
        "etc/java-$_jname/psfontj2d.properties"
        "etc/java-$_jname/sound.properties")
options=('!strip') # JDK debug-symbols
install=$pkgname.install
source=("http://download.oracle.com/otn-pub/java/jdk/${pkgver}+${_build}/${pkgname}-${pkgver}_linux-x64_bin.tar.gz"
        "jconsole-$_jname.desktop"
        "jmc-$_jname.desktop"
        "jvisualvm-$_jname.desktop"
        "policytool-$_jname.desktop")
sha256sums=('2cdaf0ff92d0829b510edd883a4ac8322c02f2fc1beae95d048b6716076bc014'
            '100fd0162a4be04371d9d53121bd511aeb0a230475497a8c19ed0cff20915efc'
            'e4059de8ec0dee1a5eabd1d67a053509aa0009ba6e08739b11140c26f2fcc55a'
            '1f74cc627bd6a934681fe2d453058c21794d1435205c501f7fecdaf2c94f5485'
            'ff6684d7d5c26cc805e6f3918284a95b48223db4f37956f35a344373a2931aa4')

package() {
    cd $pkgname-$pkgver

    msg2 "Creating directory structure..."
    install -d "$pkgdir"/etc/.java/.systemPrefs
    install -d "$pkgdir"/usr/lib/jvm/java-$_major-$pkgname/bin
    install -d "$pkgdir"/usr/lib/mozilla/plugins
    install -d "$pkgdir"/usr/share/licenses/java$_major-$pkgname

    msg2 "Removing redundancies..."
    rm -r lib/desktop/icons/HighContrast
    rm -r lib/desktop/icons/HighContrastInverse
    rm -r lib/desktop/icons/LowContrast
    rm    lib/fontconfig.*.bfc
    rm    lib/fontconfig.*.properties.src

    msg2 "Moving contents..."
    mv * "$pkgdir"/$_jvmdir

    # Cd to the new playground
    cd "$pkgdir"/$_jvmdir

    # Create a placeholder 'jre' link
    ln -s . jre

    msg2 "Fixing directory structure..."
    # Suffix .desktops + icon (sun-jcontrol.png -> sun-jcontrol-$_jname.png)
    for i in $(find lib/desktop/ -type f); do
        rename -- "." "-$_jname." $i
    done

    # Link missing icons
    for i in $(find lib/desktop/icons/ -name "sun-jcontrol-$_jname.png" -type f); do
        ln -s "sun-jcontrol-$_jname.png" "${i/jcontrol/java}"
        ln -s "sun-jcontrol-$_jname.png" "${i/jcontrol/javaws}"
    done

    # Fix .desktop's
    sed -e '/JavaWS/!s|Name=Java|Name=Java '"$_major"'|' \
        -e "s|Name=JavaWS|Name=JavaWS $_major|" \
        -e "s|Comment=Java|Comment=Java $_major|" \
        -e "s|Exec=|Exec=$_jvmdir/bin/|" \
        -e "s|.png|-$_jname.png|" \
    -i lib/desktop/applications/*

    # Move .desktops + icons to /usr/share
    mv lib/desktop/* "$pkgdir"/usr/share/
    install -m644 "$srcdir"/*.desktop "$pkgdir"/usr/share/applications/

    # Move confs to /etc and link back to /usr: /usr/lib/jvm/java-$_jname/conf -> /etc
    for old_usr_path in $(find conf/ -type f); do
        # New location
        new_etc_path="/etc/java-$_jname/${old_usr_path/conf\/}"

        # Move /link
        install -Dm644 "$old_usr_path" "$pkgdir/$new_etc_path"
        ln -sf "$new_etc_path" "$old_usr_path"
    done

    # Move confs to /etc and link back to /usr: /usr/lib/jvm/java-$_jname/lib -> /etc
    for new_etc_path in ${backup[@]}; do
        # Old location
        old_usr_path="lib/${new_etc_path#*$_jname/}"

        # Move/link
        if [[ -f $old_usr_path ]]; then
            install -Dm644 "$old_usr_path" "$pkgdir/$new_etc_path"
            ln -sf "/$new_etc_path" "$old_usr_path"
        fi
    done

    # Link NPAPI plugin
    ln -sf $_jvmdir/lib/libnpjp2.so "$pkgdir"/usr/lib/mozilla/plugins/libnpjp2-$_jname.so

    # Replace JKS keystore with 'ca-certificates-java'
    ln -sf /etc/ssl/certs/java/cacerts lib/security/cacerts

    # Move/link licenses
    mv legal/ "$pkgdir"/usr/share/licenses/java$_major-$pkgname/
    ln -sf /usr/share/licenses/java$_major-$pkgname/ "$pkgdir"/usr/share/licenses/$pkgname

    # msg2 "Enabling Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy..."
    # # Replace default "strong", but limited, cryptography to get an "unlimited strength" one for
    # # things like 256-bit AES. Enabled by default in OpenJDK:
    # # - http://suhothayan.blogspot.com/2012/05/how-to-install-java-cryptography.html
    # # - http://www.eyrie.org/~eagle/notes/debian/jce-policy.html
    # sed -i "s/crypto.policy=limited/crypto.policy=unlimited/" "$pkgdir"/etc/java-$_jname/security/java.security

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
