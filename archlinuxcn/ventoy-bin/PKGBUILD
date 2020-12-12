# Maintainer: DuckSoft <realducksoft at gmail dot com>
# Co-Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: KokaKiwi <kokakiwi+aur@kokakiwi.net>

pkgname=ventoy-bin
pkgver=1.0.30
pkgrel=1
pkgdesc='A new multiboot USB solution (Binary)'
url='http://www.ventoy.net/'
arch=('i686' 'x86_64')
license=('GPL3')
depends=('bash' 'util-linux' 'xz' 'exfat-utils' 'dosfstools' 'lib32-glibc')
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
source=("https://github.com/ventoy/Ventoy/releases/download/v${pkgver}/${pkgname%-bin}-${pkgver}-linux.tar.gz"
        "${pkgname%-bin}" 'sanitize.patch')
sha256sums=('0410043931953e7805fdb747f2a25c409ad0b6ed85807e222f30e995ab7352c4'
            '1ad5d314e02b84127a5a59f3871eb1d28617218cad07cde3eeddcac391473000'
            '88dd56d98cb98d18cb73a1ca142fbc12769d09343207c6546e934b39d6b760a3')

prepare() {
  msg2 "Decompress tools..."
  cd "$srcdir/${pkgname%-bin}-${pkgver}/tool/$CARCH"
  for file in *.xz; do
    xzcat $file > ${file%.xz}
    chmod +x ${file%.xz}
  done

  msg2 "Cleaning up .xz crap..."
  rm -fv ./*.xz

  msg2 "Applying sanitize patch..."
  cd ../..
  patch --verbose -p0 < "$srcdir/sanitize.patch"

  msg2 "Cleaning up unused binaries..."
  rm -fv tool/$CARCH/{mkextfatfs_{32,64},mount.exfat-fuse_{32,64},ash,hexdump,xzcat}
}

package() {
  cd "$srcdir/${pkgname%-bin}-${pkgver}"

  msg2 "Copying package files..."
  install -Dm644 -vt      "$pkgdir/opt/${pkgname%-bin}/boot/"            boot/*
  install -Dm644 -vt      "$pkgdir/opt/${pkgname%-bin}/${pkgname%-bin}/" "${pkgname%-bin}"/*
  install -Dm755 -vt      "$pkgdir/opt/${pkgname%-bin}/tool/"            tool/*.{cer,sh}
  install -Dm755 -vt      "$pkgdir/opt/${pkgname%-bin}/tool/$CARCH/"     tool/$CARCH/*
  install -Dm755 -vt      "$pkgdir/opt/${pkgname%-bin}/"                 *.sh
  cp --no-preserve=o -avt "$pkgdir/opt/${pkgname%-bin}/"                 plugin

  msg2 "Linking system binaries..."
  ln -svf /usr/bin/xzcat            "$pkgdir/opt/${pkgname%-bin}/tool/"
  ln -svf /usr/bin/hexdump          "$pkgdir/opt/${pkgname%-bin}/tool/"
  ln -svf /usr/bin/mkfs.exfat       "$pkgdir/opt/${pkgname%-bin}/tool/mkextfatfs_32"
  ln -svf /usr/bin/mkfs.exfat       "$pkgdir/opt/${pkgname%-bin}/tool/mkextfatfs_64"
  ln -svf /usr/bin/mount.exfat-fuse "$pkgdir/opt/${pkgname%-bin}/tool/mount.exfat-fuse_32"
  ln -svf /usr/bin/mount.exfat-fuse "$pkgdir/opt/${pkgname%-bin}/tool/mount.exfat-fuse_64"

  msg2 "Creating /usr/bin entries..."
  install -Dm755 "$srcdir/${pkgname%-bin}" -t "$pkgdir"/usr/bin/
}
