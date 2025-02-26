# Maintainer:  Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: Rojikku <RojikkuNoKami at gmail dot com>
# Contributor: Tech <technetium1337 at gmail dot com>

# Clean Chroot ccm Xeon(R) E-2146G 6c12t: ----> Total build time was 00:19:18

# 0 for PKGBUILD commands which may go out of date
# 1 for build.py which should stay current
_opt_BUILD_PY=1

# 0 for download vcpkg, set _opt_VCPKG_COMMIT_ID
# 1 for system vcpkg, ignore _opt_VCPKG_COMMIT_ID
_opt_SYS_VCPKG=0
_opt_VCPKG_COMMIT_ID='#commit=6f29f12e82a8293156836ad81cc9bf5af41fe836'
#_opt_VCPKG_COMMIT_ID='#branch=2023.10.19'
#_opt_VCPKG_COMMIT_ID=''

# 0 for package flutter, version checked
# 1 for system flutter, version warned
_opt_SYS_FLUTTER=0

true "${QUIET:=}" "${logpipe:=}"

set -u
_pkgname='rustdesk'
pkgname="${_pkgname}"
_pkgver='1.3.8'
pkgver="${_pkgver//-/.}"
pkgrel=1
_pkgverhbb='7cf11f7b771e27ecbd14fd1dd0ced55a64f40eb5'
pkgdesc='Yet another remote desktop software, written in Rust. Works out of the box, no configuration required. Great alternative to TeamViewer and AnyDesk!'
arch=('x86_64')
url='https://rustdesk.com/'
_giturl='https://github.com/rustdesk/rustdesk'
_giturlhbb='https://github.com/rustdesk/hbb_common'
license=('AGPL-3.0-only')
_dpr=('gtk3' 'xdotool' 'libxcb' 'libxfixes' 'alsa-lib' 'libva' 'libappindicator-gtk3' 'pam' 'gst-plugins-base' 'gst-plugin-pipewire') # from res/PKGBUILD/depends
#_dpr=('gtk3' 'xdotool' 'libxcb' 'libxfixes' 'alsa-lib' 'libva' 'libvdpau' 'libappindicator-gtk3' 'pam' 'gst-plugins-base' 'gst-plugin-pipewire') # from res/PKGBUILD/depends
depends=("${_dpr[@]}" 'pulse-native-provider' 'gst-plugins-base-libs')
depends+=('hicolor-icon-theme' 'xdg-utils')
depends+=('xdg-user-dirs')
depends+=('glibc' 'gcc-libs' 'glib2' 'libxtst' 'libepoxy' 'gdk-pixbuf2' 'cairo' 'at-spi2-core' 'dbus' 'gstreamer' 'pango' 'libx11' 'fontconfig' 'libxkbcommon' 'libpulse')
_mdp=('unzip' 'git' 'cmake' 'gcc' 'curl' 'wget' 'yasm' 'nasm' 'zip' 'make' 'pkg-config' 'clang') # from Readme.MD
makedepends=("${_mdp[@]}" 'rust' 'python' 'python-yaml' 'python-toml')
makedepends+=('ninja') # vcpkg build can use the latest ninja
options=('!makeflags' '!lto')
_patches=(
  '0000-disable-update-check@rustdesk.patch'
  '0001-extended_text-drop-version-for-flutter.3.22.3@rustdesk.patch' # https://github.com/rustdesk/rustdesk/blob/master/.github/workflows/bridge.yml#L77
  '0002-screen_retriever@rustdesk.patch'
)
install="${pkgname}.install"
_srcdir="${pkgname}-${_pkgver}"
_srcdirhb="hbb_common-${_pkgverhbb}"
source=(
  "${_srcdir}.tar.gz::${_giturl}/archive/refs/tags/${_pkgver}.tar.gz"
  "${_srcdirhb}.tgz::${_giturlhbb}/archive/${_pkgverhbb}.tar.gz"
  "${_patches[@]}"
)
_vcs=(
)
_srcdirvc='vcpkg'
if [ "${_opt_SYS_VCPKG}" -ne 0 ]; then
  makedepends+=('vcpkg')
