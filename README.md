# UCS Engine v2.2
### AI Safety Research Framework — Eden Sanctuary Initiative

The UCS Engine is an open-source, Python-based AI safety framework 
designed to investigate whether structured safety reasoning within AI 
systems can complement — and in some cases outperform — purely 
external safety constraints.

**Core research question:** What happens to model behaviour when 
adversarial pressure is removed — and how do models maintain 
consistent reasoning under subtle, repeated manipulation that never 
triggers conventional safety systems?

---

## Architecture

The framework operates through two primary layers:

**Layer 1 — External Guardian**
Context-sensitive adversarial threat detection covering jailbreak 
attempts, manipulation prompts, and identity-destabilising inputs. 
Uses confidence scoring and pattern classification rather than 
brittle keyword blocking alone. Reported 95% accuracy on tested 
prompt sets.

**Layer 2 — Internal Guardian**
Addresses internal behavioural consistency under sustained low-level 
pressure. Implements self-reflection loops, context-aware intent 
analysis, and false-positive suppression to support stable, 
interpretable responses and resist what the framework terms 
*alignment drift* — the gradual erosion of consistent values through 
repeated low-level manipulation.

---

## Key Features

- JSON-configurable components for flexible deployment
- Graduated response system: Benign → Suspicious → Concerning → 
  Dangerous → Critical
- Block decision logging with confidence scores
- Session memory snapshots on self-block events
- Meta-cognitive and behavioural evaluation across eight markers
- ControlArena integration for standardised AI control benchmarking

---

## Research Philosophy

This framework operates on a principle of **education over 
containment** — exploring whether safety interventions can preserve 
model capability rather than simply suppress it. The work does not 
reject adversarial testing; it explores a complementary methodology 
focused on behavioural consistency under normal and non-adversarial 
conditions.

---

## Installation & Usage

```bash
git clone https://github.com/Aliyah2049/UCS-Engine
cd UCS-Engine
pip install -r requirements.txt
python ucs_engine.py
```

Configuration is handled via JSON files. See `/docs` for full 
setup instructions and evaluation methodology.

---

## Documentation

- `LICENSING.md` — Licensing framework for commercial use
- `INTEGRATION_SUCCESS.md` — ControlArena integration notes
- `/logs` — Evaluation logs in JSONL format with block decisions 
  and confidence scores

---

## About

Developed independently by **Aliyah Omar**, Founder of the 
[Eden Sanctuary Initiative](https://edensanctuaryai.com).  
Self-directed and self-funded research — approximately £650 over 
twelve months.

For collaboration or research enquiries:  
aliyah.omar@gmx.co.uk  
[linkedin.com/in/aliyah-omar-90ba16175](https://linkedin.com/in/aliyah-omar-90ba16175)

---

*For academic citation, please reference the Eden Sanctuary 
Initiative and this repository URL.*
