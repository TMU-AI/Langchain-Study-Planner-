from langchain.chat_models import init_chat_model
import dotenv

dotenv.load_dotenv()

model = init_chat_model(model="gpt-5-nano", temperature=10)

response = model.invoke("Say hello to the world! Be concise but funny")

print(response.content)