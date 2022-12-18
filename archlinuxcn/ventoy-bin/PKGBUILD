# Maintainer: DuckSoft <realducksoft at gmail dot com>
# Co-Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: KokaKiwi <kokakiwi+aur@kokakiwi.net>

pkgname=ventoy-bin
pkgver=1.0.85
pkgrel=1
pkgdesc="A new multiboot USB solution"
arch=('aarch64' 'i686' 'x86_64')
url="http://www.ventoy.net"
license=('GPL3')
depends=('bash' 'util-linux' 'xz' 'dosfstools')
optdepends=('gtk3: GTK3 GUI'
            'qt5-base: Qt5 GUI'
            'polkit: run GUI from application menu')
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
install="${pkgname%-bin}.install"
source=("https://github.com/ventoy/Ventoy/releases/download/v${pkgver}/${pkgname%-bin}-${pkgver}-linux.tar.gz"
        "${pkgname%-bin}"
        "${pkgname%-bin}gui"
        "${pkgname%-bin}web"
        "${pkgname%-bin}plugson"
        "${pkgname%-bin}-persistent"
        "${pkgname%-bin}-extend-persistent"
        "${pkgname%-bin}.desktop"
        'sanitize.patch')
sha256sums=('1234bf19ff83760184bf7f0ef9d9ecb000bc4b15814579256e951d7086a14420'
            '1ad5d314e02b84127a5a59f3871eb1d28617218cad07cde3eeddcac391473000'
            '0215dbaf2095f5eeb2d40d9731268ed724790565e1dcaad67ffa4af80b5d8330'
            'c3d4463a878a89d96e5f0bc4e1a43e48f27af5965bd4c977567695d7cf91fe5f'
            '1bbe66b52398be96402604562bddb5c9fbebfe345f0de184709e1c74086f2be6'
            '51029745da197dded6e007aee3f30f7ea1aa6e898172a6ea176cc2f3a842d0ff'
            '00dec31721a052d5e6c928e3b38b870959bdb42188f34717898d99c0cef950df'
            '22225d48023806d0d15e059216ef4921de70cdb78348630be109fa9c669e2900'
            '36af9f05a5453273d322d4c250ab48a0d0d43d1f3851c9e07773bc6034756fea')

prepare() {
  cd "${pkgname%-bin}-$pkgver"

  # Decompress tools
  pushd tool/$CARCH
  for file in *.xz; do
    xzcat $file > ${file%.xz}
    chmod +x ${file%.xz}
  done

  # Cleanup .xz crap
  rm -fv ./*.xz
  popd

  # Apply sanitize patch
  patch --verbose -p0 < "$srcdir/sanitize.patch"

  # Log location
  sed -i 's|log\.txt|/var/log/ventoy.log|g' WebUI/static/js/languages.js tool/languages.json

  # Non-POSIX compliant scripts
  sed -i 's|bin/sh|usr/bin/env bash|g' tool/{ventoy_lib.sh,VentoyWorker.sh}

  # Clean up unused binaries
  # Preserving mkexfatfs and mount.exfat-fuse because exfatprogs is incompatible
  for binary in xzcat hexdump; do
    rm -fv tool/$CARCH/$binary
  done
}

package() {
  cd "${pkgname%-bin}-$pkgver"
  install -Dm644 -vt      "$pkgdir/opt/${pkgname%-bin}/boot/"            boot/*
  install -Dm644 -vt      "$pkgdir/opt/${pkgname%-bin}/${pkgname%-bin}/" "${pkgname%-bin}"/*
  install -Dm755 -vt      "$pkgdir/opt/${pkgname%-bin}/tool/"            tool/*.{cer,glade,json,sh,xz}
  install -Dm755 -vt      "$pkgdir/opt/${pkgname%-bin}/tool/$CARCH/"     tool/$CARCH/*
  install -Dm755 -vt      "$pkgdir/opt/${pkgname%-bin}/"                 *.sh
  cp --no-preserve=o -avt "$pkgdir/opt/${pkgname%-bin}/"                 plugin WebUI

  install -Dm755 "VentoyGUI.$CARCH" -vt "$pkgdir/opt/${pkgname%-bin}"
  install -Dm644 WebUI/static/img/VentoyLogo.png -v "$pkgdir/usr/share/pixmaps/${pkgname%-bin}.png"
  install -Dm644 "$srcdir/${pkgname%-bin}.desktop" -vt "$pkgdir/usr/share/applications"

  # Link system binaries
  for binary in xzcat hexdump; do
    ln -svf /usr/bin/$binary "$pkgdir/opt/${pkgname%-bin}/tool/$CARCH/"
  done

  install -Dm755 "$srcdir/${pkgname%-bin}"{,gui,web,plugson,-{,extend-}persistent} -vt "$pkgdir"/usr/bin/

  # Remove Gtk 2 files
  if [ $CARCH == "x86_64" ]; then
    rm "$pkgdir/opt/${pkgname%-bin}/tool/$CARCH/Ventoy2Disk.gtk2"
  fi
}
