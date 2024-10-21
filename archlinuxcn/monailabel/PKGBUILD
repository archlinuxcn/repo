# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=MONAILabel
pkgname=monailabel
pkgver=0.8.4
pkgrel=1
epoch=1
pkgdesc='An intelligent open source image labeling and learning tool'
arch=('any')
url='https://github.com/Project-MONAI/MONAILabel'
license=('Apache-2.0')
depends=(
  python-aiofiles
  python-bcrypt
  python-cachetools
  python-dicomweb-client
  python-dotenv
  python-einops
  python-expiring-dict
  python-expiringdict
  python-fastapi
  python-filelock
  python-girder-client
  python-httpx
  python-itk
  python-jose
  python-lmdb
  python-monai
  python-multipart
  python-nibabel
  python-numpy
  python-opencv
  python-openslide
  python-passlib
  python-pillow
  python-psutil
  python-pydantic
  python-pydicom
  python-pydicom-seg
  python-pynetdicom
  python-pynrrd
  python-pytorch
  python-pytorch-ignite
  python-requests-toolbelt
  python-schedule
  python-scikit-image
  python-scikit-learn
  python-shapely
  python-simplecrf
  python-timeloop
  python-torchvision
  python-tqdm
  python-watchdog
  python-yaml
  tensorboard
  uvicorn
)
makedepends=(
  gradle
  java-environment=17
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  gdown
  python-mlflow
  python-pandas
  python-parameterized
  python-transformers
)
install="${pkgname}.install"
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Project-MONAI/MONAILabel/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('ac3d391c5b610de17e7b0da26e3ec9812959de538e2eace88bf99ffb9e31f84c3c91cc974f50a3aa6dc63383ae319e33386c51c4dfafdc7f96c39910ba4ea237')

build() {
  cd "${_pkgname}-${pkgver}"
  BUILD_OHIF=OFF python -m build --wheel --no-isolation --skip-dependency-check
  cd "plugins/qupath"
  # build with jdk17
  gradle clean build -Porg.gradle.java.home=/usr/lib/jvm/default -Ptoolchain=17
}

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  rm -rfv "${pkgdir}/usr/logconfig"
  rm -rfv ${pkgdir}${site_packages}/tests
  rm -rfv ${pkgdir}/usr/${pkgname}/plugins
  rm -vf "${pkgdir}/usr/bin/monailabel.bat"
  install -dm755 "${pkgdir}/usr/share/java/qupath-extention-monailabel"
  find "plugins/qupath/build/libs" -type f -name "*.jar" -exec install -Dm644 {} "${pkgdir}/usr/share/java/qupath-extention-monailabel" \;
}
# vim:set ts=2 sw=2 et:
