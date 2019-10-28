# Maintainer: Jean Lucas <jean@4ray.co>

pkgname=signal-desktop
_pkgname=Signal-Desktop
pkgver=1.27.4
pkgrel=4
pkgdesc='Electron application that links with Signal on mobile'
arch=(x86_64)
url=https://signal.org
license=(GPL3)
depends=('electron>=6.1.1')
makedepends=(yarn git python2 'nodejs>=12' npm python)
provides=(signal)
replaces=(signal)
source=(
  $pkgname-$pkgver.tar.gz::https://github.com/signalapp/Signal-Desktop/archive/v$pkgver.tar.gz
  $pkgname.desktop
  openssl-linking.patch
)
sha512sums=('92a934d7680f33803bd7be21f4604719b211036931a6e00565e21a7008d0b35da7dda5c6527458a9498f82a9c9a96a94b868274d1d7e73e09ccb09fe1aea295a'
            'bcbf8ffc6f6f7e99e59b5ab1517ba231f1d3b2b16a0e27541580f028ebee5027685a8c397212c43008844be352d3b6acf2269e631bc2c6ba05c2eb95f56fef36'
            '2c10d4cc6c0b9ca650e786c1e677f22619a78c93465f27fc4cf4831f1cfe771f3b9885a416e381a9e14c3aea5d88cb3545264046188db72d54b8567266811e51')

prepare() {
  cd $_pkgname-$pkgver

  # Bump Electron version for newer ABI compatibility
  sed 's#\("electron": "\).*"#\16.1.2"#' -i package.json

  # Allow higher Node versions
  sed 's#"node": "#&>=#' -i package.json

  yarn install

  # Have SQLCipher dynamically link from OpenSSL
  # See https://github.com/signalapp/Signal-Desktop/issues/2634
  patch -Np0 -i ../openssl-linking.patch
}

build() {
  cd $_pkgname-$pkgver

  # Gruntfile expects Git commit information which we don't have in a tarball download
  # See https://github.com/signalapp/Signal-Desktop/issues/2376
  yarn generate exec:build-protobuf exec:transpile concat copy:deps sass

  yarn build-release --dir
}

package() {
  cd $_pkgname-$pkgver

  install -d "$pkgdir"/usr/{lib,bin}
  cp -a release/linux-unpacked/resources "$pkgdir"/usr/lib/$pkgname
  cat << EOF > "$pkgdir"/usr/bin/$pkgname
#!/bin/sh

NODE_ENV=production electron /usr/lib/$pkgname/app.asar "\$@"
EOF
  chmod +x "$pkgdir"/usr/bin/$pkgname

  install -Dm 644 ../$pkgname.desktop -t "$pkgdir"/usr/share/applications
  for i in 16 24 32 48 64 128 256 512 1024; do
    install -Dm 644 build/icons/png/${i}x${i}.png \
      "$pkgdir"/usr/share/icons/hicolor/${i}x${i}/apps/$pkgname.png
  done
}
