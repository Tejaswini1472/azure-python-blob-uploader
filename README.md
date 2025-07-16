# Azure Python Blob Uploader 🚀

This mini project uses **Azure Functions** and **Azure Blob Storage** with **Python** to handle HTTP POST requests and automatically process uploaded files using **Blob Triggers**.

## Features 💡
- Upload a file using HTTP request (POST)
- Automatically detect and process uploaded blob in the storage container
- Logs blob name and size on successful upload

## Technologies Used 🛠️
- Azure Functions (Python)
- Azure Blob Storage
- GitHub for version control

## How It Works 🔁
1. User sends a POST request with data.
2. Azure Function processes the request and uploads a file to Blob Storage.
3. Blob Trigger function detects the new blob and logs its metadata (name, size).

## Run Locally 🖥️

1️⃣ Install Azure Functions Core Tools 
2️⃣ Install required Python packages:

```bash
pip install -r requirements.txt

3️⃣ Start the Azure Function app:
func start
Now visit http://localhost:7071/api/upload to test the API locally.

📂 Folder Structure
<pre> ``` azure-python-blob-uploader/ ├── function_app.py # Main HTTP trigger and blob logic ├── requirements.txt # Python dependencies ├── host.json # Azure Functions host config ├── local.settings.json # Local environment variables ├── .vscode/ # VS Code configurations └── .gitignore # Files to ignore in Git ``` </pre>

📡 Example Request (HTTP POST)
POST http://localhost:7071/api/upload
Content-Type: application/json

{
  "filename": "example.txt",
  "content": "Hello from Azure Function!"
}

🖨️ Output Example

Blob uploaded: example.txt (24 bytes)
✍️ Author
Tejaswini Sahare
GitHub: Tejaswini1472