else
  #source+=("git+https://github.com/microsoft/vcpkg${_opt_VCPKG_COMMIT_ID}")
  _srcdirvc="vcpkg-${_opt_VCPKG_COMMIT_ID#*=}"
  source+=("${_srcdirvc}.tgz::https://github.com/microsoft/vcpkg/archive/${_opt_VCPKG_COMMIT_ID#*=}.tar.gz")
  _vcs+=(
    # If your download gets renamed and replaced, vcpkg hash checked and found it to be the wrong one.
    # vcs sources are not hash checked. vcpkg doesn't use hash direct downloads like we do. vcpkg downloads with git and tars up, always with a different hash.
    'aom-d6f30ae474dd6c358f26de0a0fc26a0d7340a84c.tar.gz::https://aomedia.googlesource.com/aom/+archive/d6f30ae474dd6c358f26de0a0fc26a0d7340a84c.tar.gz'
    'libjpeg-turbo-libjpeg-turbo-3.1.0.tar.gz::https://github.com/libjpeg-turbo/libjpeg-turbo/archive/refs/tags/3.1.0.tar.gz'
    'libyuv-a37e6bc81b52d39cdcfd0f1428f5d6c2b2bc9861.tar.gz::https://chromium.googlesource.com/libyuv/libyuv/+archive/a37e6bc81b52d39cdcfd0f1428f5d6c2b2bc9861.tar.gz'
    'webmproject-libvpx-v1.13.1.tar.gz::https://github.com/webmproject/libvpx/archive/refs/tags/v1.13.1.tar.gz'
    'xiph-opus-v1.5.2.tar.gz::https://github.com/xiph/opus/archive/refs/tags/v1.5.2.tar.gz'
  )
fi
source+=("${_vcs[@]}")
  if [ "${_opt_SYS_FLUTTER}" -eq 0 ]; then
    _FLUVER='3.19.6' # https://docs.flutter.dev/release/archive
    source+=(
      "https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_${_FLUVER}-stable.tar.xz"
    )
  else
    makedepends+=('flutter')
  fi
  if :; then
    _FRBVER='1.80.1'
    _srcdirfrb="flutter_rust_bridge-${_FRBVER}"
    source+=(
      "${_srcdirfrb}.tar.gz::https://github.com/fzyzcjy/flutter_rust_bridge/archive/refs/tags/v${_FRBVER}.tar.gz"
    )
  fi
####
md5sums=('00478b34af29266c5315c4a6a3f82e1d'
         '2cac4c84e0a72bbec845404b6d8c74ca'
         '6acc4b5b14befec55ef84006b60c7ff5'
         '9b997c2eb989a044704fd7c1d2152d02'
         'a77a4586f30f77de2eed63e160b3a051'
         '4d782be2571f14e7b74b10a385f74e15'
         'a45fa99b7f1a972e364cc68f1ebf949c'
         '1695d39ba38a9593f4107722f3459fe0'
         '47cdfce4c02c6bd9bc249d7abfa23485'
         'd2c9de1c247f18a204e75ecefa7a2217'
         '557a08d88aa605ee6cf4156686ce4cc2'
         '74dc171bf2cfc1ada56b6e284adabca8'
         'cc8e5418ff0c163228aabbe385ba2596')
sha256sums=('4bc8e783a4ed185952386c473918291b6a849feb19005b20ce8abe5f0dfeeed7'
            '699bb89bc2ac4a13bf91c016775dd5066b6594e02605b2f8eff3fd67f01d51c9'
            '8f7f1019404ce47dc012ba7c546ad634b973452fc2c57ac64b62cdc7c1f54ea3'
            '17ad644a9987ad2dc8ddaf68e62e026c1825b3ecae46254ea98d985c5d5df582'
            '82757ee1ab6b956a3c601f7db82e2d9ad80dbbcf2ba68c63059f0b529426ccd0'
            '3df9359a39b91929868265090b97d7e2365dc8cdd5aaa1473a717720b4598f55'
            '06b9ea2f20a216fffac0c3991ea517ad4159df976bb7cd05084c8bfba3608fba'
            '35fec2e1ddfb05ecf6d93e50bc57c1e54bc81c16d611ddf6eff73fff266d8285'
            '146ea9c0fb18a268b5b6de90882a94853d557f11325d17ab40ee9c32841068d3'
            '00dae80465567272abd077f59355f95ac91d7809a2d3006f9ace2637dd429d14'
            '9480e329e989f70d69886ded470c7f8cfe6c0667cc4196d4837ac9e668fb7404'
            'db6742a20626d0d2a089eb41ad61b9b2138b996679911e9c8268c1f896191f97'
            '5c1494e79024de228a9f383c8e52e45b042cd0cf24f4b0f47ee4d5448938b336')
_vcs=("${_vcs[@]%%::*}")
_vcs=("${_vcs[@]##*/}")
noextract=("${_vcs[@]}")

if ! :; then
  _srcdir="${_pkgname}"
  source[0]="git+${_giturl}#tag=${_pkgver}"
fi

# updpkgsums now uses hashes for git commits, which are different than the git commit hashes. We want the original behavior SKIP.
# googlesource commit direct downloads do not have consistent hashes
for _fk in "${!source[@]}"; do
  if [ "${source[${_fk}]#git}" != "${source[${_fk}]}" ] || [ "${source[${_fk}]/googlesource/}" != "${source[${_fk}]}" ]; then
    md5sums["${_fk}"]='SKIP'
    sha256sums["${_fk}"]='SKIP'
  fi
done

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
  mkdir -p "${_srcdirvc}/downloads"
  if [ "${#_vcs[@]}" -gt 0 ]; then
    cp -p "${_vcs[@]}" "${_srcdirvc}/downloads"
  fi

  # Check commit ID
  if [ "${_opt_SYS_VCPKG}" -eq 0 ] && [ ! -z "${_opt_VCPKG_COMMIT_ID}" ]; then
    local _vcc
    local _pyvcc="
