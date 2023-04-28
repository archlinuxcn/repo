# Maintainer: Fredy García <frealgagu at gmail dot com>

pkgname=nodejs-nativefier
pkgver=50.1.1
pkgrel=1
pkgdesc="A command-line tool to easily create a desktop app for any web site with minimal configuration"
arch=("any")
url="https://github.com/${pkgname#nodejs-}/${pkgname#nodejs-}/"
license=("MIT")
depends=("nodejs" "unzip")
makedepends=("jq" "npm")
source=("${pkgname}-${pkgver}.tgz::http://registry.npmjs.org/${pkgname#nodejs-}/-/${pkgname#nodejs-}-${pkgver}.tgz")
noextract=("${pkgname}-${pkgver}.tgz")
sha1sums=("6a18dd3a684fb519e011dffd16fb56187e1f77d9")
sha256sums=("11587e877bad9a6859bb14268d56a60548d44e550f0d5da6d8535d9051957207")

prepare() {
  # Unpacking license file
  tar -zxvf "${srcdir}/${pkgname}-${pkgver}.tgz" --directory "${srcdir}" "package/LICENSE.md"
}

package() {
  # Thanks jeremejevs and je-vv for the pointers on these!
  npm install -g --cache "${srcdir}/npm-cache" --prefix "${pkgdir}/usr" "${srcdir}/${pkgname}-${pkgver}.tgz"

  # Installing license file
  install -Dm644 "${srcdir}/package/LICENSE.md" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"

  # Fixing permissions
  find "${pkgdir}/usr" -type d -exec chmod 755 {} +

  # npm gives ownership of ALL FILES to build user
  # https://bugs.archlinux.org/task/63396
  chown -R root:root "${pkgdir}"

  # Removing references to pkgdir
  find "${pkgdir}" -type f -name "package.json" -print0 | xargs -0 sed -i "/_where/d"

  # Removing references to srcdir
  local tmppackage="$(mktemp)"
  local pkgjson="${pkgdir}/usr/lib/node_modules/${pkgname#nodejs-}/package.json"
  jq '.|=with_entries(select(.key|test("_.+")|not))' "${pkgjson}" > "${tmppackage}"
  mv "${tmppackage}" "${pkgjson}"
  chmod 644 "${pkgjson}"
}
