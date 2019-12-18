# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Philip Goto <philip.goto@gmail.com>

pkgname=flutter
pkgver=1.12.13+hotfix.5
pkgrel=1
pkgdesc="A new mobile app SDK to help developers and designers build modern mobile apps for iOS and Android."
arch=("x86_64")
url="https://${pkgname}.io"
license=("custom" "BSD" "CCPL")
depends=("glu" "java-environment" "lib32-libglvnd")
optdepends=(
  "android-sdk"
  "android-studio"
  "bash"
  "dart"
  "git"
  "intellij-idea-community-edition"
  "intellij-idea-ultimate-edition"
  "perl"
  "python"
  "sh"
)
makedepends=("git" "python")
backup=("opt/${pkgname}/packages/${pkgname}_test/pubspec.yaml" "opt/${pkgname}/packages/${pkgname}/pubspec.yaml")
options=("!emptydirs")
install="${pkgname}.install"
source=(
  "${pkgname}-${pkgver}.tar.xz::https://storage.googleapis.com/flutter_infra/releases/stable/linux/${pkgname}_linux_v${pkgver/.hotfix/+hotfix}-stable.tar.xz"
  "${pkgname}.sh"
  "${pkgname}.csh"
)
sha256sums=(
  "d792c92895623da35e1a9ccd8bc2fe84c81dd72c2c54073f56fe70625866d800"
  "1dea1952d386c43948b9970382c2da5b65b7870684b8ad2ad89124e873aa485a"
  "7ef10d753cfaac52d243549764a793f44f8284a1f4b11715ccd2fa915b026a6f"
)

build() {
  cd "${srcdir}/${pkgname}"
  "${srcdir}/${pkgname}/bin/${pkgname}" doctor
}

package() {
  install -Dm644 "${srcdir}/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
  install -Dm755 "${srcdir}/${pkgname}.csh" "${pkgdir}/etc/profile.d/${pkgname}.csh"
  install -dm755 "${pkgdir}/opt/${pkgname}"
  install -dm755 "${pkgdir}/usr/bin"
  cp -ra "${srcdir}/${pkgname}" "${pkgdir}/opt/"
  find "${pkgdir}/opt/${pkgname}" -type d -exec chmod a+rx {} +
  find "${pkgdir}/opt/${pkgname}" -type f -exec chmod a+r {} +
  chmod a+rw "${pkgdir}/opt/${pkgname}/bin/cache/lockfile" "${pkgdir}/opt/${pkgname}/version"
  ln -s "/opt/${pkgname}/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
}
