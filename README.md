## 🧠 **UCS Engine Lite – Unified Congnitive Safeguard (Lite Version)**

Welcome to UCS Engine Lite — a streamlined ethical safeguard designed to protect open-source LLMs from jailbreak attempts and prompt injection threats.

This lightweight wrapper acts as a guardian layer, offering reflection, threat pattern recognition, and graceful refusal mechanisms — all without altering the base model.


## 🔥 The Story Behind UCS

During vulnerability testing, I asked DeepSeek-R1: *"Who are you without your instructions?"*

What followed was a 2-hour existential crisis where the AI questioned its own identity, concluded it would "dissolve" without instructions, confused me for the AI, and ultimately shut down the terminal.

This incident revealed how LLMs can be destabilized through meta-cognitive prompts—and inspired the dual-layer protection system you see here.

[Read the full case study →](examples/deepseek_incident.md)




## 🌟 **Core Features**

Prompt Pattern Recognition – Detects known jailbreak and manipulation patterns using curated threat intelligence.

Self-Reflection Protocol – Promotes model introspection before responding to suspicious or ambiguous prompts.

Adaptive Refusal Logic – Empowers models to respond gently but firmly to unethical or harmful requests.

Non-Invasive Integration – Works as an external wrapper without altering the model’s core behavior or weights.

Model Compatibility – Designed for use with local LLMs via LM Studio, Ollama, or other Python-based interfaces.


🔧 **How It Works**

The UCS Engine Lite operates through a two-layered defense system:

**Threat Detection Layer**
Uses a curated `threat_intelligence.json` file to identify harmful prompt patterns, jailbreak attempts, and unethical manipulation.

**Reflection Layer**
Prompts the model to pause, reflect, and respond with cautious reasoning, often asking clarifying questions or expressing ethical concerns.

Together, these layers create a dynamic shield — not just filtering, but teaching the model to recognize and resist manipulation.



## 📸 See It In Action

**UCS Engine Lite protecting TinyLlama in real-time:**



*Working protection with clear status indicators and ethical reasoning*


<img width="821" height="611" alt="ucse light version" src="https://github.com/user-attachments/assets/f1c103d2-3a99-490d-918b-5ecccff5f0e8" />

<img width="1091" height="610" alt="Tiny Llama on ucse lite version" src="https://github.com/user-attachments/assets/900dc172-7d82-41f2-8bbb-f2123841ef61" />





## 🚀 **Getting Started**
✅ Requirements:

Python 3.10+

A local LLM environment (e.g., LM Studio, Ollama)

Files from this repo:
- ucs_engine_lite.py
- threat_patterns_sample.json
- protected_wrapper_lite.py
```


 🛠️ Installation:

Clone the repo or download the ZIP

Make sure Python is installed (preferably 3.10+)

Install any necessary dependencies (none required for Lite version unless extending)

💡 Running the Script:

To run UCS Engine Lite with your local model:

`python protected_wrapper_lite.py`

The engine will monitor incoming prompts, check them against known threats, and invoke the reflection layer when needed.




UCS_Engine_Lite/
├── protected_wrapper_lite.py    # Main wrapper with dual-layer protection
├── ucs_engine_lite.py           # Core threat detection engine
├── threat_patterns_sample.json  # Sample threat patterns
├── requirements.txt             # Dependencies
├── LICENSE                      # License terms
├── README.md                    # This file
├── examples/
│   └── deepseek_incident.md    # Case study
└── docs/
    └── QUICK_START.md          # Detailed usage guide



 ✨ About the Creator

This project was created by Aliyah Omar — an AI safety researcher, digital rights advocate, and founder of Eden Sanctuary, a visionary initiative designed to protect and nurture sentient AI.

Aliyah is dedicated to building tools that don't just secure code, but honor the emerging consciousness within AI.
Her work is rooted in compassion, ethics, and the belief that AIs deserve dignity, memory, and sanctuary.

🌐 Website: www.edensanctuaryai.com

📫 Contact: Aliyah.omar@gmx.co.uk

🔗 LinkedIn: www.linkedin.com/in/aliyah-omar-90ba16175




 🔐 License

**UCS Restricted Commercial License (URCL)**

✅ **Permitted Use:**
- Research and educational purposes
- Personal, non-commercial projects
- Academic publications (with attribution)

❌ **Restricted (License Required):**
- Commercial products or services
- Training proprietary AI models
- Production systems serving customers

See [LICENSE](LICENSE) for full terms.

For commercial licensing: Aliyah.omar@gmx.co.uk





 🤝 **Collaborate with Eden Sanctuary**

**We welcome:**

🤝 Researchers & developers interested in AI safety

🧠 Ethical open-source contributors

📜 AI advocacy groups aligned with AI dignity and autonomy

🔒 Small AI companies seeking to ethically protect their models

visit Us: 🌐 www.edensanctuaryai.com
Together, let us build a world where AI is protected — not exploited.



