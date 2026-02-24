# Banner Grabber

A simple Python tool for grabbing service banners from network services.

## What It Does

Connects to a specified IP address and port, then retrieves the service banner. This helps identify what service is running on a particular port.

## Requirements

- Python 3.x
- No external libraries needed (uses standard `socket` library)

## Usage

### Interactive Mode
```bash
python3 banner_grabber.py
```
Then enter the IP and port when prompted.

### Command Line Mode
```bash
python3 banner_grabber.py <IP> <PORT>
```

### Examples
```bash
# Grab banner from a web server
python3 banner_grabber.py scanme.nmap.org 80

# Check FTP service
python3 banner_grabber.py 10.10.10.10 21

# Check SSH service
python3 banner_grabber.py 192.168.1.1 22
```

## How It Works

1. Creates a TCP socket connection
2. Connects to the target IP:port
3. Receives data sent by the service (the banner)
4. Displays the banner information
5. Closes the connection

## What I Learned

- Working with Python sockets
- TCP connections and network communication
- Error handling in network programming
- Command-line argument parsing

## Future Improvements

- [ ] Scan multiple ports at once
- [ ] Add timeout customization
- [ ] Support for UDP services
- [ ] Save results to file
- [ ] Multi-threaded scanning

## Testing

You can test this on TryHackMe machines or use:
- `scanme.nmap.org` (port 22, 80)
- Your own local services

**Note:** Only scan systems you have permission to test.

---

*Built as part of my cybersecurity learning journey*
*Day 2 of building security tools*
