import requests
import sys
import argparse

def validate_google_play_app(app_id):
    base_url = "https://play.google.com/store/apps/details"
    
    params = {
        'id': app_id
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(base_url, params=params, headers=headers, allow_redirects=True)
    
    if response.status_code != 200:
        return False, f"Failed to access app page. Status code: {response.status_code}"
    
    if app_id not in response.text:
        return False, "App not found"
        
    return True, "App is available"

def main():
    parser = argparse.ArgumentParser(description='Check Google Play Store app availability')
    parser.add_argument('--app-id', required=True, help='Google Play Store app ID (e.g., com.whatsapp)')
    args = parser.parse_args()
    
    is_valid, message = validate_google_play_app(args.app_id)
    print(f"App ID: {args.app_id}")
    print(f"Is app valid: {is_valid}")
    print(f"Message: {message}")

if __name__ == "__main__":
    main()
