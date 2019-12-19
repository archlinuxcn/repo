# Maintainer: Urs Wolfer <uwolfer @ fwo.ch>

pkgbase=intellij-idea-ultimate-edition
pkgname=(intellij-idea-ultimate-edition intellij-idea-ultimate-edition-jre)
pkgver=2019.3.1
_buildver=193.5662.53
pkgrel=1
arch=('any')
pkgdesc="An intelligent IDE for Java, Groovy and other programming languages with advanced refactoring features intensely focused on developer productivity."
url="https://www.jetbrains.com/idea/"
license=('Commercial')
options=(!strip)
source=("https://download.jetbrains.com/idea/ideaIU-$pkgver.tar.gz"
        "jetbrains-idea.desktop")
sha256sums=('87543537c524c6f67c88e1e2af3865bb233099bf405db2df131a66ebf4655532'
            '83af2ba8f9f14275a6684e79d6d4bd9b48cd852c047dacfc81324588fa2ff92b')

prepare() {
  # Extract the JRE from the main pacakge
  rm -rf "$srcdir"/jbr
  mv idea-IU-$_buildver/jbr "$srcdir"/jbr
}

package_intellij-idea-ultimate-edition() {
  backup=("opt/$pkgname/bin/idea.vmoptions" "opt/${pkgname}/bin/idea64.vmoptions" "opt/${pkgname}/bin/idea.properties")
  depends=('giflib' 'libxtst')
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
  install -D -m644 "$pkgdir"/opt/$pkgbase/bin/idea.png "$pkgdir"/usr/share/pixmaps/"$pkgname".png

  # workaround FS#40934
  sed -i 's|lcd|on|'  "$pkgdir"/opt/$pkgname/bin/*.vmoptions
}

package_intellij-idea-ultimate-edition-jre() {
  arch=('x86_64')
  install -d -m 755 "$pkgdir"/opt/$pkgbase
  mv "$srcdir"/jbr "$pkgdir"/opt/$pkgbase
}

# vim:set ts=2 sw=2 et:
