import requests
import json


def get_gemma_response(prompt):
    # Define the correct API endpoint URL for Groq or Hugging Face
    url = 'https://console.groq.com/playground'

    # Define the headers with the correct authorization token
    headers = {
        'Authorization': 'Bearer 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',
        'Content-Type': 'application/json'
    }

    # Define the payload with the input prompt
    payload = {
        'inputs': prompt,
    }

    try:
        # Make a POST request to the API endpoint
        response = requests.post(url, headers=headers, json=payload)

        # Debugging outputs
        print('Status Code:', response.status_code)

        # Safely print a portion of the response to avoid encoding issues
        try:
            response_text = response.text.encode('utf-8', 'replace').decode('utf-8')
            print('Response Text (partial):', response_text[:200], '...')  # Print only the first 1000 characters
        except UnicodeEncodeError:
            print("Failed to encode response text")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Ensure the response is JSON
            print('Test 1 PASSED')
            #print(json.dumps(response.text, indent=4, sort_keys=True, default=lambda o:'<not serializable>'))
            return response

            #print('response ;', str(response.content))
            #if response.headers.get('Content-Type') == 'application/json':
            #    return response.json()
            #else:   
            #    print('Unexpected content type:', response.headers.get('Content-Type'))
            #    return None
        #else:
         #   print('Error:', response.status_code, response.text)
          #  return None
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None

def main():
    # Open the input file and read the prompt
    with open('D:\\DashLabs\\Development\\input.txt', 'r') as f:
        prompt = f.read().strip()  # Strip to remove any extra whitespace or newline characters
        print (prompt)
    response = get_gemma_response(prompt)
    print('Response Recieved, Response TYPE:', type(response.content))
    
    if response:
        #print('RESPONSE:', response.json())
        with open ('D:\DashLabs\Development\output.json', 'w') as f:
            #json.dump(response.content,f)
            json.dumps(response.text, indent=4, sort_keys=True, default=lambda o:'<not serializable>')

    else:
        print('Failed to fetch response from API.')

if __name__ == '__main__':
    main()
