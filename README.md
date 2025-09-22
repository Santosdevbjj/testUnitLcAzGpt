## Gerando Testes Unitários com LangChain e Azure ChatGPT.

![bairesDev](https://github.com/user-attachments/assets/d31bdcf1-fde1-485e-86b5-c1de9392f425)


**Bootcamp BairesDev - Machine Learning Training.**


---


# Gerando Testes Unitários com LangChain e Azure ChatGPT

## Descrição do Projeto

Este projeto demonstra a automação da geração de testes unitários em Python utilizando **LangChain** e **Azure OpenAI (ChatGPT)**. 

A ferramenta analisa o código-fonte fornecido e, com a ajuda de um agente de IA, propõe testes unitários robustos com a biblioteca `pytest`, cobrindo tanto casos de sucesso quanto de falha. 

O objetivo é aumentar a produtividade e a cobertura de código, garantindo mais qualidade em projetos de desenvolvimento.

---


## Funcionalidades

- **Agente de IA:** Implementado em Python com LangChain e Azure OpenAI.
- 
- **Entrada:** Um arquivo Python contendo funções ou classes.
- 
- **Saída:** Um arquivo de testes (`test_<nome>.py`) com o código Python gerado.
- 
- **Testes Automáticos:** O agente cria testes para casos de sucesso e, quando aplicável, para tratamento de erros e exceções.
- 
- **Integração:** Os testes gerados são compatíveis com o `pytest` e podem ser executados diretamente.

  ---
  

## Pré-requisitos

Para rodar este projeto, você precisa ter:

- **Python 3.8+** instalado.
- Acesso a uma conta no **Azure** com um serviço **OpenAI** e um modelo de `deployment` configurado (ex: `gpt-35-turbo`).
- A **chave de API** e o **endpoint** do seu serviço OpenAI no Azure.

  ---
  

## Passo a Passo para Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Santosdevbjj/testUnitLcAzGpt.git](https://github.com/Santosdevbjj/testUnitLcAzGpt.git)
    cd testUnitLcAzGpt
    ```

---

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

    ---
    

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *Observação:* Você precisará criar um arquivo `requirements.txt` com as dependências necessárias, como `langchain`, `langchain-openai`, `python-dotenv`, e `pytest`.

5.  **Configure as variáveis de ambiente:**
    - Crie um arquivo chamado `.env` na raiz do projeto, a partir do `.env.example`.
    - Preencha as chaves de API com suas credenciais do Azure OpenAI.

    `.env.example`
    ```ini
    AZURE_OPENAI_API_KEY="sua_chave_aqui"
    AZURE_OPENAI_ENDPOINT="seu_endpoint_aqui"
    AZURE_OPENAI_DEPLOYMENT_NAME="seu_nome_de_deployment_aqui"
    AZURE_OPENAI_API_VERSION="2023-05-15"
    ```

    ---
    

6.  **Gere os testes unitários:**
    - Execute o script principal. Ele irá ler as funções de exemplo em `src/functions.py` e chamar o agente para gerar os testes.

    ```bash
    python main.py
    ```

7.  **Execute os testes gerados:**
    - Após o script `main.py` ser concluído, os testes serão salvos em `tests/generated_tests/test_functions.py`.
    - Use o `pytest` para rodá-los.

    ```bash
    pytest tests/generated_tests/
    ```

    Se tudo estiver correto, você verá a saída do `pytest` indicando que os testes passaram.

---

## Exemplos de Uso

As funções de exemplo estão no arquivo `src/functions.py`:

- `add(a, b)`: Soma dois números.
- `subtract(a, b)`: Subtrai dois números.
- `divide(a, b)`: Divide dois números, com tratamento para divisão por zero.

O agente de IA gerará testes para cada uma dessas funções, incluindo casos como `add(2, 3)` e o tratamento da exceção `ValueError` em `divide(10, 0)`.


