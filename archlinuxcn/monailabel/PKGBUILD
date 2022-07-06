# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=MONAILabel
pkgname=monailabel
pkgver=0.4.1
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
install="${pkgname}.install"
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Project-MONAI/MONAILabel/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('95e985ae19f3bced0144ce3bee8afcfab8f59f196dbb59216a8d6b9306d309139a0f3aa41073d7e1ff64f5cc1e26caf3b3dad6890360fcb1fd3dd2cd1db1ba51')

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
