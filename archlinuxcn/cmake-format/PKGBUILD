# Maintainer: Martchus <martchus@gmx.net>

# All my PKGBUILDs are managed at https://github.com/Martchus/PKGBUILDs where
# you also find the URL of a binary repository.

pkgname=cmake-format
pkgver=0.6.13
pkgrel=3
pkgdesc='Source code formatter for CMake listfiles'
arch=('any')
url='https://github.com/cheshirekow/cmake_format'
license=('GPL3')
depends=('python-six>=1.13.0')
makedepends=('python-setuptools')
optdepends=('python-yaml>=5.3: YAML config files' 'python-jinja>=2.10.3: complete HTML annotation' 'python-argcomplete: automatic shell completion')
checkdepends=('cmake')
provides=('python-cmakelang')
conflicts=('python-cmakelang')
source=("$pkgname-$pkgver.tar.gz::https://github.com/cheshirekow/cmake_format/archive/v${pkgver}.tar.gz")
sha512sums=('eb7fde540860b6119d0bb528f22592fb4b507f9319aeda0999da10bcc89ee1348fd7d701fc49aa5dac7616e1577e436cbd73de94dbbab0cafdf28e1812612342')

check() {
  mkdir "$srcdir/check"
  cd "$srcdir/check"
  export CTEST_OUTPUT_ON_FAILURE=1
  cmake "$srcdir/cmake_format-$pkgver"
  ctest --exclude-regex 'verify-export|cmakelang-command-db-test|cmakelang-validate-database|cmakelang-doc-verify-README\.rst'

  # note: Excluding the tests cmakelang-validate-database (would require gpg2 and
  # python-pgpy and currently fails because an internet connection is required) and
  # cmakelang-command-db-test (fails if CMake version doesn't match the version
  # in upstream's CI). Also exluding verify-export and cmakelang-doc-verify-README.rst
  # which seem specific to how upstream manages their Git repo.
}

package() {
  cd "$srcdir/cmake_format-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1
}
