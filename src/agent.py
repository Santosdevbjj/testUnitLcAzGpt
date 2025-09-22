# src/agent.py

import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do Azure OpenAI
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

# Validação das variáveis de ambiente
if not all([AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT_NAME, AZURE_OPENAI_API_VERSION]):
    raise ValueError("As variáveis de ambiente do Azure OpenAI não estão configuradas. Por favor, verifique seu arquivo .env.")

# Inicializa o modelo da Azure OpenAI
llm = AzureChatOpenAI(
    openai_api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT_NAME,
)

# Template do prompt para instruir a IA
prompt_template = """
Você é um desenvolvedor Python especialista em testes de software e sua tarefa é gerar testes unitários com a biblioteca `pytest` para o código Python fornecido.

Sua resposta deve ser **apenas** o código Python completo e funcional dos testes.
- A primeira linha do código deve ser `import pytest`.
- Para cada função, crie uma função de teste `def test_<nome_da_funcao>`.
- Inclua testes para casos de sucesso e, se aplicável, para casos de falha (por exemplo, erros ou exceções).
- Use `assert` para verificar o comportamento esperado.

Código para o qual você deve gerar os testes:

{code}

"""

def generate_tests(code: str, output_file_path: str):
    """
    Gera testes unitários para o código fornecido e salva em um arquivo.

    Args:
        code (str): O código Python para o qual os testes serão gerados.
        output_file_path (str): O caminho completo do arquivo onde os testes serão salvos.
    """
    print("Gerando testes... isso pode levar alguns segundos.")

    # Cria o prompt com o código de entrada
    prompt = ChatPromptTemplate.from_template(prompt_template)
    
    # Cria a cadeia de processamento (LangChain Expression Language)
    chain = prompt | llm | StrOutputParser()

    # Invoca a cadeia e obtém o código dos testes
    test_code = chain.invoke({"code": code})
    
    # Garante que o diretório de saída existe
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Salva o código gerado em um arquivo
    with open(output_file_path, "w") as f:
        f.write(test_code)

    print(f"Testes gerados com sucesso e salvos em: {output_file_path}")
