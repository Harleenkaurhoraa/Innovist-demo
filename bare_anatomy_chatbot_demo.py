
import streamlit as st

st.set_page_config(page_title="Bare Anatomy Chatbot", page_icon="💬")

st.title("💬 Bare Anatomy - Smart Haircare Assistant")
st.markdown("Ask me anything about your hair concerns, products, or orders!")

# Sample Product Info (simplified)
products = {
    "Anti-Dandruff Shampoo": "Fights flakes and soothes your scalp with zinc and salicylic acid.",
    "Hair Fall Control Shampoo": "Strengthens roots and reduces breakage with keratin boosters.",
    "Frizz Control Shampoo": "Smoothens hair using argan oil and natural hydrators."
}

# Sample FAQs
faqs = {
    "How long does it take to see visible results?": "Typically, users see noticeable results within 2-4 weeks of consistent use.",
    "How do I track my order?": "You can track your order using the tracking link sent to your email after dispatch.",
    "Do you ship internationally?": "Currently, we ship only within India. International shipping is coming soon!",
    "What is your return or refund policy?": "We offer a 7-day return policy if the product is unopened and unused.",
    "How do I know which product is right for me?": "You can use this chatbot or our product filter to find personalized recommendations.",
    "Are your products cruelty-free?": "Yes! All Bare Anatomy products are cruelty-free and vegan.",
    "Can I use your products on colored hair?": "Absolutely! Our shampoos are safe for chemically treated or colored hair.",
    "Are there any side effects?": "Our products are dermatologically tested and generally safe. Patch testing is always recommended.",
    "Can I use two shampoos together?": "Yes, alternate use is possible based on your hair needs.",
    "Do your shampoos contain sulfates or parabens?": "No, all our products are free from sulfates, parabens, and harmful chemicals.",
    "Can men use Bare Anatomy products?": "Yes, our formulations are gender-neutral and suitable for all.",
    "What makes Bare Anatomy unique?": "Our products are backed by science and are customized for Indian hair types.",
    "Do you offer trial packs?": "We occasionally launch mini-packs or bundles. Stay tuned on our website or subscribe for updates."
}

# Chat Functionality
query = st.text_input(" Hi there 💕! Tell me about your hair concerns, and I’ll help you pick the best shampoo.")

if query:
    response = None
    query_lower = query.lower()

    # Check for product recommendations
    if "dandruff" in query_lower:
        response = "You might want to try our Anti-Dandruff Shampoo. Would you like to know more?"
    elif "hair fall" in query_lower:
        response = "I recommend the Hair Fall Control Shampoo for you. Want ingredient info?"
    elif "frizz" in query_lower:
        response = "Our Frizz Control Shampoo works wonders. Shall I add it to cart for you?"

    # Match against FAQs
    for question, answer in faqs.items():
        if question.lower() in query_lower:
            response = answer
            break

    # Default fallback
    if not response:
        response = "I'm still learning! Can you try rephrasing your question or be more specific?"

    st.markdown(f"**Bot:** {response}")
