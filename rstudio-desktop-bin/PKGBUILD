# Maintainer: Meow < leon.tty1 at gmail dot com >

# Get download links and md5sums for latest version of RStudio desktop
## R code #############
#
#  require(XML)
#  page = htmlTreeParse("http://www.rstudio.com/products/rstudio/download/",useInternalNodes = T)
#  links = sapply(getNodeSet(page,'//table[@class="downloads"]/thead/tr/th[text()="Installers"]/../../..//a[contains(@href,".deb")]'),xmlGetAttr,'href')
#  md5sums = sapply(getNodeSet(page,'//table[@class="downloads"]/thead/tr/th[text()="Installers"]/../../..//a[contains(@href,".deb")]/../..//code'),xmlValue)
#  print(cbind(links,md5sums))
#
#######################

# NOTE: If you are experiencing segmentation fault, delete the ".rstudio-desktop" folder from your home directory then restart the program should fix the issue.

pkgname=rstudio-desktop-bin
pkgver=1.1.463
pkgrel=1
pkgdesc="An integrated development environment (IDE) for R (binary from RStudio official repository)"
arch=('i686' 'x86_64')
license=('GPL')
url="http://www.rstudio.org/"
depends=('r' 'hicolor-icon-theme' 'libxcomposite' 'libxslt' 'shared-mime-info' 'libxrandr')
#makedepends=('patchelf')
optdepends=('pandoc: markdown support'
            'pandoc-citeproc: markdown support')
conflicts=('rstudio-desktop' 'rstudio-desktop-git' 'rstudio-desktop-preview-bin')
provides=("rstudio-desktop=${pkgver}")
options=(!strip)

md5sums_i686=(
8a6755fa9fae2bafce289df3358aaf63
795a3ca3f2048c4dc32d25560e191c35
eca697b2b8efbed3d2241f6b0c8c15e4)
md5sums_x86_64=(
bc50d6bd34926c1cc3ae4a209d67d649
84e61f5eda991b978fa168d6762f7990
391ba54997d6faddbfe41a185a823ee4)

source_i686=("https://download1.rstudio.org/rstudio-${pkgver}-i386.deb"
"http://archive.ubuntu.com/ubuntu/pool/main/g/gstreamer0.10/libgstreamer0.10-0_0.10.36-1.2ubuntu3_i386.deb"
"http://security.ubuntu.com/ubuntu/pool/main/g/gst-plugins-base0.10/libgstreamer-plugins-base0.10-0_0.10.36-1.1ubuntu2.1_i386.deb")
source_x86_64=("https://download1.rstudio.org/rstudio-${pkgver}-amd64.deb"
"http://archive.ubuntu.com/ubuntu/pool/main/g/gstreamer0.10/libgstreamer0.10-0_0.10.36-1.2ubuntu3_amd64.deb"
"http://security.ubuntu.com/ubuntu/pool/main/g/gst-plugins-base0.10/libgstreamer-plugins-base0.10-0_0.10.36-1.1ubuntu2.1_amd64.deb")

install="$pkgname".install

package() {

	shopt -s extglob

  msg "Converting debian package..."

  cd "$srcdir"
  tar zxpf data.tar.gz -C "$pkgdir"
  install -dm755 "$pkgdir/usr/bin"

  ARCH=${CARCH/686/386/}
  ARCH=${ARCH/x86_64/amd64}

  ar x libgstreamer0.10-0_0.10.36-1.2ubuntu3_${ARCH}.deb
  tar Jxf data.tar.xz \
      --wildcards \
      -C "${pkgdir}/usr/lib/rstudio/bin" \
      ./usr/lib/${CARCH/686/386}-linux-gnu/libgstreamer-0.10.so.\* \
      ./usr/lib/${CARCH/686/386}-linux-gnu/libgstbase-0.10.so.\* \
      --strip-components=4

  ar x libgstreamer-plugins-base0.10-0_0.10.36-1.1ubuntu2.1_${ARCH}.deb
  tar Jxf data.tar.xz \
      --wildcards \
      -C "${pkgdir}/usr/lib/rstudio/bin" \
      ./usr/lib/${CARCH/686/386/}-linux-gnu/libgstapp-0.10.so.\* \
      ./usr/lib/${CARCH/686/386/}-linux-gnu/libgstinterfaces-0.10.so.\* \
      ./usr/lib/${CARCH/686/386/}-linux-gnu/libgstpbutils-0.10.so.\* \
      ./usr/lib/${CARCH/686/386/}-linux-gnu/libgstvideo-0.10.so.\* \
      --strip-components=4

  #cd "$pkgdir/usr/lib/rstudio/bin"
  #ln -sf /usr/lib/libncursesw.so.6 libtinfo.so.5
  #ln -sf /usr/lib/libedit.so.0  libedit.so.2

#  cd "$pkgdir/usr/lib/rstudio/bin/rsclang"
#  patchelf --set-rpath '$ORIGIN/..' libclang.so

  cd "$pkgdir/usr/lib/rstudio/bin/pandoc"
  ln -sf /usr/bin/pandoc ./
  ln -sf /usr/bin/pandoc-citeproc ./

#  cd "$pkgdir/usr/lib/rstudio/bin/plugins"
#  ls */*.so | xargs -n1 patchelf --set-rpath '$ORIGIN/../..'

  find "$pkgdir/usr" -type d -print0 | xargs -0 chmod 755
  find "$pkgdir/usr" -type f -name '*.so.*' -print0 | xargs -0 chmod 644

  cd "$pkgdir/usr/lib/rstudio/bin"
  ls libQt*.so.*| grep '\.[0-9]\{1,\}\.[0-9]\{1,\}\.[0-9]\{1,\}$'|
  while read x;do
    if [[ ! -e "${x%.+([0-9]).+([0-9])}" ]];then
      ln -s "$x" "${x%.+([0-9]).+([0-9])}"
    fi
  done
  ls lib*.so.* | grep '\.so\.[0-9]\{1,\}\.[0-9]\{1,\}$'|
  while read x;do
    if [[ ! -e "${x%.+([0-9])}" ]];then
      ln -s "$x" "${x%.+([0-9])}"
    fi
  done

  ln -sf /usr/lib/qt/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so plugins/platforminputcontexts/
  ls /usr/lib/libFcitxQt5WidgetsAddons.so{,.*} \
      /usr/lib/libFcitxQt5DBusAddons.so{,.*} |
      while read x;do
          ln -sf "$x" ./
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
