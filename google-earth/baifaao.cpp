/* amirpli 2013/11/28 */
#include <QtCore/QAtomicInt>
extern "C" {
        int _Z34QBasicAtomicInt_fetchAndAddOrderedPVii(QAtomicInt* a, int b) {
                return a->fetchAndAddOrdered(b);
        }
}