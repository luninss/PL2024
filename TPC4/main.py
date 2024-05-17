import ply.lex as lex
import sys

# Lista de tokens
tokens = (
    'SELECT',
    'FROM', 
    'WHERE',
    'ID', 
    'COMMA', 
    'MAIORIGUAL', 
    'MENORIGUAL',
    'IGUAL',
    'DIFERENTE',
    'MENOR',
    'MAIOR',
    'NUMBER', 
    'IDENTIFIER'
)

# Regras de expressões regulares para tokens simples
t_SELECT = r'Select'
t_FROM = r'From'
t_WHERE = r'Where'
t_COMMA = r','
t_MAIORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_IGUAL = r'='
t_DIFERENTE = r'!='
t_MENOR = r'<'
t_MAIOR = r'>'

# Expressões regulares com ações incorporadas
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.lower() == 'select':
        t.type = 'SELECT'
    elif t.value.lower() == 'where':
        t.type = 'WHERE'
    elif t.value.lower() == 'from':
        t.type = 'FROM'
    return t

# Ignorar espaços e tabs
t_ignore = ' \t'

# Regra para erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Função para processar o arquivo de entrada e escrever o resultado no arquivo de saída
def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()
    
    lexer.input(data)
    output_lines = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        output_lines.append(str(tok))

    with open(output_file, 'w') as file:
        file.write('\n'.join(output_lines))

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        return
    
    input_file = sys.argv[1]
    output_file = "out.txt"

    process_file(input_file, output_file)

if __name__ == "__main__":
    main()
