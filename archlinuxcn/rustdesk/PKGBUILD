# Maintainer:  Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: Rojikku <RojikkuNoKami at gmail dot com>
# Contributor: Tech <technetium1337 at gmail dot com>

# 0 for PKGBUILD commands which may go out of date
# 1 for build.py which should stay current
_opt_BUILD_PY=1

# 0 for download vcpkg, set _opt_VCPKG_COMMIT_ID
# 1 for system vcpkg, ignore _opt_VCPKG_COMMIT_ID
_opt_SYS_VCPKG=0
#_opt_VCPKG_COMMIT_ID='#commit=14e7bb4ae24616ec54ff6b2f6ef4e8659434ea44'
_opt_VCPKG_COMMIT_ID=''

# 0 for package flutter, version checked
# 1 for system flutter, version warned
_opt_SYS_FLUTTER=0

set -u
_pkgname='rustdesk'
pkgname="${_pkgname}"
_pkgver='1.3.2'
pkgver="${_pkgver//-/.}"
pkgrel=1
pkgdesc='Yet another remote desktop software, written in Rust. Works out of the box, no configuration required. Great alternative to TeamViewer and AnyDesk!'
arch=('x86_64')
url='https://rustdesk.com/'
_giturl='https://github.com/rustdesk/rustdesk'
license=('AGPL-3.0-only')
_dpr=('gtk3' 'xdotool' 'libxcb' 'libxfixes' 'alsa-lib' 'libva' 'libvdpau' 'libappindicator-gtk3' 'pam' 'gst-plugins-base' 'gst-plugin-pipewire') # from res/PKGBUILD/depends
depends=("${_dpr[@]}" 'pulse-native-provider' 'gst-plugins-base-libs')
depends+=('hicolor-icon-theme' 'xdg-utils')
depends+=('xdg-user-dirs')
depends+=('glibc' 'gcc-libs' 'glib2' 'libxtst' 'libepoxy' 'gdk-pixbuf2' 'cairo' 'at-spi2-core' 'dbus' 'gstreamer' 'pango' 'libx11' 'fontconfig' 'libxkbcommon' 'libpulse')
_mdp=('unzip' 'git' 'cmake' 'gcc' 'curl' 'wget' 'yasm' 'nasm' 'zip' 'make' 'pkg-config' 'clang') # from Readme.MD
makedepends=("${_mdp[@]}" 'rust' 'python' 'python-yaml' 'python-toml')
makedepends+=('ninja') # vcpkg build can use the latest ninja
options=('!makeflags' '!lto')
install="${pkgname}.install"
_srcdir="${pkgname}-${_pkgver}"
source=(
  "${_srcdir}.tar.gz::https://github.com/rustdesk/rustdesk/archive/refs/tags/${_pkgver}.tar.gz"
)
_vcs=(
)
if [ "${_opt_SYS_VCPKG}" -ne 0 ]; then
  makedepends+=('vcpkg')
  _vcs+=(
  )
else
  source+=("git+https://github.com/microsoft/vcpkg${_opt_VCPKG_COMMIT_ID}")
fi
source+=("${_vcs[@]}")
  if [ "${_opt_SYS_FLUTTER}" -eq 0 ]; then
    _FLUVER='3.19.6'
    source+=(
      "https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_${_FLUVER}-stable.tar.xz"
    )
  else
    makedepends+=('flutter')
  fi
  if :; then
    _FRBVER='1.80.0'
    source+=(
      "flutter_rust_bridge-${_FRBVER}.tar.gz::https://github.com/fzyzcjy/flutter_rust_bridge/archive/refs/tags/v${_FRBVER}.tar.gz"
    )
  fi
if ! :; then
  _srcdir="${_pkgname}"
  source[0]="git+${_giturl}#tag=${_pkgver}"
fi
md5sums=('5801689428f121994a3fa0b7763dfc1c'
         'SKIP'
         '74dc171bf2cfc1ada56b6e284adabca8'
         'a63659fb966758db9fe95e5aae89757a')
sha256sums=('90d4fc82c4578c7641d0b0cf96bff99d64e904b864bb5d0ddf55d4a6afe95325'
            'SKIP'
            'db6742a20626d0d2a089eb41ad61b9b2138b996679911e9c8268c1f896191f97'
            'b3a05ffca1f57afa48bd006d732969146dafa164c71390070623ba569977f9d3')
_vcs=("${_vcs[@]%%::*}")
_vcs=("${_vcs[@]##*/}")
noextract=("${_vcs[@]}")

_vcpkg=(libvpx libyuv opus aom)

