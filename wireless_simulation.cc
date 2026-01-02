#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/wifi-module.h"
using namespace ns3;
int main() {
 NodeContainer nodes; nodes.Create(2);
 WifiHelper wifi; wifi.SetStandard(WIFI_STANDARD_80211n);
 WifiMacHelper mac; mac.SetType("ns3::AdhocWifiMac");
 YansWifiPhyHelper phy;
 YansWifiChannelHelper ch = YansWifiChannelHelper::Default();
 phy.SetChannel(ch.Create());
 wifi.Install(phy, mac, nodes);
 Simulator::Run(); Simulator::Destroy(); return 0;
}
