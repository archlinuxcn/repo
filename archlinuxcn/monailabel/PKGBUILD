# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=MONAILabel
pkgname=monailabel
pkgver=0.3.1
pkgrel=1
pkgdesc='An intelligent open source image labeling and learning tool'
arch=('any')
url='https://github.com/Project-MONAI/MONAILabel'
license=('Apache')
depends=(
  python-aiofiles
  python-dicomweb-client
  python-dotenv
  python-einops
  python-expiringdict
  python-fastapi
  python-filelock
  python-httpx
  python-itk
  python-lmdb
  python-monai
  python-multipart
  python-nibabel
  python-numpy
  python-openslide
  python-pillow
  python-psutil
  python-pydantic
  python-pydicom
  python-pydicom-seg
  python-pynetdicom
  python-pytorch
  python-pytorch-ignite
  python-requests-toolbelt
  python-schedule
  python-scikit-image
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
  python-pip
  python-setuptools
)
optdepends=(
  gdown
  python-lmdb
  python-mlflow
  python-pandas
  python-parameterized
  python-pillow
  python-psutil
  python-transformers
  tensorboard
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Project-MONAI/MONAILabel/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('bfd4c430b6b25f1b7ba4ecd6f75bdf9f9e0af44f54d3de3cf47e13542d8a4bcab200aec819f8d8fd4521113a027ef44f9957c96741fbf2bd2d6e56ade4627324')

prepare() {
  # quick fix to work with python-dicomweb-client > 0.52.0
  find "${_pkgname}-${pkgver}" -type f -name "*.py" -exec sed -i "s#from dicomweb_client.api import load_json_dataset#import pydicom\nload_json_dataset = pydicom.dataset.Dataset.from_json#" {} \;
}

build() {
  cd "${_pkgname}-${pkgver}"
  BUILD_OHIF=OFF \
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  BUILD_OHIF=OFF \
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  rm -rfv "${pkgdir}/usr/logconfig"
  rm -vf "${pkgdir}/usr/bin/monailabel.bat"
  install -dm755 "${pkgdir}/usr/share/docs"
  mv "${pkgdir}/usr/${pkgname}" "${pkgdir}/usr/share/docs"
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
