# $Id: PKGBUILD 266875 2017-11-15 14:29:11Z foutrelis $
# Maintainer:  https://aur.archlinux.org/account/toropisco
# Contributor: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: yugrotavele <yugrotavele@archlinux.us>
# Contributor: Paolo Stivanin <admin@polslinux.it>
# Contributor: Fabio Loli <fabio.loli@disroot.org>

pkgbase=winff
pkgname=(winff-common winff-gtk2 winff-gtk3 winff-qt5 winff-qt6)
pkgver=1.6.4
pkgrel=3
pkgdesc='GUI for ffmpeg written in Lazarus'
url='https://github.com/WinFF/winff/'
license=('GPL-3.0-or-later')
arch=('x86_64')
makedepends=('lazarus' 'gendesk' 'git' 'gtk2' 'gtk3' 'qt5pas' 'qt6pas')
source=("git+https://github.com/WinFF/winff.git#tag=winff-$pkgver")
md5sums=('SKIP')

prepare() {
  gendesk -n -f \
    --pkgname "winff-gtk2" \
    --pkgdesc "GUI for ffmpeg written in Lazarus/GTK+2" \
    --genericname 'Video converter' \
    --categories 'AudioVideo;AudioVideoEditing;GTK'

  gendesk -n -f \
    --pkgname "winff-gtk3" \
    --pkgdesc "GUI for ffmpeg written in Lazarus/GTK+3" \
    --genericname 'Video converter' \
    --categories 'AudioVideo;AudioVideoEditing;GTK'

  gendesk -n -f \
    --pkgname "winff-qt5" \
    --pkgdesc "GUI for ffmpeg written in Lazarus/Qt5" \
    --genericname 'Video converter' \
    --categories 'AudioVideo;AudioVideoEditing;QT'

  gendesk -n -f \
    --pkgname "winff-qt6" \
    --pkgdesc "GUI for ffmpeg written in Lazarus/Qt6" \
    --genericname 'Video converter' \
    --categories 'AudioVideo;AudioVideoEditing;QT'
}

build() {
  cd "$pkgbase/$pkgbase"

  lazbuild --lazarusdir=/usr/lib/lazarus winff.lpr --ws=gtk2 --os=linux --cpu=$ARCH
  mv winff winff-gtk2

  lazbuild --lazarusdir=/usr/lib/lazarus winff.lpr --ws=gtk3 --os=linux --cpu=$ARCH
  mv winff winff-gtk3

  lazbuild --lazarusdir=/usr/lib/lazarus winff.lpr --ws=qt5 --os=linux --cpu=$ARCH
  mv winff winff-qt5

  lazbuild --lazarusdir=/usr/lib/lazarus winff.lpr --ws=qt6 --os=linux --cpu=$ARCH
  mv winff winff-qt6
}

package_winff-common() {
  arch=(any)

  cd "$pkgbase/$pkgbase"

  install -d "$pkgdir/usr/share/$pkgbase/"
  cp presets.xml "$pkgdir/usr/share/$pkgbase/"

  install -Dm644 'winff-icons/48x48/winff.png' \
    "$pkgdir/usr/share/pixmaps/winff.png"

  for size in 16x16 24x24 32x32 48x48; do
    install -Dm644 "winff-icons/$size/winff.png" \
      "$pkgdir/usr/share/icons/hicolor/$size/apps/winff.png"
  done

  install -dm755 "$pkgdir/usr/share/winff"
  cp -a languages "$pkgdir/usr/share/$pkgbase/"

  install -dm755  "$pkgdir/usr/share/man/man1"
  cp winff.1 "$pkgdir/usr/share/man/man1"

  install -dm755  "$pkgdir/usr/share/doc"
  cp -a docs "$pkgdir/usr/share/doc/$pkgbase" 
}

package_winff-gtk2() {
  depends=(winff-common ffmpeg gtk2)

  install -Dm644 -t "$pkgdir/usr/share/applications/" winff-gtk2.desktop

  cd "$pkgbase/$pkgbase"
  install -Dt "${pkgdir}/usr/bin/" winff-gtk2
}

package_winff-gtk3() {
  depends=(winff-common ffmpeg gtk3)

  install -Dm644 -t "$pkgdir/usr/share/applications/" winff-gtk3.desktop

  cd "$pkgbase/$pkgbase"
  install -Dt "${pkgdir}/usr/bin/" winff-gtk3
}

package_winff-qt5() {
  depends=(winff-common ffmpeg qt5pas)

  install -Dm644 -t "$pkgdir/usr/share/applications/" winff-qt5.desktop

  cd "$pkgbase/$pkgbase"
  install -Dt "${pkgdir}/usr/bin/" winff-qt5
}

package_winff-qt6() {
  depends=(winff-common ffmpeg qt6pas)

  install -Dm644 -t "$pkgdir/usr/share/applications/" winff-qt6.desktop

  cd "$pkgbase/$pkgbase"
  install -Dt "${pkgdir}/usr/bin/" winff-qt6
}

# getver: -u 2 github.com/WinFF/winff/tree/master/winff
# vim:set ts=2 sw=2 et:
