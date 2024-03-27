# Maintainer: The one with the braid <info@braid.business>

pkgbase=flutter-artifacts-google-bin
_pkgbase=flutter
pkgver=3.19.4
# in order to update these version hashes, consult the PKGBUILD and update-artifact-versions.sh
# script of https://aur.archlinux.org/pkgbase/flutter
_enginever=a5c24f538d05aaf66f7972fb23959d8cafb9f95a
_materialfontsver=3012db47f3130e62f7cc0beabff968a33cbec8d8
_gradlewver=fd5c1f2c013565a3bea56ada6df9d2b8e96d56aa
_flutterarch=$(uname -m | sed s/aarch64/arm64/ | sed s/x86_64/x64/)
# this host is blocked in China, according to Flutter docs, the FLUTTER_STORAGE_BASE_URL environment variable
# should be used to provide an alternative mirror
_storagebase="${FLUTTER_STORAGE_BASE_URL:-"https://storage.googleapis.com"}"
pkgrel=2
_pkgdesc="Flutter SDK artifacts (binary from Google)"
pkgdesc="${_pkgdesc}"
arch=("x86_64" "aarch64")
url="https://${_pkgbase}.dev"
license=("custom" "BSD" "CCPL")
makedepends=(
	"unzip"
	"tar"
)
options=("!emptydirs")
source=(
  # material_fonts
  "material_fonts.zip::${_storagebase}/flutter_infra_release/flutter/fonts/${_materialfontsver}/fonts.zip"
  # gradle_wrapper
  "gradle_wrapper.tar.gz::${_storagebase}/flutter_infra_release/gradle-wrapper/${_gradlewver}/gradle-wrapper.tgz"

  # engine/android-x86
  "android-x86.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-x86/artifacts.zip"
  # engine/android-x64
  "android-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-x64/artifacts.zip"
  # engine/android-arm
  "android-arm.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-arm/artifacts.zip"
  # engine/android-arm-profile
  "android-arm-profile.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-arm-profile/artifacts.zip"
  # engine/android-arm-release
  "android-arm-release.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-arm-release/artifacts.zip"
  # engine/android-arm64
  "android-arm64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-arm64/artifacts.zip"
  # engine/android-arm64-profile
  "android-arm64-profile.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-arm64-profile/artifacts.zip"
  # engine/android-arm64-release
  "android-arm64-release.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-arm64-release/artifacts.zip"

  # engine/android-x64-profile
  "android-x64-profile.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-x64-profile/artifacts.zip"
  # engine/android-x64-release
  "android-x64-release.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-x64-release/artifacts.zip"
  # engine/android-x86-jit-release
  "android-x64-jit-release.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-x86-jit-release/artifacts.zip"

  # flutter_web_sdk
  "flutter_web_sdk.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/flutter-web-sdk.zip"
  # pkg
  "sky_engine.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/sky_engine.zip"

  # engine/common
  "flutter_patched_sdk.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/flutter_patched_sdk.zip"
  # engine/common
  "flutter_patched_sdk_product.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/flutter_patched_sdk_product.zip"
)
source_x86_64=(
  # engine/android-arm-profile/linux-x64
  "android-arm-profile-linux-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-arm-profile/linux-x64.zip"
  # engine/android-arm-release/linux-x64
  "android-arm-release-linux-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-arm-release/linux-x64.zip"
  # engine/android-arm64-profile/linux-x64
  "android-arm64-profile-linux-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-arm64-profile/linux-x64.zip"
  # engine/android-arm64-release/linux-x64
  "android-arm64-release-linux-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-arm64-release/linux-x64.zip"
  # engine/android-x64-profile/linux-x64
  "android-x64-profile-linux-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-x64-profile/linux-x64.zip"
  # engine/android-x64-release/linux-x64
  "android-x64-release-linux-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/android-x64-release/linux-x64.zip"

  # engine/linux-$ARCH
  "engine-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/linux-x64/artifacts.zip"
  # engine/linux-$ARCH
  "gtk-debug-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/linux-x64-debug/linux-x64-flutter-gtk.zip"
  # engine/linux-$ARCH-profile
  "gtk-profile-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/linux-x64-profile/linux-x64-flutter-gtk.zip"
  # engine/linux-$ARCH-release
  "gtk-release-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/linux-x64-release/linux-x64-flutter-gtk.zip"
  # engine/linux-$ARCH
  "font-subset-x64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/linux-x64/font-subset.zip"
)
source_aarch64=(
  # engine/linux-$ARCH
  "engine-arm64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/linux-arm64/artifacts.zip"
  # engine/linux-$ARCH
  "gtk-debug-arm64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/linux-arm64-debug/linux-arm64-flutter-gtk.zip"
  # engine/linux-$ARCH-profile
  "gtk-profile-arm64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/linux-arm64-profile/linux-arm64-flutter-gtk.zip"
  # engine/linux-$ARCH-release
  "gtk-release-arm64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/linux-arm64-release/linux-arm64-flutter-gtk.zip"
  # engine/linux-$ARCH
  "font-subset-arm64.zip::${_storagebase}/flutter_infra_release/flutter/${_enginever}/linux-arm64/font-subset.zip"
)
noextract=(
  "material_fonts.zip"
  "gradle_wrapper.tar.gz"

  "android-x86.zip"
  "android-x64.zip"
  "android-arm.zip"
  "android-arm-profile.zip"
  "android-arm-release.zip"
  "android-arm64.zip"
  "android-arm64-profile.zip"
  "android-arm64-release.zip"

  "android-x64-profile.zip"
  "android-x64-release.zip"
  "android-x64-jit-release.zip"

  "flutter_web_sdk.zip"
  "sky_engine.zip"
  "flutter_patched_sdk.zip"
  "flutter_patched_sdk_product.zip"

  # x64
  "android-arm-profile-linux-x64.zip"
  "android-arm-release-linux-x64.zip"
  "android-arm64-profile-linux-x64.zip"
  "android-arm64-release-linux-x64.zip"
  "android-x64-profile-linux-x64.zip"
  "android-x64-release-linux-x64.zip"

  "engine-x64.zip"
  "gtk-debug-x64.zip"
  "gtk-profile-x64.zip"
  "gtk-release-x64.zip"
  "font-subset-x64.zip"

  # arm64
  "engine-arm64.zip"
  "gtk-debug-arm64.zip"
  "gtk-profile-arm64.zip"
  "gtk-release-arm64.zip"
  "font-subset-arm64.zip"
)



