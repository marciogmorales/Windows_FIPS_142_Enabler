import winreg as wrg

location = wrg.HKEY_LOCAL_MACHINE
reg_path = wrg.OpenKeyEx(location, r"SYSTEM\CurrentControlSet\Control\Lsa\\")

input("Do you want to enable FIPS mode? Press (y/n): ")
if input == "y":
    print("Checking if FIPS more is already enabled")
    wrg.QueryValueEx(reg_path, "FipsAlgorithmPolicy")[0] == True
    print("FIPS mode is already enabled")
else:
    print("Enabling FIPS mode")
    key_1 = wrg.CreateKey(reg_path, "FipsAlgorithmPolicy")
    wrg.SetValueEx(key_1, "FipsAlgorithmPolicy", 0, wrg.REG_DWORD, 0x00000001)
    print("FIPS mode enabled")
    (wrg.CloseKey(key_1))