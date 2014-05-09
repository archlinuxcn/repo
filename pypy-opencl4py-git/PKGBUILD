pkgbase=pypy-opencl4py-git
pkgname=pypy-opencl4py-git
pkgname=(pypy3-opencl4py-git pypy-opencl4py-git)
pkgver=1.0.2.0.33.g92d79ce
pkgrel=1
epoch=1
pkgdesc="Python cffi OpenCL bindings and helper classes. pypy version"
url="https://github.com/ajkxyz/opencl4py"
arch=('i686' 'x86_64')
license=('BSD')
makedepends=('git' 'pypy' 'pypy3')
depends=('pypy')
provides=('pypy-opencl4py')
options=('debug' 'strip')

_gitname=opencl4py

_gitroot=https://github.com/ajkxyz/opencl4py
_gitref=master
exec 5>&1

_fetch_git() {
  cd "$srcdir"

  if [ -d "$srcdir/$_gitname/.git" ]; then
    cd "$_gitname"
    msg "Reset current branch"
    git reset --hard HEAD
    git clean -fdx
    msg "Fetching branch $_gitref from $_gitroot..."
    git fetch --force --update-head-ok \
      "$_gitroot" "$_gitref:$_gitref" --
    msg "Checking out branch $_gitref..."
    git checkout "$_gitref" --
    git reset --hard "$_gitref"
    git clean -fdx
    msg "The local files are updated."
  else
    msg "Cloning branch $_gitref from $_gitroot to $_gitname..."
    git clone --single-branch --branch "$_gitref" \
      "$_gitroot" "$_gitname"
    cd "$_gitname"
  fi
  msg "GIT checkout done or server timeout"
}

pkgver() {
  (_fetch_git >&5 2>&1)
  cd "$srcdir/$_gitname"

  git describe --tags | sed -e 's/^[^0-9]*//' -e 's/-/.0./' -e 's/-/./g'
}

build() {
  (_fetch_git)

  rm -rf "${srcdir}/$_gitname-python2"
  cp -a "${srcdir}/$_gitname" "${srcdir}/$_gitname-python2"
}

_fix_py2_cffi() {
  cd "${srcdir}"
  PYTHONPATH="${pkgdir}/opt/pypy/site-packages" \
    pypy -c "import opencl4py; opencl4py.initialize()"
  find "$pkgdir/" -name '*.o' -delete
  find "$pkgdir/" -type d -empty -delete
}

_fix_py3_cffi() {
  cd "${srcdir}"
  PYTHONPATH="${pkgdir}/opt/pypy3/lib/python3.2/site-packages" \
    pypy3 -c "import opencl4py; opencl4py.initialize()"
  find "$pkgdir/" -name '*.o' -delete
  find "$pkgdir/" -type d -empty -delete
}

package_pypy3-opencl4py-git() {
  depends=('pypy3')
  provides=('pypy3-opencl4py')
  cd "$srcdir/$_gitname"

  pypy3 setup.py install --root="$pkgdir" --optimize=1 \
    --install-lib=/opt/pypy3/lib/python3.2/site-packages
  # _fix_py3_cffi opencl4py
}

package_pypy-opencl4py-git() {
  cd "$srcdir/$_gitname"

  pypy setup.py install --root="$pkgdir" --optimize=1
  # _fix_py2_cffi opencl4py
}
