# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=MONAILabel
pkgname=monailabel
pkgver=0.6.0
pkgrel=3
epoch=1
pkgdesc='An intelligent open source image labeling and learning tool'
arch=('any')
url='https://github.com/Project-MONAI/MONAILabel'
license=('Apache')
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
sha512sums=('c2a4d0795aa9dadff59d483029cd6e27d9bafead81dc250b5a49a3149ee1e7c0c9c6c88e4122dbded7062f36c42c761303afc79e843febd59d2010a679cd38b0')

build() {
  cd "${_pkgname}-${pkgver}"
  BUILD_OHIF=OFF python -m build --wheel --no-isolation --skip-dependency-check
  cd "plugins/qupath"
  # build with jdk17
  sed -i "s,version = 11,version = 17," build.gradle
  gradle clean build -Porg.gradle.java.home=/usr/lib/jvm/default
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
