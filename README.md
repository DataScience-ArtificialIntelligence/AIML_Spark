#Energy-Efficient Fine-Tuning of Large Language Models on Devanagari Script-based Languages
This project focuses on fine-tuning the Llama 2 language model for Devanagari script languages, emphasizing Hindi and Sanskrit. The goal is to enhance language understanding and generation with a particular emphasis on energy-efficient strategies.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)


## Introduction

This project presents the fine-tuning of the Llama 2 language model for Devanagari script languages, specifically focusing on Hindi and Sanskrit. The aim is to overcome challenges in language understanding and generation while emphasizing energy-efficient strategies for accessibility in resource-constrained settings.

## Features

- Fine-tuned Llama 2 model for improved Devanagari language understanding.
- Implementation of energy-efficient strategies for fine-tuning.
- Open-source alternative for developers seeking cost-effective language processing tools.

## Getting Started

### Prerequisites

- accelerate==0.21.0
- peft==0.4.0
- bitsandbytes==0.40.2
- transformers==4.31.0
- trl==0.4.7
- datasets
- Python==3.11

## Usage

For Training Please refer to the notebooks. <br>
For inference from the model use ```python inference.py```
## Methodology

For detailed information on the methodology used in this project, please refer to the [Report]().

## Results

Our fine-tuned Llama 2 model excelled in understanding diverse Devanagari languages, achieving a commendable BLEU score. While ChatGPT boasts a higher BLEU score for Hindi, our model’s versatility extends to Sanskrit and other Devanagari languages.
| Model             | BLEU Score |
|-------------------|------------|
| Baseline Llama 2  | 5.20       |
| OURS              | 34.87      |
| ChatGPT-3.5 Turbo | 72.69      |