sha256sums=('e56fa8e9bb4589fde964be3de451f3e5b251e4a1eafb1dc98d94add034dd5a86'
            '31e9428baf1a2b2f485f1110c5899f852649b33d46a2e9b07f9d17752d50190a'
            'd5da421c4849c169766be16f51e2634e02f1536416befb61f5f6551fb60c32d9'
            'ec7e0d94b5fa32efe772e246893e9cc832e1f133e737f498fb7f7da5b84192c2'
            'e5be895a4e8d2bf7d553839eeb097aff109fcc2efc45d76d7feebb18855831c8'
            'e56fa8dfcaa3830eaa616c66faae0910a32df772d01a2d68d3fa2c895e6d65ff'
            '3921c7e7f95e6d95731fbc673da5e692da006738f3667a7db0295cb5ee7c1632'
            '3e7f49b80b31db50b6b74fc91a4d9a69407ebb1b1a33a6525e3e6dad0a397d99'
            'e82408b2c0d7fa57f490a03492bfd9110a8ef923d4f22417fa99fd8854022dc8'
            'c00b0d2b848dbbb184d263e7be87225219cf6d13fc2193d986c8684630b18fac'
            'b50fed99cd5f6ae41282beab6c97380832aa0a1b81c261fe855bbff7ca95e9d3'
            '69153dd195a753bafd0f06ac0991cc92d408590e7b1dc398370dd4aa0255f614'
            '5a38c17cfc0e9aef522d20b6b889462b340cc0430ece8d9a456b947d0cb731e4'
            'efa93f450398060b49a89b04caeac7d4a8bf2c3870170e6b619acaf0ffb0337b'
            'b1f8faafcc0f3492aa1d0dab511e9a026de19356e35c55a237b8cfa3c0b1bcf1'
            '0a52880f8f3aff667db1a29ec2e68567689b378e773345427f9e5cf6cb80dea3'
            '2e848e6ee2dd591c0e558ee37d80391e4acb5bf8672cbe3e02af9a52d39e25b8')
sha256sums_x86_64=('f41f8cf16ed627f94c9ad2c60602fdedb585ff1f8d50f4c44927da706dbe1808'
                   '9032d360fb258fba392fd00a150881674bfa88598c6fad2c73f552a03501f1ce'
                   '33517b19738cf68a4c1de7566d3602a09b3be037b9f4aca17f10a364b476cb9e'
                   '29780ca6efbcdabe6988cd7eae6dbf995c5839d3f4c0b1f3ee6de2f9bfdc6c5c'
                   '6a35206886a116ba4ae83432035b877818b883033a70697a8330c473f9374b8e'
                   '1778a36d34657f853b1c6cb848c5dae6a1480babd357131ab723d8b41109ffd3'
                   'c72981b583838b6016f3ab5bf5240f041acefc82c3f67983e447373b520e54e5'
                   '214302538b9c983bc075cb59770329f4f751f2a0f73c390566f68d670cdcdb6f'
                   '70edb9c63fe08d77cb2a9b59f9d4d1ec16e28a49737e8dd0cdbf5ccefcc562bb'
                   '6f5d86f207c78cb64744889c34ed3ac45e403ea035d512674e5b348cb0d6355a'
                   '05778e62c2da50d8280dc55589225871bf90bb2d543b48d2f1d6acd73460d573')
