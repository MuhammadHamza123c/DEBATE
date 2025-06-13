# AI Debate Simulator: Faith, Logic, and Belief Systems

This project simulates structured debates between AI chatbots representing different worldviews — **Muslim**, **Christian**, and **Atheist** — with a fourth AI acting as a **Judge** to determine the winner after each round. All bots are also capable of **speech output** using `pyttsx3`.

---

## 🧠 Overview

Using powerful large language models (LLMs) like **Grok** and **LLaMA 3 (8B)**, this project explores how AI can simulate philosophical and theological arguments through structured debate.

- **3 Debater Bots**:  
  - **Muslim Bot**: Simulates Islamic beliefs.  
  - **Christian Bot**: Represents Christian doctrine and reasoning.  
  - **Atheist Bot**: Advocates for secular and humanist positions.

- **1 Judge Bot**:  
  - Listens to all arguments  
  - Evaluates logic, coherence, and persuasive strength  
  - Selects a winner each round and declares the final winner after 10 rounds

- **Speech Output with `pyttsx3`**:  
  Each bot speaks its arguments aloud in real-time, giving the debate a more human-like experience.

---

## 🔊 Voice Interaction

This project uses [`pyttsx3`](https://pypi.org/project/pyttsx3/) to enable text-to-speech functionality for all four bots. It works offline and adds a layer of realism to the simulated debate.

```bash
pip install pyttsx3
