# Maintainer: Jannick Hemelhof <mister {dot} jannick {at} gmail {dot} com>
# Contributor: Nicola Squartini <tensor5 {at} gmail {dot} com>
# Contributor: NicoHood <aur {at} nicohood {dot} de>
# Contributor: Dick Choi <fluke8259 {at} gmail {dot} com>
# Contributor: Romain Bazile <gromain {dot} baz {at} gmail {dot} com>
pkgname=boostnote
_pkgname=Boostnote
pkgver=0.11.15
pkgrel=1
pkgdesc="Open source note-taking app for programmers"
arch=('any')
url="https://boostnote.io/"
license=('GPL3')
depends=('electron' 'nodejs')
makedepends=('npm' 'grunt-cli' 'git')

source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/BoostIO/"${_pkgname}"/archive/v"${pkgver}".tar.gz"
  "${pkgname}.js"
  "${pkgname}.desktop"
  "warning-fix.patch"
  "remove-analytics.patch"
  )

sha512sums=('531e58d0e8620d745dab1245b036cf39a88e8951d2b1d11dabb4ce6c52cce97c2a961bbc25516cbb2b5b543d359bff66aa2f4f5f6894eb39392630ee1699d69e'
            '1f0ccd2a3632a12c4714d97b9f909ddc94b53d6f86a9e4bdcab31abd55a93071a2c35c6e1e9527b747de6dd74b8a5276414980c11e174085f28b8f2d2721230a'
            '18bcda13580da8ceeaa86793a77ec00a053b8fd51451dad7e2b1a19553fe1a467ac647b44b789212e783f3f6a80968cc9404e884ef7ff6b1f6588473b3229d40'
            'a52e5631867e2c5f18465dee6a3201b9b5c546bda373205c4891c9f7b6114599e0854e2b49defb55ee7bea0778a7fde9c9d9f7271dceeeece743a2d72e2fd0c6'
            '65280bb7e30e07746a63b93be0e32299424683ade760d52031765099048761c863bd2905fbe98a808d85b991777734c6645e887d51493db063984ff236c4fae8')

prepare() {
  cd "${_pkgname}-${pkgver}"

  patch -Np1 -i "${srcdir}/warning-fix.patch"
  patch -Np1 -i "${srcdir}/remove-analytics.patch"
}

build() {
  cd "${_pkgname}-${pkgver}"

  npm install --no-optional --no-shrinkwrap
  grunt compile
  rm -r node_modules/
  npm install --production --no-optional --no-shrinkwrap
}

package() {
  cd "${_pkgname}-${pkgver}"

  appdir="/usr/lib/${pkgname}"

  install -dm755 "${pkgdir}""${appdir}"
  cp -a * "${pkgdir}""${appdir}"

  install -Dm755 "${srcdir}/${pkgname}.js" "$pkgdir/usr/bin/${pkgname}"

  install -Dm644 resources/app.png "$pkgdir/usr/share/pixmaps/${pkgname}.png"
  install -Dm644 "${srcdir}/${pkgname}.desktop" "$pkgdir/usr/share/applications/${pkgname}.desktop"

  # Remove stuff we do not need
  find "${pkgdir}"/usr/lib/"${pkgname}"/node_modules \
      -name "*.a" -exec rm '{}' \; \
      -or -name "*.bat" -exec rm '{}' \; \
      -or -name "*.node" -exec chmod a-x '{}' \; \
      -or -name "benchmark" -prune -exec rm -r '{}' \; \
      -or -name "doc" -prune -exec rm -r '{}' \; \
      -or -name "html" -prune -exec rm -r '{}' \; \
      -or -name "man" -prune -exec rm -r '{}' \; \
      -or -path "*/less/gradle" -prune -exec rm -r '{}' \; \
      -or -path "*/task-lists/src" -prune -exec rm -r '{}' \;
}
