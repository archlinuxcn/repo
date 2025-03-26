# Maintainer: picokan <todaysoracle@protonmail.com>
# Contributor: Plague-doctor <plague at privacyrequired dot com >

pkgname=freetube
_pkgname=FreeTube
pkgver=0.23.2
pkgrel=1
pkgdesc='An open source desktop YouTube player built with privacy in mind.'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
license=('AGPL-3.0-or-later')
depends=( 'electron34')
makedepends=('yarn' 'nodejs>=20.0.0')
url=https://freetubeapp.io
source=(https://github.com/FreeTubeApp/FreeTube/archive/v$pkgver-beta.tar.gz
        freetube.desktop
        freetube.sh)
sha256sums=('274168eef02637497045fa3410f612c426b4924a103e22065868daeffddd828e'
            'ada2b4b8f6a1e8896acbce4f4d311228d2c86026c273ffa00afa3247294f8b1e'
            '77db5d399ee84e4f005f5a72c96e273d9e1f6dd57d2fe98c65a67b3d13c9ec68')

prepare() {
  sed -i "4i electronDist: '/usr/lib/electron'," "$srcdir/$_pkgname-$pkgver-beta/_scripts/ebuilder.config.js"
  sed -i "s/targets = Platform.LINUX.*/targets = Platform.LINUX.createTarget(['dir'], arch)/" "$srcdir/$_pkgname-$pkgver-beta/_scripts/build.js"
}

build() {
  cd "$srcdir/$_pkgname-$pkgver-beta"
  yarn --cache-folder "${srcdir}/yarn-cache" install
  yarn --cache-folder "${srcdir}/yarn-cache" run build
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
