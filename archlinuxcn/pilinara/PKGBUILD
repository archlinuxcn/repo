# Maintainer: nlsdt <nlsdt@archlinuxcn.org>

pkgname=pilinara
_pkgname=pilinara
pkgver=2.1.2
pkgrel=3
url="https://github.com/Starfallan/PiliNara"
pkgdesc="PiliPlus 的第三方Fork版本，做了一些自用改动"
arch=('x86_64')
license=('GPL-3.0-or-later')
depends=('gtk3' 'mpv' 'libayatana-appindicator' 'webkit2gtk-4.1')
makedepends=('clang' 'cmake' 'git' 'ninja' 'fvm' 'patchelf')
provides=('pilinara')
conflicts=('pilinara-bin' 'pilinara-git')
options=('!debug')

source_x86_64=("${_pkgname}::git+${url}.git#tag=${pkgver}"
               "0001-fix-refresh-layout-semantics.patch")
sha256sums_x86_64=('83bfd5e1a4ed9d533ab131a5414568ba9baf782dd81948d7e1c301c1a419f6b2'
                   '75d7a11411bbb713665e0c3eb1ed6a666b1641bb95fe3dd5c4b89aaeebe08906')

prepare() {
  cd "${_pkgname}/"
  printf "正在生成编译参数...\n"
  local _vername _vercode _verhash _buildtime
  _vername="$(grep -m1 '^version:' pubspec.yaml | sed -E 's/^version:[[:space:]]*([0-9.]+).*/\1/')"
  _vercode="$(git rev-list --count HEAD)"
  _verhash="$(git rev-parse HEAD)"
  _buildtime="$(date +%s)"
  printf '{"pili.name":"%s","pili.code":%s,"pili.hash":"%s","pili.time":%s}\n' \
    "${_vername}" "${_vercode}" "${_verhash}" "${_buildtime}" > pili_release.json
  sed -i "s/^version:.*/version: ${_vername}+${_vercode}/" pubspec.yaml
  # 回归补丁
  patch -Np1 < "${srcdir}/0001-fix-refresh-layout-semantics.patch"
  fvm install
  fvm flutter --disable-analytics
  fvm flutter --no-version-check pub get
}

build() {
  cd "${_pkgname}/"
  local _sdk _scripts
  _sdk="$(readlink -f .fvm/flutter_sdk)"
  _scripts="${PWD}/lib/scripts"

  printf "正在运行 Flutter SDK 补丁...\n"
  git -C "${_sdk}" reset --hard HEAD
  local _patches=(modal_barrier text_selection mouse_cursor image_anim
                  layout_builder navigation_drawer popup_menu fab
                  null_safety_for_selectable_region selectable_region
                  editable_text text_field scroll_position scrollable
                  scrollable_gesture draggable_scrollable_sheet scaffold
                  text text_painter sliver refresh_indicator)
  for _patch in "${_patches[@]}"; do
    git -C "${_sdk}" apply "${_scripts}/${_patch}.patch"
  done

  printf "正在应用 material_ui 包补丁...\n"
  local _pubcache _material _mp
  _pubcache="${PUB_CACHE:-${HOME}/.pub-cache}/hosted/pub.dev"
  rm -rf "${_pubcache}"/material_ui-*
  fvm flutter pub get
  _material="$(ls -d "${_pubcache}"/material_ui-* 2>/dev/null | sort -V | tail -1)"
  if [[ -z "${_material}" ]]; then
    printf "警告: 未找到 material_ui, 跳过其补丁。\n"
  else
    for _mp in "${_scripts}"/material/*.patch; do
      case "$(basename "${_mp}")" in
        bottom_sheet_android.patch|bottom_sheet_ios_flutter_material.patch) continue ;;
      esac
      sed -i 's/\r$//' "${_mp}"
      git -C "${_material}" apply "${_mp}"
    done
  fi

  printf "补丁应用完成, 开始构建...\n"
  if fvm flutter build linux --no-pub --release --dart-define-from-file=pili_release.json; then
    git -C "${_sdk}" reset --hard HEAD
  else
    _rc=$?
    printf "构建失败, 正在恢复 Flutter SDK...\n"
    git -C "${_sdk}" reset --hard HEAD
    return ${_rc}
  fi
  printf "构建完成, Flutter SDK 已恢复.\n"
}

package() {
  cd "${_pkgname}/"
  local _srcdir=build/linux/x64/release/bundle

  install -d "${pkgdir}/opt/${_pkgname}"
  install -d "${pkgdir}/usr/bin"
  install -Dm755 "${_srcdir}/${_pkgname}" "${pkgdir}/opt/${_pkgname}/${_pkgname}"
  cp -a "${_srcdir}/lib" "${pkgdir}/opt/${_pkgname}/"
  cp -a "${_srcdir}/data" "${pkgdir}/opt/${_pkgname}/"

  find "${pkgdir}/opt/${_pkgname}/lib" -type f -name "*.so*" -exec \
  patchelf --set-rpath '$ORIGIN' {} \;

  install -Dm644 "assets/images/logo/logo.png" \
    "${pkgdir}/usr/share/icons/hicolor/512x512/apps/${_pkgname}.png"
  install -Dm644 "assets/linux/com.example.${_pkgname}.desktop" \
    "${pkgdir}/usr/share/applications/com.example.${_pkgname}.desktop"
  ln -s "/opt/${_pkgname}/${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
}