sha256sums_aarch64=('7f99e5020f79d3a9a369e579543db860afef6f2a41403992733a2b707b73e757'
                    '10ae30dac5b3ed1cc820a2d0ea9796ce2fa0a6e87813d212a15e9d595a1c3afc'
                    'ddc83cb35141192222529db34e57e26aef70b3960d4c688b73121a434d580232'
                    '65500e40641c62f470d36034e3579c87108964660788d67fc3d771be66b1a096'
                    '6e0044cf445b8650efe57daf9415adb99f063c7a529437f2dbe58c7774e57cab')

prepare() {
  mkdir -p "${srcdir}/${_pkgbase}/bin/cache/artifacts"

  cd "${srcdir}/${_pkgbase}/bin/cache"

  unzip -o -q "${srcdir}/flutter_web_sdk.zip" -d flutter_web_sdk
  unzip -o -q "${srcdir}/sky_engine.zip" -d pkg

  cd "${srcdir}/${_pkgbase}/bin/cache/artifacts"

  mkdir -p "gradle_wrapper"
  tar -xzf "${srcdir}/gradle_wrapper.tar.gz" -C "gradle_wrapper"
  unzip -o -q "${srcdir}/material_fonts.zip" -d "material_fonts"

  mkdir -p engine/android-arm-profile
  mkdir -p engine/android-arm64-profile
  mkdir -p engine/android-x64-profile
  mkdir -p engine/android-arm-release
  mkdir -p engine/android-arm64-release
  mkdir -p engine/android-x64-release

  if [ "$(uname -m)" == "x86_64" ]; then

  unzip -o -q "${srcdir}/android-arm-profile-linux-x64.zip" -d engine/android-arm-profile/linux-x64
  unzip -o -q "${srcdir}/android-arm-release-linux-x64.zip" -d engine/android-arm-release/linux-x64
  unzip -o -q "${srcdir}/android-arm64-profile-linux-x64.zip" -d engine/android-arm64-profile/linux-x64
  unzip -o -q "${srcdir}/android-arm64-release-linux-x64.zip" -d engine/android-arm64-release/linux-x64
  unzip -o -q "${srcdir}/android-x64-profile-linux-x64.zip" -d engine/android-x64-profile/linux-x64
  unzip -o -q "${srcdir}/android-x64-release-linux-x64.zip" -d engine/android-x64-release/linux-x64

  fi

  unzip -o -q "${srcdir}/android-x86.zip" -d engine/android-x86
  unzip -o -q "${srcdir}/android-x64.zip" -d engine/android-x64
  unzip -o -q "${srcdir}/android-arm.zip" -d engine/android-arm
  unzip -o -q "${srcdir}/android-arm-profile.zip" -d engine/android-arm-profile
  unzip -o -q "${srcdir}/android-arm-release.zip" -d engine/android-arm-release
  unzip -o -q "${srcdir}/android-arm64.zip" -d engine/android-arm64
  unzip -o -q "${srcdir}/android-arm64-profile.zip" -d engine/android-arm64-profile
  unzip -o -q "${srcdir}/android-arm64-release.zip" -d engine/android-arm64-release

  unzip -o -q "${srcdir}/android-x64-profile.zip" -d engine/android-x64-profile
  unzip -o -q "${srcdir}/android-x64-release.zip" -d engine/android-x64-release
  unzip -o -q "${srcdir}/android-x64-jit-release.zip" -d engine/android-x86-jit-release

  unzip -o -q "${srcdir}/flutter_patched_sdk.zip" -d engine/common
  unzip -o -q "${srcdir}/flutter_patched_sdk_product.zip" -d engine/common

  unzip -o -q "${srcdir}/engine-${_flutterarch}.zip" -d engine/linux-${_flutterarch}
  unzip -o -q "${srcdir}/gtk-debug-${_flutterarch}.zip" -d engine/linux-${_flutterarch}
  unzip -o -q "${srcdir}/gtk-profile-${_flutterarch}.zip" -d engine/linux-${_flutterarch}-profile
  unzip -o -q "${srcdir}/gtk-release-${_flutterarch}.zip" -d engine/linux-${_flutterarch}-release
  unzip -o -q "${srcdir}/font-subset-${_flutterarch}.zip" -d engine/linux-${_flutterarch}
}

