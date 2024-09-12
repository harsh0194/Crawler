Web Crawler and Directory Brute Force Tools
This repository contains two Python scripts designed for web security testing. One script is a web crawler to recursively extract and explore links from a given target URL, while the other script performs directory brute-forcing to discover hidden files and directories on a target web server.

Prerequisites
Before running the scripts, ensure you have the following installed:

Python 3.x
requests library (can be installed via pip if not already present)
bash


1. Web Crawler Script (crawl.py)
This script crawls a given target URL and recursively extracts links from the page. It helps in identifying various accessible pages and resources within a website by recursively following the internal links.

How it works:
Sends a GET request to the target URL.
Extracts all links (href attributes) from the HTML content.
Follows each extracted link if it's part of the target domain.
Avoids revisiting links to prevent infinite loops.
Usage:
Edit the target_url to the desired target.
Run the script.



2. Directory Brute Force Script (spider.py)
This script performs brute force attacks to discover hidden files and directories on a web server by appending common directory/file names (from a wordlist) to the target URL.

How it works:
Reads from a wordlist file (common.txt).
Appends each word to the target URL and sends a request.
If the response status code is 200, the script identifies it as a valid/accessible URL.
Usage:
Modify the target_url to point to the target server.
Provide the path to a wordlist (e.g., /root/Downloads/common.txt).
Run the script.



Notes
These tools are for educational purposes and should only be used on authorized systems. Unauthorized use of these scripts may violate laws and regulations.
Modify the target_url and wordlist paths in each script to match your environment before running.
