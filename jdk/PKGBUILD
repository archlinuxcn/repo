# Maintainer: Det <nimetonmaili g-mail>

pkgname=jdk
pkgver=10.0.2
_major=${pkgver/.*}
_build=13
_hash=19aef61b38124481863b1413dce1855f
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
          "java-openjfx=$_major" "$_jname")
conflicts=("$_jname")
_jvmdir=/usr/lib/jvm/java-$_major-$pkgname
backup=("etc/java-$_jname/management/jmxremote.access"
        "etc/java-$_jname/management/management.properties"
        "etc/java-$_jname/security/java.policy"
        "etc/java-$_jname/security/java.security"
        "etc/java-$_jname/security/javaws.policy"
        "etc/java-$_jname/logging.properties"
        "etc/java-$_jname/net.properties"
        "etc/java-$_jname/sound.properties")
options=('!strip') # JDK debug-symbols
install=$pkgname.install
source=("http://download.oracle.com/otn-pub/java/jdk/${pkgver}+${_build}/${_hash}/${pkgname}-${pkgver}_linux-x64_bin.tar.gz"
        "jconsole.desktop"
        "jmc.desktop"
        "policytool.desktop")
sha256sums=('6633c20d53c50c20835364d0f3e172e0cbbce78fff81867488f22a6298fa372b'
            '3ea717825268a66837380c9ca2b076f02a3298d2df48c3450152fdaf1d0dbc6e'
            '365b33b197e6be65ad746e5ed864428e45ae1e24dba53aa7d9c71de0644cf4e2'
            '5dfde6ee531056571d9601d47fbb4a3e56062e4d611667a56ba7931ec7948b36')
            
DLAGENTS=('http::/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -b oraclelicense=a -o %o %u')

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
  rm  lib/fontconfig.*.bfc
  rm  lib/fontconfig.*.properties.src

  msg2 "Moving contents..."
  mv * "$pkgdir"/$_jvmdir

  # Cd to the new playground
  cd "$pkgdir"/$_jvmdir

  msg2 "Fixing directory structure..."
  # Create a placeholder 'jre' link
  ln -s . jre

  # Fix bundled .desktops
  sed -e "s|Exec=|Exec=$_jvmdir/bin/|" \
      -e "s|.png|-$_jname.png|" \
      -i lib/desktop/applications/*

  # Move .desktops + icons to /usr/share
  mv lib/desktop/* "$pkgdir"/usr/share/
  install -m644 "$srcdir"/*.desktop "$pkgdir"/usr/share/applications/

  # Suffix .desktops + icon (sun-jcontrol.png -> sun-jcontrol-$_jname.png)
  for i in $(find "$pkgdir"/usr/share/ -type f); do
    rename -- "." "-$_jname." $i
  done

  # Write versions to .desktops + .install
  sed -i "s/<version>/$_major/" "$pkgdir"/usr/share/applications/* "$startdir"/$pkgname.install

  # Link missing icons
  for i in $(find "$pkgdir"/usr/share/icons/ -name "sun-jcontrol-$_jname.png" -type f); do
    ln -s "sun-jcontrol-$_jname.png" "${i/jcontrol/java}"
    ln -s "sun-jcontrol-$_jname.png" "${i/jcontrol/javaws}"
  done

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
