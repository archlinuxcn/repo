_name=iredis
pkgname=iredis
pkgver=1.14.0
pkgrel=4
pkgdesc="Terminal client for Redis with auto-completion and syntax highlighting."
arch=(any)
url="https://github.com/laixintao/iredis"
license=('BSD-3-Clause')
depends=('python' 'python-redis' 'python-packaging' 'python-prompt_toolkit' 'python-pygments' 'python-mistune' 'python-configobj' 'python-click' 'python-pendulum')
makedepends=('python-setuptools' 'python-build' 'python-installer' 'python-wheel' 'python-poetry' 'python-build' 'python-installer' 'python-wheel')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/iredis-1.14.0.tar.gz")
sha256sums=('821336ab54e4cea7169ac51bd94f3daa45a3b9843b1adee1bf2ea3dd3230f184')

build() {
  cd "$srcdir/iredis-1.14.0"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/iredis-1.14.0"
  python -m installer --destdir="$pkgdir" dist/*.whl

  # make sure we don't install any world-writable or root-readable-only files
  # we shouldn't need to fix ownership as we extract tarballs as a non-root user
  # https://github.com/pypa/setuptools/issues/1328
  # https://github.com/LonamiWebs/Telethon/issues/1605
  chmod u=rwX,go=rX -R "$pkgdir"
  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

