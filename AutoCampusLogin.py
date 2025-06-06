import re
import requests
from urllib.parse import urlparse, parse_qs, urlencode, quote

USERNAME = ""   #学号
PASSWORD = ""   #校园网密码


def is_online(test_url="https://www.baidu.com/favicon.ico", timeout=3) -> bool:
    print("Checking network status...")
    try:
        response = requests.get(test_url, timeout=timeout)
        return response.status_code == 200
    except requests.RequestException:
        return False


def get_redirect_url():
    try:
        response = requests.get("http://baidu.com", allow_redirects=False)
        match = re.search(r"href='(.*?)'</script>", response.text)
        if match:
            redirect_url = match.group(1)
            print("Authentication URL:", redirect_url)

            parsed_url = urlparse(redirect_url)
            host = parsed_url.hostname or ""
            port = parsed_url.port or 80
            host_port = f"{host}:{port}"

            if "eportal" in redirect_url:
                return redirect_url, host_port
        print("No authentication redirect found.")
    except Exception as e:
        print("Error retrieving redirect URL:", e)
    return None, None


def parse_login_params(url):
    print("Parsing login parameters...")
    parsed = urlparse(url)
    params = parse_qs(parsed.query, keep_blank_values=True)
    return {k: v[0] for k, v in params.items()}


def gbk_urlencode(data: dict) -> str:
    return '&'.join(f"{quote(k, encoding='gbk')}={quote(v, encoding='gbk')}" for k, v in data.items())


def login_to_campus_net(login_params, redirect_url, host_port):
    login_url = f"http://{host_port}/eportal/webGateModeV2.do"

    query_params = {
        "method": "login",
        "param": "true",
        **login_params
    }

    post_data = {
        "is_auto_land": "false",
        "usernameHidden": USERNAME,
        "username_tip": "Username",
        "username": USERNAME,
        "strTypeAu": "",
        "uuidQrCode": "",
        "authorMode": "",
        "pwd_tip": "Password",
        "pwd": PASSWORD,
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": redirect_url
    }

    # 构造 payload
    payload = gbk_urlencode(post_data) + "&net_access_type=%BB%A5%C1%AA%CD%F8"

    try:
        print("Logging in...")
        r = requests.post(login_url, params=query_params, data=payload, headers=headers, allow_redirects=False)

        if r.status_code == 302 and r.headers.get("Auth-Result") == "success":
            print("CampusNet Authentication successful!")
        else:
            print("Login failed.")
            print("Status Code:", r.status_code)
            print("Headers:", r.headers)

    except Exception as e:
        print("Login error:", e)


def main():

    if is_online():
        print("Network is online.")
        exit(0)
    print("Starting authentication process...")
    redirect_url, host_port = get_redirect_url()
    if redirect_url:
        login_params = parse_login_params(redirect_url)
        login_to_campus_net(login_params, redirect_url, host_port)
    else:
        print("Could not find login page.")


if __name__ == "__main__":
    main()