build() {
    true
}

_package-engine-common-google-bin() {
  pkgdesc="${_pkgdesc} - common engine files"
  depends=(
	"${_pkgbase}-common=${pkgver}"
	"${_pkgbase}-sky-engine=${pkgver}"
	"${_pkgbase}-material-fonts=${pkgver}"
  )
  provides=(
	"${_pkgbase}-engine-common=${pkgver}"
  )
  conflicts=(
	"${_pkgbase}-engine-common=${pkgver}"
  )

  install -dm755 "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"

  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/common" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine/common"
}

_package-sky-engine-google-bin() {
  pkgdesc="${_pkgdesc} - sky-engine"
  depends=(
	"${_pkgbase}-engine-common=${pkgver}"
  )
  provides=(
	"${_pkgbase}-sky-engine=${pkgver}"
  )
  conflicts=(
	"${_pkgbase}-sky-engine=${pkgver}"
  )

  install -dm755 "${pkgdir}/usr/lib/${_pkgbase}/bin/cache"

  cp -ra "${srcdir}/${_pkgbase}/bin/cache/pkg" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/pkg"
}

_package-material-fonts-google-bin() {
  pkgdesc="${_pkgdesc} - material fonts"
  depends=(
	"${_pkgbase}-engine-common=${pkgver}"
  )
  provides=(
	"${_pkgbase}-material-fonts=${pkgver}"
  )
  conflicts=(
	"${_pkgbase}-material-fonts=${pkgver}"
  )

  install -dm755 "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts"

  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/material_fonts" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/material_fonts"
}

_package-engine-linux-google-bin() {
  pkgdesc="${_pkgdesc} - linux engine"
  depends=(
	"${_pkgbase}-engine-common=${pkgver}"
  )
  provides=(
	"${_pkgbase}-engine-linux=${pkgver}"
  )
  conflicts=(
	"${_pkgbase}-engine-linux=${pkgver}"
  )

  install -dm755 "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"

  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/linux-${_flutterarch}" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"
  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/linux-${_flutterarch}-profile" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"
  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/linux-${_flutterarch}-release" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"
}

_package-engine-web-google-bin() {
  pkgdesc="${_pkgdesc} - web engine"
  depends=(
	"${_pkgbase}-engine-common=${pkgver}"
  )
  provides=(
	"${_pkgbase}-engine-web=${pkgver}"
  )
  conflicts=(
	"${_pkgbase}-engine-web=${pkgver}"
  )

  install -dm755 "${pkgdir}/usr/lib/${_pkgbase}/bin/cache"

  cp -ra "${srcdir}/${_pkgbase}/bin/cache/flutter_web_sdk" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache"
}

_package-gradle-google-bin() {
  pkgdesc="${_pkgdesc} - gradle wrapper"
  depends=(
	"${_pkgbase}-common=${pkgver}"
  )
  provides=(
	"${_pkgbase}-gradle=${pkgver}"
  )
  conflicts=(
	"${_pkgbase}-gradle=${pkgver}"
  )

  install -dm755 "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts"

  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/gradle_wrapper" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts"
}

_package-engine-android-google-bin() {
  pkgdesc="${_pkgdesc} - android engine"
  depends=(
	"${_pkgbase}-engine-common=${pkgver}"
  )
  provides=(
	"${_pkgbase}-engine-android=${pkgver}"
  )
  conflicts=(
	"${_pkgbase}-engine-android=${pkgver}"
  )

  install -dm755 "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"

  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/android-arm" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"
  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/android-arm-release" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"
  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/android-arm-profile" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"

  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/android-arm64" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"
  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/android-arm64-release" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"
  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/android-arm64-profile" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"

  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/android-x64" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"
  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/android-x64-release" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"
  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/android-x64-profile" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"

  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/android-x86" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"
  cp -ra "${srcdir}/${_pkgbase}/bin/cache/artifacts/engine/android-x86-jit-release" "${pkgdir}/usr/lib/${_pkgbase}/bin/cache/artifacts/engine"
}

pkgname=("${_pkgbase}-engine-common-google-bin" "${_pkgbase}-engine-linux-google-bin" "${_pkgbase}-engine-web-google-bin" "${_pkgbase}-engine-android-google-bin" "${_pkgbase}-sky-engine-google-bin" "${_pkgbase}-material-fonts-google-bin" "${_pkgbase}-gradle-google-bin")

for _p in "${pkgname[@]}"; do
  eval "package_$_p() {
    $(declare -f "_package${_p#$_pkgbase}")
    _package${_p#$_pkgbase}
  }"
done

