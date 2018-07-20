# Maintainer: Michael Lass <bevan@bi-co.net>
# Contributor: Sebastian Wolf < sebastian at melonkru dot de >
# Contributor: gost < gostrc at gmail dot com >
# Contributor: Mikolaj Pastuszko <deluminathor@gmail.com>
# Contributor: Stefan Seemayer < mail at semicolonsoftware dot de >
# Contributor: Gordin < 9ordin @t gmail dot com >
# Contributor: David Davis < davisd<a@t>davisd.com >

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=yed
pkgver=3.18.1
pkgrel=2
epoch=1
pkgdesc='Very powerful graph editor written in java'
arch=('any')
url='http://www.yworks.com/en/products_yed_about.html'
license=('custom')
depends=('archlinux-java-run>=4' 'java-openjfx>=8' 'java-openjfx<11'

         # Additional dependencies for the JavaFX UI, determined using
         # ldd /usr/lib/jvm/java-8-openjdk/jre/lib/amd64/libglass.so|awk '{print $3}'|xargs pacman -Qo|awk '{print $4}'|sort -u
         'atk'
         'bzip2'
         'cairo'
         'expat'
         'fontconfig'
         'freetype2'
         'fribidi'
         'gcc-libs'
         'gdk-pixbuf2'
         'glib2'
         'glibc'
         'graphite'
         'gtk2'
         'harfbuzz'
         'libdatrie'
         'libffi'
         'libpng'
         'libthai'
         'libutil-linux'
         'libx11'
         'libxau'
         'libxcb'
         'libxcomposite'
         'libxcursor'
         'libxdamage'
         'libxdmcp'
         'libxext'
         'libxfixes'
         'libxi'
         'libxinerama'
         'libxrandr'
         'libxrender'
         'libxtst'
         'pango'
         'pcre'
         'pixman'
         'zlib'
         )
source=("https://www.yworks.com/resources/yed/demo/yEd-${pkgver}.zip"
        'yed.desktop'
        'yed')
sha256sums=('6aefd87cd925b4a4c86871a3772de243b4e520a86f82158189ae8c19a9a5ecf8'
            '342dba6defac88d035253b22e6377d9570858f59367cd486dba4a4dba1621f91'
            '2752e6ccc5cb5e19f483e5fd5f3274e81c8ef32d77c92b0d18951c8325179abd')

install=${pkgname}.install

package() {
  # Install jars
  install -Dm644 ${srcdir}/yed-${pkgver}/yed.jar ${pkgdir}/usr/share/java/yed/yed.jar
  install -dm755 ${pkgdir}/usr/share/java/yed/lib
  install -m644 ${srcdir}/yed-${pkgver}/lib/* ${pkgdir}/usr/share/java/yed/lib/

  # Install license
  install -Dm644 ${srcdir}/yed-${pkgver}/license.html ${pkgdir}/usr/share/licenses/yed/license.html

  # Install icon
  install -Dm644 ${srcdir}/yed-${pkgver}/icons/yicon32.png ${pkgdir}/usr/share/pixmaps/yed.png

  # Install .desktop file
  install -Dm644 ${srcdir}/yed.desktop ${pkgdir}/usr/share/applications/yed.desktop

  # Install run script
  install -Dm755 ${srcdir}/yed ${pkgdir}/usr/bin/yed
}
