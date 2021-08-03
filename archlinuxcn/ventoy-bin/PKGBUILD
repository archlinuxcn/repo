# Maintainer: DuckSoft <realducksoft at gmail dot com>
# Co-Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: KokaKiwi <kokakiwi+aur@kokakiwi.net>

pkgname=ventoy-bin
pkgver=1.0.49
pkgrel=1
pkgdesc='A new multiboot USB solution (Binary)'
url='http://www.ventoy.net/'
arch=('i686' 'x86_64')
license=('GPL3')
depends=('bash' 'util-linux' 'xz' 'dosfstools' 'lib32-glibc')
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
install="${pkgname%-bin}.install"
source=("https://github.com/ventoy/Ventoy/releases/download/v${pkgver}/${pkgname%-bin}-${pkgver}-linux.tar.gz"
        "${pkgname%-bin}" "${pkgname%-bin}web" "${pkgname%-bin}-persistent" "${pkgname%-bin}-extend-persistent"
        'sanitize.patch')
sha256sums=('db7b4411ff41add4acc62c694fba15cbdedef1b7c9b3fb3c3ff57aefe64360e4'
            '1ad5d314e02b84127a5a59f3871eb1d28617218cad07cde3eeddcac391473000'
            'c3d4463a878a89d96e5f0bc4e1a43e48f27af5965bd4c977567695d7cf91fe5f'
            '51029745da197dded6e007aee3f30f7ea1aa6e898172a6ea176cc2f3a842d0ff'
            '00dec31721a052d5e6c928e3b38b870959bdb42188f34717898d99c0cef950df'
            '1555f65997e6d92ca29a774b45052e97a3358430fa5869f521a4fe7818427a1f')

_msg2() { printf "\e[1;34m  ->\e[0;1m %s\e[0m\n" "$1"; }

prepare() {
  _msg2 "Decompress tools..."
  cd "$srcdir/${pkgname%-bin}-${pkgver}/tool/$CARCH"
  for file in *.xz; do
    xzcat $file > ${file%.xz}
    chmod +x ${file%.xz}
  done

  _msg2 "Cleaning up .xz crap..."
  rm -fv ./*.xz

  _msg2 "Applying sanitize patch..."
  cd ../..
  patch --verbose -p0 < "$srcdir/sanitize.patch"
  sed -i 's|log\.txt|/var/log/ventoy.log|g' WebUI/static/js/languages.js

  _msg2 "Cleaning up unused binaries..."
  # Preserving mkexfatfs and mount.exfat-fuse because exfatprogs is incompatible
  for binary in xzcat hexdump; do
    rm -fv tool/$CARCH/$binary
  done
}

package() {
  cd "$srcdir/${pkgname%-bin}-${pkgver}"

  _msg2 "Copying package files..."
  install -Dm644 -vt      "$pkgdir/opt/${pkgname%-bin}/boot/"            boot/*
  install -Dm644 -vt      "$pkgdir/opt/${pkgname%-bin}/${pkgname%-bin}/" "${pkgname%-bin}"/*
  install -Dm755 -vt      "$pkgdir/opt/${pkgname%-bin}/tool/"            tool/*.{cer,sh}
  install -Dm755 -vt      "$pkgdir/opt/${pkgname%-bin}/tool/$CARCH/"     tool/$CARCH/*
  install -Dm755 -vt      "$pkgdir/opt/${pkgname%-bin}/"                 *.sh
  cp --no-preserve=o -avt "$pkgdir/opt/${pkgname%-bin}/"                 plugin WebUI

  _msg2 "Linking system binaries..."
  for binary in xzcat hexdump; do
    ln -svf /usr/bin/$binary "$pkgdir/opt/${pkgname%-bin}/tool/$CARCH/"
  done

  _msg2 "Creating /usr/bin entries..."
  install -Dm755 "$srcdir/${pkgname%-bin}"{,web,-{,extend-}persistent} -vt "$pkgdir"/usr/bin/
}
