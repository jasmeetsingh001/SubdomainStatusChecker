# SubdomainStatusChecker

A fast, simple Python tool to check which subdomains are active on HTTP or HTTPS and output their status code.
It auto-detects whether each subdomain is live over HTTPS or HTTP, prints the result, and lets you save to a text file.

*Features*

    - Checks each subdomain for the first working protocol: HTTPS or HTTP.
    - Shows result as:
      https://sub.example.com
    - Ignores subdomains that aren’t live.
    - Fast: uses threading for quick scanning.
    - Optional flag to save output to a text file.
    - Command-line help with -h.

*Requirements*

    - Python 3.6+
    - requests package

*To install dependencies:*

**bash**

pip install requests

Usage
1. Prepare Your Subdomain List

Create a text file (e.g., subdomains.txt) with one subdomain per line:
example.com
www.example.com
test.example.com

2. Run the Script

bash

python3 script.py subdomains.txt
You’ll see live domains/protocols and their status codes printed to the console.

3. Save Output to File

Add the -o or --output flag:

bash

python3 script.py subdomains.txt -o live_subdomains.txt

4. Show Help

bash

python3 script.py -h

Example Output:
https://example.com [200]
http://old.example.com [301]
