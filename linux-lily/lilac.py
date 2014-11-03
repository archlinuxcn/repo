#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

build_prefix = 'makepkg'

config_version = '3.17.2'
cjktty_version = '3.17'
aufs_version = '3.17'
bfq_version = '3.17.0-v7r6'
bfq_patches = [
  '0001-block-cgroups-kconfig-build-bits-for-BFQ-v7r6-3.17.patch',
  '0002-block-introduce-the-BFQ-v7r6-I-O-sched-for-3.17.patch',
  '0003-block-bfq-add-Early-Queue-Merge-EQM-to-BFQ-v7r6-for-3.17.0.patch',
]

bfq_baseurl = 'http://algo.ing.unimo.it/people/paolo/disk_sched/patches/'

def prepare_source(version):
  config = os.path.join(os.getcwd(), 'config.x86_64')
  mypatch = os.path.join(os.getcwd(), 'config.diff.' + config_version)

  with at_dir(os.path.expanduser('~/linux-git')):
    git_reset_hard()
    run_cmd(["git", "fetch", "--all"])
    run_cmd(["git", "checkout", "-b", 'v%s-lily' % version, "v" + version])
    run_cmd(["git", "merge", "--no-edit", 'cjktty/%s-utf8' % cjktty_version])
    run_cmd(["git", "merge", "--no-edit", 'aufs/aufs%s' % aufs_version])

    run_cmd(["sh", "-c", 'patch -p1 < ~/uksm-0.1.2.3-for-v3.17.patch'])
    run_cmd(["git", "add", "."])
    run_cmd(["git", "commit", "-m", 'apply uksm patch'])

    cmd = ['curl'] + [bfq_baseurl + bfq_version + '/' + x
                      for x in bfq_patches]
    curl = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    gitam = subprocess.Popen(['git', 'am'], stdin=curl.stdout)
    curl.wait()
    gitam.wait()

    run_cmd(["cp", config, ".config"])
    run_cmd(["patch", ".config", mypatch])
    run_cmd(["make", "silentoldconfig"])

def pre_build():
  g.files = download_official_pkgbuild('linux')
  prepare_source(_G.newver)

  source_count = 0
  ignoring = False
  for line in edit_file('PKGBUILD'):
    if source_count:
      if ')' in line:
        source_count = 0
      elif source_count == 1:
        source_count += 1
        # remove second source url or sum
        continue
    elif line.startswith('pkgbase='):
      line = line.replace('linux', 'linux-lily')
    elif line.startswith('pkgver='):
      line = 'pkgver=' + _G.newver
    elif line.startswith('makedepends='):
      line = "makedepends=('kmod' 'inetutils' 'bc' 'parallel')"
    elif line.startswith('options='):
      line = "options=('strip' 'debug')\nSTRIP_BINARIES=-S"
    elif line.startswith('source='):
      # remove second source url
      line = 'source=('
      source_count = 1
    elif line.startswith('sha256sums='):
      # remove second source sum
      line = 'sha256sums=('
      source_count = 1
    elif line.lstrip() == 'cd "${srcdir}/${_srcname}"':
      line = '  cd ~/linux-git'
    elif 'patch-${pkgver}' in line:
      line = line.replace('patch ', '#patch ')
    elif line.strip() == 'if [ "${CARCH}" = "x86_64" ]; then':
      ignoring = True
    elif ignoring and line.strip() == 'fi':
      ignoring = False
      continue
    elif 'pkgdesc="The' in line:
      line = '  pkgdesc="The ${pkgbase/linux/Linux} kernel and modules, with x32, aufs3, latencytop, kgdb, cjktty, uksm and bfq support"'
    elif line.strip() == 'provides=("kernel26${_kernelname}=${pkgver}")':
      line = '  provides=("kernel26${_kernelname}=${pkgver}" "linux=${pkgver}")'
    elif line.strip() == 'provides=("kernel26${_kernelname}-headers=${pkgver}")':
      line = '  provides=("kernel26${_kernelname}-headers=${pkgver}" "linux-headers=${pkgver}")'
    elif line.strip() == 'provides=("kernel26${_kernelname}-docs=${pkgver}")':
      line = '  provides=("kernel26${_kernelname}-docs=${pkgver}" "linux-docs=${pkgver}")'
    elif '# gzip -9 all modules' in line:
      line = '''\
  export dbgdir="$pkgdir-debug/usr/lib/debug"
  mkdir -p "$dbgdir"
  pushd "$pkgdir"
  find . -name '*.ko' -print0 | parallel -j20 -0 kostrip
  popd\n''' + line
    elif 'gzip -9 {}' in line:
      line = '''  find "${pkgdir}" -name '*.ko' -print0 | parallel -j8 -0 gzip -9'''
    elif '-m644 vmlinux' in line:
      line += '''
  # for systemtap
  install -D -m644 System.map "${pkgdir}/boot/System.map-${_kernver}"'''
    elif line.strip() == 'install -dm755 "${pkgdir}/usr/lib/modules/${_kernver}"':
      line = '''\
  KARCH=x86

  cd ~/linux-git
  # get kernel version
  _kernver="$(make LOCALVERSION= kernelrelease)"
  _basekernel=${_kernver%%-*}
  _basekernel=${_basekernel%.*}\n''' + line
    elif line.startswith('pkgname='):
      line = 'pkgname=("${pkgbase}" "${pkgbase}-headers") # "${pkgbase}-docs")'

    if not ignoring:
      print(line)

def post_build():
  removing = [x for x in g.files if x != 'PKGBUILD']
  run_cmd(["rm", "--"] + removing)
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  _G = SimpleNamespace(newver = FILL_THIS)
  single_main()
