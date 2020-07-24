# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>

pkgname=hikarujs
pkgver=1.2.10
pkgrel=1
pkgdesc='A static site generator that generates routes based on directories naturally.'
arch=('any')
url='https://hikaru.alynx.one/'
license=('Apache')
depends=('nodejs>=8.9.0')
makedepends=('npm' 'jq')
source=("https://registry.npmjs.org/${pkgname}/-/${pkgname}-${pkgver}.tgz")
noextract=("${pkgname}-${pkgver}.tgz")
sha512sums=('150414c823b4b3577783d4a53bf8b502e67437e4091c3db98f48f069580d4d5d7d0c6600e04e0f8c44f2ad409a210f99632194be55b6805d7dfbcdd0c30ef7f4')

package() {
  # Use `--cache="${srcdir}/.npm"` to prevent npm from generating cache in home.
  # Use `--loglevel=error` to remove fsevents warning.
  npm install \
    --global \
    --user=root \
    --loglevel=error \
    --prefix="${pkgdir}/usr" \
    --cache="${srcdir}/.npm" \
    "${srcdir}/${pkgname}-${pkgver}.tgz"

  # Remove all src dir reference in dependencies' package.json with sed.
  find "${pkgdir}" -name package.json -print0 | xargs -r -0 sed -i '/_where/d'
  # Remove src dir reference in package.json with jq.
  local tmpjson="$(mktemp)"
  local pkgjson="${pkgdir}/usr/lib/node_modules/${pkgname}/package.json"
  jq '.|=with_entries(select(.key|test("_.+")|not))' "${pkgjson}" > "${tmpjson}"
  mv "${tmpjson}" "${pkgjson}"
  chmod 0644 "${pkgjson}"

  # npm sometimes gives dirs 777, fix it.
  find "${pkgdir}" -type d -exec chmod 0755 {} +
  # npm sets all owner to build user, which results in a lot of error which package checking.
  chown -R root:root "${pkgdir}"

  # Install LICENSE.
  install -Dm0644 \
    "${pkgdir}/usr/lib/node_modules/${pkgname}/LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

