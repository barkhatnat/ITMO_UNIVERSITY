@echo off
chcp 65001
setlocal ENABLEDELAYEDEXPANSION
echo Выберите один из способов настройки сетевого интерфейса:
echo 1. Через DHCP
echo 2. Вручную
set /p choice="Введите номер выбранного способа: "
if %choice%==1 (
netsh interface ip set address "Беспроводная сеть" dhcp
netsh interface ip set dns "Беспроводная сеть" dhcp
echo Настройки сетевого интерфейса успешно получены через DHCP.
) else if %choice%==2 (
set /p ip="Введите IP-адрес: "
set /p mask="Введите маску подсети: "
set /p gateway="Введите шлюз: "
set /p dns="Введите адрес DNS-сервера: "
netsh interface ip set address "Беспроводная сеть" static !ip! !mask! !gateway!
netsh interface ipv4 add dnsservers "Беспроводная сеть" address=!dns! index=1
echo Статические настройки успешно применены.
) else (
echo Выбор некорректен. Выберите 1 или 2 вариант
)
netsh interface ip show addresses "Беспроводная сеть"
netsh interface ip show dnsservers "Беспроводная сеть"
pause