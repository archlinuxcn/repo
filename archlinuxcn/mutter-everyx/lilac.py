from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

# MR 5122: wayland/text-input: Fix cursor location update for v1 clients
# b2sum 用 SKIP: MR 会持续更新(由 everyx 维护), 不固定校验
_MR5122 = 'https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/5122.patch'

def pre_build():
    g.files = download_official_pkgbuild('mutter')

    state = None
    for line in edit_file('PKGBUILD'):
        s = line.strip()

        if state == 'pkgname':              # 折叠官方 split pkgname 为单包
            if s == ')':
                state = None
            continue
        if state == 'source':               # source 末尾追加 5122.patch
            if s == ')':
                state = None
                print('  "5122.patch::%s"' % _MR5122)
                print(line)
                continue
            print(line)
            continue
        if state == 'b2sums':               # b2sums 末尾追加(与 source 顺序对齐)
            if line.rstrip().endswith(')'):
                state = None
                print(line[:-1])
                print('        SKIP')
                print(')')
                continue
            print(line)
            continue
        if state == 'skip':                 # 丢弃 mutter-devkit / mutter-docs 子包函数
            if line == '}':
                state = None
            continue
        if state == 'pm':                   # 主包函数: 改名, 删 _pick 行与 devkit optdepends
            if line == '}':
                state = None
                print(line)
                continue
            if s.startswith('_pick '):
                continue
            if "'mutter-devkit:" in line:
                continue
            if s.startswith('provides=(') and not s.startswith('provides+=('):
                # 官方用 = 赋值会覆盖顶层 provides+=(mutter), 改为叠加
                print(line.replace('provides=(', 'provides+=(', 1))
                continue
            print(line)
            continue

        # ---- 普通行 anchor ----
        if line.startswith('pkgbase='):
            # 非 split 包: 删除 pkgbase 行
            continue
        if line.startswith('pkgname=('):
            print('pkgname=mutter-everyx')
            state = 'pkgname'
            continue
        if line.startswith('pkgdesc='):
            line = line[:-1] + ' (with patches picked from everyx)"'
            print(line)
            continue
        if line == 'arch=(x86_64)':         # 顶替官方 mutter: 提供/冲突
            print(line)
            print('provides+=(mutter)')
            print('conflicts+=(mutter)')
            continue
        if line.startswith('source=('):
            state = 'source'
            print(line)
            continue
        if line.startswith('b2sums=('):
            state = 'b2sums'
            print(line)
            continue
        if s == 'cd mutter':                # prepare() 内应用 patch
            print(line)
            print('  git apply -3 ../5122.patch')
            continue
        if '-D docs=true' in line:          # 只留主体, 关闭 docs 与 devkit(MDK) 构建
            print(line.replace('docs=true', 'docs=false'))
            print('    -D devkit=disabled')
            continue
        if line.startswith('_pick() {'):
            state = 'skip'   # 死代码: 单包不再拆子包, 丢弃 _pick helper
            continue
        if line.startswith('package_mutter-devkit()') or line.startswith('package_mutter-docs()'):
            state = 'skip'
            continue
        if line.startswith('package_mutter()'):
            print('package() {')
            state = 'pm'
            continue
        print(line)

def post_build():
    git_add_files(g.files)
    git_commit()
