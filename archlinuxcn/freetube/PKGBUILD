# Maintainer: picokan <todaysoracle@protonmail.com>
# Contributor: Plague-doctor <plague at privacyrequired dot com >

pkgname=freetube
_pkgname=FreeTube
pkgver=0.21.3
pkgrel=1
pkgdesc='An open source desktop YouTube player built with privacy in mind.'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
license=('AGPL3')
depends=( 'electron31')
makedepends=('yarn')
url=https://freetubeapp.io
source=(https://github.com/FreeTubeApp/FreeTube/archive/v$pkgver-beta.tar.gz
        freetube.desktop
        freetube.sh)
sha256sums=(4454c94c5fc2290c31006f5897f06b8132154fc8d889f872de100461842541d9
            ada2b4b8f6a1e8896acbce4f4d311228d2c86026c273ffa00afa3247294f8b1e
			380704e34595fd430ab48dcf778e1c671757f914f7b81ac6707dce13ca3a67f6)

prepare() {
  sed -i "4i electronDist: '/usr/lib/electron'," "$srcdir/$_pkgname-$pkgver-beta/_scripts/ebuilder.config.js"
  sed -i "s/targets = Platform.LINUX.*/targets = Platform.LINUX.createTarget(['dir'], arch)/" "$srcdir/$_pkgname-$pkgver-beta/_scripts/build.js"
}

build() {
  cd "$srcdir/$_pkgname-$pkgver-beta"
  UV_USE_IO_URING=0 yarn --cache-folder "${srcdir}/yarn-cache" install
  UV_USE_IO_URING=0 yarn --cache-folder "${srcdir}/yarn-cache" run build
}

package() {
  install -d "${pkgdir}"/usr/lib/${pkgname}
  cp -R "./$_pkgname-$pkgver-beta/build/linux-unpacked/resources/app.asar" "$pkgdir/usr/lib/$pkgname"
  install -Dm755 "./freetube.sh" "$pkgdir/usr/bin/$pkgname"
  
  cd $_pkgname-$pkgver-beta
  install -Dm644 "./_icons/icon.svg" "$pkgdir/usr/share/pixmaps/$pkgname.svg"
  cd ..
  install -Dm644 "freetube.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
}
