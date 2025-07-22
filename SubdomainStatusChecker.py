import requests
import concurrent.futures
import argparse

ACTIVE_STATUS_CODES = {200, 201, 202, 203, 204, 205, 206,
                       300, 301, 302, 303, 304, 305, 307, 308}

def detect_protocol(subdomain):
    """Try https, then http. Return first active protocol with status code."""
    for protocol in ("https", "http"):
        url = f"{protocol}://{subdomain}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code in ACTIVE_STATUS_CODES:
                return f"{url} [{response.status_code}]"
        except requests.exceptions.RequestException:
            continue
    return None  # No working protocol found

def main():
    parser = argparse.ArgumentParser(
        description="Check subdomains for live protocol and status code; auto-detects http or https."
    )
    parser.add_argument("subdomain_file", help="File with subdomains to check")
    parser.add_argument("-o", "--output", help="File to save results", default=None)
    args = parser.parse_args()

    try:
        with open(args.subdomain_file, "r") as file:
            subdomains = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{args.subdomain_file}' not found.")
        return

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_sub = {executor.submit(detect_protocol, sd): sd for sd in subdomains}
        for future in concurrent.futures.as_completed(future_to_sub):
            result = future.result()
            if result:
                print(result)
                results.append(result)

    if args.output:
        try:
            with open(args.output, "w") as f:
                for line in results:
                    f.write(line + "\n")
            print(f"\nResults saved to {args.output}")
        except Exception as e:
            print(f"Error saving results to file: {e}")

if __name__ == "__main__":
    main()
