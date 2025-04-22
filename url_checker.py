import requests

def check_urls(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("❌ urls.txt not found.")
        return

    with open("results.txt", "w") as output:
        for url in urls:
            try:
                response = requests.get(url, timeout=5)
                status = response.status_code
            except requests.RequestException:
                status = "ERR"
            result = f"[{status}] {url}"
            print(result)
            output.write(result + "\n")

if __name__ == "__main__":
    check_urls("urls.txt")
