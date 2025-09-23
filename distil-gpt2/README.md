```markdown
# 🧠 Disease–Symptom Prediction using Fine-Tuned GPT-2

Dive into the world of **Language Models** as we train a small transformer model to understand the relationship between **diseases** and **symptoms**!  
In this tutorial, we fine-tune **DistilGPT-2** (a lightweight version of GPT-2) on a medical dataset to generate **symptom descriptions** when given a disease name.  

---



## 📂 Project Overview

This project demonstrates how to:
1. **Load and preprocess a dataset** of diseases and symptoms.  
2. **Tokenize text** using GPT-2’s tokenizer.  
3. **Fine-tune GPT-2** on domain-specific text.  
4. **Monitor training and validation losses** to ensure effective learning.  
5. **Generate predictions** that map diseases to possible symptoms.  

---



## ⚙️ Dataset
- Source: Hugging Face dataset – QuyenAnhDE/Diseases_Symptoms (open-source).  
- Format:  
```



| Name           | Symptoms                                               |
| -------------- | ------------------------------------------------------ |
| heart attack   | Chest pain, swelling, redness, numbness or pressure... |
| lung-infection | Painless swelling, redness, numbness, limited range... |

````
- Preprocessing:  
- Each row combined into a text string:  
  ```
  disease_name | symptom_1, symptom_2, ...
  ```

---

## 🔧 Model & Training Setup
- **Base Model:** `distilgpt2`  
- **Tokenizer:** GPT-2 tokenizer (`AutoTokenizer`)  
- **Training Framework:** PyTorch + Hugging Face Transformers  
- **Hyperparameters:**  
- Batch size: 8  
- Epochs: 7  
- Optimizer: AdamW  
- Loss: Cross-Entropy Loss  
- Learning rate: default (2e-4, tuned slightly during runs)  

---

## 🔄 Training Loop
The training loop consisted of:  
- Forward pass → compute loss  
- Backward pass → gradient update  
- Validation pass after each epoch  

Training and validation losses were logged per epoch.

---

## 📊 Training Metrics

| Epoch | Train Loss | Validation Loss | Time (s) |
|-------|------------|-----------------|----------|
| 1     | 0.722      | 0.598           | 8.0      |
| 2     | 0.671      | 0.527           | 7.9      |
| 3     | 0.399      | 0.529           | 7.8      |
| 4     | 0.442      | 0.536           | 7.8      |
| 5     | 0.379      | 0.530           | 7.7      |
| 6     | 0.356      | 0.561           | 7.8      |
| 7     | 0.240      | 0.589           | 8.3      |

### 📉 Loss Curves
**Training vs Validation Loss**  
![Loss Curve](loss_curve.png)  

**Epoch Duration**  
![Epoch Duration](epoch_duration.png)  

---

## 🎯 Evaluation Metrics
- **Training Loss (final):** `0.240`  
- **Validation Loss (final):** `0.589`  
- **Perplexity (exp(Validation Loss)):** ~ **1.80**  
- Accuracy (token-level) can also be computed, but primary metric is **loss & perplexity** for language models.  

---

## 🧪 Example Predictions

### Example 1
**Input: heart attack **  
````

```
**Generated Output: heart attack | Chest pain, swelling, redness, numbness or pressure in the hand and fingers**  
```

```

---

### Example 2
**Input: lung-infection**  
```

```
**Generated Output: lung-infection | Painless swelling, redness, numbness, limited range of motion**  
```
````

---

## 🚀 Usage Guide

### 1️⃣ Install dependencies
```bash
pip install torch transformers datasets
````

### 2️⃣ Load fine-tuned model

```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("./trained_model")
tokenizer = GPT2Tokenizer.from_pretrained("./trained_model")

input_text = "lung-infection"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

output = model.generate(
    input_ids,
    max_length=20,
    num_return_sequences=1,
    do_sample=True,
    top_k=8,
    top_p=0.95,
    temperature=0.3,
    repetition_penalty=1.2,
    pad_token_id=tokenizer.eos_token_id
)

print(tokenizer.decode(output[0], skip_special_tokens=True))
```

---

## 🔮 Future Improvements

* Experiment with **larger GPT-2 models** (`gpt2`, `gpt2-medium`)
* Add **BLEU/ROUGE scores** for evaluating generated text
* Expand dataset with more diseases and symptom variations
* Deploy as a simple **API / Web App**



