Below is a **step-by-step guide** aimed at absolute beginners. It explains how to:

1. Download (clone) the Cisco Data Bridge AI Agent from GitHub.  
2. Prepare a local development environment or sandbox environment.  
3. Create and configure the `.env` file (including what it is and how it’s used).  
4. Spin up optional Cisco Sandboxes (Meraki & Catalyst Center) to demonstrate the AI agent.  

---

## 1. Prerequisites

Before you start, you’ll need:

1. **Git**  
   - Git is a version control tool used to download (“clone”) projects from GitHub.  
   - [Download Git here](https://git-scm.com/downloads) if you don’t already have it.  
   - During installation, you can mostly accept the defaults.

2. **Python 3.9+** (Recommended)  
   - The AI Agent’s code is written in Python. You need Python installed to run it locally.  
   - [Download Python here](https://www.python.org/downloads/).

3. **Pip** or **Poetry** (for installing Python dependencies)  
   - If you have Python 3.9+, Pip should already be installed.  
   - Alternatively, some developers prefer **Poetry** as a more modern package manager. This is optional.

4. (**Optional**) **Docker**  
   - You can containerize and run the AI Agent inside Docker if you prefer.  
   - [Download Docker here](https://docs.docker.com/get-docker/).  
   - If you’re completely new, you can skip Docker for now and run directly on your local machine.

---

## 2. Download (Clone) the Repository

1. **Open a Terminal or Command Prompt**  
   - On Windows, search for “Command Prompt” or open Git Bash.  
   - On Mac/Linux, open Terminal.

2. **Navigate to a Folder Where You Want to Download the Code**  
   - For example:
     ```bash
     cd Documents
     ```

3. **Clone the Repository**  
   - Run the following command:
     ```bash
     git clone https://github.com/APO-SRE/cisco-data-bridge-ai-agent.git
     ```
   - This will create a new folder named `cisco-data-bridge-ai-agent` in your current directory.

4. **Enter the Project Folder**  
   ```bash
   cd cisco-data-bridge-ai-agent
   ```

Now you’ve successfully downloaded (“cloned”) the AI agent code to your local machine.

---

## 3. Install Dependencies

There are two main ways to install all necessary Python libraries:

### Option A: Using `requirements.txt` + `pip`

1. **Make sure you’re inside the project folder**  
   ```bash
   cd cisco-data-bridge-ai-agent
   ```
2. **Install using pip**  
   ```bash
   pip install -r requirements.txt
   ```
   - This downloads and installs all dependencies listed in `requirements.txt`.

### Option B: Using Poetry

1. **Install Poetry (if you haven’t already)**  
   - [Poetry Installation Guide](https://python-poetry.org/docs/#installation).
2. **Install dependencies**  
   ```bash
   poetry install
   ```
3. **(Optional) Activate the virtual environment**  
   ```bash
   poetry shell
   ```

Either option is fine. If you’re brand new to Python, Option A with pip is usually simpler.

---

## 4. Understand & Create the `.env` File

In the project folder, there is a file named `ENV_TEMPLATE`. This is an example configuration file. You need to **copy** or **rename** `ENV_TEMPLATE` to `.env` so the application knows where to read your environment variables.

1. **What Is a `.env` File?**  
   - A `.env` file stores configuration **secrets** or **settings** (such as API keys, service URLs, or usernames/passwords) needed by your application.  
   - By keeping this info separate, you don’t accidentally share sensitive data when you commit code to GitHub.

2. **Copy `ENV_TEMPLATE` to `.env`**  
   - In the terminal (Mac/Linux):
     ```bash
     cp ENV_TEMPLATE .env
     ```
   - In Windows Command Prompt:
     ```bat
     copy ENV_TEMPLATE .env
     ```
   - Or just manually rename the file in your file explorer from `ENV_TEMPLATE` → `.env`.

3. **Open `.env` in a text editor** (Notepad, VS Code, Sublime, etc.)  
   - Fill in the variables according to your setup.  
   - Each variable is in the format:  
     ```
     VARIABLE_NAME=value
     ```

4. **Important Variables**  
   - **`LLM_TYPE`**: Whether you’re using Azure OpenAI or another model.  
   - **`RAG_TYPE`**: If you do not want retrieval-augmented generation, set this to `"none"`.  
   - **`AZURE_OPENAI_ENDPOINT`** and **`AZURE_OPENAI_KEY`**: If you are using Azure OpenAI, fill in your endpoint and key here.  
   - **`CISCO_MERAKI_API_KEY`**: If you want to demo Meraki integrations, add your Meraki API key.  
   - **`CISCO_CATALYST_USERNAME`**, **`CISCO_CATALYST_PASSWORD`**, **`CISCO_CATALYST_URL`**, and **`CISCO_CATALYST_VERSION`**: If you want to demo Catalyst Center integration.  
   - If you **do not** want to enable certain integrations, like Catalyst Center or Webex, set the corresponding `ENABLE_*` variable to `false`.

Example snippet (from `ENV_TEMPLATE`):
```
ENABLE_CATALYST_CENTER=false
ENABLE_MERAKI=true
ENABLE_CISCO_SPACES=true
ENABLE_CISCO_WEBEX=false

LLM_TYPE=azure_openai
RAG_TYPE=none  # If you don't want retrieval-augmented generation
AZURE_OPENAI_ENDPOINT=<your-azure-openai-endpoint>
AZURE_OPENAI_KEY=<your-azure-openai-key>
...
CISCO_MERAKI_API_KEY=<your-meraki-api-key>
...
```

---

## 5. (Optional) Setting Up Cisco Sandboxes

If you **only** want to run the AI Agent with minimal functionality, you can **skip** the Cisco integrations. However, to demonstrate how the AI Agent can interact with actual Cisco platforms, you can set up one or more sandboxes. Cisco offers free sandbox environments via [developer.cisco.com/site/sandbox/](https://developer.cisco.com/site/sandbox/).

### A. Meraki Sandbox Setup

1. **Go to** [Cisco DevNet Sandbox](https://developer.cisco.com/site/sandbox/).  
2. **Search for “Meraki Always On”**.  
3. **Click “Launch Environment”** to begin spinning up the sandbox.  
   - Setup usually takes 1–2 minutes.
4. **Check Your Email** (from `noreply@meraki.com`)  
   - It will ask you to accept access to the “Always-On Organisation.”  
   - If you are new to Meraki, you may need to change your Meraki password.
5. **Obtain Your Meraki API Key**  
   - In the Meraki dashboard, go to your user profile to generate an API key.  
   - **Copy** this API key (it’s a long alphanumeric string).

6. **Add Your Meraki API Key to `.env`**  
   - Open `.env`  
   - Find the line:  
     ```
     CISCO_MERAKI_API_KEY=<your-meraki-api-key>
     ```
   - Replace `<your-meraki-api-key>` with your actual key.  
   - Ensure `ENABLE_MERAKI=true` near the top of `.env`.  

> **Troubleshooting**: If you already have a Meraki account, you might have to click approval a couple of times for the Always-On org to be added to your account.

### B. Catalyst Center Sandbox Setup

1. **Go to** [Cisco DevNet Sandbox](https://developer.cisco.com/site/sandbox/).  
2. **Search for “Catalyst Center”**.  
3. **Select “Catalyst-Center-Always-On_catalyst-center-always-on”**.  
4. Note the **Default Credentials**:
   - Username: `devnetuser`
   - Password: `Cisco123!`
   - URL: `https://sandboxdnac2.cisco.com`
   - Version: `2.3.7.6`
5. **Fill In `.env`**  
   - Set:
     ```
     ENABLE_CATALYST_CENTER=true
     CISCO_CATALYST_USERNAME=devnetuser
     CISCO_CATALYST_PASSWORD=Cisco123!
     CISCO_CATALYST_URL=https://sandboxdnac2.cisco.com
     CISCO_CATALYST_VERSION=2.3.7.6
     ```
   - If you don’t plan to use Catalyst Center, leave `ENABLE_CATALYST_CENTER=false`.

---

## 6. Run the AI Agent

### Option A: Directly with Python

1. **Ensure you’ve installed all dependencies** (`pip install -r requirements.txt`).  
2. **Make sure your `.env` file is properly configured**.  
3. **Run the FastAPI server**:
   ```bash
   cd cisco-data-bridge-ai-agent
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   - This starts a server on `http://localhost:8000`.

4. **Open the Static Front-End** (if provided)  
   - By default, you might open a separate local page (from the `static/` folder) or navigate to `http://localhost:8000` (depending on how the `static/` files are served).  
   - Some example routes might be:
     - `http://localhost:8000` → Basic health check or docs
     - `http://localhost:8000/docs` → Interactive API docs (FastAPI’s automatic docs)
     - `http://localhost:8000/static/` → The example chat UI (if configured)

### Option B: Using Docker

1. **Build the Docker Image**  
   - In the project root folder (where the `Dockerfile` is located), run:
     ```bash
     docker build -t cisco-data-bridge:latest .
     ```
2. **Run the Docker Container**  
   ```bash
   docker run -p 8000:8000 --env-file .env cisco-data-bridge:latest
   ```
   - `--env-file .env` tells Docker to use your local `.env` for environment variables.  
   - The application should be accessible at `http://localhost:8000`.

---

## 7. Testing the Agent

1. **Access the Application in Your Browser**  
   - Point your browser to [http://localhost:8000/static/](http://localhost:8000/static/) or wherever the front-end is served.  
   - You can test chat features, ask the LLM questions, etc.

2. **Verify API Connectivity**  
   - If you’ve enabled Meraki or Catalyst in your `.env`, try an example query like:  
     > “Hey, can you retrieve information about the Meraki networks I have access to?”  
   - The AI agent will use your Meraki API Key or Catalyst credentials to access sandbox data (read-only).

3. **Review Logs & Debug**  
   - Return to your Terminal/Command Prompt to view logs.  
   - Check for any error messages related to network calls or environment variables.

---

## 8. Summary & Next Steps

- You now have the **Cisco Data Bridge AI Agent** running locally or in a Docker container.  
- You can **enable or disable** various Cisco integrations using the `.env` file.  
- If you want more advanced features, such as retrieval-augmented generation (RAG) with Azure Cognitive Search or other vector databases (Chroma, Elastic), set `RAG_TYPE` accordingly and **fill out** the associated environment variables.

### Key Points to Remember

- **`.env` file**: Stores credentials and toggles for integrations. Keep this private.  
- **Sandbox integrations**: You only need to configure the ones you want to demo.  
- **Azure OpenAI**: You’ll need your Azure OpenAI endpoint and key if you plan on using GPT-4 or GPT-3.5. Otherwise, set `LLM_TYPE` to something else or skip it.  
- **Containerization**: The provided `Dockerfile` makes it easy to run in a container.  

---

## 9. Additional Help

- **Git & GitHub**: If you’re unfamiliar, check out a beginner tutorial like [GitHub Docs](https://docs.github.com/en/get-started).  
- **Python Basics**: The official [Python Tutorials](https://docs.python.org/3/tutorial/) can help.  
- **Docker**: The official [Docker Documentation](https://docs.docker.com/get-started/) has a quick-start tutorial.  
- **Cisco DevNet**: Their [Sandbox Documentation](https://developer.cisco.com/docs/) has more details on each sandbox environment.

---

**Congratulations!** You’ve set up your very own Cisco Data Bridge AI Agent. You can now explore its capabilities, integrate new Cisco platforms, or adapt the front-end for your own needs.