# Maintainer: ZeekoZhu <vaezt@outlook.com>

pkgname=rime-sbxlm
pkgver=20240915
pkgrel=1
pkgdesc='声笔系列码配置'
arch=(any)
url="https://github.com/sbsrf/sbsrf"
source=('sbxlm-init' "${pkgname}-${pkgver}.zip::${url}/releases/download/${pkgver}/sbsrf.zip" "${pkgname}-${pkgver}-src.zip::${url}/archive/refs/tags/${pkgver}.zip")
noextract=("${pkgname}-${pkgver}.zip" "${pkgname}-${pkgver}-src.zip")
license=('BSD-3-Clause')
sha256sums=('ddd93d18c5ecd40df142666df06d8588d4c345d662c38e31ea22402c3308549f'
            '4a29ed34bbd522c597e7a6f35d060b140f6000dbb74e2fdb3a633b4f862f871f'
            '9026e69b9929b9bc26e0833dc35d8f4f44cc151060af9cd1baf3778069757d0f')
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
