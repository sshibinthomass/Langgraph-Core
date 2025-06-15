### End to End Project Agentic AI Chatbots

---

## Setup Instructions

After pulling (cloning or downloading) this application, follow these steps to set up your environment:

### 1. Install [UV](https://github.com/astral-sh/uv) (if not already installed)
UV is a fast Python package manager. You can install it by following the instructions on the [official UV GitHub page](https://github.com/astral-sh/uv#installation).

### 2. Initialize UV in the project directory
```sh
uv init
```
This will set up UV for your project.

### 3. Create a virtual environment using UV
```sh
uv venv
```
This will create a `.venv` folder in your project directory.

### 4. Activate the virtual environment
On **Windows**:
```sh
.venv\Scripts\activate
```
On **macOS/Linux**:
```sh
source .venv/bin/activate
```

### 5. Install dependencies from `requirements.txt`
```sh
uv add -r requirements.txt
```
This will install all required packages listed in `requirements.txt` using UV.

---

You are now ready to use the application!

## Running the Streamlit App

To start the Streamlit application, run the following command in your project directory:

```sh
streamlit run app.py
```

This will launch the app in your default web browser. Make sure your virtual environment is activated before running this command.
