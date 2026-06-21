import os
from dotenv import load_dotenv
from openinference.instrumentation.langchain import LangChainInstrumentor
from openinference.instrumentation.openai import OpenAIInstrumentor
from arize.otel import register
load_dotenv() #Pull the keys from the hidden .env file

# 3. Configure the Arize tracer provider
tracer_provider = register(
    space_id=os.environ.get("ARIZE_SPACE_ID"),
    api_key=os.environ.get("ARIZE_API_KEY"),
    project_name="Document Q and A"
)
#Activate the listener using the registered provider
LangChainInstrumentor().instrument(tracer_provider=tracer_provider)
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)

print("✅ Arize tracing active — project: Document Q and A")



