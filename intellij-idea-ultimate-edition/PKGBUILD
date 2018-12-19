# Maintainer: Urs Wolfer <uwolfer @ fwo.ch>

pkgbase=intellij-idea-ultimate-edition
pkgname=(intellij-idea-ultimate-edition intellij-idea-ultimate-edition-jre)
pkgver=2018.3.2
_buildver=183.4886.37
pkgrel=1
arch=('any')
pkgdesc="An intelligent IDE for Java, Groovy and other programming languages with advanced refactoring features intensely focused on developer productivity."
url="https://www.jetbrains.com/idea/"
license=('Commercial')
options=(!strip)
source=("https://download.jetbrains.com/idea/ideaIU-$pkgver.tar.gz"
        "jetbrains-idea.desktop")
sha256sums=('885dc4fc4da5a277dcf149d7ab8fcb4ce09d1a8ed14e8e615bf6f817f386b7a4'
            '83af2ba8f9f14275a6684e79d6d4bd9b48cd852c047dacfc81324588fa2ff92b')

prepare() {
  # Extract the JRE from the main pacakge
  mv idea-IU-$_buildver/jre64 "$srcdir"/jre64
}

package_intellij-idea-ultimate-edition() {
  backup=("opt/$pkgname/bin/idea.vmoptions" "opt/${pkgname}/bin/idea64.vmoptions" "opt/${pkgname}/bin/idea.properties")
  depends=('giflib' 'libxtst')
  optdepends=('intellij-idea-ultimate-edition-jre: JetBrains custom JRE (Recommended)' 'java-environment: Required if intellij-idea-ultimate-edition-jre is not installed')

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
  mv "$srcdir"/jre64 "$pkgdir"/opt/$pkgbase
}

# vim:set ts=2 sw=2 et:
