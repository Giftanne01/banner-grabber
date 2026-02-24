#!/usr/bin/env python3
"""
Simple Banner Grabber
Connects to a target IP:port and retrieves the service banner
"""

import socket
import sys

def grab_banner(ip, port, timeout=2):
    """
    Attempt to grab banner from a service
    
    Args:
        ip: Target IP address
        port: Target port number
        timeout: Connection timeout in seconds
    
    Returns:
        Banner string or None if failed
    """
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        
        # Connect to the target
        print(f"[*] Connecting to {ip}:{port}...")
        s.connect((ip, port))
        
        # Receive the banner (some services send it immediately)
        banner = s.recv(1024).decode().strip()
        
        # Close the connection
        s.close()
        
        return banner
        
    except socket.timeout:
        return None
    except socket.error as e:
        return None
    except Exception as e:
        print(f"[!] Error: {e}")
        return None

def main():
    """Main function"""
    print("="*50)
    print("Simple Banner Grabber")
    print("="*50)
    
    # Get user input
    if len(sys.argv) == 3:
        target_ip = sys.argv[1]
        target_port = int(sys.argv[2])
    else:
        target_ip = input("Enter target IP: ")
        target_port = int(input("Enter target port: "))
    
    # Grab the banner
    banner = grab_banner(target_ip, target_port)
    
    # Display results
    if banner:
        print(f"[+] Banner received:")
        print(f"    {banner}")
    else:
        print(f"[-] No banner received or connection failed")
    
    print("="*50)

if __name__ == "__main__":
    main()
