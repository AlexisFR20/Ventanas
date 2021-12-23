Write-Host "INSTALACION LMS 12.2"
Write-Host "Antes de continuar verifica que:"
Write-Host "1. El usuario este definido como administrador"
Write-Host "2. User Account Control: Run all administrators in Admin Approval Mode: Disable"
Write-Host " "
Write-Host "IMPORTANTE: Si no cumple esos dos requisitos cierra el script y procede a realizarlos"
Write-Host "Presiona enter para continuar, si es que cumple con los requisitos"
$x = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
Write-Host " "
Write-Host "INSTALACION INICIALIZADA"
Write-Host '[1] Modificando archivo host'
 
Write-Host '[2] Obtencion de archivos a utilizar'
$DIRE = "C:\temp"
if ( Test-Path $DIRE ) {
    echo "Directory Exists"
} else {
    md C:\temp
}
$DIRE = "C:\Apps"
if ( Test-Path $DIRE ) {
    echo "Directory Exists"
} else {
    md C:\Apps
}
Write-Host 'Creando cliente'
Start-Sleep -s 2
$client = new-object System.Net.WebClient
Write-Host 'Cliente creado'
Start-Sleep -s 2
Write-Host 'Descargando archivo gunzip'
$client.DownloadFile("http://172.16.11.8/lms/gunzip.exe", "C:\temp\gunzip.exe")

Write-Host 'Descargando archivo web client 32'
$client.DownloadFile("http://172.16.11.8/lms/WebClient32.zip", "C:\Apps\WebClient32.zip")
Write-Host 'Descomprimiendo archivo WebClient32.zip'
Expand-Archive -Path C:\Apps\WebClient32.zip -DestinationPath C:\Apps\WebClient32
Write-Host 'Eliminando carpeta zip restante'
Remove-Item C:\Apps\WebClient32.zip

Write-Host 'Descargando archivo LMS 12.2.prowcapc'
$client.DownloadFile("http://172.16.11.8/lms/versiones/12.2.022/LMS%2012.2.prowcapc", "C:\Apps\LMS 12.2.prowcapc")

Write-Host '[3] Verificando WordPad'
& 'C:\Program Files\Windows NT\Accessories\wordpad.exe'
taskkill /IM wordpad.exe /F
Set-ItemProperty -Path HKCU:\Software\Microsoft\Windows\CurrentVersion\Applets\Wordpad\Options -Name Wrap -Value 0

Write-Host '[4] Verificando formato de fecha y numeracion'
Write-Host 'Definiendo el lenguaje: English-US'
Set-Culture en-US

Write-Host 'Ajustando formato de fecha month/day/year'
Set-ItemProperty -Path "HKCU:\Control Panel\International" -Name sLongDate -Value "dddd, MMMM d, yyyy"
Write-Host 'Ajustando formato de numeracion'
Set-ItemProperty -Path "HKCU:\Control Panel\International" -Name sMonThousandSep -Value ","
Set-ItemProperty -Path "HKCU:\Control Panel\International" -Name sMonDecimalSep -Value "."

Write-Host '[5] Ejecutando archivo setup.exe de WebClient32'
& 'C:\Apps\WebClient32\WebClient32\setup.exe' | Out-Null

Write-Host '[6] Se abrira Software Center, para instalar WinSCP'
Write-Host 'Al finalizar, cierra Software Center para continuar'
Start-Sleep -s 5
&"C:\WINDOWS\CCM\ClientUX\SCClient.exe" softwarecenter:SoftwareID=ScopeId_C37154BF-A1F4-4B62-B5FF-0CC6F41A762B/Application_a7748e45-eae3-42ae-bc24-999e58c00df7 | Out-Null
Start-Sleep -s 2
Write-Host 'Agregando variable del sistema'
$pathElements = @([Environment]::GetEnvironmentVariable("Path", "User") -split ";")
$pathElements += "C:\Program Files (x86)\WinSCP"
$newPath = $pathElements -join ";"
[Environment]::SetEnvironmentVariable("Path", $newPath, "User")
Start-Sleep -s 2
Write-Host '[7] Ejecutando archivo LMS 12.2.prowcapc'
Write-Host 'Una vez que termine la configuracion en la ventana'
Write-Host 'La instalacion habra concluido'
Start-Sleep -s 4
& 'C:\Apps\LMS 12.2.prowcapc'