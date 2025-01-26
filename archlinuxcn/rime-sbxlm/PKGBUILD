# Maintainer: ZeekoZhu <vaezt@outlook.com>

pkgname=rime-sbxlm
pkgver=20250126
pkgrel=1
pkgdesc='声笔系列码配置'
arch=(any)
url="https://github.com/sbsrf/sbsrf"
source=('sbxlm-init' "${pkgname}-${pkgver}.zip::${url}/releases/download/${pkgver}/sbsrf.zip" "${pkgname}-${pkgver}-src.zip::${url}/archive/refs/tags/${pkgver}.zip")
noextract=("${pkgname}-${pkgver}.zip" "${pkgname}-${pkgver}-src.zip")
license=('BSD-3-Clause')
sha256sums=('ddd93d18c5ecd40df142666df06d8588d4c345d662c38e31ea22402c3308549f'
            '5216f622eac7c5c06efc0967ffb9aef41d0beee1e50e84fd5a0d4f7b5344fe18'
            '41aa3a0fabb04a969a43a8ca92fb51f89a3264ed0d09ec5d43f7da3c9a5278b5')
makedepends=('unzip')
optdepends=('librime' 'fcitx5-rime')
replaces=('rime-sbxlm-sbfm' 'rime-sbxlm-sbkm' 'rime-sbxlm-sbzr' 'rime-sbxlm-sbxh')
install=$pkgname.install
groups=(sbxlm)

prepare () {
  cd "$srcdir"
  unzip -juo ./${pkgname}-${pkgver}-src.zip sbsrf-${pkgver}/LICENSE
  unzip -uo ./${pkgname}-${pkgver}.zip -d ./assets
  chmod 755 $srcdir/assets
}

package() {
  mkdir -p $pkgdir/usr/share/sbxlm/
  mv $srcdir/assets/default.custom.yaml $pkgdir/usr/share/sbxlm
  mkdir -p $pkgdir/usr/bin
  cp sbxlm-init $pkgdir/usr/bin
  mkdir -p $pkgdir/usr/share/rime-data/
  cp -r $srcdir/assets/* $pkgdir/usr/share/rime-data/
  install -Dm664 $srcdir/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
