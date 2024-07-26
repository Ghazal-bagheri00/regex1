import re

log = """2024/07/11 15:30:45 [error] 1234#1234: *56789 connect() failed (111: Connection refused) while connecting to upstream, client: 192.168.1.100, server: example.com, request: “GET /api/data HTTP/1.1”, upstream: “http://127.0.0.1:8000/api/data”, host: “example.com”, referrer: “https://example.com/”


"""
time=r'(\d{2}:\d{2}:\d{2})'
date=r'(\d{4}/\d{2}/\d{2})'
client=r'(\d{3}.\d{3}.\d{1,3}.\d{3})'
server=r'(\w{1,10}.com)'

time_match = re.search(time,log)
date_match = re.search(date, log)
client_match=re.search(client,log)
server_match=re.search(server,log)

if time_match:
    print(f"Time: {time_match.group(1)}")
if date_match:
    print(f"Date: {date_match.group(1)}")
if client_match:
    print(f"client):{client_match.group(1)}")
if server_match:
    print(f"server):{server_match.group(1)}")