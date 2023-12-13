import requests
import datetime

# Define your ShareX server endpoint and API token
sharex_server_url = 'https://x.mikn.dev/api/upload/'
api_token = 'le58Hu59X7VviUNBACzM1Wgi.MTY5NzcwNjcyMDMzMQ'

def upload_log_to_sharex_server():
    # Generate a unique filename based on the current date
    current_date = datetime.datetime.now().strftime('%Y%m%d')
    filename = f'./log/{current_date}_log.txt'

    # Prepare the log file for upload as multipart/form-data
    files = {'file': (filename, open(filename, 'rb'))}

    # Define the headers, including the Authorization header
    headers = {'Authorization': f'{api_token}'}

    # Perform the POST request to the ShareX server
    response = requests.post(sharex_server_url, headers=headers, files=files)

    if response.status_code == 200:
        print(f"Log file uploaded successfully to ShareX server as '{filename}'")
    else:
        print(f"Error uploading log file. Status code: {response.status_code}")

upload_log_to_sharex_server()