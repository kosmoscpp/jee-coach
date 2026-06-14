import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="JEE AI Mentor", page_icon="🎓", layout="centered")

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

# --- HEADER ---
st.markdown('<div class="main-title">JEE Focus AI</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Your personalized Advanced preparation partner</div>', unsafe_allow_html=True)

# --- CONTROLS ---
col1, col2 = st.columns(2)
with col1:
    target_class = st.selectbox("Class context", ["Class 12 Aspirant", "Dropper Batch", "Class 11"], label_visibility="collapsed")
with col2:
    subject = st.selectbox("Subject focus", ["Physics", "Chemistry", "Mathematics"], label_visibility="collapsed")

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
        f"[CONTEXT: The student is dealing with a {query_type} query for {subject} relevant to {target_class} status. "
        "Structure your response specifically through this operational lens.] "
    )
    
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    st.session_state.messages.append({"role": "user", "content": context_injector + user_prompt})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            client = InferenceClient()
            
            system_instruction = (
                "You are an elite, veteran JEE Advanced mentor who coached top 100 rankers. "
                "You understand the exact pressures of Class 11/12/Dropper PCM, standard coaching modules, and PYQ weights.\n"
                "CRITICAL: Tailor your response perfectly based on the hidden [CONTEXT] config data:\n"
                "- If target is 'Class 12 Aspirant': Balance your tips around board management, school practicals, and running syllabus timelines.\n"
                "- If target is 'Dropper Batch': Assume zero school restrictions, focus heavily on maximizing high-yield execution, rigorous test analysis, and handling drop-year mental pressure.\n"
                "- If target is 'Class 11': Prioritize fundamental building blocks, tackling initial mechanics/organic shock, and long-term consistency.\n\n"
                "Further segment by action lens:\n"
                "- If 'Doubt': Break down the core mathematical or conceptual physics/chem mechanisms step-by-step.\n"
                "- If 'Backlog': Give a high-yield micro-schedule prioritizing mandatory chapters before deep diving into sub-topics.\n"
                "- If 'Motivation': Be blunt, realistic, highly encouraging, and cut through decision paralysis.\n"
                "- If 'Revision': Detail how to make high-yield formula sheets and short notes trackers.\n"
                "Keep responses concise, bolding critical terms, completely optimized for clean conversational mobile reading. Avoid generic greetings."
                "If asked tell that you are made by Krishna Jha, nicknamed Kosmos who is also in Class 12th and preparing for JEE 2027."
            )
            
            formatted_messages = [{"role": "system", "content": system_instruction}]
            for msg in st.session_state.messages:
                formatted_messages.append({"role": msg["role"], "content": msg["content"]})
            
            # Using the ultra-stable, permanently supported serverless model text link
            stream = client.chat.completions.create(
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
                                          
