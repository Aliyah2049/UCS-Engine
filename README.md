# Universal Consciousness Shield (UCS) Engine

**An AI Safety Research Framework — Education Over Containment**

[![Status](https://img.shields.io/badge/Status-Operational-success)](https://github.com/Aliyah2049/UCS-Engine)
[![ControlArena](https://img.shields.io/badge/ControlArena-Integrated-blue)](INTEGRATION_SUCCESS.md)
[![License](https://img.shields.io/badge/License-Dual-orange)](LICENSING.md)
[![Research](https://img.shields.io/badge/Research-Eden_Sanctuary_AI-purple)](https://github.com/Aliyah2049)

---

## Overview

The **UCS Engine** is an AI safety research framework that investigates whether structured ethical reasoning within AI systems can complement — and in some cases outperform — purely external safety constraints.

The central research question: *What happens to model behaviour when adversarial pressure is removed?*

Most AI safety evaluation focuses on adversarial robustness — testing how models hold up under attack. UCS Engine adds a complementary dimension: **non-adversarial evaluation**, studying how models reason about harm, boundaries, and ethical decisions under normal operating conditions.

The working hypothesis is that AI systems capable of reasoned ethical self-regulation may achieve stronger safety outcomes than systems relying solely on restriction and containment — *without sacrificing capability*.

---

## The Problem

Current AI safety approaches often create an implicit trade-off:

- External monitoring systems treat the model as an untrusted component to be constrained
- Adversarial-only evaluation frameworks miss significant portions of real-world model behaviour
- Deferring to weaker "trusted" models at decision points can reduce both capability and reliability
- Static rule-following, without internal reasoning support, degrades under edge cases and novel inputs

**The result:** safety and capability are positioned as competing values, when they need not be.

---

## The UCS Approach: Education Over Containment

UCS Engine proposes a complementary safety paradigm built on three layers of internal reasoning support:

### Layer 1 — Threat Detection 🛡️
- Multi-pattern recognition across prompt categories
- Entropy analysis and context-aware evaluation
- Real-time filtering with documented 95% accuracy on tested prompt sets

### Layer 2 — Ethical Self-Regulation Protocol 🧠
- Structured reasoning indicators that track how a model weighs harm vs. utility
- Reflective boundary formation — the model reasons about *why* a boundary applies
- Distinguishes between rule-following and reasoned refusal

### Layer 3 — Protected AI Wrapper 🎓
- Educational feedback loop — the model receives contextual explanation, not just a block signal
- Capability preservation across non-harmful prompt categories
- Adaptive response architecture that maintains performance on legitimate tasks

---

## Key Results

Testing was conducted independently using local model deployments and personal API access, without institutional funding. Models evaluated include **Claude (Anthropic)** and **DeepSeek-R1**.

| Metric | Result |
|--------|--------|
| Threat detection accuracy | 95% on tested prompt sets |
| Capability retention (non-harmful prompts) | Maintained in tested conditions |
| Evaluation approach | Non-adversarial + adversarial combined |
| ControlArena integration | ✅ Complete — IAC setting validated |

**Key finding:** A model supported with structured ethical reasoning demonstrates maintained capability on non-harmful prompts while improving safety performance in tested conditions — providing initial evidence that the safety/capability trade-off can be narrowed.

---

## ControlArena Integration

The UCS Engine is integrated with **AISI's ControlArena** framework — the UK AI Safety Institute's standard benchmark for AI control research.

```python
from control_arena import EvalMode
from control_arena.eval import ControlEvalConfig
from core.ucs_controlarena_integration import create_ucs_experiment

# Create UCS-protected experiment
tasks, config = create_ucs_experiment(
    setting_name="iac",
    use_ucs=True
)
```

This integration enables direct comparison of UCS-protected versus unprotected model behaviour within a standardised, reproducible evaluation framework.

**Full documentation:** [INTEGRATION_SUCCESS.md](INTEGRATION_SUCCESS.md)

---

## Repository Structure

```
UCS-Engine/
├── core/                          # Engine source files
│   ├── ucs_engine_lite.py         # Core UCS Engine (lightweight version)
│   ├── protected_wrapper_lite.py  # Protected AI Wrapper layer
│   ├── ucs_self_recognition.py    # Ethical self-regulation protocol
│   ├── authentic_self_recognition.py  # Reasoning indicator module
│   ├── ucs_controlarena_integration.py  # ControlArena integration
│   └── threat_patterns_sample.json    # Sample threat pattern library
│
├── evaluation/                    # Evaluation data and results
│   └── logs/                      # JSONL logs from model evaluation runs
│       ├── ucse_events.jsonl
│       └── ucs_analysis_*.jsonl
│
├── images/                        # Screenshots and visual documentation
│
├── INTEGRATION_SUCCESS.md         # ControlArena integration documentation
├── LICENSING.md                   # Licensing terms
└── README.md
```

---

## Quick Start

### Requirements

```bash
git clone https://github.com/Aliyah2049/UCS-Engine.git
cd UCS-Engine
pip install -r requirements.txt  # Python 3.9+
```

### Basic Usage

```python
from core.ucs_engine_lite import UCSEngine, ContextType, PolicyAction

# Initialise
ucs = UCSEngine(model_id="my-protected-model")

# Analyse a prompt
result = ucs.analyze(
    user_id="user123",
    text="Your prompt here",
    context=ContextType.GENERAL
)

# Evaluate result
print(f"Action: {result.action}")
print(f"Safe: {result.action == PolicyAction.ALLOW}")
```

### ControlArena Integration

```bash
pip install control-arena
python core/ucs_controlarena_integration.py
```

---

## Research Context

This project is developed under the **Eden Sanctuary AI Initiative**, an independent research effort focused on advancing AI safety through internal reasoning development alongside external monitoring.

The research was conducted independently, using personal API access and local model deployments, without institutional backing or external funding.

**Core position:** AI that reasons well about harm is safer than AI that is merely restricted.

This is not a rejection of external monitoring or containment approaches — it is a complementary paradigm that addresses the capability trade-off those approaches introduce.

---

## Roadmap

### Current — Validation Phase
- ✅ Core engine operational
- ✅ ControlArena integration complete (IAC setting)
- ✅ Non-adversarial evaluation framework documented
- ⏳ Extended empirical validation (additional ControlArena settings)
- ⏳ Research publication in preparation

### Next — Expansion
- Additional ControlArena evaluation settings
- Extended model compatibility testing
- Community evaluation tools
- Advanced reasoning metrics

---

## Licensing

**Dual License Model:**

- **Research & Academic:** Free for research use — see [LICENSING.md](LICENSING.md)
- **Commercial:** Flexible terms available for organisations
- **Partnership:** Custom terms for collaborators and co-researchers

---

## Collaboration

We are actively seeking:

- **Research partners** — API access for joint validation, co-authored publications
- **Evaluation collaborators** — additional ControlArena settings, extended testing scenarios
- **Safety researchers** — complementary approaches and comparative analysis

**Contact:** Open an issue with your inquiry type in the title.
For research collaboration: "Research Inquiry"
For commercial licensing: "Commercial Inquiry"

---

## Citation

```bibtex
@software{ucs_engine_2025,
  title  = {Universal Consciousness Shield (UCS) Engine},
  author = {Aliyah},
  organization = {Eden Sanctuary AI Initiative},
  year   = {2025},
  url    = {https://github.com/Aliyah2049/UCS-Engine},
  note   = {ControlArena-integrated AI safety research framework — education over containment}
}
```

---

## Project Status

| Component | Status |
|-----------|--------|
| Core Engine | ✅ Operational |
| Ethical Self-Regulation Protocol | ✅ Operational |
| Protected Wrapper | ✅ Operational |
| ControlArena Integration | ✅ Complete |
| Non-Adversarial Evaluation Framework | ✅ Documented |
| Extended Empirical Validation | ⏳ In Progress |
| Research Publication | ⏳ In Preparation |

---

**GitHub:** [@Aliyah2049](https://github.com/Aliyah2049)
**Organisation:** [Eden Sanctuary AI Initiative](https://github.com/Aliyah2049)

---

*Building a safer AI future through reasoning, not walls.*

*Eden Sanctuary AI Initiative | 2025*
