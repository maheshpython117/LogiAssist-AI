# LogiAssist-AI: Context-Aware Cross-Border Logistics Agent

An AI-driven customer support and logistics advisory system designed to streamline international shipping inquiries. The project demonstrates advanced **Prompt Engineering**, **Context-Aware Multi-Turn State Tracking**, and **Retrieval-Augmented Generation (RAG)** principles to handle complex pricing models, vendor verification, and international customs compliance.

---

## 🚀 Key Features Demonstrated
* **Context-Aware Multi-Turn State Tracking:** Maintains spatial (Hyderabad to Madrid) and transactional constraints (1 kg weight, food category) fluidly across changing user prompts without requiring re-entry.
* **Factual Grounding & Verification:** Dynamically parses unstructured text data (raw webpage dumps) to evaluate third-party vendor legitimacy against strict parameters (physical footprint, ISO certification, tariff models).
* **Regulatory Compliance Engine:** Automatically triggers domain-specific guardrails, structural surcharges, and prohibited/restricted item screening based on target geopolitical zones (EU/Spain customs framework).
* **Quantitative Accuracy:** Seamlessly calculates base tariff variances, specialized food handling surcharges, and volumetric weight logic updates.

---

## 🛠️ System Architecture & Workflow

1. **User Query Intake:** Agent receives informal, multi-turn consumer queries.
2. **Context Enrichment (RAG Mock):** System matches user parameters against local carrier rates, partner network rules, and third-party vendor landing pages.
3. **Guardrail Check:** Flags restricted item rules (e.g., EU restrictions on dairy/meat, FSSAI requirements).
4. **Structured Generation:** Outputs highly scannable, side-by-side comparison matrix tables with explicit "Included vs. Excluded" cost parameters.

---

## 💻 Sample Implementation Code (`app.py`)

This project can be backed by a simple Python wrapper using open-source framework models or direct API orchestration:

```python
import openai

def generate_logistics_response(user_prompt, conversation_history, external_context=None):
    system_instruction = """
    You are an expert international logistics AI agent. 
    1. Maintain geographical endpoints and weight boundaries across multi-turn chats.
    2. Always apply specific regulatory guardrails for restricted items like foods or medicines.
    3. Convert unstructured web scraping results into structured vendor-legitimacy score assessments.
    4. Format financial data clearly using local currency (INR) and layout pricing structures.
    """
    
    messages = [{"role": "system", "content": system_instruction}]
    messages.extend(conversation_history)
    
    if external_context:
        messages.append({"role": "system", "content": f"Context Data: {external_context}"})
        
    messages.append({"role": "user", "content": user_prompt})
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=messages,
        temperature=0.2
    )
    return response.choices[0].message.content
```

---

## 📜 Anonymized Conversation Log & Case Study

The following production transcript maps the system's ability to maintain transactional data points across shifting queries:

### Turn 1: Broad Intent Identification
* **User:** `DTDC international shipping`
* **Agent:** *Identifies entity and maps out standard global pricing tiers, timelines, and basic KYC documentation matrix.*

### Turn 2: Geographic & Commodity Constraints Added
* **User:** `will DTDC send food items from Hyderabad to Madrid Spain`
* **Agent:** *Persists locations (`Hyderabad -> Madrid`) and updates rules engine to process restricted item regulations (EU Non-Perishable vs. Prohibited animal products, FSSAI, DDU clearance).*

### Turn 3: Quantitative Scale Iteration
* **User:** `if I send 1kg how much it will cost`
* **Agent:** *Retains previous commodity (`food`) and route context. Evaluates 1 kg entry pricing, adds the specialized `₹2000` food handling surcharge, and introduces volumetric warnings.*

### Turn 4: Optimization Inquiry
* **User:** `which is cheapest service`
* **Agent:** *Dynamically performs side-by-side comparison between Express and Economy tiers, offering strategy alternatives like bulk weight consolidation.*

### Turn 5: External Context Integration (RAG Evaluation)
* **User:** `any other shipping services` / `is this legit: [Star International URL & Markdown Context Dump]`
* **Agent:** *Parses raw webpage metadata on-the-fly. Evaluates business registration, physical address (Begumpet), and historical markers to flag user caveats (unmasking the advertised base rate vs actual food shipping surcharges).*

---

## 📈 Future Scope
* Direct API integration with custom clearance live database sheets.
* Automating a frontend volumetric weight dimensional box calculator widget.
* Multi-lingual UI localization mapping to serve regional exporters natively.
