# femtocell
import subprocess
def port_scan():
    addr = input("enter ipv4 addr: ")
    try:
        result = subprocess.run(['nmap', '-p-', addr], capture_output=True, text=True)
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


def whois_look():
    lookup = input("input domain / ip addr for whoislookup: ")
    try:
        response = subprocess.run(['whois', lookup], capture_output=True, text=True)
        return response.stdout
    except Exception as e:
        print(f"Error: {e}")

def quickskan():
    option = input("""Pick an option:
                        1. Port scan
                        2. dnslookup
                        3. whois
                        """)
    if option == "1":
        return port_scan()
    elif option == "2":
        return dnslookup()
    elif option == "3":
        return whois_look()
    else:
        print("Option not picked/chosen. Rerun script") 

quickskan()

