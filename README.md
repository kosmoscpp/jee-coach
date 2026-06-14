# 🎓 JEE Coach — Advanced Mentor Dashboard

A sleek, minimalist, AI mentoring engine designed to help students optimize their **IIT-JEE Advanced** preparation strategy. Built completely with Streamlit, Docker, and Python, this application runs independently on cloud architecture using serverless LLM compilation loops.

🚀 **Live Deployment:** [jeecoach-kosmos.up.railway.app](https://jeecoach-kosmos.up.railway.app)

---

## ⚡ Key Architectural Features

* **Targeted Segmentation Architecture:** Dynamically splits operational workflows across three completely distinct student baselines:
  * **Class 11:** Focuses heavily on structural fundamentals, core mechanics/organic logic transitions, and consistency.
  * **Class 12 Aspirant:** Balances deep Advanced prep with board exams schedules, mock series, and practical allocations.
  * **Dropper Batch:** Assumes zero schooling restrictions, optimizing purely for high-yield multi-revision sprints and test analysis loops.
* **Operational Lens Filters:** Instantly mutates system instruction weights depending on user selection:
  * 📚 **Doubt:** Step-by-step mathematical and conceptual mechanism breakdowns.
  * ⏳ **Backlog:** Strategic micro-schedules prioritizing critical mandatory chapters.
  * 🔥 **Motivation:** Direct, high-energy, realistic focus adjustments to shatter decision paralysis.
  * 🧠 **Revision:** Clear structures for building formula frameworks and active short-note trackers.
---

## 🛠️ Stack Configuration

* **Frontend Engine:** [Streamlit](https://streamlit.io/) 
* **Model Orchestration:** Meta-Llama-3-8B-Instruct via the serverless `huggingface_hub` token pipeline
* **Deployment System:** Docker Engine on [Railway.app](https://railway.app)

---

## 📦 Local Workspace Setup

If you want to pull down this project and spin it up inside your local terminal environment, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

```
### 2. Install Package Dependencies
Ensure you have Python 3.10+ installed globally, then execute:
```bash
pip install -r requirements.txt

```
### 3. Establish System Environment Secrets
Create a local .env configuration file or export your Hugging Face Access Token directly to your shell environment:
```bash
export HF_TOKEN="your_huggingface_access_token_here"

```
### 4. Execute the Application Engine
```bash
streamlit run app.py

```
## 🐳 Docker Containerization Layout
This platform is configured with an automated container blueprint via the included Dockerfile to enable seamless integration with modern DevOps cloud environments:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

```
## 🤝 Project Origin & Connection
Built out of a deep appreciation for open-source AI models and modular deployment infrastructure.
💻 Created by Developer **Kosmos**
📸 Keep up with updates or reach out for architecture collaborations on Instagram: @kosmos.cpp
```

### How to add this to your project:
1. Open your GitHub repository on your device.
2. Click **Add file** -> **Create new file**.
3. Name the file exactly **`README.md`** (all caps is standard).
4. Paste the text code block above into the text area. Change `YOUR_GITHUB_USERNAME` and `YOUR_REPO_NAME` in the cloning snippet to match your real links if you want it extra perfect!
5. Hit **Commit changes**.

The second you save it, GitHub will render it into a beautifully styled showcase project page right below your files list. Your profile's contribution graph gets another dark green square, and your repo looks 100% production-ready! 🔥🟩

```
