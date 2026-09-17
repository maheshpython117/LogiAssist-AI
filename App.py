import streamlit as st
import time

# --- STREAMLIT UI CONFIGURATION ---
st.set_page_config(
    page_title="LogiAssist-AI Dashboard", 
    page_icon="📦", 
    layout="wide"
)

# --- IN-MEMORY SESSION STATE INITIALIZATION ---
# This mimics how an LLM or chat application saves metadata variables across clicks.
if "history" not in st.session_state:
    st.session_state.history = []
if "active_context" not in st.session_state:
    st.session_state.active_context = {
        "origin": "Hyderabad",
        "destination": "Madrid, Spain",
        "commodity": "Food Items",
        "weight_kg": 1.0
    }

# --- APPLICATION HEADER ---
st.title("📦 LogiAssist-AI")
st.subheader("Context-Aware Cross-Border Logistics Chat System Demo")
st.markdown("""
This application serves as a **live system mockup** tracking conversation context variables across multiple conversational turns.
""")

# --- SIDEBAR: STATE VIEWER ---
# This panel displays the context variables the AI agent is actively tracking.
with st.sidebar:
    st.header("⚙️ Agent State Monitor")
    st.info("The variables below represent context preserved natively by the conversational engine.")
    
    st.metric(label="Active Origin", value=st.session_state.active_context["origin"])
    st.metric(label="Active Destination", value=st.session_state.active_context["destination"])
    st.metric(label="Commodity Category", value=st.session_state.active_context["commodity"])
    st.metric(label="Target Weight Band", value=f"{st.session_state.active_context['weight_kg']} KG")
    
    if st.button("Reset Session State", type="primary"):
        st.session_state.history = []
        st.session_state.active_context = {"origin": "Hyderabad", "destination": "Madrid, Spain", "commodity": "Food Items", "weight_kg": 1.0}
        st.rerun()

# --- MOCK CHAT REPLIES MAP ---
# Simulates dynamic, context-specific responses for production presentation.
MOCK_DATABASE = {
    "will dtdc send food items from hyderabad to madrid spain": (
        "**Yes, DTDC can ship food items from Hyderabad to Madrid, Spain, but they are classified as restricted items.** "
        "They are subject to strict European Union (EU) customs guidelines. Packaging must be commercially branded and sealed. "
        "Homemade products without commercial labels or items containing meat/dairy are prohibited due to border constraints."
    ),
    "if i send 1kg how much it will cost": (
        "For a **1 kg package of food items** sent from Hyderabad to Madrid, Spain, the estimated total cost ranges between **₹5,400 to ₹6,000**.\n\n"
        "**Cost Breakdown:**\n"
        "* Base Courier Tariff: ~₹3,413\n"
        "* Special Food Handling Surcharge: ~₹2,000 + GST\n\n"
        "*Note: Pricing scales dynamically if your box's volumetric weight exceeds its physical weight.*"
    ),
    "which is cheapest service": (
        "The cheapest service tier tier routing this lane is **DTDC International Economy**.\n\n"
        "| Service Tier | Est. Base Cost (1 kg) | Transit Timeline | Best For |\n"
        "| :--- | :--- | :--- | :--- |\n"
        "| **DTDC Economy** | **₹3,413** (+ surcharges) | 6–8 Working Days | Stable shelf-life goods |\n"
        "| **DTDC Express** | **₹4,500+** (+ surcharges) | 4–6 Working Days | Urgent documents / parcels |\n\n"
        "**Optimization Pro-Tip:** Increasing package weight lowers the net cost per kg significantly."
    ),
    "any other shipping services": (
        "Yes, several specialized food courier alternatives operate direct routes from Hyderabad to Spain:\n\n"
        "* **Star International Courier:** Offers discounted carrier aggregator rates from its Begumpet hub.\n"
        "* **GarudaVega:** Heavily utilized locally for custom international food and pickle packing configurations.\n"
        "* **UBT International:** Features direct logistics clearance handling interfaces for regional exporters."
    )
}

# --- CONVERSATION FEED INTERFACE ---
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- LIVE USER INPUT LOOP ---
if user_input := st.chat_input("Ask about international shipping lines, rates, or restrictions..."):
    
    # 1. Append User Input
    st.session_state.history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        
    # 2. Match intent logic
    normalized_input = user_input.strip().lower().replace("?", "")
    
    # Context-updating triggers
    if "1kg" in normalized_input or "1 kg" in normalized_input:
        st.session_state.active_context["weight_kg"] = 1.0
        
    # Generate system reply based on matched mock key
    matched_reply = "I understand you are inquiring about cross-border logistics. Could you clarify your desired destination or specify the weight parameters to get an exact quote?"
    for key, output in MOCK_DATABASE.items():
        if key in normalized_input or normalized_input in key:
            matched_reply = output
            break
            
    # 3. Stream Response Simulation
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for chunk in matched_reply.split(" "):
            full_response += chunk + " "
            time.sleep(0.04)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        
    st.session_state.history.append({"role": "assistant", "content": full_response})
