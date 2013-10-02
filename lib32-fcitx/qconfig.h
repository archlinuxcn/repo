#ifdef QT_BUILD_KEY
#undef QT_BUILD_KEY
#endif

#ifdef QT_BUILD_KEY_COMPAT
#undef QT_BUILD_KEY_COMPAT
#endif

#ifdef QT_ARCH_X86_64
#undef QT_ARCH_X86_64
#endif

#include "/usr/include/qt4/QtCore/qconfig.h"

#ifdef QT_BUILD_KEY
#undef QT_BUILD_KEY
#endif
#define QT_BUILD_KEY "i386 linux g++-4 full-config"

#ifdef QT_BUILD_KEY_COMPAT
#undef QT_BUILD_KEY_COMPAT
#endif
#define QT_BUILD_KEY_COMPAT "i386 Linux g++-4 full-config"

#ifdef QT_ARCH_X86_64
#undef QT_ARCH_X86_64
#endif

#ifndef QT_ARCH_I386
#define QT_ARCH_I386
#endif
