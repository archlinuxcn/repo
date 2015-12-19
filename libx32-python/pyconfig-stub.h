// This is replaced by libx32-python.
// Old file is renamed to pyconfig-64.h.

#if !defined __x86_64__
# include "pyconfig-64.h" // no lib32-python yet
#endif
#if defined __x86_64__ && defined __LP64__
# include "pyconfig-64.h"
#endif
#if defined __x86_64__ && defined __ILP32__
# include "pyconfig-x32.h"
#endif

