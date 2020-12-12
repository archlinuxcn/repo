# Contributor: chrisl echo archlinux@c2h0r1i2s4t5o6p7h8e9r-l3u4n1a.com|sed 's/[0-9]//g'

pkgname=cemu
pkgver=1.22.1
pkgrel=1
pkgdesc="Wii U emulator (via wine). Includes the Cemuhook plugin"
arch=(x86_64)
url="http://cemu.info/"
license=('custom')
depends=('wine' 'winetricks')
_cemuhookver=1159_0573
source=(
  cemu.sh
  cemu.xpm
  cemu.desktop
  http://cemu.info/releases/cemu_${pkgver}.zip
  https://files.sshnuke.net/cemuhook_${_cemuhookver}.zip
  https://web.archive.org/web/20180907210517if_/https://files.sshnuke.net/sharedFonts.7z
)
# The link for the sharedFonts comes from here: https://github.com/decaf-emu/decaf-emu/issues/29#issuecomment-315511347
noextract=("cemuhook_${_cemuhookver}.zip")
install=${pkgname}.install

# Sometimes, they update the zip file without changing its name, which causes the md5sum to fail.
# If you notice this, please mark this package as out-of-date in the aur website and I'll fix it.

md5sums=('cb1dbf192ad3237a087260aa16758e95'
         '54d70005a8975812ab54fcfef53f7bde'
         '57b3e9277e965d75b10df8ec87711f01'
         '7124513626fb044b937636acece25e6c'
         'f5f0de02b9df62d5b6018c7a82e6d43b'
         '336a0bc0e44eede4ddf613a0eebf3bb9')

options=(!strip)

build() {
  cd $srcdir/
  cd cemu_$pkgver
  bsdtar -x -f $srcdir/cemuhook_${_cemuhookver}.zip
}
package() {
  cd $srcdir
  install -d -m755 $pkgdir/usr/share/
  install -d -m755 $pkgdir/usr/share/$pkgname
  install -d -m755 $pkgdir/usr/bin
  install -m755 cemu.sh $pkgdir/usr/bin/$pkgname
  install -d -m755 $pkgdir/usr/share/applications
  install -d -m755 $pkgdir/usr/share/pixmaps
  install -m644 cemu.desktop $pkgdir/usr/share/applications
  install -m644 cemu.xpm $pkgdir/usr/share/pixmaps/cemu.xpm
  cp -R sharedFonts $pkgdir/usr/share/$pkgname
  cd cemu_$pkgver
  install -m644 Cemu.exe $pkgdir/usr/share/$pkgname
  install -m644 dbghelp.dll $pkgdir/usr/share/$pkgname
  install -m644 keystone.dll $pkgdir/usr/share/$pkgname
  cp -R gameProfiles $pkgdir/usr/share/$pkgname
  mkdir $pkgdir/usr/share/$pkgname/mlc01
  cp -R shaderCache $pkgdir/usr/share/$pkgname
  find $pkgdir/usr/share/$pkgname -type f -exec chmod 644 {} \;
  find $pkgdir/usr/share/$pkgname -type d -exec chmod 755 {} \;
}

