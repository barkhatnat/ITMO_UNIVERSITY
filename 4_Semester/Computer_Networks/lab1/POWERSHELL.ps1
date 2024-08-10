param (
	[string]$Name,
	[IPAddress]$IP = "192.168.1.109",
    	[string]$CIDR = 24,
	[string]$Gateway = "192.168.1.1",
	[string]$Dns = "1.1.1.1",
	[string]$IPType = "IPv4",
    	[string]$Type = "DHCP",
	[switch]$ShowNetDevices,
	[switch]$IsPhysicalConnection,
	[switch]$AdapterInfo
)
chcp 65001
$adapter = Get-NetAdapter -Name $Name
if ($Type -eq "Static") {
    if (($adapter | Get-NetIPConfiguration).IPv4Address.IPAddress) {
        Write-Host "Removing current IP"
        $adapter | Remove-NetIPAddress -AddressFamily $IPType -Confirm:$false
    }

    if (($adapter | Get-NetIPConfiguration).Ipv4DefaultGateway) {
        Write-Host "Removing current gateway"
        $adapter | Remove-NetRoute -AddressFamily $IPType -Confirm:$false
    }

    Write-Host "Configuring new intefrace settings"
    $adapter | New-NetIPAddress -AddressFamily $IPType -IPAddress $IP -PrefixLength $CIDR -DefaultGateway $Gateway -Confirm:$false
    $adapter | Set-DnsClientServerAddress -ServerAddresses $DNS
}
else {
    $interface = $adapter | Get-NetIPInterface -AddressFamily $IPType

    if ($interface.Dhcp -eq "Disabled") {
        Write-Host "Removing current gateway"
        If (($interface | Get-NetIPConfiguration).Ipv4DefaultGateway) {
            $interface | Remove-NetRoute -Confirm:$false
        }
        Write-Host "Enabling DHCP on interface"
        $interface | Set-NetIPInterface -DHCP Enabled
        Write-Host "Enabling automatic DNS"
        $interface | Set-DnsClientServerAddress -ResetServerAddresses
    }
	Get-NetIPConfiguration -InterfaceAlias $Name
}
if ($ShowNetDevices){
	Write-Host "Network description:"
	Get-NetAdapter -Physical | SELECT InterfaceDescription
}
if ($IsPhysicalConnection){
if ((Get-NetAdapter -Physical | SELECT * | WHERE status -eq 'Up' | WHERE name -eq 'Ethernet').Count > 0){
	Write-Host "There is physical connection"
}
else {
	Write-Host "There is no physical connection"
}
}

if ($AdapterInfo){
	Get-NetAdapter -Physical -InterfaceAlias $Name | SELECT speed
	Get-NetAdapter -Physical -InterfaceAlias $Name | SELECT FullDuplex
}
