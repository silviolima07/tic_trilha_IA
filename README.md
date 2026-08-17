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


# Aula 05 - Document, Langchain
## Document objetivos relacionados ao artigo bioetica_e_ia.md
<img width="936" height="383" alt="image" src="https://github.com/user-attachments/assets/d9abda7e-ffc5-41a0-900c-207894d776b5" />

## Schema de metadados
<img width="389" height="339" alt="image" src="https://github.com/user-attachments/assets/79ffd0b5-0fa9-4b13-a9ba-7f900276b1c9" />

schema_de_metadados = {
    "file_path": {
        "tipo": "string",
        "descricao": "Caminho completo do arquivo original do qual o chunk foi extraído."
    },
    
    "file_name": {
        "tipo": "string",
        "descricao": "Nome do arquivo original (ex: 'bioetica_e_ia.md')."
    },
    
    "file_type": {
        "tipo": "string",
        "descricao": "Tipo do arquivo (ex: 'text/markdown', 'application/pdf')."
    },
    
    "file_size": {
        "tipo": "integer",
        "descricao": "Tamanho do arquivo original em bytes."
    },
    "creation_date": {
        "tipo": "string",
        "formato": "YYYY-MM-DD",
        "descricao": "Data de criação do arquivo original."
    },
    "last_modified_date": {
        "tipo": "string",
        "formato": "YYYY-MM-DD",
        "descricao": "Data da última modificação do arquivo original."
    },
    "language": {
        "tipo": "string",
        "descricao": "Idioma predominante do conteúdo do chunk (ex: 'pt-BR', 'en-US')."
    },
    "source": {
        "tipo": "string",
        "descricao": "Caminho ou URL da fonte do documento (equivalente à nossa 'fonte' nos documentos manuais)."
    },
    "page": {
        "tipo": "integer",
        "descricao": "Número da página onde o chunk se origina, se aplicável."
    },
    "chunk_id": {
        "tipo": "string",
        "descricao": "Identificador único para este chunk específico."
    },
    "section_title": {
        "tipo": "string",
        "descricao": "Título da seção ou subtítulo dentro do documento original de onde o chunk foi extraído."
    },
    "keywords": {
        "tipo": "array de string",
        "descricao": "Lista de palavras-chave que descrevem o conteúdo principal do chunk."
    }
}

import json
print(json.dumps(schema_de_metadados, indent=2))

## Exemplo de chunk preenchido (json)

<img width="599" height="339" alt="image" src="https://github.com/user-attachments/assets/5fb76ea6-6b8c-42d1-ae84-c6b615b9bd5c" />

<img width="692" height="338" alt="image" src="https://github.com/user-attachments/assets/5af52d89-9a6b-45bf-897b-208c14ca5fb1" />

## Perguntas e Respostas
<img width="908" height="294" alt="image" src="https://github.com/user-attachments/assets/fb43bf6c-246b-4416-80a9-a72cc658ac53" />


# Aula 06 - Projeto e Arquitetura de uma Aplicação RAG

<img width="1010" height="545" alt="image" src="https://github.com/user-attachments/assets/5db98fb4-0071-42f4-ab3e-37c00d894a64" />

## Qual é o problema que você deseja resolver?
## - Problemas:
- Departamento de Suporte: Permitir a consulta a base de dados de atendimento de tickets resolvidos para visualizar a solução adotada em problemas semelhantes em tickets novos.
- Departamento de RH: Permitir a consulta a base de dados de funcionarios para identificar dados cadastrais, periodos de férias e promoções.

## Quem utilizaria a aplicação? Descreva o usuário concretamente: cargo, contexto de uso, nível técnico.
## Que tipo de informação o usuário gostaria de consultar?

- Departamento de Suporte ao usuário e departamento de RH.
- Colaboradores que atuam no suporte aos usuários podem fazer uso do RAG para acessar a base de tickets resolvidos.
- Colaboradores do RH podem consultar dados dos demais colaboradores e administrar as informações relacionadas ao colaborador.

## De onde vêm essas informações?
- base de dados histórico de atendimentos fechados.
- base de dados de colaboradores ativos.


## Por que utilizar um LLM sozinho não seria suficiente?
- Uma LLM foi treinada com base de dados tipo wikipedia, livros, artigos, etc...
- Dados confidencias de empresas não fazem do treinamento e por consequencia o LLM não tem como responder a respeito desse assunto.
  - A estratégia do RAG permite acrescentar conhecimento para o LLM.


## Como o usuário vai utilizar o sistema? (API, aplicativo, interface web?)
- Depende da situação, se deseja uma resposta única e completa.
- - Uma consulta a tickets resolvidos, seria feita pelo pessoal do suporte através de uma interface web, onde visualizaria a solução e poderia repassar para o usuário. Ou ir pessoalmente e aplicar a solução encontrada.
- no RH a consulta a dados de colaboradores é confidencial, pode ser feita via interface web, com acesso apenas via login e senha.

## Perguntas que o usuário poderia fazer:
## Suporte
- Quais tickets resolvidos a respeito de impressoras ?
- Quantos tickets resolvidos foram a respeito da impressora modelo Nasa?
  - Qual o ticket mais antigo de impressoras ?
