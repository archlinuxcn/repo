# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tensorflow-datasets
pkgver=4.7.0
pkgrel=1
pkgdesc='A collection of datasets ready to use with TensorFlow, Jax, ...'
arch=(any)
url='https://github.com/tensorflow/datasets'
license=(Apache)
depends=(python absl-py python-{dill,etils,numpy,promise,protobuf,requests,six,tensorflow,tensorflow-metadata,termcolor,toml,tqdm})
makedepends=(python-setuptools)
checkdepends=(python-pytest python-dm-tree python-pydub)
optdepends=(
  'python-scipy: for aflw2k3d, duke_ultrasound, imagenet2012_corrupted, svhn, the300w_lp'
  # 'python-apache-beam: for beir, c4, wiki_dialog, wikipedia'
  'python-gcsfs: for ble_wind_field'
  'python-zarr: for ble_wind_field'
  'python-gcld3: for c4'
  'python-langdetect: for c4'
  'python-nltk: for c4'
  'python-tldextract: for c4'
  'python-matplotlib: for cats_vs_dogs'
  'python-pillow: for colorectal_histology, wider_face'
  'python-pydub: for common_voice, groove, gtzan, librispeech'
  'python-scikit-image: for eurosat, imagenet2012_corrupted'
  'python-tifffile: for eurosat'
  'python-imagecodecs: for eurosat'
  # 'python-pretty-midi: for groove'
  'python-opencv: for imagenet2012_corrupted'
  # 'python-tensorflow-io: for lsun'
  # 'python-crepe: for nsynth'
  'python-librosa: for nsynth'
  'python-scikit-learn: for nsynth'
  'python-pandas: for ogbg_molpcba, pet_finder, smartwatch_gestures'
  'python-networkx: for ogbg_molpcba'
  'python-h5py: for robonet'
  # 'python-envlogger: for robosuite_panda_pick_place_can'
  'python-mwparserfromhell: for wikipedia'
  'python-beautifulsoup4: for wsc273'
  'python-lxml: for wsc273'
  'python-pycocotools: for youtube_vis'
)
source=(https://github.com/tensorflow/datasets/archive/v$pkgver/$pkgname-$pkgver.tar.gz
        get_optdepends.py)
sha256sums=('ed7c3b959d10ba762137e18b93631ab42f4ed0915bc3d9ce98ee66eef9c61418'
            '91f3819b43c38faa17120ea6bc36e0733470acc9e8f91cf614954416b4904d9a')

prepare() {
  cd datasets-$pkgver
  mv -vf tensorflow_datasets/{version_stable,version}.py
  # PYTHONPATH="$PWD" python ../get_optdepends.py
}

build() {
  cd datasets-$pkgver
  python setup.py build
}

check() {
  cd datasets-$pkgver
  # Collect tests to check for missing dependencies. Actually running tests takes too much time.
  # Skipped tests: https://github.com/tensorflow/datasets/blob/v4.6.0/.github/workflows/pytest.yml#L71-L77
  # Two other skipped tests: needs apache_beam
  pytest --collect-only \
    --ignore="tensorflow_datasets/audio/nsynth_test.py" \
    --ignore="tensorflow_datasets/core/features/features_test.py" \
    --ignore="tensorflow_datasets/testing/test_utils.py" \
    --ignore="tensorflow_datasets/image/lsun_test.py" \
    --ignore="tensorflow_datasets/image_classification/imagenet2012_corrupted_test.py" \
    --ignore="tensorflow_datasets/scripts/documentation/build_api_docs_test.py" \
    --ignore="tensorflow_datasets/core/dataset_builder_beam_test.py" \
    --ignore="tensorflow_datasets/core/split_builder_test.py"
}

package() {
  cd datasets-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
