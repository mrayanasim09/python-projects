# Machine Learning

Computer vision, NLP, and predictive analytics experiments using OpenCV, MediaPipe, and scikit-learn.

## Prerequisites

```bash
pip install -e ".[ml]"
```

A **webcam** is required for the camera-based scripts (`brightness_controllor.py`, `eye_blink.py`, `camera.py`, `sketch.py`).

> **Platform note:**
> `brightness_controllor.py` adjusts screen brightness via `screen-brightness-control`.
> This is supported on **Windows** and **Linux** only. On macOS the brightness level is printed to stdout instead.

## Scripts

| Script | Description | Run |
|--------|-------------|-----|
| `brightness_controllor.py` | Control screen brightness using hand gestures (webcam + MediaPipe) | `python brightness_controllor.py` |
| `eye_blink.py` | Eye blink detection using Haar cascades | `python eye_blink.py` |
| `sketch.py` | Convert webcam feed to pencil sketch in real time | `python sketch.py` |
| `camera.py` | Use phone camera as a PC webcam | `python camera.py` |
| `lang_dect.py` | Detect the language of input text | `python lang_dect.py` |
| `sentiments.py` | Sentiment analyser (VADER + TextBlob) | `python sentiments.py` |
| `spam_dect.py` | Spam message classifier | `python spam_dect.py` |
| `text_to_speech.py` | Convert text to spoken audio (pyttsx3) | `python text_to_speech.py` |
| `crypto_prices.py` | Cryptocurrency price prediction (Prophet) | `python crypto_prices.py` |
| `gold_price.py` | Gold price prediction (Prophet) | `python gold_price.py` |

## Stopping Camera Scripts

Press **`q`** in the OpenCV window to quit cleanly and release the camera.
