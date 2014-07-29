// This is replaced by binx32-python2.
// Old file is renamed to pyconfig-64.h.

#if !defined __x86_64__
# include <pyconfig-64.h> // bin32-python2 does not exist yet
#endif
#if defined __x86_64__ && defined __LP64__
# include <pyconfig-64.h>
#endif
#if defined __x86_64__ && defined __ILP32__
# include <pyconfig-x32.h>
#endif

