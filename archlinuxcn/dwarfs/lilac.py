#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['KokaKiwi'])
    pkgver, _ = get_pkgver_and_pkgrel()
    pkgver: str
    need_patch = pkgver == '0.15.8'
    for line in edit_file('PKGBUILD'):
        line: str
        if '--exclude-regex' in line and line.endswith("'"):
            print(line[:-1] + "|mkdwarfs_log_mem_usage_test\\.log_memory_usage'")
        elif need_patch:
            if line.startswith('source'):
                print(line[:-1] + ' 0001-fix-filesystem_extractor.patch)')
            elif line.startswith('sha256sum'):
                print(line[:-1] + " 'da8fd28f3ddc853b4ddfe0ecb1b121856318b7458c61c5a985dba7e94e2f498c')")
            elif line.startswith('b2sum'):
                print(line[:-1] + " '253c98d982d48034c3ba547c32c1327b83461ad9999be2a0815a87751af50e36dd37def4606750b88461efca45f49f3b6ec6f54232e3a977acd218ec34334b01')")
            elif line.startswith('build()'):
                print("""
    prepare() {
      cd "$pkgname-$pkgver"
      # Upstream fix for incompatibility with latest libarchive
      patch -p1 -l -F3 < ../0001-fix-filesystem_extractor.patch
    }""")
                print(line)
            else:
                print(line)
        else:
            print(line)
