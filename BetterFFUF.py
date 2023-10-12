import os
import time
import keyboard
import platform


# Basic FFUF Scan Function
def basic_fuzz():
    Usr_Url = input("URL you are attacking (Ex. https://google.com/FUZZ): ")
    Usr_Wrd = input("Path to wordlist: ")
    Usr_Rate = input("Rate in seconds specify 1-10: ")
    # Command
    os.system(f"ffuf -u {Usr_Url} -w {Usr_Wrd} -p {Usr_Rate}")
    print("Fuzz complete returning to main menu please wait 2 seconds.")
    time.sleep(2)
    main_func()


# Filtered Scan
def filter_fuzz():
    Usr_Url = input("URL you are attacking (Ex. https://google.com/FUZZ): ")
    Usr_Wrd = input("Path to wordlist: ")
    Usr_Rate = input("Rate in seconds specify 1-10: ")
    Status_Code = input("Filter by status code (Format: 200,301,Etc.): ")
    # Command
    os.system(f"ffuf -u {Usr_Url} -w {Usr_Wrd} -p {Usr_Rate} -fc {Status_Code}")
    print("Fuzz complete returning to main menu please wait 2 seconds.")
    time.sleep(2)
    main_func()

# Main Function Block
def main_func():
    print(
        "This is a basic fuzzer that uses ffuf but mitigates the amount of input you need in order to fuzz a web "
        "application or api.\nInclude FUZZ wherever necessary when prompted to specify the URL you are attacking.\n("
        "EX: https://FUZZ.google.com/)")
    print(f"What would you like to do?\n[1] Run a basic FUZZ scan.\n[2] Run a filtered scan.")
    # Choices
    Scan_Q = input('')

    # Function Index
    if Scan_Q == '1':
        basic_fuzz()
    elif Scan_Q == '2':
        filter_fuzz()
    else:
        time.sleep(2)
        main_func()

# Compiles and calls the program
main_func()
