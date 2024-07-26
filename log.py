import re

log = """
2024/07/11 16:15:20 [error] 1234#1234: *67890 open() “/usr/share/nginx/html/not_found.html” failed (2: No such file or directory), client: 192.168.1.101, server: example.com, request: “GET /nonexistent-page HTTP/1.1”, host: “example.com”, referrer: “https://example.com/”


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