_prepare_vc() {
  msg '_prepare_vc'
  set -u
  if [ "${_opt_SYS_VCPKG}" -ne 0 ] && [ ! -d 'vcpkg' ]; then
    local _vcp='/opt/vcpkg'
    if [ ! -d "${_vcp}" ]; then
      _vcp='/usr/lib/vcpkg'
    fi
    set +u; msg2 "Copy ${_vcp}"; set -u
    cp -pr "${_vcp}" .
  fi
  mkdir -p 'vcpkg/downloads'
  if [ "${#_vcs[@]}" -gt 0 ]; then
    cp -p "${_vcs[@]}" 'vcpkg/downloads'
  fi

  # Check commit ID
  if [ "${_opt_SYS_VCPKG}" -eq 0 ] && [ ! -z "${_opt_VCPKG_COMMIT_ID}" ]; then
    local _vcc
    local _pyvcc="
import yaml
import io
with open('rustdesk/.github/workflows/flutter-build.yml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)
#print(data_loaded.get('env').keys())
print(data_loaded.get('env').get('VCPKG_COMMIT_ID'))
"
    _vcc="$(python -c "${_pyvcc}")"
    if [ "${_vcc}" != "${_opt_VCPKG_COMMIT_ID#*=}" ]; then
      echo "Flag package out of date: _opt_VCPKG_COMMIT_ID must be changed to ${_vcc}"
      set +u
      false
    fi
  fi
  set +u
}

# Same elements in same order
_dpr_check() {
  msg '_dpr_check'
  set -u
  pushd "${_srcdir}" > /dev/null
  (
    source 'res/PKGBUILD'
    if [ "${#_dpr[@]}" -ne "${#depends[@]}" ]; then
      echo 'Flag package out of date: Update _dpr from res/PKGBUILD/depends=()'
      false
    fi
    for((f=0; f<"${#_dpr[@]}"; f++)); do
      if [ "${_dpr[f]}" != "${depends[f]}" ]; then
        echo 'Flag package out of date: Update _dpr from res/PKGBUILD/depends=()'
        set +u
        false
      fi
    done
  )
  popd > /dev/null
  set +u
}

_flutter_check() {
  set +u; msg '_flutter_check'; set -u

    local _FLUTTER_VERSION
    local _pyfv="
import yaml
import io
with open('.github/workflows/flutter-build.yml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)
#print(data_loaded.get('env').keys())
print(data_loaded.get('env').get('FLUTTER_VERSION'))
"
    _FLUTTER_VERSION="$(python -c "${_pyfv}")"
    if [ "${_opt_SYS_FLUTTER}" -ne 0 ]; then
      local _FLUVER
      _FLUVER="$(pacman -Q flutter)"
      _FLUVER="${_FLUVER##* }"
      _FLUVER="${_FLUVER%%-*}"
    fi
    if [ "${_FLUTTER_VERSION}" != "${_FLUVER}" ]; then
      if [ "${_opt_SYS_FLUTTER}" -ne 0 ]; then
        set +u; msg2 "Warning: expected Flutter version is ${_FLUTTER_VERSION}"; set -u
        _FLUTTER_VERSION="${_FLUVER}"
      else
        printf 'Flutter version has changed to %s\n' "${_FLUTTER_VERSION}"
        set +u
        false
      fi
    fi
    set +u; msg2 "FLUTTER_VERSION=${_FLUTTER_VERSION}"; set -u
    local _flutter_rust_bridge
    local _pyfrb="
import toml
new_toml_string = toml.load('Cargo.toml')
#print(new_toml_string.keys())
print(new_toml_string.get('dependencies').get('flutter_rust_bridge').get('version'))
"
    _flutter_rust_bridge="$(python -c "${_pyfrb}")"
    _flutter_rust_bridge="${_flutter_rust_bridge#=}"
    if [ "$(vercmp "${_flutter_rust_bridge}" "${_FRBVER%.0}")" -gt 0 ]; then
      printf 'flutter_rust_bridge version has changed to %s\n' "${_flutter_rust_bridge}"
      set +u
      false
    fi
    set +u; msg2 "flutter_rust_bridge=${_flutter_rust_bridge}"; set -u

}

_mod_py() {
  if [ "$(grep -c -F -e 'os.system' 'build.py')" -gt 1 ]; then
    local _lf=$'\n'
    local _nc='
def systemecho(cmd):
    print(cmd)
    return os.system(cmd)

'
    _nc="${_nc//${_lf}/\\n}"
    sed -e '# echo all system commands' \
        -e 's:os.system:systemecho:g' \
        -e "s/^def get_version/${_nc}&/g" \
        -e '# Disable makepkg' \
        -e 's:makepkg:true &:g' \
        -e '/pkg.tar.zst/ s:mv:true &:g' \
        -i 'build.py'
  fi
  if [ "${source[0]#git}" = "${source[0]}" ]; then
    sed -e 's:git checkout:true &:g' -i 'build.py'
  fi
}

prepare() {
  _dpr_check
  #rm -rf ~/'.cache/vcpkg/archives' ~/'.vcpkg'
  _prepare_vc
  set -u
    if [ "${_opt_SYS_FLUTTER}" -ne 0 ]; then
      set +u; msg2 'Copy /opt/flutter'; set -u
      rm -rf 'flutter'
      if [ -d '/opt/flutter' ]; then
        cp -pr '/opt/flutter' .
      else
        cp -pr '/usr/lib/flutter' .
      fi
    fi
    if [ ! -d 'flutter_rust_bridge' ]; then
      ln -s "flutter_rust_bridge-${_FRBVER}" 'flutter_rust_bridge'
      test -d 'flutter_rust_bridge'
    fi

  cd "${_srcdir}"
  _flutter_check
  _mod_py
  set +u
}

build() {
  msg2 'Build vcpkg'
  set -u
  if [ ! -x vcpkg/vcpkg ]; then
    vcpkg/bootstrap-vcpkg.sh
  fi
  export VCPKG_ROOT="${PWD}/vcpkg"
  nice vcpkg/vcpkg install "${_vcpkg[@]}"

  cd "${_srcdir}"
    set +u; msg2 'Build rustdesk Flutter'; set -u
    set -x
    export CPATH="$(clang -v 2>&1 | grep "Selected GCC installation: " | cut -d' ' -f4-)/include"
    export PATH="${srcdir}/flutter/bin:$PATH"
    dart pub global activate ffigen --version 5.0.1
    pushd "${srcdir}/flutter_rust_bridge/frb_codegen"; nice cargo install --path . ; popd
    pushd flutter ; flutter clean; flutter pub get ; popd
    local _CGdefault=~/.cargo
    "${CARGO_HOME:-${_CGdefault}}"/bin/flutter_rust_bridge_codegen --rust-input ./src/flutter_ffi.rs --dart-output ./flutter/lib/generated_bridge.dart
    if [ "${_opt_BUILD_PY}" -ne 0 ]; then
      nice ./build.py --flutter
    else
      git checkout src/ui/common.tis
      nice cargo build --features flutter --lib --release
      pushd flutter
      nice flutter build linux --release
      popd
    fi
    set +x
  set +u
}

# This rebuilds the entire package
check_disabled() {
  cd "${_srcdir}"
  nice cargo test --release
}

package() {
  set -u
  cd "${_srcdir}"

    install -d "${pkgdir}/usr/lib/"
    cp -pr 'flutter/build/linux/x64/release/bundle' "${pkgdir}/usr/lib/"
    mv "${pkgdir}/usr/lib/"{bundle,${_pkgname}}
      install -d "${pkgdir}/usr/bin/"
      ln -s -t "${pkgdir}/usr/bin/" "/usr/lib/${_pkgname}/${_pkgname}"

  install -Dm0644 "res/${_pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system/"

  install -Dm0644 'res/32x32.png' "${pkgdir}/usr/share/icons/hicolor/32x32/apps/${_pkgname}.png"
  install -Dm0644 'res/128x128.png' "${pkgdir}/usr/share/icons/hicolor/128x128/apps/${_pkgname}.png"
  install -Dm0644 'res/128x128@2x.png' "${pkgdir}/usr/share/icons/hicolor/256x256/apps/${_pkgname}.png"

  install -Dm0644 /dev/stdin "${pkgdir}/usr/share/applications/${_pkgname}.desktop" << EOF
[Desktop Entry]
Version=${pkgver%.r*}
Name=RustDesk
GenericName=Remote Desktop
GenericName[zh_CN]=远程桌面
Comment=Remote Desktop
Comment[zh_CN]=远程桌面
Exec=${_pkgname} %u
Icon=${_pkgname}
Terminal=false
Type=Application
MimeType=text/html;text/xml;application/xhtml+xml;application/vnd.mozilla.xul+xml;text/mml;x-scheme-handler/http;x-scheme-handler/https;
StartupNotify=true
Categories=Network;RemoteAccess;GTK;
Keywords=internet;
Actions=new-window;

X-Desktop-File-Install-Version=0.23

[Desktop Action new-window]
Name=Open a New Window
EOF
  install -Dm644 'LICENCE' -t "${pkgdir}/usr/share/licenses/${_pkgname}"
  set +u
}
set +u
