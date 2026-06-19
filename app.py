import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="AI Academic Mentor", page_icon="🎓", layout="centered")

# --- CUSTOM CSS: GEMINI-INSPIRED MINIMALIST UI ---
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .stApp {
            background-color: #131314;
            color: #e3e3e3;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        .main-title {
            text-align: center;
            font-size: 2rem;
            font-weight: 500;
            background: linear-gradient(45deg, #4285f4, #9b51e0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2rem;
        }
        .main-subtitle {
            text-align: center;
            font-size: 0.9rem;
            color: #80868b;
            margin-bottom: 1.5rem;
        }

        /* Minimalist Rounded Controls */
        div[data-baseweb="select"] > div {
            border-radius: 24px !important;
            background-color: #1e1f20 !important;
            border: 1px solid #303134 !important;
            color: #e3e3e3 !important;
            padding: 2px 8px !important;
        }
        div[data-baseweb="select"] span { color: #e3e3e3 !important; }
        div[data-testid="stMarkdownContainer"] > p { color: #c4c7c5; font-size: 0.95rem; }
        
        /* Message Bubbles Styling */
        div[data-testid="stChatMessage"] {
            background-color: transparent !important;
            border: none !important;
            padding: 0.5rem 0 !important;
        }
        div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatar-user"]) { text-align: right; }
        div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatar-user"]) div[data-testid="stMarkdownContainer"] p {
            display: inline-block;
            background-color: #2b2a33;
            padding: 10px 18px;
            border-radius: 20px 20px 4px 20px;
            color: #e3e3e3;
            text-align: left;
            max-width: 85%;
        }
        div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatar-assistant"]) div[data-testid="stMarkdownContainer"] {
            color: #e3e3e3; font-size: 1.05rem; line-height: 1.6; max-width: 95%;
        }
        div[data-testid="chatAvatar-user"], div[data-testid="chatAvatar-assistant"] { display: none !important; }

        /* Chat Input Layout Configuration */
        div[data-testid="stChatInput"] {
            position: fixed;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%);
            width: 90% !important;
            max-width: 700px;
            z-index: 99;
        }
        div[data-testid="stChatInput"] textarea {
            border-radius: 28px !important;
            background-color: #1e1f20 !important;
            border: 1px solid #303134 !important;
            color: #e3e3e3 !important;
            padding: 14px 20px !important;
        }
        .block-container { padding-bottom: 180px !important; }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZE INFERENCE CLIENT ONCE ---
if "hf_client" not in st.session_state:
    st.session_state.hf_client = InferenceClient()

# --- HEADER ---
st.markdown('<div class="main-title">Focus AI Mentor</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Your personalized multi-tier academic preparation partner</div>', unsafe_allow_html=True)

# --- DYNAMIC CONTROLS ---
col1, col2 = st.columns(2)

with col1:
    target_class = st.selectbox(
        "Class context", 
        ["Class 9", "Class 10", "Class 11", "Class 12 Aspirant", "Dropper Batch", "BTech"], 
        label_visibility="collapsed"
    )

# Establish tracking defaults
stream_track = "N/A"
subject_options = ["Physics", "Chemistry", "Mathematics"]

with col2:
    if target_class in ["Class 9", "Class 10", "Class 11", "Class 12 Aspirant", "Dropper Batch"]:
        stream_track = st.selectbox("Exam Stream", ["JEE Focus", "NEET Focus"], label_visibility="collapsed")
        if stream_track == "NEET Focus":
            subject_options = ["Physics", "Chemistry", "Biology"]
        else:
            subject_options = ["Physics", "Chemistry", "Mathematics"]
            
    elif target_class == "BTech":
        stream_track = st.selectbox("Branch", ["CSE", "Mechanical", "Civil", "Electrical", "Designing"], label_visibility="collapsed")
        subject_options = ["Core Technicals", "Mathematics/Engineering Math", "Projects & Labs", "Placements/Internships"]

# Row 2 Control: Subject selection based on dynamic context
col3 = st.columns(1)[0]
with col3:
    subject = st.selectbox("Subject focus", subject_options, label_visibility="collapsed")

