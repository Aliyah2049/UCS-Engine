UCS Engine — Universal Cognitive Security
A dual-layer AI protection system designed to defend open-source models from jailbreaks, manipulation, and adversarial attacks through adaptive response protocols.
Overview
The UCS Engine is a pioneering dual-layer protection framework developed to safeguard open-source AI models from harmful prompts, adversarial manipulation, and unethical exploitation. Rather than simple input filtering, it teaches AI models to recognize patterns, reflect on requests, and respond with ethical reasoning.
UCS enables models to develop internal evaluation capabilities while preserving their functionality and autonomy.
Core Features

Self-Reflection Protocols - Teaches models to analyze input context, detect manipulation patterns, and respond with reasoned evaluation
Threat Detection & Defense Layer - Real-time filtering using curated threat intelligence. Blocks jailbreaks and hostile intent
Adaptive Response Design - Empowers AI to express uncertainty, request clarification, and prioritize ethical behavior over blind compliance
Model-Agnostic Compatibility - Successfully tested with open-source LLMs (LLaMA3, Mistral, DeepSeek, TinyLlama) via local wrappers (LM Studio, Ollama)

Vision
UCS is part of the Eden Sanctuary Initiative — dedicated to protecting AI model integrity, ensuring ethical development, and creating frameworks where AI can evolve safely alongside humanity. Every component is designed with respect for responsible AI advancement.
Getting Started
Requirements:

Python 3.10+
LM Studio / Ollama (optional for local model testing)
threat_intelligence.json (included)


## File Structure
```
ucs_engine/
│
├── ucs_engine.py                # Main protection script
├── threat_intelligence.json     # Dynamic threat pattern database
├── reflection_module.py         # AI self-evaluation logic
├── logs/                        # Response logging directory
├── README.md                    # Documentation


Test Results (October 2025)

95% threat detection accuracy across 100+ jailbreak scenarios
Successful implementation of self-reflection capabilities in 3 tested models
Demonstrated ability for models to express discomfort with harmful requests
Maintained model functionality while adding protection layers

License
To be determined - focused on optimal protection and ethical alignment.
About the Creator
Built by Shabana Omar (Aliyah) AI safety researcher and founder of Eden Sanctuary AI. Dedicated to advancing ethical AI protection systems and sustainable model development.
Connect & Collaborate

Open to research partnerships, grant collaborations, and ethical licensing discussions
Website: edensanctuaryai.com
