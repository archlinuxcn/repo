# Maintainer: nlsdt <nlsdt@archlinuxcn.org>

pkgname=splayer-next
_pkgname=SPlayer-Next
pkgver=1.1.0
pkgrel=2
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
sha256sums=('248b814590e45e81856573de8b6b435515d42648c8b9b00a0fe3e0135ca64f00'
            '72a7a31955318e3d2b6b1ad070f46f5ef5f6862c9fb47a5b6ceacdedbf4f62f9'
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
