# Configure Gemini API
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables
api_key = os.getenv('API_KEY')

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro")


def summarize_content(content, language):
    language_prompts = {
        'en': "Summarize the terms of service (ToS) for the provided company in a concise, easy-to-understand format including bullet points and titles, avoiding legal jargon. Highlight any unusual or unexpected clauses that users might be agreeing to. Finally, provide a rating out of 10 based on how user-friendly, transparent, and fair the terms are, with 10 being the ideal terms of service. The rating should consider elements like privacy, data ownership, cancellation policies, and overall fairness:",
        'es': "Eres un asistente legal español. Resuma los términos de servicio (TdS) de la empresa proporcionada en un formato conciso y fácil de entender, evitando la jerga legal. Resalte cualquier cláusula inusual o inesperada que los usuarios puedan estar aceptando. Finalmente, proporcione una calificación sobre 10 en función de cuán fáciles de usar, transparentes y justos sean los términos, siendo 10 los términos de servicio ideales. La calificación debe considerar elementos como la privacidad, la propiedad de los datos, las políticas de cancelación y la equidad general.:",
        'ht': "Ou se yon asistan legal panyòl. Rezime kondisyon sèvis (ToS) pou konpayi yo bay la nan yon fòma kout, fasil pou konprann, evite jagon legal. Mete aksan sou nenpòt kloz etranj oswa inatandi ke itilizatè yo ta ka dakò. Finalman, bay yon evalyasyon sou 10 ki baze sou fason ki fasil pou itilize, transparan, ak jis kondisyon yo, ak 10 se kondisyon ideyal yo nan sèvis yo. Evalyasyon an ta dwe konsidere eleman tankou vi prive, pwopriyetè done, règleman anilasyon, ak jistis an jeneral:"
    }
    prompt = f"{language_prompts[language]}\n\n{content}"
    response = model.generate_content(prompt)
    return response.text
