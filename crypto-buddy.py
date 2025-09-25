# crypto-buddy.py
# Week 1 Assignment: Cryptocurrency Advisor Chatbot
# Course: AI for SE Specialization
# Student: Juliet Asiedu
# Disclaimer: This is for educational purposes only. Not financial advice.

# Step 1: Predefined crypto dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3.0
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6.0
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8.0
    }
}

BOT_NAME = "CryptoBuddy"

# Step 2: Start chatbot
print(f"Hi — I'm {BOT_NAME}, your AI-powered financial sidekick! 🚀🌱")
print("Ask me about trending coins, sustainability, or growth. Type 'exit' to quit.")

while True:
    user_query = input("\nYou: ").lower()

    # Exit condition
    if user_query in ["exit", "quit"]:
        print(f"{BOT_NAME}: Thanks for chatting! Remember: Crypto is risky! 👋")
        break

    # Sustainability rule
    elif "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda c: crypto_db[c]["sustainability_score"])
        print(f"{BOT_NAME}: I recommend {recommend}! 🌱 Best sustainability score in my dataset.")

    # Trending rule
    elif "trending" in user_query or "up" in user_query:
        trending = [c for c in crypto_db if crypto_db[c]["price_trend"] == "rising"]
        if trending:
            print(f"{BOT_NAME}: These coins are trending up: {', '.join(trending)} 🚀")
        else:
            print(f"{BOT_NAME}: No coins are trending up at the moment.")

    # Profitability rule
    elif "growth" in user_query or "profit" in user_query or "buy" in user_query:
        for c, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"{BOT_NAME}: {c} looks great for long-term growth! 📈")
                break
        else:
            print(f"{BOT_NAME}: None fit my profitability rule right now.")

    # Show dataset
    elif "show" in user_query or "list" in user_query or "coins" in user_query:
        print(f"{BOT_NAME}: Here’s what I know:")
        for c, d in crypto_db.items():
            print(f"- {c}: trend={d['price_trend']}, sustainability={d['sustainability_score']}/10")

    # Help
    elif "help" in user_query or "commands" in user_query:
        print(f"{BOT_NAME}: You can ask things like:")
        print("- Which crypto is trending up?")
        print("- What is the most sustainable coin?")
        print("- Which crypto should I buy for growth?")
        print("- Show all coins")

    # Fallback
    else:
        print(f"{BOT_NAME}: Sorry, I didn’t understand. Try asking about 'sustainability', 'growth', or 'trending'.")
