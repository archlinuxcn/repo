# $Id$
# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Maintainer: Levente Polyak <anthraxx@archlinux.org>

pkgname=steam-libs
pkgver=1.0.0.52
pkgrel=4
pkgdesc='Collection of libraries to launch Steam without its runtime environment'
arch=('x86_64')
url='https://wiki.archlinux.org/index.php/Steam#Using_native_runtime'
license=('None')
depends=('lib32-alsa-lib' 'lib32-alsa-plugins' 'lib32-atk' 'lib32-cairo'
         'lib32-curl' 'lib32-dbus-glib' 'lib32-fontconfig' 'lib32-freetype2'
         'lib32-gconf' 'lib32-gdk-pixbuf2' 'lib32-glew1.10' 'lib32-glib2'
         'lib32-glu' 'lib32-gtk2' 'lib32-libcaca' 'lib32-libcanberra'
         'lib32-libcups' 'lib32-libcurl-compat' 'lib32-libcurl-gnutls'
         'lib32-libdbus' 'lib32-libdrm' 'lib32-libice' 'lib32-libjpeg6'
         'lib32-libnm-glib' 'lib32-libpng12' 'lib32-libpulse' 'lib32-libsm'
         'lib32-libtheora' 'lib32-libtiff4' 'lib32-libudev0' 'lib32-libusb'
         'lib32-libvorbis' 'lib32-libxcomposite' 'lib32-libxcursor'
         'lib32-libxft' 'lib32-libxi' 'lib32-libxinerama' 'lib32-libxmu'
         'lib32-libxrandr' 'lib32-libxrender' 'lib32-libxtst'
         'lib32-libxxf86vm' 'lib32-nspr' 'lib32-nss' 'lib32-openal'
         'lib32-pango' 'lib32-sdl' 'lib32-sdl2' 'lib32-sdl2_image'
         'lib32-sdl2_mixer' 'lib32-sdl_image' 'lib32-sdl_mixer'
         'lib32-sdl_ttf')
source=('steam-native'
        'steam-native.desktop')
sha256sums=('3e377d93d667d81efbbfb456760d4ce0f1b207085788693099839e6fcf26bca0'
            '88ee3daafe792a9eb9d6c2b8cb4429dd5da3b18737a0eae54d64296a6a878332')

package() {
  install -Dm 755 steam-native -t "${pkgdir}"/usr/bin/
  install -Dm 644 steam-native.desktop -t "${pkgdir}"/usr/share/applications/
}

# vim: ts=2 sw=2 et:

