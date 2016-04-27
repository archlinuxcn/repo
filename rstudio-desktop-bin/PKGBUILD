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
pkgver=0.99.896
pkgrel=1
pkgdesc="A new integrated development environment (IDE) for R (binary version from RStudio official website)"
arch=('i686' 'x86_64')
license=('GPL')
url="http://www.rstudio.org/"
depends=('r' 'gstreamer0.10-base' 'hicolor-icon-theme' 'libxcomposite' 'libxslt' 'shared-mime-info' 'libxrandr' 'pandoc' 'pandoc-citeproc')
makedepends=('patchelf')
conflicts=('rstudio-desktop' 'rstudio-desktop-git' 'rstudio-desktop-preview-bin')
provides=("rstudio-desktop=${pkgver}")
options=(!strip)


_x86md5=94f8742df675e0c076a24406d37df868
_x64md5=d7c4933a4a523c2168b6d5784eb4f8d2

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

	shopt -s extglob

  msg "Converting debian package..."

  cd "$srcdir"
  tar zxpf data.tar.gz -C "$pkgdir"
  install -dm755 "$pkgdir/usr/bin"

  cd "$pkgdir/usr/lib/rstudio/bin"
  ln -sf /usr/lib/libncursesw.so.6 libtinfo.so.5
  ln -sf /usr/lib/libedit.so.0  libedit.so.2

  cd "$pkgdir/usr/lib/rstudio/bin/rsclang"
  patchelf --set-rpath '$ORIGIN/..' libclang.so

  cd "$pkgdir/usr/lib/rstudio/bin/pandoc"
  ln -sf /usr/bin/pandoc ./
  ln -sf /usr/bin/pandoc-citeproc ./

  cd "$pkgdir/usr/lib/rstudio/bin/plugins"
  ls */*.so | xargs -n1 patchelf --set-rpath '$ORIGIN/../..'

  find "$pkgdir/usr" -type d -print0 | xargs -0 chmod 755
  find "$pkgdir/usr" -type f -name '*.so.*' -print0 | xargs -0 chmod 644

  cd "$pkgdir/usr/lib/rstudio/bin"
  ls libQt*.so.*| grep '\.[0-9]\{1,\}\.[0-9]\{1,\}\.[0-9]\{1,\}$'|
  while read x;do
    ln -sf "$x" "${x%.+([0-9]).+([0-9])}"
  done
  ls lib*.so.* | grep '\.so\.[0-9]\{1,\}\.[0-9]\{1,\}$'|
  while read x;do
    ln -sf "$x" "${x%.+([0-9])}"
  done

  cd "$pkgdir/usr/bin"
  #ln -s -f ../lib/rstudio/bin/rstudio rstudio-bin
  echo '#!/bin/sh
export QT_DIR=/usr/lib/rstudio/bin
export QT_PLUGIN_PATH=$QT_DIR/plugins
export QT_QPA_PLATFORM_PLUGIN_PATH=$QT_PLUGIN_PATH/platforms
export KDEDIRS=/usr
exec /usr/lib/rstudio/bin/rstudio "$@"
' > "$pkgdir/usr/bin/rstudio-bin"
  chmod 755 "$pkgdir/usr/bin/rstudio-bin"

  sed -i 's|/usr/lib/rstudio/bin/rstudio|/usr/bin/rstudio-bin|' "$pkgdir/usr/share/applications/rstudio.desktop"
}
# vim:ft=sh tabstop=2 expandtab
