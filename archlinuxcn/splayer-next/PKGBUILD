# Maintainer: nlsdt <nlsdt@archlinuxcn.org>

pkgname=splayer-next
_pkgname=SPlayer-Next
pkgver=1.2.0
pkgrel=1
pkgdesc="Cross-platform desktop music player with rich lyric support and wide audio format compatibility"
arch=('x86_64' 'aarch64')
url="https://github.com/SPlayer-Dev/SPlayer-Next"
license=('AGPL-3.0-only')
depends=(
  'alsa-lib'
  'at-spi2-core'
  'gtk3'
  'hicolor-icon-theme'
  'libnotify'
  'libpipewire'
  'libpulse'
  'libsecret'
  'libxss'
  'libxtst'
  'nss'
  'xdg-utils'
)
makedepends=(
  'clang'
  'git'
  'nodejs'
  'pkgconf'
  'pnpm'
  'python'
  'rust'
)
conflicts=('splayer-next-bin' 'splayer-next-git')
options=('!lto')
source=(
  "${_pkgname}-${pkgver}.tar.gz::https://github.com/SPlayer-Dev/SPlayer-Next/archive/refs/tags/v${pkgver}.tar.gz"
  '0001-Disable-builtin-updater.patch'
  'top.imsyy.splayer_next.desktop'
)
sha256sums=('ff8e5b7259a434cd3854bed3e73ba9926f31076d2b962fa469648977d33afac6'
            'fc87c1223f89603c5be1e991ba9c589469c4cd677e789ec3bd34cee8c4c7176d'
            'f9530b38c0222ce185bb2dfcd9f5c6ece6fdadb3ba7a0eb10a41846be8b7b632')

prepare() {
  cd "${_pkgname}-${pkgver}"

  patch -Np1 -i "${srcdir}/0001-Disable-builtin-updater.patch"
  rm -f .npmrc
}

build() {
  cd "${_pkgname}-${pkgver}"

  # 保留调试符号
  export CARGO_PROFILE_RELEASE_STRIP=none
  export npm_config_manage_package_manager_versions=false

  pnpm install --frozen-lockfile
  pnpm build:unpack
}

package() {
  cd "${_pkgname}-${pkgver}"

  # 安装运行时
  local _appdir=linux-unpacked
  [[ "${CARCH}" == "aarch64" ]] && _appdir=linux-arm64-unpacked
  install -d "${pkgdir}/opt/${_pkgname}"
  cp -a "dist/${_appdir}/." "${pkgdir}/opt/${_pkgname}/"

  # 设置沙盒权限
  chmod 755 "${pkgdir}/opt/${_pkgname}/chrome-sandbox"

  # 创建入口链接
  install -d "${pkgdir}/usr/bin"
  ln -s "/opt/${_pkgname}/${_pkgname}" "${pkgdir}/usr/bin/${pkgname}"

  # 安装桌面入口
  install -Dm644 "${srcdir}/top.imsyy.splayer_next.desktop" \
    "${pkgdir}/usr/share/applications/top.imsyy.splayer_next.desktop"

  # 安装图标
  install -Dm644 "public/icons/favicon-512x512.png" \
    "${pkgdir}/usr/share/icons/hicolor/512x512/apps/${_pkgname}.png"
}
