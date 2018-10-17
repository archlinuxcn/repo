# Maintainer: Det <nimetonmaili g-mail>

pkgname=jdk
pkgver=11.0.1
_major=${pkgver/.*}
_build=13
_hash=90cf5d8f270a4347a95050320eef3fb7
_jname=${pkgname}${_major}
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
          "$_jname")
conflicts=("$_jname")
_jvmdir=/usr/lib/jvm/java-$_major-$pkgname
backup=("etc/java-$_jname/management/jmxremote.access"
        "etc/java-$_jname/management/management.properties"
        "etc/java-$_jname/security/java.policy"
        "etc/java-$_jname/security/java.security"
        "etc/java-$_jname/logging.properties"
        "etc/java-$_jname/net.properties"
        "etc/java-$_jname/sound.properties")
options=('!strip') # JDK debug-symbols
install=$pkgname.install
source=("http://download.oracle.com/otn-pub/java/jdk/${pkgver}+${_build}/${_hash}/${pkgname}-${pkgver}_linux-x64_bin.tar.gz"
        'java.desktop'
        'jconsole.desktop'
        'java_16.png'
        'java_48.png')
sha256sums=('e7fd856bacad04b6dbf3606094b6a81fa9930d6dbb044bbd787be7ea93abc885'
            'a7514af04107ed225ebafefd9997ee0332e8ecc4ef12a7dec5aaff7e8a2385d1'
            'f0a863cfdf57e963d74a84b914096c79951e7a6001a35370acf4bebfc5f4a081'
            'd27fec1d74f7a3081c3d175ed184d15383666dc7f02cc0f7126f11549879c6ed'
            '7cf8ca096e6d6e425b3434446b0835537d0fc7fe64b3ccba7a55f7bd86c7e176')
            
DLAGENTS=('http::/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -b oraclelicense=a -o %o %u')

package() {
  cd $pkgname-$pkgver

  msg2 "Creating directory structure..."
  install -d "$pkgdir"/etc/.java/.systemPrefs
  install -d "$pkgdir"/usr/lib/jvm/java-$_major-$pkgname/bin
  install -d "$pkgdir"/usr/lib/mozilla/plugins
  install -d "$pkgdir"/usr/share/licenses/java$_major-$pkgname

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
  mv legal/ "$pkgdir"/usr/share/licenses/java$_major-$pkgname/
  ln -sf /usr/share/licenses/java$_major-$pkgname/ "$pkgdir"/usr/share/licenses/$pkgname

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
