# $Id: PKGBUILD 266875 2017-11-15 14:29:11Z foutrelis $
# Maintainer: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: yugrotavele <yugrotavele@archlinux.us>
# Contributor: Paolo Stivanin <admin@polslinux.it>

pkgname=winff
pkgver=1.5.5+5475df4
pkgrel=1
pkgdesc='GUI for ffmpeg'
url='https://github.com/WinFF/winff/'
license=('GPL3')
arch=('x86_64')
depends=('ffmpeg' 'gtk2')
makedepends=('lazarus' 'lazarus-gtk2' 'gendesk' 'tar' 'git')
source=('git+https://github.com/WinFF/winff.git#commit=5475df4')
md5sums=('SKIP')

prepare() {
  gendesk -n -f \
    --pkgname "$pkgname" \
    --pkgdesc "$pkgdesc" \
    --genericname 'Video converter' \
    --categories 'AudioVideo;AudioVideoEditing;GTK'
}

build() {
  cd "$pkgname/$pkgname"

  lazbuild --lazarusdir=/usr/lib/lazarus winff.lpr --ws=gtk2
}

package() {
  cd "$pkgname/$pkgname"

  install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -d "$pkgdir/usr/share/winff/"
  find . -name "*.xml" \
    -exec install -Dm644 {} "$pkgdir/usr/share/winff/" \; &> /dev/null
  install -Dm644 "$srcdir/winff.desktop" \
    "$pkgdir/usr/share/applications/winff.desktop"
  install -Dm644 'winff-icons/48x48/winff.png' \
    "$pkgdir/usr/share/pixmaps/winff.png"
  for size in 16x16 24x24 32x32 48x48; do
    install -Dm644 "winff-icons/$size/winff.png" \
      "$pkgdir/usr/share/icons/hicolor/$size/apps/winff.png"
  done
  install -dm755 "$pkgdir/usr/share/winff/languages/"
  find . -name "*.po" \
    -exec install -Dm644 {} "$pkgdir/usr/share/winff/languages/" \; &> /dev/null
  rm -f 'presets.xml'
}

# getver: -u 2 github.com/WinFF/winff/tree/master/winff
# vim:set ts=2 sw=2 et:
