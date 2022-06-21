# Maintainer: Nico <d3sox at protonmail dot com>
pkgname=fluent-reader
pkgver=1.1.2
pkgrel=1
_pkgname="${pkgname}-${pkgver}"
pkgdesc='Modern desktop RSS reader built with Electron, React, and Fluent UI'
arch=('any')
url='https://hyliu.me/fluent-reader/'
license=('BSD')
depends=('hicolor-icon-theme')
makedepends=('nodejs' 'node-gyp' 'npm')
source=("https://github.com/yang991178/fluent-reader/archive/v${pkgver}.tar.gz"
        'fluent-reader.desktop')
sha256sums=('313bf3d0a3ac607d919434234828064f6739b6f009a39088b44531a6c91ff060'
            '8094dd526fcb3bd67913a20224fa8c167068d58b8e0ba51b74e8b74c23f73026')

build() {
  cd "$_pkgname"
  npm install
  export NODE_ENV=production
  npm run build
  node_modules/.bin/electron-builder --linux dir -p never
}

package() {
  cd "$srcdir/$_pkgname"
  install -d "$pkgdir/opt/"
  cp -dr --no-preserve=ownership "bin/linux/x64/linux-unpacked" "$pkgdir/opt/$pkgname"
  
  # install binary symlink
  install -d "${pkgdir}/usr/bin/"
  ln -sf /opt/fluent-reader/fluent-reader "${pkgdir}/usr/bin/fluent-reader"
  
  install -Dm644 -t "$pkgdir/usr/share/applications" "$srcdir/$pkgname.desktop"
  
  install -Dm644 "build/icons/512x512.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/$pkgname.png"
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname/LICENSE" LICENSE
}
 
