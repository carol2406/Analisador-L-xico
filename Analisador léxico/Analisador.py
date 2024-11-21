import re

class LexicalAnalyzer:
    def __init__(self, token_definitions):

        self.token_definitions = token_definitions
        self.token_regex = self.compile_regex()

    def compile_regex(self):
       
        token_patterns = [f"(?P<{name}>{pattern})" for name, pattern in self.token_definitions.items()]
        return re.compile("|".join(token_patterns))

    def analyze(self, code):
        
        tokens = []
        for match in self.token_regex.finditer(code):
            token_type = match.lastgroup
            token_value = match.group(token_type)
            if token_type != "WHITESPACE":  # Ignorar espaços em branco
                tokens.append({"type": token_type, "value": token_value})
        return tokens

token_definitions = {
    "Numero": r"\d+(\.\d+)?",                     # Números inteiros e de ponto flutuante
    "String": r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'',  # Strings entre aspas duplas ou simples
    "IDENTIFIER": r"[A-Za-z_][A-Za-z0-9_]*",      # Identificadores (variáveis, funções, etc.)
    "ASSIGN": r"=",                               # Operador de atribuição
    "ARITH_OP": r"[\+\-\*/]",                     # Operadores aritméticos
    "COMPARISON_OP": r"[<>]=?|==|!=",             # Operadores de comparação
    "DELIMITER": r"[;,]",                         # Delimitadores como ponto e vírgula
    "PAREN": r"[\(\)]",                           # Parênteses
    "BRACE": r"[\{\}]",                           # Chaves
    "BRACKET": r"[\[\]]",                         # Colchetes
    "WHITESPACE": r"\s+",                         # Espaços em branco
    "COMMENT": r"//.*?$|/\*.*?\*/",               # Comentários (de linha e bloco)
    "Pontuação": r"."                               # Qualquer coisa inválida
}

# Inicializar o analisador léxico com os tokens definidos
analyzer = LexicalAnalyzer(token_definitions)

# Código de exemplo para análise
example_code = input('Digite um codigo: ')
# Analisar o código e exibir os tokens
tokens = analyzer.analyze(example_code)

# Exibir os tokens encontrados
for token in tokens:
    print(f"{token['type']}: {token['value']}")

print('Quantidade de Tokens {}'.format(len(tokens)))
