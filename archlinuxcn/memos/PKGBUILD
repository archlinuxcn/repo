# Maintainer: envolution
# Contributor: Lindasy Zhou <i@lin.moe>
# shellcheck shell=bash disable=SC2034,SC2154

pkgname="memos"
pkgver=0.24.0
pkgrel=2
pkgdesc="A privacy-first, lightweight note-taking service. Easily capture and share your great thoughts."
url="https://github.com/usememos/${pkgname}"
arch=("any")
license=('MIT')
makedepends=("go" "git" "npm" "pnpm" "nvm")
backup=('etc/memos.conf')
options=(!strip !debug)
source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/usememos/memos/archive/refs/tags/v${pkgver}.tar.gz"
  "systemd.service"
  "sysusers.conf"
  "memos.conf"
  'tmpfiles.conf'
)
sha512sums=('cdbe6e53620cb875dd30091fc42990365f59d22034b7dac8ab3ba47811c1a607c5f62a3611e2ece5b4e5ff6957cc3c0feae74459dddf8e8f1ccaa838c8cd456e'
            '9c37361974d8b3beecdd8b0bf8db929a4a882623ea7b23aa51bddf37790b66042cef593d6da89b34e7dde4a9a9a1e097ea31ec713b33fee6a699448fb300d4a2'
            '692dc4674b86b36c5464c78f493ace50091068f962d40130a32b4ed17517d77e33860333e870f5e80a5e17b6cbd5de45bf57e7de5ea7984bd4e36f95a8daf0fa'
            '251e01c4f5fc8aea209453d91da5dde91d58397668e34b78e52a31940e30a89be5601a6ea8cdebe791a96c9324733095de3567998b45ce1542578b1d9b7a5b76'
            'cf88b91a88825dcfda35f45461513b8a2e03b07890189fd1cf7b60aa4085c9e88d8338596b69a3d9c3e513e668093ab7cb246febbb7f6ac7796d37e1189db565')

_ensure_local_nvm() {
  export NVM_DIR="${srcdir}/.nvm"
  source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]
  nvm install
  nvm use
  echo "in _ensure nvm dir = ${NVM_DIR}"
}

build() {
  export COREPACK_ENABLE_STRICT=0
  export COREPACK_ENABLE_DOWNLOAD_PROMPT=0

  cd "${pkgname}-${pkgver}/web"

  # Build frontend
  echo "lts/iron" >.nvmrc
  _ensure_local_nvm
  pnpm install
  pnpm build

  # Set up backend build environment
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/backend_build_dir/server/router/frontend/dist/"
  rm -rf "${srcdir}/${pkgname}-${pkgver}/server/router/frontend/dist"
  cp -r "${srcdir}/${pkgname}-${pkgver}/web/dist" "${srcdir}/${pkgname}-${pkgver}/server/router/frontend/"

  # Compile the backend Go binary
  CGO_ENABLED=0 go build -o "${srcdir}/${pkgname}.bin" "${srcdir}/${pkgname}-${pkgver}/bin/memos/main.go"
}
package() {
  install -vDm644 systemd.service "$pkgdir/usr/lib/systemd/system/${pkgname}.service"
  install -vDm644 sysusers.conf "$pkgdir/usr/lib/sysusers.d/${pkgname}.conf"
  install -vDm644 tmpfiles.conf "$pkgdir/usr/lib/tmpfiles.d/${pkgname}.conf"
  install -vDm644 memos.conf "$pkgdir/etc/memos.conf"

  install -Dm755 "memos.bin" "$pkgdir/usr/bin/memos"
  install -Dm0644 "${pkgname}-${pkgver}/LICENSE" "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
