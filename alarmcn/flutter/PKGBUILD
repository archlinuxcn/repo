# Maintainer: WithTheBraid <info@braid.business>
# Co-Maintainer: Polarian <polarian@polarian.dev>, Fredy García <frealgagu at gmail dot com>
# Contributor: Philip Goto <philip.goto@gmail.com>

pkgname=flutter
pkgver=3.19.2
pkgrel=1
pkgdesc="A new mobile app SDK to help developers and designers build modern mobile apps for iOS and Android."
arch=("x86_64" "aarch64")
url="https://${pkgname}.dev"
license=("custom" "BSD" "CCPL")
depends=( # commands first
	 "bash"
	 "curl"
	 "file" # base-devel, but runtime dependency
	 "git"
	 "coreutils" # explicit dependency to mkdir, rm
	 "unzip"
	 "which" # base-devel, but runtime dependency
	 "xz"
	 "zip"
	 # runtime shared libraries
	 "glu" # libGLU.so.1 required for flutter test
	 "libglvnd" # https://github.com/flutter/engine/pull/16924
)
optdepends=("android-sdk: develop for Android devices"
	    "java-environment: develop for Android devices"
            "android-studio"
            "intellij-idea-community-edition"
            "intellij-idea-ultimate-edition"
	    "clang: clang++ is required for Linux development"
	    "cmake: CMake is required for Linux development"
            "ninja: ninja is required for Linux development"
	    "pkgconf: pkg-config is required for Linux development" # base-devel, but runtime dependency
	    "gtk3: GTK 3.0 development libraries are required for Linux development")
backup=("opt/${pkgname}/packages/${pkgname}_test/pubspec.yaml" "opt/${pkgname}/packages/${pkgname}/pubspec.yaml")
options=("!emptydirs")
install="${pkgname}.install"
source=(
  "${pkgname}-${pkgver}.tar.xz::https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/${pkgname}_linux_${pkgver/.hotfix/+hotfix}-stable.tar.xz"
  "${pkgname}.sh"
  "${pkgname}.csh"
)
sha256sums=('bb4aa5cbabedcba76469841ff16a5dfe75b24c05b0fdaee6c05db829cba58b4e'
            '1dea1952d386c43948b9970382c2da5b65b7870684b8ad2ad89124e873aa485a'
            '7ef10d753cfaac52d243549764a793f44f8284a1f4b11715ccd2fa915b026a6f')

build() {
  rm -rf "${srcdir}/${pkgname}/bin/cache" "${srcdir}/${pkgname}/.pub-cache"
  "${srcdir}/${pkgname}/bin/internal/update_dart_sdk.sh"
  "${srcdir}/${pkgname}/bin/flutter" --no-version-check precache
}

package() {
  install -Dm644 "${srcdir}/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
  install -Dm755 "${srcdir}/${pkgname}.csh" "${pkgdir}/etc/profile.d/${pkgname}.csh"
  install -dm755 "${pkgdir}/opt/${pkgname}"
  install -dm755 "${pkgdir}/usr/bin"
  cp -ra "${srcdir}/${pkgname}" "${pkgdir}/opt/"

  # version overriding, something broken; not my fault *grumble*
  echo "${pkgver}" > "${pkgdir}/opt/${pkgname}/version" 
  find "${pkgdir}/opt/${pkgname}" -type d -exec chmod a+rx {} +
  find "${pkgdir}/opt/${pkgname}" -type f -exec chmod a+r {} +

  # those files *must* be read-write for end-users; not my fault *grumble*
  chmod a+rw "${pkgdir}/opt/${pkgname}" "${pkgdir}/opt/${pkgname}/.pub-preload-cache"
  chmod -R a+rw "${pkgdir}/opt/${pkgname}/version" "${pkgdir}/opt/${pkgname}/bin/cache" "${pkgdir}/opt/${pkgname}/.git" "${pkgdir}/opt/${pkgname}/packages/flutter_tools/gradle"
  find "${pkgdir}/opt/${pkgname}" -name "pubspec.lock" -exec chmod a+rw {} +
  find "${pkgdir}/opt/${pkgname}" -name "package_config.json" -exec chmod a+rw {} +

  # fix git ref migrations
  mv "${pkgdir}/opt/${pkgname}/.git" "${pkgdir}/opt/${pkgname}/.git-refs"

  ln -s "/opt/${pkgname}/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
}
