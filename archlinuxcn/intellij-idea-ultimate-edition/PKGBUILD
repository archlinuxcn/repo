# Maintainer: D. Can Celasun <can[at]dcc[dot]im>
# Co-Maintainer: Urs Wolfer <uwolfer @ fwo.ch>


pkgbase=intellij-idea-ultimate-edition
pkgname=(intellij-idea-ultimate-edition intellij-idea-ultimate-edition-jre)
pkgver=2022.3.1
pkgrel=1
_buildver=223.8214.52
jbr_ver=17.0.4
jbr_build=aarch64-b469
jbr_minor=53
arch=('x86_64' 'aarch64')
pkgdesc="An intelligent IDE for Java, Groovy and other programming languages with advanced refactoring features intensely focused on developer productivity."
url="https://www.jetbrains.com/idea/"
license=('custom:commercial')
options=(!strip)
source=("https://download.jetbrains.com/idea/ideaIU-$pkgver.tar.gz"
        "jetbrains-idea.desktop")
source_aarch64=("https://cache-redirector.jetbrains.com/intellij-jbr/jbr-$jbr_ver-linux-$jbr_build.$jbr_minor.tar.gz"
                "https://github.com/JetBrains/intellij-community/raw/master/bin/linux/aarch64/fsnotifier")
sha256sums=('ce807ba3a776e14f85dbd38f2744fc97e54318561eddd1c265f0d2cacc2565da'
            '83af2ba8f9f14275a6684e79d6d4bd9b48cd852c047dacfc81324588fa2ff92b')
sha256sums_aarch64=('b86531e3bc2f3760636e818dab80f3967935ffdf77996b19fda2bdb72f9b258b'
                    'eb3c61973d34f051dcd3a9ae628a6ee37cd2b24a1394673bb28421a6f39dae29')

prepare() {
  # Extract the JRE from the main pacakge
  rm -rf "$srcdir"/jbr

  # https://youtrack.jetbrains.com/articles/IDEA-A-48/JetBrains-IDEs-on-AArch64#linux
  if [ "${CARCH}" == "aarch64" ]; then
    cp -a "$srcdir"/jbr-$jbr_ver-$jbr_build "$srcdir"/jbr
    cp -f fsnotifier "$srcdir"/idea-IU-$_buildver/bin/fsnotifier
    chmod +x "$srcdir"/idea-IU-$_buildver/bin/fsnotifier
    rm -rf "$srcdir"/idea-IU-$_buildver/jbr
  else
    mv idea-IU-$_buildver/jbr "$srcdir"/jbr
  fi


}

package_intellij-idea-ultimate-edition() {
  backup=("opt/${pkgname}/bin/idea64.vmoptions" "opt/${pkgname}/bin/idea.properties")
  depends=('giflib' 'libxtst' 'libxrender')
  optdepends=(
    'intellij-idea-ultimate-edition-jre: JetBrains custom JRE (Recommended)' 'java-environment: Required if intellij-idea-ultimate-edition-jre is not installed'
    'libdbusmenu-glib: For global menu support'
  )

  cd "$srcdir"

  install -d "$pkgdir"/{opt/$pkgname,usr/bin}
  mv idea-IU-${_buildver}/* "$pkgdir"/opt/$pkgbase

  # https://youtrack.jetbrains.com/issue/IDEA-185828
  chmod +x "$pkgdir"/opt/$pkgbase/plugins/maven/lib/maven3/bin/mvn

  ln -s /opt/$pkgname/bin/idea.sh "$pkgdir"/usr/bin/$pkgname
  install -D -m644 "$srcdir"/jetbrains-idea.desktop "$pkgdir"/usr/share/applications/jetbrains-idea.desktop
  install -D -m644 "$pkgdir"/opt/$pkgbase/bin/idea.svg "$pkgdir"/usr/share/pixmaps/"$pkgname".svg

  # workaround FS#40934
  sed -i 's|lcd|on|'  "$pkgdir"/opt/$pkgname/bin/*.vmoptions
}

package_intellij-idea-ultimate-edition-jre() {
  install -d -m 755 "$pkgdir"/opt/$pkgbase
  mv "$srcdir"/jbr "$pkgdir"/opt/$pkgbase
}

# vim:set ts=2 sw=2 et:
