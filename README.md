# VocaNova AI prototype

## Included
- Burgundy themed Streamlit site
- CEFR A1–C2 vocabulary cards with Kazakh translation, collocations and examples
- Timed topic quiz with restart on wrong answer
- Session-based progress and saved words
- Optional OpenAI-powered AI Coach

## Run
Install Python 3.10+, then:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy for a public link
Upload `app.py` and `requirements.txt` to a GitHub repository, then deploy them using Streamlit Community Cloud. Do not upload API keys. To enable AI Coach, add `OPENAI_API_KEY` in the hosting platform's Secrets settings. API usage may cost money.

## Honest limitations
This is an early research demo. Progress is not yet saved to a shared database; leaderboard and push notifications are not implemented. Test it before presenting and describe it as a prototype, not as a validated product.