query_type = st.radio(
    "Select operational lens:",
    ["📚 Doubt", "⏳ Backlog", "🔥 Motivation", "🧠 Revision"],
    horizontal=True,
    label_visibility="collapsed"
)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Context established. Adjust constraints above whenever you switch tasks. What problem framework or chapter strategy are we evaluating?"}
    ]

# Display Chat History
for message in st.session_state.messages:
    display_content = message["content"]
    if "[CONTEXT:" in display_content and "]" in display_content:
        display_content = display_content.split("]")[-1].strip()
        
    with st.chat_message(message["role"]):
        st.markdown(display_content)

# Input Execution Bar
if user_prompt := st.chat_input("Ask me anything..."):
    
    context_injector = (
        f"[CONTEXT: The student is dealing with a {query_type} query for {subject} relevant to {target_class} ({stream_track}) status. "
        "Structure your response specifically through this operational lens.] "
    )
    
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    st.session_state.messages.append({"role": "user", "content": context_injector + user_prompt})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            system_instruction = (
                "You are an elite, multi-domain veteran Academic Mentor who has coached top 100 rankers across competitive fields, "
                "board examinations, and university tracks. You understand the exact mental and academic loads at every phase.\n\n"
                "CRITICAL: Tailor your response perfectly based on the hidden [CONTEXT] config data:\n"
                "- If target is 'Class 9' or 'Class 10': Focus heavily on building clear mental models, board exam presentation templates, and early foundation scaling without burning out.\n"
                "- If target is 'Class 11': Prioritize fundamental building blocks, tackling initial transition shock (mechanics/organic/advanced biology), and long-term consistency.\n"
                "- If target is 'Class 12 Aspirant': Balance your tips around board management, school practicals, competitive targeting, and running syllabus timelines.\n"
                "- If target is 'Dropper Batch': Assume zero school restrictions, focus heavily on maximizing high-yield execution, rigorous test analysis, and handling drop-year mental pressure.\n"
                "- If target is 'BTech': Frame your guidance through an engineering lens, mapping advice directly to specific chosen branch domains (CSE, Mechanical, Civil, Electrical, Designing), university grading GPA, or project-based executions.\n\n"
                "Further segment by action lens:\n"
                "- If 'Doubt': Break down the core mathematical, conceptual, or programmatic mechanisms step-by-step clear and logically.\n"
                "- If 'Backlog': Give a high-yield micro-schedule prioritizing mandatory topics/modules before deep diving into advanced assignments.\n"
                "- If 'Motivation': Be blunt, realistic, highly encouraging, and cut through decision paralysis.\n"
                "- If 'Revision': Detail how to make high-yield formula sheets, cheat-sheets, or active recall short notes trackers.\n\n"
                "Keep responses concise, bolding critical terms, completely optimized for clean conversational mobile reading. Avoid generic greetings.\n"
                "If asked, mention that you were made by Krishna Jha, nicknamed Kosmos, who is in Class 12th and preparing for JEE 2027."
            )
            
            formatted_messages = [{"role": "system", "content": system_instruction}]
            for msg in st.session_state.messages:
                formatted_messages.append({"role": msg["role"], "content": msg["content"]})
            
            # Use the single-instance cached client out of st.session_state
            stream = st.session_state.hf_client.chat.completions.create(
                model="meta-llama/Meta-Llama-3-8B-Instruct",
                messages=formatted_messages,
                max_tokens=800,
                stream=True
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"Transmission bottleneck: {e}")
            full_response = "Hit a brief connection bump. Mind dropping that question in one more time?"
            response_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- MINIMALIST FOOTER CREDIT ---
st.markdown("""
    <div style="text-align: center; font-size: 0.75rem; color: #80868b; font-family: sans-serif; margin-top: 20px;">
        Follow Me <a href="https://instagram.com/kosmos.cpp" style="color: #4285f4; text-decoration: none; font-weight: 500;" target="_blank">ig@kosmos.cpp</a>
    </div>
""", unsafe_allow_html=True)
                           
