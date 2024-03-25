# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=MONAILabel
pkgname=monailabel
pkgver=0.8.0
pkgrel=2
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
sha512sums=('b3c15d93aac76ba89f0d15f663ebbb80c63b69b4d6aa7c7b6b0a76f3443dfaa30c1e70b43b36f9b0b3be3eeb7544932908414da08e8455bc85e7bbab338185a8')

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
