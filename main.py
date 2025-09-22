# main.py

import os
import sys
from src.agent import generate_tests

def main():
    """
    Ponto de entrada do programa.
    Lê o código de exemplo e chama o agente para gerar os testes.
    """
    functions_file_path = 'src/functions.py'
    output_dir = 'tests/generated_tests'
    output_file_path = os.path.join(output_dir, 'test_functions.py')

    # Verifica se o arquivo de funções existe
    if not os.path.exists(functions_file_path):
        print(f"Erro: O arquivo {functions_file_path} não foi encontrado.", file=sys.stderr)
        sys.exit(1)

    # Lê o código das funções de exemplo
    with open(functions_file_path, 'r') as f:
        code_to_test = f.read()

    # Chama a função principal do agente para gerar os testes
    generate_tests(code_to_test, output_file_path)
    
    print("\n---")
    print("Pronto para testar!")
    print(f"Para rodar os testes gerados, execute o seguinte comando no terminal:")
    print(f"  pytest {output_file_path}")

if __name__ == '__main__':
    main()
