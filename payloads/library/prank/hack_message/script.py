import time
import sys
import subprocess

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)  # Adjust the sleep time to control the typing speed
    sys.stdout.write('\n')

def fake_hacking():
    print_slow("Initiating hack...")
    loading_bar(0.005)
    print_slow("Accessing mainframe...")
    loading_bar(0.01)
    print_slow("Extracting passwords...")
    loading_bar(0.0001)
    print_slow("Extracting files...")
    loading_bar(0.01)
    print_slow("Encrypting passwords and files ...")
    loading_bar(0.005)
    print_slow("Uploading encrypted passwords and files... ")
    loading_bar(0.007)
    print_slow("Hacking complete. Your computer has been compromised.\n\n")
    red_start = "\033[1;91m"
    color_end = "\033[0m"
    print_slow("Retrive your files and passwords by buying the 5$ decrypting key at " f"{red_start}https://tinyurl.com/hack-ransom-portal{color_end}.\n\n\n\n")
    print("PS C:\\Users\\cryptd\\tegwna\\axfgbw\\phef_we>")


def loading_bar(sleep_time):
    for i in range(51):
        sys.stdout.write('\r')
        sys.stdout.write("[%-50s] %d%%" % ('=' * i, i*2))
        sys.stdout.flush()
        time.sleep(sleep_time)  # Adjust the sleep time to control the speed of the loading bar
    print("\n")

if __name__ == "__main__":
    subprocess.run(["powershell", "Clear-Host"])
    fake_hacking()
    while True : 
        time.sleep(1)
