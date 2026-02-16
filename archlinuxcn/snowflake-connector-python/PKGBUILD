# Maintainer: Hasan Çatalgöl <hasancatalgol@gmail.com>

pkgname=snowflake-connector-python
pkgver=3.17.1
pkgrel=1
pkgdesc="Snowflake Connector for Python (DB-API 2.0)"
arch=('any')
url="https://github.com/snowflakedb/snowflake-connector-python"
license=('Apache')
# Keep hard deps lean; most cloud/dataframe bits are optional.
depends=(
  'python'
  'python-requests'
  'python-urllib3'
  'python-cryptography'
  'python-pyopenssl'
  'python-cffi'
  'python-certifi'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-wheel'
  'python-setuptools'
  'cython'               # needed to build from sdist
)
optdepends=(
  'python-pyarrow: Arrow fast paths (to_pandas, write_pandas)'
  'python-pandas: DataFrame helpers (write_pandas)'
  'python-keyring: secure local token storage'
  'python-boto3: S3 external stage transfers'
  'python-azure-storage-blob: Azure external stage transfers'
  'python-google-cloud-storage: GCS external stage transfers'
)

# PyPI sdist (filename uses underscores)
source=("https://files.pythonhosted.org/packages/source/s/snowflake-connector-python/snowflake_connector_python-${pkgver}.tar.gz")
sha256sums=('1881025adea6dd732fe02065df8693a45b446a8db8e0e0ed7d728a7f09734076')

build() {
  cd "snowflake_connector_python-${pkgver}"
  python -m build --wheel --no-isolation
}

# Upstream tests need creds/extras; skip here.
# check() { :; }

package() {
  cd "snowflake_connector_python-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl

  # License files (varies between LICENSE / LICENSE.txt)
  install -Dm644 LICENSE* "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  [[ -f NOTICE ]] && install -Dm644 NOTICE "$pkgdir/usr/share/licenses/$pkgname/NOTICE"
}
