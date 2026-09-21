# GHOST // IP INFO TRACKER - By Destroyer445
import requests
import socket

def banner():
    print(r"""
  ____ _   _  ___  ____ _____
 / ___| | | |/ _ \/ ___|_   _|
| |  _| |_| | | | \___ \ | |
| |_| |  _  | |_| |___) || |
 \____|_| |_|\___/|____/ |_|
      IP TRACKER v1.0
    """)

def track_ip(ip):
    try:
        print(f"\n[+] Tracking IP: {ip}")
        # Get IP details from ip-api
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,isp,org,as,query"
        res = requests.get(url).json()

        if res['status'] == 'fail':
            print(f"[-] Failed: {res['message']}")
            return

        print(f"""
[+] IP: {res['query']}
[+] Country: {res['country']}
[+] Region: {res['regionName']}
[+] City: {res['city']} - {res['zip']}
[+] Latitude: {res['lat']} | Longitude: {res['lon']}
[+] ISP: {res['isp']}
[+] Org: {res['org']}
[+] AS: {res['as']}
[+] Google Map: https://www.google.com/maps?q={res['lat']},{res['lon']}
        """)
        print("[✓] Track Complete!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    banner()
    target = input("Enter IP Address (or press Enter for your IP): ").strip()
    if not target:
        target = requests.get('https://api.ipify.org').text
        print(f"Your IP: {target}")
    
    # Resolve if domain given
    try:
        ip = socket.gethostbyname(target) if not target.replace('.','').isdigit() else target
    except:
        ip = target

    track_ip(ip)
