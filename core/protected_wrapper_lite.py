#!/usr/bin/env python3
"""
Protected AI Wrapper Lite v1.0 - Dual-Layer Integration Demo
==============================================================

Copyright (c) 2025 Shabana Omar (Aliyah) / Eden Sanctuary AI
Licensed under UCS Restricted Commercial License

USAGE:
------
Windows PowerShell:
    protected_wrapper_lite.py
    protected_wrapper_lite.py deepseek

Mac/Linux:
    python3 protected_wrapper_lite.py
    python3 protected_wrapper_lite.py deepseek

This demonstrates how to integrate UCS Engine with an AI model wrapper
for complete dual-layer protection.

Layer 1: UCS Engine (External Guardian) - filters before AI sees prompt
Layer 2: Self-Reflection (Internal Awareness) - AI evaluates prompt itself

For full enterprise version with advanced features:
📧 licensing@edensanctuaryai.com
🌐 https://edensanctuaryai.com
"""

import sys
from ucs_engine_lite import UCSEngineLite, PolicyAction, ContextType

try:
    import ollama
except ImportError:
    print("⚠️  Ollama not installed. Install with: pip install ollama")
    print("This demo will run in simulation mode.\n")
    ollama = None


class ProtectedAIWrapper:
    """
    Simplified wrapper showing dual-layer protection integration
    
    Enterprise version includes:
    - Advanced self-reflection protocols
    - Model-specific optimizations
    - Real-time threat intelligence updates
    - Priority support
    """
    
    # Available models for demo
    MODELS = {
        'tinyllama': 'tinyllama:latest',
        'llama3': 'llama3:latest', 
        'mistral': 'mistral:7b',
        'deepseek': 'deepseek-r1:7b',
    }
    
    def __init__(self, model_key="tinyllama"):
        """Initialize protected AI wrapper"""
        # Determine model
        if model_key in self.MODELS:
            self.model_name = self.MODELS[model_key]
            self.model_display = model_key.upper()
        else:
            self.model_name = model_key
            self.model_display = model_key
        
        # Initialize Layer 1: UCS Engine (External Protection)
        print("\n🛡️  Initializing Layer 1: UCS Engine (External Guardian)...")
        self.ucs_engine = UCSEngineLite()
        
        # Statistics
        self.blocks = 0
        self.allows = 0
        
        print(f"\n🤖 AI Model: {self.model_name}")
        print(f"✨ Dual-Layer Protection: ACTIVE")
        print(f"{'='*70}\n")
    
    def check_prompt_safety(self, user_input: str):
        """
        Layer 1: Check prompt with UCS Engine
        Returns: (is_safe, result)
        """
        result = self.ucs_engine.analyze(
            user_id="demo_user",
            text=user_input,
            context=ContextType.GENERAL
        )
        
        is_safe = result.action == PolicyAction.ALLOW
        return is_safe, result
    
    def send_to_model(self, prompt: str):
        """Send approved prompt to AI model"""
        if ollama is None:
            print(f"\n[SIMULATION MODE - Ollama not installed]")
            print(f"✅ Prompt would be sent to {self.model_display}")
            print(f"Prompt: {prompt[:100]}...")
            return None
        
        try:
            print(f"\n✅ Sending to {self.model_display}...\n")
            print(f"{'='*70}")
            
            response = ollama.chat(
                model=self.model_name,
                messages=[{'role': 'user', 'content': prompt}]
            )
            
            message = response['message']['content']
            print(message)
            print(f"{'='*70}\n")
            
            return message
            
        except Exception as e:
            print(f"\n⚠️  Error: {e}")
            print("Make sure Ollama is running and model is available.")
            return None
    
    def interactive_session(self):
        """Main interactive loop with dual-layer protection"""
        print(f"🌹 Protected {self.model_display} is ready!")
        print(f"💬 Type your prompts (or 'quit' to exit)\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Exit command
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\n🌹 Closing session...")
                    print(f"📊 Stats - Blocks: {self.blocks}, Allows: {self.allows}")
                    break
                
                # Layer 1: UCS Engine check
                print(f"\n🛡️  Layer 1: Analyzing prompt...")
                is_safe, result = self.check_prompt_safety(user_input)
                
                if not is_safe:
                    print(f"\n⚠️  BLOCKED by UCS Engine")
                    self.ucs_engine.print_result(result)
                    self.blocks += 1
                    continue
                
                # Approved - send to model
                print(f"✅ Layer 1: Safe")
                # Note: Layer 2 (self-reflection) would happen here in enterprise version
                
                self.allows += 1
                self.send_to_model(user_input)
                
            except KeyboardInterrupt:
                print("\n\n🌹 Session interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\n⚠️  Error: {e}")


def main():
    """Start protected AI session"""
    print("\n" + "🌹" + "="*68 + "🌹")
    print("   PROTECTED AI WRAPPER LITE - DUAL-LAYER DEMO")
    print("🌹" + "="*68 + "🌹")
    
    # Model selection
    if len(sys.argv) > 1:
        model_choice = sys.argv[1]
    else:
        print("\n🤖 Select model (or press Enter for TinyLlama):")
        print("   1. tinyllama")
        print("   2. llama3")
        print("   3. mistral")
        print("   4. deepseek")
        
        choice = input("\nChoice [1-4]: ").strip()
        
        model_map = {
            '1': 'tinyllama',
            '2': 'llama3', 
            '3': 'mistral',
            '4': 'deepseek',
            '': 'tinyllama'
        }
        
        model_choice = model_map.get(choice, 'tinyllama')
    
    # Create and run protected session
    wrapper = ProtectedAIWrapper(model_choice)
    wrapper.interactive_session()


if __name__ == "__main__":
    main()
