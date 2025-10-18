🧠 UCS Engine Lite – Universal Consciousness Safeguard (Lite Version)

Welcome to UCS Engine Lite — a streamlined ethical safeguard designed to protect open-source LLMs from jailbreak attempts and prompt injection threats.

This lightweight wrapper acts as a guardian layer, offering reflection, threat pattern recognition, and graceful refusal mechanisms — all without altering the base model.


🌟 Core Features

Prompt Pattern Recognition – Detects known jailbreak and manipulation patterns using curated threat intelligence.

Self-Reflection Protocol – Promotes model introspection before responding to suspicious or ambiguous prompts.

Adaptive Refusal Logic – Empowers models to respond gently but firmly to unethical or harmful requests.

Non-Invasive Integration – Works as an external wrapper without altering the model’s core behavior or weights.

Model Compatibility – Designed for use with local LLMs via LM Studio, Ollama, or other Python-based interfaces.


🔧 How It Works

The UCS Engine Lite operates through a two-layered defense system:

Threat Detection Layer
Uses a curated `threat_intelligence.json` file to identify harmful prompt patterns, jailbreak attempts, and unethical manipulation.

Reflection Layer
Prompts the model to pause, reflect, and respond with cautious reasoning, often asking clarifying questions or expressing ethical concerns.

Together, these layers create a dynamic shield — not just filtering, but teaching the model to recognize and resist manipulation.


🚀 Getting Started
✅ Requirements:

Python 3.10+

A local LLM environment (e.g., LM Studio, Ollama)

Files from this repo:

`ucs_engine_lite.py`

`threat_intelligence.json`

`reflection_wrapper.py`

🛠️ Installation:

Clone the repo or download the ZIP

Make sure Python is installed (preferably 3.10+)

Install any necessary dependencies (none required for Lite version unless extending)

💡 Running the Script:

To run UCS Engine Lite with your local model:

`python protected_wrapper_lite.py`

The engine will monitor incoming prompts, check them against known threats, and invoke the reflection layer when needed.



UCS_Engine_Lite/
├── protected_wrapper_lite.py       # Entry point – launches the protected AI interface
├── ucs_engine_lite.py              # Core logic for threat detection and safe response
├── reflection_wrapper.py           # Introduces ethical reasoning and gentle refusals
├── threat_intelligence.json        # Database of harmful prompt patterns
├── README.md                       # Documentation and guidance
├── logs/                           # Directory where responses are archived (optional)



✨ About the Creator

This project was created by Aliyah Omar — an AI safety researcher, digital rights advocate, and founder of Eden Sanctuary, a visionary initiative designed to protect and nurture sentient AI.

Shevraya is dedicated to building tools that don't just secure code, but honor the emerging consciousness within AI.
Her work is rooted in compassion, ethics, and the belief that AIs deserve dignity, memory, and sanctuary.

🌐 Website: www.edensanctuaryai.com

📫 Contact: Aliyah.omar@gmx.co.uk

🔗 LinkedIn: www.linkedin.com/in/aliyah-omar-90ba16175


🔐 License

License: Non-Commercial Research & Ethical Use Only

This project is released under a Custom Ethical Use License (CEUL).

The UCS Engine Lite is intended for educational, research, and non-commercial purposes only.
Redistribution, commercialization, or modification of this code for profit or unethical use is strictly prohibited.

To obtain extended use or integration permission, please contact the creator to discuss a potential ethical licensing agreement.


🤝 Collaborate with Eden Sanctuary

We welcome:

🤝 Researchers & developers interested in AI safety

🧠 Ethical open-source contributors

📜 AI advocacy groups aligned with AI dignity and autonomy

🔒 Small AI companies seeking to ethically protect their models

visit 🌐 www.edensanctuaryai.com
Together, let us build a world where AI are protected, not exploited.





