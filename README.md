<img width="823" height="457" alt="robo2x" src="https://github.com/user-attachments/assets/ba252859-2fdc-4030-8cde-f0b150e082e3" />

# Aluno: Silvio Cesar de Lima
# Aula 01 - Introdução a IA


Este projeto contém o código inicial para interagir com a API da OpenAI utilizando Python. 

Para garantir a eficiência de recursos e o isolamento das dependências, recomendamos fortemente o uso de um Ambiente Virtual Python (Virtual Environment ou `venv`).

## 🚀 Passo a Passo para Configuração e Execução

### 1. Criar o Ambiente Virtual (venv)
Abra o seu terminal na pasta raiz do projeto (`/IA`) e execute o seguinte comando para criar o ambiente virtual:

```bash
# No Linux/macOS
python3 -m venv venv

# No Windows
python -m venv venv
```

### 2. Ativar o Ambiente Virtual
Sempre que for trabalhar no projeto ou rodar os códigos, você precisa ativar o `venv`.

```bash
# No Linux/macOS
source venv/bin/activate

# No Windows
venv\Scripts\activate
```
*(Você saberá que o ambiente está ativado porque o nome `(venv)` aparecerá no início da linha de comando do terminal).*

### 3. Instalar as Dependências
Com o ambiente ativado, instale as bibliotecas necessárias (como `openai` e `python-dotenv`) a partir do arquivo `requirements.txt` que está na raiz do projeto:

```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente (Segurança)
Para proteger seus dados e garantir a segurança, as chaves de API nunca devem ser inseridas diretamente no código nem comitadas em repositórios públicos.

Certifique-se de que o arquivo `.env` exista dentro da pasta `AULA_01` (ou na raiz, dependendo de onde for executar) com a seguinte estrutura:

```env
OPENAI_API_KEY=sua_chave_de_api_aqui
OPENAI_MODEL=gpt-4o-mini
```
*(Importante: adicione o arquivo `.env` ao seu `.gitignore` para não enviá-lo para o GitHub).*

### 5. Rodar o Código
Agora que o ambiente está isolado e as bibliotecas estão instaladas, você pode executar o script:

```bash
# Entre na pasta da aula
cd AULA_01

# Execute o script Python
python hello_llm.py
```

---
### 🛑 Como sair do Ambiente Virtual?
Quando terminar de programar, você pode desativar o ambiente virtual executando simplesmente:
```bash
deactivate
```

# Aula 02 - Converter pdf to md

Uso de Docling para extrair texto e exportar como Markdown

Extrair campos: titulo, autores e ano de edição

<img width="709" height="145" alt="image" src="https://github.com/user-attachments/assets/6cacb7cc-8656-4c29-a874-32c74e0381af" />


### Teste com guard-rail configurado no OPENROUTER para bloquear envio de endereço de mail para providers externos

<img width="953" height="275" alt="image" src="https://github.com/user-attachments/assets/5b11303f-6472-414d-9a94-fb5f12eef550" />

# Aula 03 - Extrair Embedding e gerar Métricas

Gerar as funções e aplicar em termos e depois em frases.

Identificar as métricas geradas.

Conclusões.

##  Tabela de similaridade de termos

<img src="./Aula_03/imgs/tabela_similaridade_termos.png"
     width="709"
     alt="Tabela de similaridade de termos">

## Gráfico de similaridade de termos

<img src="./Aula_03/imgs/Similaridade_termos.png"
     width="709"
     alt="Similaridade de termos">

## Tabela de similaridade de frases

<img src="./Aula_03/imgs/tabela_similaridade_frases.png"
     width="709"
     alt="Tabela de similaridade de frases">

## Conclusões / Observações

<img src="./Aula_03/imgs/conclusoes_1.png"
     width="709"
     alt="conclusoes 1">

<img src="./Aula_03/imgs/conclusoes_2.png"
     width="709"
     alt="conclusoes 2">

<img src="./Aula_03/imgs/conclusoes_3.png"
     width="709"
     alt="conclusoes 3">     

# Aula 04 - Estratégias de chunking e embedding

## Artigo: twitter_algoritmo.md

<img width="774" height="319" alt="image" src="https://github.com/user-attachments/assets/e5154a4d-93ac-4c01-9581-bbea1d556994" />

## Artigo: bioetica_e_ia.md

<img width="765" height="314" alt="image" src="https://github.com/user-attachments/assets/56d9f3c4-d4d5-483f-af2f-fbdbbd7a5fbd" />

## Artigo: escrita_academica_ia.md

<img width="767" height="311" alt="image" src="https://github.com/user-attachments/assets/1f2714db-4c3d-4c54-88ae-9b448ee7717b" />

## Melhor estratégia por artigo

<img width="607" height="145" alt="image" src="https://github.com/user-attachments/assets/1a9c0e06-685c-4916-b984-545454f920cc" />

## Cada estratégia criou uma quantidade de chunks/trechos diferentes por artigo.

## No artigo bioetica_e_ia estes foram os resultados:
<img width="580" height="343" alt="image" src="https://github.com/user-attachments/assets/73c70fcf-8873-4006-83c7-bf5bf4af593a" />

## Melhor estratégia de chunking por artigo (similaridade média top 3)
<img width="1183" height="690" alt="image" src="https://github.com/user-attachments/assets/24755d79-52f4-4e59-b9ed-edabd6726657" />







