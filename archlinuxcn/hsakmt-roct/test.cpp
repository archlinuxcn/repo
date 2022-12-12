#include <hsakmt/hsakmt.h>
#include <iostream>

int main()
{
    HsaVersionInfo info;
    HsaSystemProperties prop;

    hsaKmtOpenKFD();

    hsaKmtGetVersion(&info);

    std::cout << "HSA version " << info.KernelInterfaceMajorVersion
        << "." << info.KernelInterfaceMinorVersion << "\n";

    hsaKmtAcquireSystemProperties(&prop);

    std::cout << "Topology information:\n"
        << "Number of memory nodes: " << prop.NumNodes << "\n"
        << "Platform OEM: " << prop.PlatformOem << "\n"
        << "Platform ID: " << prop.PlatformId << "\n"
        << "Platform Revision: " << prop.PlatformRev << "\n";

    hsaKmtReleaseSystemProperties();

    hsaKmtCloseKFD();
}
