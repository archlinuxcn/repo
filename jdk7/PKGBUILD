# Maintainer: Jochen Schalanda <jochen+aur@schalanda.name>
# Contributor: Det
# Contributor: isiachi <isiachi@rhyeworld.it>
# Based on jre: https://aur.archlinux.org/packages.php?ID=51908

_pkgname=jdk
pkgname=${_pkgname}7
_major=7
_minor=80
_build=b15
_pkg=${_major}u$_minor
pkgver=$_major.$_minor
pkgrel=2
pkgdesc="Oracle Java $_major Development Kit"
arch=('i686' 'x86_64')
url=http://www.oracle.com/technetwork/java/javase/downloads/index.html
license=('custom')
depends=('ca-certificates-java' 'desktop-file-utils' 'hicolor-icon-theme' 'java-environment-common'
         'java-runtime-common' 'libx11' 'libxrender' 'libxslt' 'libxtst' 'shared-mime-info' 'xdg-utils')
optdepends=('alsa-lib: for basic sound support'
            'derby: for Oracle Apache Derby Java database (AUR)'
            'eclipse: "Oracle Java Mission Control" plugins for Eclipse'
            'gtk2: for Gtk+ look and feel (desktop)'
            'ttf-font: fonts'
            'visualvm: for lightweight profiling capabilities'
            'jdk7-docs: Oracle JDK 7 documentation'
            'java7-jce_ustrength: Unrestricted cryptographic libraries')
provides=("java-runtime=$_major" "java-runtime-headless=$_major" "java-web-start=$_major" "java-environment=$_major"
          "java-runtime-jre=$_major" "java-runtime-headless-jre=$_major" "java-web-start-jre=$_major" "java-environment-jdk=$_major")

# Variables
_arch=x64
_arch2=amd64
if [[ $CARCH = i686 ]]; then
  _arch=i586
  _arch2=i386
fi
DLAGENTS=('http::/usr/bin/curl -LC - -b oraclelicense=a -O')
_jname=jdk${_major}
_jvmdir=/usr/lib/jvm/java-$_major-${_pkgname}
backup=("etc/java-$_jname/$_arch2/jvm.cfg"
        "etc/java-$_jname/$_arch2/server/Xusage.txt"
        "etc/java-$_jname/images/cursors/cursors.properties"
        "etc/java-$_jname/management/jmxremote.access"
        "etc/java-$_jname/management/jmxremote.password.template"
        "etc/java-$_jname/management/management.properties"
        "etc/java-$_jname/management/snmp.acl.template"
        "etc/java-$_jname/security/java.policy"
        "etc/java-$_jname/security/java.security"
        "etc/java-$_jname/security/javaws.policy"
        "etc/java-$_jname/calendars.properties"
        "etc/java-$_jname/content-types.properties"
        "etc/java-$_jname/flavormap.properties"
        "etc/java-$_jname/fontconfig.properties.src"
        "etc/java-$_jname/javafx.properties"
        "etc/java-$_jname/jvm.hprof.txt"
        "etc/java-$_jname/logging.properties"
        "etc/java-$_jname/net.properties"
        "etc/java-$_jname/psfont.properties.ja"
        "etc/java-$_jname/psfontj2d.properties"
        "etc/java-$_jname/sound.properties")
install=jdk.install
source=("http://download.oracle.com/otn-pub/java/${_pkgname}/$_pkg-$_build/${_pkgname}-$_pkg-linux-$_arch.tar.gz"
        "jconsole-$_jname.desktop"
        "jmc-$_jname.desktop"
        "jvisualvm-$_jname.desktop"
        "policytool-$_jname.desktop")
sha256sums=('bad9a731639655118740bee119139c1ed019737ec802a630dd7ad7aab4309623'
            'ab4a2e49825df4e6055e90283f9d0b432e28a6d66f0f7ed659985e7c53847751'
            '535d86adeb183340442c307e0ba579d0f7718b30fe6ed319bdc91bb2cee47763'
            'cf20cdf39583e1a992a85ab366437b80217951aeb9dec6b2ee54b77b4d0af6be'
            'af15efe8b471d0ab147f4a88215aed3fc50b1a605ce31100dfa7a404f29e85b1')
[ "$CARCH" = 'i686' ] && sha256sums[0]='9ded1318a7223cf6e09ac4b6ee4db1f4c5d1aef1d3d291f6db8491a32eaa57ba'

package() {
  msg2 "Creating required dirs"
  cd ${_pkgname}1.${_major}.0_${_minor}
  install -d "$pkgdir"/{usr/{lib/{jvm/java-$_major-$_pkgname/bin,mozilla/plugins},share/licenses/java$_major-$_pkgname},etc/.java/.systemPrefs}

  msg2 "Preparing"
  # Link duplicate binaries from jre/
  for i in $(ls jre/bin/); do
    ln -sf $_jvmdir/jre/bin/$i bin/$i
  done

  # Link NPAPI plugin
  ln -sf $_jvmdir/jre/lib/$_arch2/libnpjp2.so "$pkgdir"/usr/lib/mozilla/plugins/libnpjp2-$_jname.so

  # Replace JKS keystore with 'ca-certificates-java'
  ln -sf /etc/ssl/certs/java/cacerts jre/lib/security/cacerts

  # Suffix .desktops, icons and MIME packages
  for i in $(find jre/lib/desktop/ -type f); do
    rename -- "." "-$_jname." $i
  done

  # Suffix man pages
  rename -- ".1" "-$_jname.1" man/{,ja_JP.UTF-8/}man1/*

  # Fix .desktop paths
  sed -e "s,Exec=,&$_jvmdir/jre/bin/," \
      -e "s/\.png/-$_jname/" \
      -i jre/lib/desktop/applications/*

  msg2 "Removing redundancies"
  rm -r db/ jre/lib/fontconfig.*.{bfc,properties.src} jre/plugin/ jre/{COPYRIGHT,LICENSE,README,*.txt} lib/visualvm/ man/ja

  msg2 "Moving stuff in place"
  # .desktops + icons
  mv jre/lib/desktop/* "$pkgdir"/usr/share/
  install -m644 "$srcdir"/*.desktop "$pkgdir"/usr/share/applications/

  # Move/link configs: /usr/lib/jvm/java-$_jname/jre/lib -> /etc
  for new_etc in ${backup[@]}; do
    old_usr=jre/lib/${new_etc#*$_jname/}
    install -Dm644 $old_usr "$pkgdir"/$new_etc
    ln -sf /$new_etc $old_usr
  done

  # Man pages
  mv man/ja_JP.UTF-8/ man/ja/
  mv man/ "$pkgdir"/usr/share/

  # Licenses
  mv COPYRIGHT LICENSE *.txt "$pkgdir"/usr/share/licenses/java$_major-$_pkgname/
  ln -sf /usr/share/licenses/java$_major-$pkgname/ "$pkgdir"/usr/share/licenses/$pkgname

  # Do the move
  mv * "$pkgdir"/$_jvmdir

  msg2 "Enabling copy+paste to unsigned applets"
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
