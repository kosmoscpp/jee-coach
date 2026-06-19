
# 🎓 Focus AI — Multi-Tier Academic Mentor Dashboard

A sleek, minimalist, AI mentoring engine designed to help students and engineering undergraduates optimize their academic preparation, clear systemic roadblocks, and structure high-yield study frameworks. Built completely with Streamlit, Docker, and Python, this application utilizes an efficient, single-instance serverless LLM orchestration pipeline.

🚀 **Live Deployment:** [jeecoach-kosmos.up.railway.app](https://jeecoach-kosmos.up.railway.app)

---

## ⚡ Key Architectural Features

* **Targeted Multi-Tier Segmentation:** Dynamically splits operational workflows across three completely unique academic layers:
  * **Foundation (Class 9 & 10):** Focuses on core mental models, conceptual scaling, and competitive baseline structures without burnout.
  * **High-Yield Competitive (Class 11, 12, & Droppers):** Multi-stream calibration supporting **JEE** and **NEET** pathways, adjusting topic hierarchies across Physics, Chemistry, Mathematics, and Biology.
  * **Undergraduate Engineering (BTech):** Tailor-made strategy adjustments across specialized domains (**CSE, Mechanical, Civil, Electrical, Designing**) focusing on GPA recovery, labs, core technicals, and placement readiness.
* **Efficient Session Management:** Memory-optimized execution that initializes the inference client once per user session, drastically lowering endpoint latency during continuous text streaming.
* **Operational Lens Filters:** Instantly shifts system instruction weights depending on user selection:
  * 📚 **Doubt:** Step-by-step technical, mathematical, conceptual, or programmatic breakdowns.
  * ⏳ **Backlog:** Strategic micro-schedules prioritizing critical foundational modules.
  * 🔥 **Motivation:** Direct, high-energy, realistic focus adjustments to shatter decision paralysis.
  * 🧠 **Revision:** Structured blueprints for compiling cheat sheets, active recall trackers, and core technical formulas.

---

## 🛠️ Stack Configuration

* **Frontend UI Engine:** [Streamlit](https://streamlit.io/) (Customized with Gemini-inspired minimalist dark mode UI injection)
* **Model Orchestration:** Meta-Llama-3-8B-Instruct via the serverless `huggingface_hub` token pipeline
* **Deployment System:** Docker Engine on [Railway.app](https://railway.app)

---

## 📦 Local Workspace Setup

Follow these steps to spin up this project inside your local terminal environment:

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
## 📄 License
This project is licensed under the Apache License, Version 2.0. See the Apache License 2.0 for detailed terms.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
Copyright [YEAR]
```

