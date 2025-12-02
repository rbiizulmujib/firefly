import requests
import json
import datetime
import time

with open('prompts.txt', 'r') as f:
    prompts = f.readlines()

for prompt in prompts:
    prompt = prompt.strip()
    if not prompt:
        continue

    print(f"Processing prompt: {prompt}")

    url = "https://firefly-3p.ff.adobe.io/v2/3p-images/generate-async"

    payload = json.dumps({
  "n": 1,
  "seeds": [
    73340
  ],
  "output": {
    "storeInputs": True
  },
  "prompt": prompt,
  "size": {
    "width": 1024,
    "height": 1024
  },
  "referenceBlobs": [],
  "modelSpecificPayload": {
    "parameters": {
      "addWatermark": False
    },
    "aspectRatio": "1:1"
  },
  "modelId": "gemini-flash",
  "modelVersion": "nano-banana-2",
  "generationMetadata": {
    "module": "text2image"
  },
  "groundSearch": True
})
    headers = {
      'accept': '*/*',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
      'authorization': 'Bearer eyJhxbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE3NjQ2MzYzODM2NTlfOGQ1M2Y5MzktYzZjZi00YmUyLTljZWEtYTA0MTJmYzc4ZTZkX3V3MiIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiJjbGlvLXBsYXlncm91bmQtd2ViIiwidXNlcl9pZCI6IjAzNjNCQzYxNTgzQjNGNzgwQTQ5NURFN0BBZG9iZUlEIiwiYXMiOiJpbXMtbmExIiwiYWFfaWQiOiIwMzYzQkM2MTU4M0IzRjc4MEE0OTVERTdAQWRvYmVJRCIsImN0cCI6MCwiZmciOiIyQUNBNTNKTFZMTTVBRFVLRkFRVklIQUFFND09PT09PSIsInNpZCI6IjE3NTk3MzM5NTgyNjlfYWVlMTY0MGUtNjlmOC00ZjljLTg1NmYtODhmZDQyMWE3NmMxX3V3MiIsIm1vaSI6IjY3ZWRkM2UzIiwicGJhIjoiTWVkU2VjTm9FVixMb3dTZWMiLCJleHBpcmVzX2luIjoiODY0MDAwMDAiLCJzY29wZSI6IkFkb2JlSUQsZmlyZWZseV9hcGksb3BlbmlkLHBwcy5yZWFkLGFkZGl0aW9uYWxfaW5mby5wcm9qZWN0ZWRQcm9kdWN0Q29udGV4dCxhZGRpdGlvbmFsX2luZm8ub3duZXJPcmcsdWRzX3JlYWQsdWRzX3dyaXRlLGFiLm1hbmFnZSxyZWFkX29yZ2FuaXphdGlvbnMsYWRkaXRpb25hbF9pbmZvLnJvbGVzLGFjY291bnRfY2x1c3Rlci5yZWFkLGNyZWF0aXZlX3Byb2R1Y3Rpb24iLCJjcmVhdGVkX2F0IjoiMTc2NDYzNjM4MzY1OSJ9.R2fhDbYkiE8vavWqCWoRLRHlGDfwKrMQKi6BgA3X2gLc0M-IOSuskXbFn9b6s2XgZx7-MvpCGO-NDqgsrvvgBteqc1nDEMTGK47nLsY-2y23e5hlAzwQzFP0-yaKTh8wqI65yT7FnncgnnrgA_ZS1mr5R8puKylWqx2NY2NNK-wqkTxLSBSJ669zZ2AzJXvE8yevgi8WvTTjCEZjccvZl8JqyT98CXUzVSaSQAmVq42i4d3RBiFpopeXKa8_J3wbDWlSklGlcSBc6RhkLgly7NdfyEV20AD71bZFd-JkvepMJnstGxE3q57xdL7xznHPo1wr_6MAXvWvcjsmuNcUCg',
      'content-type': 'application/json',
      'origin': 'https://firefly.adobe.com',
      'priority': 'u=1, i',
      'referer': 'https://firefly.adobe.com/',
      'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
      'x-api-key': 'clio-playground-web'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

    print("TUNGGU 15 DETIK")
    time.sleep(50)
    result_url = ""
    try:
        resp_json = response.json()
        result_url = resp_json["links"]["result"]["href"]
    except Exception as e:
        print("Gagal mengambil result:", e)
        continue

    print("INI HASIL GENERATE URL: ", result_url)

    response_img = requests.request("GET", result_url, headers=headers, data=payload)

    print("INI DATA BUAT DOWNLOAD")
    print(response_img.text)
    print(response_img.status_code)

    try:
        data = response_img.json()
        print(data)
        presigned_url = data["outputs"][0]["image"]["presignedUrl"]
        print("Presigned URL:", presigned_url)

        # Generate nama file dengan timestamp
        now = datetime.datetime.now()
        filename = now.strftime("IMG1-%Y%m%d_%H%M%S.png")

        # Download gambar
        img_resp = requests.get(presigned_url)
        if img_resp.status_code == 200:
            with open(filename, "wb") as f:
                f.write(img_resp.content)
            print(f"Gambar berhasil didownload: {filename}")
        else:
            print("Gagal download gambar:", img_resp.status_code)
    except Exception as e:
        print("INI LINK DOWNLOAD", data)
        print("Gagal mengambil presignedUrl atau download gambar:", e)

    print("-" * 20)
