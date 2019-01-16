# Maintainer: trya <tryagainprod@gmail.com>

pkgname=kega-fusion
pkgver=3.63
pkgrel=17
pkgdesc="An emulator of classic Sega consoles, including SMS/GG, Genesis/Megadrive and add-ons"
url="http://www.carpeludum.com/kega-fusion"
license=('custom')
arch=('i686' 'x86_64')
depends=('alsa-lib' 'glu' 'libsm' 'gtk2' 'mpg123')
optdepends=('gtk-engines: libclearlooks.so library')
makedepends=('upx' 'ucl')
depends_x86_64=('lib32-alsa-lib' 'lib32-glu' 'lib32-libsm' 'lib32-gtk2' 'lib32-mpg123')
optdepends_x86_64=('lib32-gtk-engines: libclearlooks.so library'
                   'lib32-alsa-plugins: for PulseAudio users')
install="kega-fusion.install"
source=("http://ftp.slackware.org.uk/slacky/slackware-13.0/games/kega-fusion/3.63x/src/Fusion363x.tar.gz"
        "http://ftp.slackware.org.uk/slacky/slackware-13.0/games/kega-fusion/3.63x/src/Plugins(Linux).tar.gz"
        "http://trya.alwaysdata.net/linux/icons/kega-fusion.png"
        kega-fusion.sh kega-fusion.desktop Fusion.ini)
sha256sums=('8f245ead905bfb389da286a6ed94d627ec73e669b0247cbc87b34020fc674693'
            '1283a359e1cd82b5f23a121eab218bab8bdeeb488f98c58794b15803371bc234'
            '13ce738c8e10f92735085f624651a7c983093c785b40f4c2e4c7aee6506fe10b'
            'fc96b04a2341aea9d8810175ae0a45a714307a0292917ddc716656c00567fed6'
            '6cf957f9cd0b9e1cf439e511a0c7114d3b309f800076bc5fd0d407682cde1c4b'
            '317ee62d71b7fb8b0f083eea4f96eaffbf37466d7e277784ae2b663bbecaac5b')
options=(!strip)

package() {
  cd "$srcdir"

  # plugins
  install -d "$pkgdir/usr/lib/kega-fusion/plugins"
  install -m644 Plugins/*.rpi "$pkgdir/usr/lib/kega-fusion/plugins"
  if [ "$CARCH" == "x86_64" ]; then
    ln -s /usr/lib32/libmpg123.so.0 "$pkgdir/usr/lib/kega-fusion"  
  else
    ln -s /usr/lib/libmpg123.so.0 "$pkgdir/usr/lib/kega-fusion" 
  fi
  
  # default configuration and documentation
  install -Dm644 Fusion.ini "$pkgdir/usr/share/kega-fusion/Fusion.ini"
  install -d "$pkgdir/usr/share/doc/kega-fusion"
  install -m644 Fusion/*.txt "$pkgdir/usr/share/doc/kega-fusion"
  
  # startup script and executable
  install -Dm755 kega-fusion.sh "$pkgdir/usr/bin/kega-fusion"
  upx -d "$srcdir/Fusion/Fusion"
  install -Dm755 Fusion/Fusion "$pkgdir/usr/lib/kega-fusion"
  
  # desktop icon
  install -Dm644 kega-fusion.desktop "$pkgdir/usr/share/applications/kega-fusion.desktop"
  install -Dm644 kega-fusion.png "$pkgdir/usr/share/pixmaps/kega-fusion.png"
}
