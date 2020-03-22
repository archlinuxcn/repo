# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=motrix-git
_pkgname=motrix
_pkgver=1.4.1
pkgver=1.4.1.r587.4037dad
pkgrel=1
pkgdesc='A full-featured download manager'
arch=('any')
url='https://motrix.app/'
license=('MIT')
depends=(
  'aria2'
  'electron'
  'nodejs'
)
makedepends=(
  'gendesk'
  'git'
  'npm'
  'python2'
)
provides=(motrix=${pkgver})
conflicts=(motrix)
source=("${_pkgname}::git+https://github.com/agalwood/Motrix.git")
sha256sums=('SKIP')

pkgver() {
  cd "${srcdir}/${_pkgname}"
  ver=$(printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)")
  echo "${_pkgver}.${ver}"
}

prepare() {
  sed -i 's/"postinstall"/"ignore"/' "${srcdir}/${_pkgname}/package.json"
  sed -i "s/4.2.4/7.1.4/g" "${srcdir}/${_pkgname}/package.json"
  rm -vf "${srcdir}/${_pkgname}/package-lock.json"
  echo "Creating desktop file..."
  gendesk -f -n --pkgname ${_pkgname} \
  --pkgdesc "${pkgdesc}" \
  --categories "Network;FileTransfer;" \
  --icon "${_pkgname}" \
  --exec "${_pkgname}"
}

build() {
  cd "${srcdir}/${_pkgname}"
  npm_config_cache="${srcdir}/npm_cache" npm install
  npm run pack
  npm prune --production
}

package() {
  install -d "${pkgdir}/usr/bin" "${pkgdir}/usr/lib/${_pkgname}" "${pkgdir}/usr/share/applications" "${pkgdir}/usr/share/pixmaps"
  install -Dm644 "${srcdir}/${_pkgname}/extra/linux/engine/aria2.conf" "${pkgdir}/usr/lib/${_pkgname}/engine/aria2.conf"
  ln -s /usr/bin/aria2c "${pkgdir}/usr/lib/${_pkgname}/engine/aria2c"
  cp -r "${srcdir}/${_pkgname}/dist" "${pkgdir}/usr/lib/${_pkgname}/app"
  cp -r "${srcdir}/${_pkgname}/node_modules" "${pkgdir}/usr/lib/${_pkgname}/app/node_modules"
  echo '{"name": "'${_pkgname}'", "version": "v'${_pkgver}'", "main": "./electron/main.js"}' > "${pkgdir}/usr/lib/${_pkgname}/app/package.json"
  install -Dm644 "${srcdir}/${_pkgname}/static/512x512.png" "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"
  # launch script
  cat << EOF > "${pkgdir}/usr/bin/${_pkgname}"
#!/bin/bash
export ELECTRON_IS_DEV=0
exec /usr/bin/electron /usr/lib/${_pkgname}/app
EOF
  chmod +x "${pkgdir}/usr/bin/${_pkgname}"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -Dm644 "${srcdir}/${_pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
# vim:set ts=2 sw=2 et:
