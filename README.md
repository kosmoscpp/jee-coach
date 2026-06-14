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
##

## License

[![License](https://shields.io)](https://opensource.org)

This project is licensed under the Apache License, Version 2.0. See the {Link: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0} 

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Copyright [Year] 
