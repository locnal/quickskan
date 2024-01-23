
import subprocess
def port_scan():

    site = input("enter ipv4 addr: ")
    try:
        result = subprocess.run(['nmap', '-p-', site], capture_output=True, text=True)
        
        return result.stdout
    except Exception as e:
        print(f"Error: {e}")

def dnslookup():
    site = input("enter site: ")
    try:
        result = subprocess.run(['nslookup', '-type=ns', site], capture_output=True, text=True )
        return result.stdout
    except Exception as e:
        print(f"Error: {e}")

def quickskan():
    option = input("""Pick an option:
                        1. Port scan
                        2. dnslookup
                        """)
    if option == "1":
        return port_scan()
    elif option == "2":
        return dnslookup()
    else:
        print("Option not picked/chosen. Rerun script") 

quickskan()
