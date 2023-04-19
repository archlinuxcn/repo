# Maintainer: Ali Molaei <ali dot molaei at protonmail dot com>
# Contributor: Maz <m47h4r at gmail dot com>
# Contributor: Molyuu <zhangjtroger at gmail dot com>

pkgname=nekoray-bin
pkgver=2.26
_releasedate=2023-04-18
pkgrel=1
pkgdesc="Qt based cross-platform GUI proxy configuration manager (backend: v2ray / sing-box)"
arch=('x86_64')
url="https://github.com/MatsuriDayo/nekoray"
license=('GPL 3.0')
groups=()
depends=('qt5-base>=5.15' 'qt5-svg' 'qt5-tools' 'qt5-x11extras')
provides=('nekoray')
conflicts=('nekoray-git' 'nekoray')
optdepends=(
    'v2ray-domain-list-community: geosite data for NekoRay'
    'v2ray-geoip: geoip data for NekoRay'
)

source=(
	"${pkgname}-${pkgver}.zip::${url}/releases/download/${pkgver}/nekoray-${pkgver}-${_releasedate}-linux64.zip"
	"nekoray.desktop"
  "nekoray.sh"
)

sha256sums=(
	'ef58336a9c10a1cb318c369467e14b25f787385b8a5caf1710ac953c9e994271'
	'86f1332c81be2c346a4cdc80a3550f6484ef89e4ee8d4f23afada0c2d0a184e2'
	'5a7cbb61608137924fb1ba3ecb057adb7973f5775f64758736b447041fa15377'
)

package() {
  mkdir -p ${pkgdir}/usr/bin/
  mkdir -p ${pkgdir}/usr/lib/nekoray/
  mkdir -p ${pkgdir}/usr/share/icons/hicolor/128x128/apps/

  install -Dt ${pkgdir}/usr/lib/nekoray/ -m755 ./nekoray/nekobox_core
  install -Dt ${pkgdir}/usr/lib/nekoray/ -m755 ./nekoray/nekoray_core
  install -Dt ${pkgdir}/usr/lib/nekoray/ -m755 ./nekoray/nekoray
	install -Dm755 ./nekoray.sh ${pkgdir}/usr/bin/nekoray 

	install -Dt ${pkgdir}/usr/share/applications/ -m644 ./nekoray.desktop
	install -Dt ${pkgdir}/usr/share/icons/hicolor/128x128/apps/ -m644 ./nekoray/nekoray.png
}

