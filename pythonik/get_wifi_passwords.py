import subprocess
import re  # regular expressions


command_output = subprocess.run(
    ['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout.decode()  # capture_output=true to przechwytujemy stdout i stdin

profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
# print(profile_names)


# lista na obiekty,np. {'ssid': 'nazwa_sieci', 'password': 'hasło'}
wifi_list = list()

if len(profile_names) != 0:
    for name in profile_names:
        # słownik na np. {'ssid': 'nazwa_sieci', 'password': 'hasło'}
        wifi_profile = dict()

        profile_info = subprocess.run(
            ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode("latin1")  # tu musi być latin1 bo mam polskie znaki, bez tego nie pójdzie

        # profile_info = subprocess.check_output(
        #     ["netsh", "wlan", "show", "profile", name]).decode('latin1')
        # print(profile_info)

        if(re.search("Security key           : Absent", profile_info)):  # to znaczy że sieć nie posiada hasła
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(
                ['netsh', 'wlan', 'show', 'profile', name, "key=clear"], capture_output=True).stdout.decode()  # szukam haseł

            password = re.search(
                "Key Content            : (.*)\r", profile_info_pass)  # tu mam hasła
            # password[0]= np Key Content            : 77132307, password[1]=77132307

            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)

for x in range(len(wifi_list)):
    print(wifi_list[x])
