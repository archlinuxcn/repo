# Maintainer: Det <nimetonmaili g-mail>

_pkgname=jdk
pkgname=jdk-devel
_major=11
_build=26
_jname=${_pkgname}${_major}
pkgver=${_major}b${_build}
pkgrel=1
pkgdesc="Oracle Java $_major Development Kit Snapshot"
arch=('x86_64')
url="http://jdk.java.net/$_major/"
license=('custom:Oracle')
depends=('ca-certificates-java' 'hicolor-icon-theme' 'java-environment-common' 'java-runtime-common' 'nss' 'xdg-utils')
optdepends=('alsa-lib: for basic sound support'
            'eclipse-java: to use "Oracle Java Mission Control" plugins in Eclipse'
            'gtk2: for Gtk+ look and feel (desktop)')
provides=("java-runtime=$_major" "java-runtime-headless=$_major" "java-web-start=$_major" "java-environment=$_major"
          "java-runtime-jre=$_major" "java-runtime-headless-jre=$_major" "java-web-start-jre=$_major" "java-environment-jdk=$_major"
          "java-openjfx=$_major" "$_jname")
conflicts=("$_jname")
_jvmdir=/usr/lib/jvm/java-$_major-$_pkgname
backup=("etc/java-$_jname/management/jmxremote.access"
        "etc/java-$_jname/management/management.properties"
        "etc/java-$_jname/security/java.policy"
        "etc/java-$_jname/security/java.security"
        "etc/java-$_jname/logging.properties"
        "etc/java-$_jname/net.properties"
        "etc/java-$_jname/sound.properties")
options=('!strip') # JDK debug-symbols
install=$pkgname.install
source=("https://download.java.net/java/early_access/jdk${_major}/${_build}/BCL/${_pkgname}-${_major}-ea+${_build}_linux-x64_bin.tar.gz"
        'java.desktop'
        'jconsole.desktop'
        'java_16.png'
        'java_48.png'
        'LICENSE-Early-Adopter-Development-Agreement.txt')
sha256sums=('c647bfd816eb1637d7e749d27a1340fe8d8050e9908fe97de7a2a8b42b296428'
            'ed7392cbad258da943d39e9a5fab1ee6ab6a287ac0c20172805d5dbfc5accedb'
            'e8544f5384d541c16973543ace0f812e2dea657eed551a70baebb1a0cd9f3771'
            'd27fec1d74f7a3081c3d175ed184d15383666dc7f02cc0f7126f11549879c6ed'
            '7cf8ca096e6d6e425b3434446b0835537d0fc7fe64b3ccba7a55f7bd86c7e176'
            '36d48f14c16f0dcc98a8ce2301fd2a111701e6f59a7da08b0e51fdb3e2f9ca89')

package() {
  cd $_pkgname-$_major

  msg2 "Creating directory structure..."
  install -d "$pkgdir"/etc/.java/.systemPrefs
  install -d "$pkgdir"/usr/lib/jvm/java-$_major-$_pkgname/bin
  install -d "$pkgdir"/usr/lib/mozilla/plugins
  install -d "$pkgdir"/usr/share/licenses/java$_major-$_pkgname

  msg2 "Moving contents..."
  mv * "$pkgdir"/$_jvmdir

  # Cd to the new playground
  cd "$pkgdir"/$_jvmdir

  msg2 "Fixing directory structure..."
  # Create a placeholder 'jre' link
  ln -s . jre

  # Move + suffix .desktops
  for i in $(printf -- '%s\n' "${source[@]}" | grep desktop | cut -d "." -f1); do
    install -Dm644 "$srcdir"/$i.desktop "$pkgdir"/usr/share/applications/$i-$_jname.desktop
  done

  # Move + suffix icons
  for i in 16 48; do
    install -Dm644 "$srcdir"/java_$i.png "$pkgdir"/usr/share/icons/hicolor/${i}x$i/apps/java-$_jname.png
  done

  # Write versions to .desktops + .install
  sed -i "s/<version>/$_major/" "$pkgdir"/usr/share/applications/* "$startdir"/$pkgname.install

  # Move confs to /etc and link back to /usr: /usr/lib/jvm/java-$_jname/conf -> /etc
  for sub_path in $(find conf/ -type f); do
    # New location
    new_etc_path="/etc/java-$_jname/${sub_path/conf\/}"

    # Move & link
    install -Dm644 "$sub_path" "$pkgdir/$new_etc_path"
    ln -sf "$new_etc_path" "$sub_path"
  done

  # Link NPAPI plugin
  ln -sf $_jvmdir/lib/libnpjp2.so "$pkgdir"/usr/lib/mozilla/plugins/libnpjp2-$_jname.so

  # Replace JKS keystore with 'ca-certificates-java'
  ln -sf /etc/ssl/certs/java/cacerts lib/security/cacerts

  # Move & link licenses
  mv legal/ "$pkgdir"/usr/share/licenses/java$_major-$_pkgname/
  install -m644 "$srcdir"/LICENSE-Early-Adopter-Development-Agreement.txt "$pkgdir"/usr/share/licenses/java$_major-$_pkgname/
  ln -sf /usr/share/licenses/java$_major-$_pkgname/ "$pkgdir"/usr/share/licenses/$pkgname

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
