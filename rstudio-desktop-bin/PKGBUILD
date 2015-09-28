# Maintainer: Meow < a.li.devtty at gmail dot com >

# Get download links and md5 sums for latest version of RStudio desktop
cat <<_EOF_ >/dev/null
## R code #############
require(XML)
page = htmlTreeParse("http://www.rstudio.com/products/rstudio/download/",useInternalNodes = T)
links = sapply(getNodeSet(page,'//table[@class="downloads"]/thead/tr/th[text()="Installers"]/../../..//a[contains(@href,".deb")]'),xmlGetAttr,'href')
md5sums = sapply(getNodeSet(page,'//table[@class="downloads"]/thead/tr/th[text()="Installers"]/../../..//a[contains(@href,".deb")]/../..//code'),xmlValue)
print(cbind(links,md5sums))
#######################
_EOF_

pkgname=rstudio-desktop-bin
pkgver=0.99.484
pkgrel=9
pkgdesc="A new integrated development environment (IDE) for R (binary version from RStudio official website)"
arch=('i686' 'x86_64')
license=('GPL')
url="http://www.rstudio.org/"
depends=('r' 'gstreamer0.10-base' 'hicolor-icon-theme' 'libxcomposite' 'libxslt' 'shared-mime-info' 'libxrandr' 'gtk2')
makedepends=('patchelf')
#'qt5-imageformats' 'qt5-webkit'
conflicts=('rstudio-desktop' 'rstudio-desktop-git' 'rstudio-desktop-preview-bin')
provides=("rstudio-desktop=${pkgver}")
options=(!strip)


_x86md5=fe0c5d879c128c5d3d035bec73150fcc
_x64md5=ee2a2ab6fce06e3936afd4b5968f7d0c

case "$CARCH" in
	'i686')
		_arch=i386
    _archx=
		md5sums=($_x86md5)
		;;
	'x86_64')
		_arch=amd64
    _archx=64
		md5sums=($_x64md5)
		;;
esac    
source=("http://download1.rstudio.org/rstudio-${pkgver}-${_arch}.deb")
install="$pkgname".install

package() {
  msg "Converting debian package..."

  cd "$srcdir"
  tar zxpf data.tar.gz -C "$pkgdir"
  install -dm755 "$pkgdir/usr/bin"

  #cd "$pkgdir/usr/lib/rstudio/bin"
  #ls lib*.so.* | grep -v libedit | grep -v libtinfo | tr \\n \\0 |xargs -0 rm
  #rm -rf plugins

  #cd "$pkgdir/usr/lib/rstudio/bin/rsclang"
  #ln -sf /usr/lib/libclang.so ./

  cd "$pkgdir/usr/lib/rstudio/bin"
  ln -sf /usr/lib/libncursesw.so.6 libtinfo.so.5
  ln -sf /usr/lib/libedit.so.0  libedit.so.2

  cd "$pkgdir/usr/lib/rstudio/bin/rsclang"
  patchelf --set-rpath '$ORIGIN/..' libclang.so

  cd "$pkgdir/usr/lib/rstudio/bin/plugins"
  ls */*.so | xargs -n1 patchelf --set-rpath '$ORIGIN/../..'

  find "$pkgdir/usr" -type d -print0 | xargs -0 chmod 755

  cd "$pkgdir/usr/bin"
  #ln -s -f ../lib/rstudio/bin/rstudio rstudio-bin
  echo '#!/bin/sh
export QT_DIR=/usr/lib/rstudio/bin
export QT_PLUGIN_PATH=$QT_DIR/plugins
export QT_QPA_PLATFORM_PLUGIN_PATH=$QT_PLUGIN_PATH/platforms
export KDEDIRS=/usr
exec /usr/lib/rstudio/bin/rstudio
' > "$pkgdir/usr/bin/rstudio-bin"
  chmod 755 "$pkgdir/usr/bin/rstudio-bin"

  sed -i 's|/usr/lib/rstudio/bin/rstudio|/usr/bin/rstudio-bin|' "$pkgdir/usr/share/applications/rstudio.desktop"
}
# vim:ft=sh tabstop=2 expandtab
