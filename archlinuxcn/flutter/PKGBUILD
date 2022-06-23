# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Philip Goto <philip.goto@gmail.com>

pkgname=flutter
pkgver=3.0.3
pkgrel=1
pkgdesc="A new mobile app SDK to help developers and designers build modern mobile apps for iOS and Android."
arch=("x86_64")
url="https://${pkgname}.dev"
license=("custom" "BSD" "CCPL")
depends=("git" "glu" "java-environment" "libglvnd" "unzip")
optdepends=("android-sdk" "android-studio" "intellij-idea-community-edition" "intellij-idea-ultimate-edition" "ninja" "perl" "python")
makedepends=("python")
backup=("opt/${pkgname}/packages/${pkgname}_test/pubspec.yaml" "opt/${pkgname}/packages/${pkgname}/pubspec.yaml")
options=("!emptydirs")
install="${pkgname}.install"
source=(
  "${pkgname}-${pkgver}.tar.xz::https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/${pkgname}_linux_${pkgver/.hotfix/+hotfix}-stable.tar.xz"
  "${pkgname}.sh"
  "${pkgname}.csh"
)
sha256sums=(
  "f3806787f3afc379769024f4f9b20c243811881a72bc9c6e62bfc2fd50676c48"
  "1dea1952d386c43948b9970382c2da5b65b7870684b8ad2ad89124e873aa485a"
  "7ef10d753cfaac52d243549764a793f44f8284a1f4b11715ccd2fa915b026a6f"
)

package() {
  rm -rf "${srcdir}/${pkgname}/bin/cache" "${srcdir}/${pkgname}/.pub-cache"
  install -Dm644 "${srcdir}/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
  install -Dm755 "${srcdir}/${pkgname}.csh" "${pkgdir}/etc/profile.d/${pkgname}.csh"
  install -dm755 "${pkgdir}/opt/${pkgname}"
  install -dm755 "${pkgdir}/usr/bin"
  cp -ra "${srcdir}/${pkgname}" "${pkgdir}/opt/"
  "${pkgdir}/opt/${pkgname}/bin/internal/update_dart_sdk.sh"
  "${pkgdir}/opt/${pkgname}/bin/flutter" precache
  find "${pkgdir}/opt/${pkgname}" -type d -exec chmod a+rx {} +
  find "${pkgdir}/opt/${pkgname}" -type f -exec chmod a+r {} +
  chmod a+rw "${pkgdir}/opt/${pkgname}/version"
  ln -s "/opt/${pkgname}/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
}
