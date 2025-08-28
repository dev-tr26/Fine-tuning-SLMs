# T5 Fine-Tuning: Hindi Question Answering

This project involves fine-tuning the [`t5-base`](https://huggingface.co/t5-base) model to check how it works on answer factual questions in Hindi. The goal is to train a model capable of generating accurate responses to domain-specific queries in english & tamil que-ans
---

## 📊 Training Summary

- **Model Used**: `google/t5-base`
- **Training Steps**: 468
- **Epochs**: 3
- **Training Loss**: 0.5332
- **Training Speed**:
  - `train_samples_per_second`: 10.49
  - `train_steps_per_second`: 2.10
- **Total FLOPs**: 81.38 TFLOPs
- **Checkpoint Saved At**: `./results/checkpoint-468`

---

## 📈 Interpretation of Results

- A training loss of ~0.53 suggests the model learned something useful, though not perfect.
- The relatively low number of steps (468) and limited data may mean the model underfits or needs more training for better generalization.
- Evaluation on a validation set is recommended to confirm performance.

---

## 🧾 Dataset Used

- **Language**: Hindi & Tamil
- **Type**: nirantk/chaii-hindi-and-tamil-question-answering
- **Structure**:
  - Input Format: `"question: <your-question>"`
  - Target: `<correct-answer>`
- **Example**:
  ```json
  {
    "input_text": "question: स्वामी निगमानन्द परमहंस के तन्त्र गुरु कौन थे?",
    "target_text": "बाबा रामकृष्ण परमहंस"
  }



## 🛠️ Troubleshooting

## ❌ Issue: Empty output or special tokens only
Fix:

- Ensure tokenizer is loaded from "t5-base", not the checkpoint.
- Use correct prompt format: "question: <your-question>".
- Set max_length explicitly during tokenization.

## ❌ Issue: Asking to truncate to max_length but no maximum length is provided
Fix:

- Add max_length=512 in tokenizer(...) call to avoid this warning.

## ❌ Issue: No improvement from base model
To Fix:

- Ensure your dataset has enough examples.
- Fine-tune for more epochs (e.g., 5–10).
- Add evaluation metrics to monitor during training.


## 🔍 Future Work
- Add validation set evaluation.

- Experiment with t5-small for faster training.

- Train on a larger or domain-specific Hindi corpus.

- Try adding context passages along with questions.



## 🔗 Checkpoint Access

The fine-tuned (experimental) model checkpoint is stored as a W&B artifact:

📦 [Download t5-checkpoint-468.zip from W&B](https://wandb.ai/turingetic_guy-iitram-institute-of-infrastructure-techno/t5-hindi-qa?nw=nwuserturingetic_guy)

> ⚠️ Note: This model was trained for experimentation and may not return valid outputs.

