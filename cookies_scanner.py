import requests

def get_cookies(url):
    try:
        # Create a session object
        session = requests.Session()

        # Send a GET request to the specified URL
        response = session.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Retrieve cookies from the response
            cookies = session.cookies.get_dict()
            
            # Print the cookies
            print(f"Cookies for {url}:")
            for cookie_name, cookie_value in cookies.items():
                print(f"{cookie_name}: {cookie_value}")
        else:
            print(f"Failed to retrieve the website. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input URL from the user
    url = input("Enter the website URL: ").strip()
    get_cookies(url)