## RH
- Quando o colaborador João terá direito a férias remuneradas ?
- Qual o cargo do colaborador João ?
- Quais colaboradores tem 5 anos de trabalho na empresa ?



# Por que RAG é adequado para esse problema?
- A base de dados são documentos que podem ser indexados, por data, por departamento, por tipo, assim a criamos um base preparada para filtrar e assim recuperar trechos relevantes em nossas pesquisas.
- Essa base pode ser facilmente atualizada e assim garantir a consistências das respostas obtidas.

# Que tipo de conhecimento precisa ser fornecido ao modelo?
- Documentos relevantes que sejam necessários para gerar a reposta correta.
- Podem ser relatórios administrativos ou histórico de atendimentos.

# Esse conhecimento muda com que frequência? (diariamente, mensalmente, quase nunca?)
- Dados administrativos podem mudar diariamente, semanalmente ou anualmente.
- Históricos de atendimentos, podem ser atualizados semanalmente.

# Existe necessidade de utilizar documentos privados ou específicos da organização?
- No departamento de RH, são dados confidenciais, o acesso é controlado.
- No departamento de suporte envolve apenas dados da própria empresa, departamentos e equipamentos.

# Que problemas poderiam ocorrer se o LLM respondesse apenas com seu conhecimento pré-treinado? Dê um exemplo concreto de resposta errada que ele daria no seu cenário.
- Nenhuma LLM poderia responder a respeito de questões de RH de uma empresa, pois foi treinado com bases gerais, que não fazem referência a qualquer empresa.
- Se perguntar para a LLM qual a faixa salarial de determinado cargo na empresa A, podem nem existir esse cargo na empresa A. Mesmo que exista, esse informação não é divulgada, a LLM pode ter pesquisado e encontrado uma média.

# Em quais situações RAG não seria a melhor solução para esse problema
# Considere e comente ao menos três alternativas:

# - busca tradicional por palavra-chave;
- O significado de uma palavra-chave tem relação com o contexto.
- O mesmo termo pode ter significados totalmente diferentes.
- Não compreende a intenção da pergunta, apenas busca por termos exatos, o que pode resultar em respostas incompletas ou irrelevantes se o termo não estiver explicitamente presente.

# - banco de dados estruturado e consultas SQL
- bancos de dados relacionais, dependem de relacionamentos, a linguagem SQL faz isso perfeitament- podem existir diversas tabelas, dimensões e tabelas fato, através do SQL, através de filtros, recuperar, gerar calculos e obter uma resposta.
- Para consultas que exigem precisão, agregações (somas, contagens, médias) e filtros complexos sobre dados estruturados, um banco de dados relacional com SQL é muito mais eficiente e preciso do que o RAG.

# - regras determinísticas;
- Para problemas que possuem respostas fixas, claras e que não variam com o contexto ou que não exigem interpretação de linguagem natural, regras determinísticas (ex: if-then-else statements, tabelas de decisão) são mais simples, rápidas e menos propensas a erros e alucinações que um LLM com RAG.

# - utilização direta de uma API;
- Se a informação desejada já está disponível através de uma API bem definida que retorna dados estruturados (ex: status de um pedido, cotação de uma ação, informações de um usuário por ID), a chamada direta a essa API é mais eficiente e confiável do que tentar extrair essa informação através de um RAG que precisaria interpretar a pergunta e, talvez, interagir com a API de forma indireta.

# - combinação de alguma dessas técnicas com RAG.
## - Em muitos casos complexos, a melhor solução é uma arquitetura híbrida. Por exemplo, usar RAG para entender a intenção da pergunta e extrair entidades, mas delegar a execução de consultas agregadas ou a busca de dados estruturados para um banco de dados SQL ou uma API específica. O RAG então combinaria os resultados para formar uma resposta completa e coerente.

# **Responda também:**

## - Existe alguma pergunta, dentro do seu próprio cenário, que RAG responderia **mal** e um banco de dados relacional responderia bem? Qual, e por quê?
- Sim, para o cenário de RH, a pergunta "Quantos colaboradores foram promovidos em 2023?" seria respondida mal pelo RAG. O RAG recuperaria documentos que mencionam promoções em 2023, mas teria dificuldade em **contar** de forma precisa o número exato de ocorrências ou de filtrar exclusivamente promoções, especialmente se a informação estiver espalhada ou implícita em textos. Um banco de dados relacional, por outro lado, com uma tabela de histórico de promoções, responderia essa pergunta de forma exata e eficiente com uma consulta SQL como `SELECT COUNT(*) FROM promocoes WHERE ano = 2023;`.

## - O que aconteceria se a pergunta do usuário exigisse **contar**, **somar** ou **ordenar** informação espalhada por muitos documentos?
- O RAG enfrentaria grandes dificuldades. Embora um LLM possa ter alguma capacidade de "contar" ou "somar" informações em um ou poucos parágrafos recuperados, ele não é projetado para realizar operações matemáticas precisas ou ordenação de dados em larga escala de forma confiável em múltiplos documentos. Ele poderia alucinar números, somar incorretamente ou apresentar uma ordenação subjetiva e inconsistente, pois seu foco é a coerência textual e a recuperação de informações relevantes, não a análise quantitativa ou estruturada. Para tais operações, um sistema que combine RAG com ferramentas de análise de dados estruturados (como SQL, Pandas, etc.) seria essencial.
  









