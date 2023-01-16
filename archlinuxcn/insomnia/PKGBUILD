# Maintainer: Gobidev <adrian[dot]groh[at]t-online[dot]de>
# Contributor: luxcem <a@luxcem.fr>
# Contributor: kpcyrd <kpcyrd[at]archlinux[dot]org>
# Contributor: vscncls <lucaslou4@protonmail.com>

pkgname=insomnia
pkgver=2022.7.3
pkgrel=1
_nodeversion=12.18.3
pkgdesc="Cross-platform HTTP and GraphQL Client"
url="https://github.com/Kong/insomnia"
arch=('any')
license=('MIT')
depends=()
makedepends=('npm' 'nvm' 'fontconfig' 'yarn')
source=(
  "https://github.com/Kong/insomnia/archive/refs/tags/core@${pkgver}.tar.gz"
  "insomnia.desktop"
)
b2sums=('3d00f53a027c1410f7ef5e42577be9abc8638016328061207a24ac66eb1091c139b97d5d774ffc854dfe7ee619e524298c49fea99c685e305ba42a07b9cc5a63'
        '38c2edd681b012931e25498a4a65007cc2a2152c9bbc5505dbb7cf03e1143a7365c41e9ad7eb2318c8ea894dccad0e0b6601cf76f680ea4085d12b5059e61a6e')

_ensure_local_nvm() {
  # lets be sure we are starting clean
  which nvm >/dev/null 2>&1 && nvm deactivate && nvm unload

  export NVM_DIR="${srcdir}/${pkgname}-core-${pkgver}/.nvm"
  # The init script returns 3 if version
  #   specified in ./.nvrc is not (yet) installed in $NVM_DIR
  #   but nvm itself still gets loaded ok
  source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]
}

prepare() {
  _ensure_local_nvm
  cd ${pkgname}-core-${pkgver}
  nvm install 
}

build() {
  _ensure_local_nvm
  cd ${pkgname}-core-${pkgver}
  npm run bootstrap  
  GIT_TAG="core@${pkgver}" NODE_OPTIONS="--max-old-space-size=4096" BUILD_TARGETS="tar.gz" npm run app-package
}

package() {
  install -Dm644 ${pkgname}.desktop -t "${pkgdir}/usr/share/applications"
  cd ${pkgname}-core-${pkgver}
  install -d "${pkgdir}/opt/insomnia"
  cp -r packages/insomnia/dist/linux-*unpacked/. "$pkgdir/opt/insomnia"
  install -Dm644 packages/insomnia/src/ui/images/insomnia-logo.svg "${pkgdir}/usr/share/pixmaps/insomnia.svg"
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

