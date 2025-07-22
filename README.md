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