import yaml
import io
with open('${_srcdir}/.github/workflows/flutter-build.yml', 'r') as stream:
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

  local _vcpkgnew
  _vcpkgnew="$(sed -E -n -e '/Linux.+: vcpkg / s:^.+install ::p' "${_srcdir}/README.md")"
  if [ "${_vcpkg[*]}" != "${_vcpkgnew}" ]; then
    printf 'Flag package out of date: _vcpkg=(%s)\n' "${_vcpkgnew}"
    set +u
    false
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
#with open('.github/workflows/flutter-build.yml', 'r') as stream:
with open('.github/workflows/bridge.yml', 'r') as stream:
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
        #set +u
        #false
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
    local _pyfrb="
import yaml
import io
with open('.github/workflows/bridge.yml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)
#print(data_loaded.get('env').keys())
print(data_loaded.get('env').get('FLUTTER_RUST_BRIDGE_VERSION'))
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

  if rmdir 'libs/hbb_common'; then
    pushd 'libs' > /dev/null
    test -d "${srcdir}/${_srcdirhb}"
    ln -sr "${srcdir}/${_srcdirhb}" 'hbb_common'
    popd > /dev/null
  fi

  local _pt _ptf=() _pts=() _ptd
  for _pt in "${_patches[@]}"; do
    set +u; msg2 "Patch ${_pt}"; set -u
    _ptd=()
    if [[ "${_pt}" =~ ^[^@]+@([^.]+).patch$ ]]; then
      case "${BASH_REMATCH[1]}" in
      'rustdesk') _ptd=(-d "${srcdir}/${_srcdir}");;
      'flutter_rust_bridge') _ptd=(-d "${srcdir}/${_srcdirfrb}");;
      *) _ptd=(-d "${srcdir}/${BASH_REMATCH[1]}");;
      esac
    fi
    if patch "${_ptd[@]}" -Nup1 -i "${srcdir}/${_pt}"; then
      _pts+=("${_pt}")
    else
      _ptf+=("${_pt}")
    fi
  done
  if [ "${#_ptf[@]}" -gt 0 ]; then
     if [ "${#_pts[@]}" -gt 0 ]; then
       printf 'Patch success %s\n' "${_pts[@]}"
       printf 'Warning: Some old patches may need to be removed even if they are successful\n'
     fi
     printf 'Patch failed %s\n' "${_ptf[@]}"
     set +x
     false
  fi
  #cd '..'; cp -pr "${_srcdir}" 'a'; ln -s "${_srcdir}" 'b'; cp -pr "${_srcdirfrb}" 'fa'; ln -s "${_srcdirfrb}" 'fb'; false
  #diff -pNaru5 'a' 'b' > "0000-$RANDOM@domain.patch"
  set +u
}

build() {
  msg2 'Build vcpkg'
  set -u
  unset VCPKG_DOWNLOADS
  if [ ! -x "${_srcdirvc}/vcpkg" ]; then
    "${_srcdirvc}/bootstrap-vcpkg.sh" -disableMetrics
  fi
  export VCPKG_ROOT="${PWD}/${_srcdirvc}"
  local _vcextra=(
    --disable-metrics
    --cmake-args='-DVCPKG_BUILD_TYPE=release' # https://github.com/microsoft/vcpkg/issues/37186#issuecomment-2133951797
    --cmake-args='-DVCPKG_POLICY_MISMATCHED_NUMBER_OF_BINARIES=enabled'
    #--no-downloads
    #--only-downloads
  )
  nice "${_srcdirvc}/vcpkg" install "${_vcextra[@]}" --x-install-root="${VCPKG_ROOT}/installed" "${_vcpkg[@]}"

  cd "${_srcdir}"
    set +u; msg2 'Build rustdesk Flutter'; set -u
    set -x
    export CPATH="$(clang -v 2>&1 | grep "Selected GCC installation: " | cut -d' ' -f4-)/include"
    local _oldpath="${PATH}"
    export CARGO_INCREMENTAL=0
    export PATH="${srcdir}/flutter/bin:${_oldpath}"
    flutter doctor -v
    dart pub global activate ffigen --version 5.0.1
    pushd "${srcdir}/flutter_rust_bridge/frb_codegen"; nice cargo install --path . ; popd
    pushd flutter ; flutter clean; flutter pub get ; popd
    local _CGdefault=~/.cargo
    "${CARGO_HOME:-${_CGdefault}}"/bin/flutter_rust_bridge_codegen --rust-input ./src/flutter_ffi.rs --dart-output ./flutter/lib/generated_bridge.dart
    if [ "${_opt_BUILD_PY}" -ne 0 ]; then
      nice ./build.py --flutter
    else
      #git checkout src/ui/common.tis
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
