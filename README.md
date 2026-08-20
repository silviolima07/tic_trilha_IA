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

# Este fluxo pode ser usado para os dois contexto:
## - Departamento de RH
## - Departamento de Suporte

# Parte 1 - Identificação dos problemas
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

 combinação de alguma dessas técnicas com RAG.
- Em muitos casos complexos, a melhor solução é uma arquitetura híbrida. Por exemplo, usar RAG para entender a intenção da pergunta e extrair entidades, mas delegar a execução de consultas agregadas ou a busca de dados estruturados para um banco de dados SQL ou uma API específica. O RAG então combinaria os resultados para formar uma resposta completa e coerente.

# **Responda também:**

## - Existe alguma pergunta, dentro do seu próprio cenário, que RAG responderia **mal** e um banco de dados relacional responderia bem? Qual, e por quê?
- Sim, para o cenário de RH, a pergunta "Quantos colaboradores foram promovidos em 2023?" seria respondida mal pelo RAG. O RAG recuperaria documentos que mencionam promoções em 2023, mas teria dificuldade em **contar** de forma precisa o número exato de ocorrências ou de filtrar exclusivamente promoções, especialmente se a informação estiver espalhada ou implícita em textos. Um banco de dados relacional, por outro lado, com uma tabela de histórico de promoções, responderia essa pergunta de forma exata e eficiente com uma consulta SQL como `SELECT COUNT(*) FROM promocoes WHERE ano = 2023;`.

## - O que aconteceria se a pergunta do usuário exigisse **contar**, **somar** ou **ordenar** informação espalhada por muitos documentos?
- O RAG enfrentaria grandes dificuldades. Embora um LLM possa ter alguma capacidade de "contar" ou "somar" informações em um ou poucos parágrafos recuperados, ele não é projetado para realizar operações matemáticas precisas ou ordenação de dados em larga escala de forma confiável em múltiplos documentos. Ele poderia alucinar números, somar incorretamente ou apresentar uma ordenação subjetiva e inconsistente, pois seu foco é a coerência textual e a recuperação de informações relevantes, não a análise quantitativa ou estruturada. Para tais operações, um sistema que combine RAG com ferramentas de análise de dados estruturados (como SQL, Pandas, etc.) seria essencial.
  
# Parte 2 - Organização dos documentos
## Quais tipos de arquivo existirão? (PDF, DOCX, HTML, Markdown, páginas web, planilhas, imagens, áudios, vídeos, outros)
Departamento de RH
- Noromalmente os registros de colaboradores estão em papel, que seriam digitalizados, salvos como PDF e a partir dai convertidos em markdown para passar pelos processos do RAG.
Departamento de Suporte
- Dados históricos estão salvos num banco de dados.
- Podem ser planilhas também.

## Qual o volume aproximado? (dezenas, centenas, milhares de documentos?)
- Com certeza milhares de documentos, de acordo com o tempo de coleta de dados na empresa.

## Qual o tamanho típico de cada documento? (Paginas, kbs)
- RH: Depende da quantidade de informação existente e tempo de casa do colaborador.
- Suporte: Se os dados são retidos permanentemente ou apagados depois de um periodo.

## Com que frequência novos documentos entram? Documentos antigos são atualizados ou substituídos?
- Entram novos dados quando novos colaboradores são contratados.
- Creio que documentos antigos ficam salvos num backup geral. E novas versões sao geradas.
- A entrada e atualização de dados é diária, dependendo do tamanho da empresa.
Organização de pastas reflete os filtros que o usuário poderia usar ao enviar uma pergunta e efetuar uma busca.
RH
- ano/documentos/
- ano/tipo de contrato de trabalho/
- ano/departamento/
Suporte
- ano/departamento
- ano/tipo de risco

O pessoal do RH precisar buscar informação a respeito de um colaborador, a busca pode iniciar ano e algum documento que o identifique. Pode ser por ano e tipo de contrato de trabalho e pode filtar por ano e departamento.

No departamento de Suporte, uma busca pode ser ano e departamento ou por ano e tipo de risco, assim pode dentificar os atendimentos pelo risco atribuído.

# Existe documento que **não deve** entrar na base? (informação sigilosa, dado pessoal, versão obsoleta) Como você impediria a entrada?
- Dados sensiveis, tipo dados confidenciais (salário, ecames médicos, etc...) não devem ser inseridos na base de dados. Existe como bloquear a leitura, isso se chama guard-rail. Por exemplo no OpenRouter, posso criar uma regra de guard-rail para identificar numero de cartão de credito, numero de celular, email, etc... e quando um documento for enviado para o OpenRouter, as informações são escondidas ou o envio negado.


# Como você lidaria com **versões** do mesmo documento? Se a política de férias mudou em 2026, o sistema pode recuperar a versão de 2024 e responder errado.
- Nesse caso extraíria o metadado de data de criação do documento, ao salvar os embedding, a informação do metadados iria ser salva no banco vetorial e quando uma busca fosse feita na base, usaria a opção filter para restringir a busca por similaridade apenas nos chunks com a data de criação desejada.

# Parte 3 - Pipeline de Ingestao

# Pipeline
- Extração, documentos PDF, serão convertidos em markdown.
- Limpezas poderiam ser feitas para remover termos irrelevantes.
- Documentos  serão divididos em chunks por paragrafo por exemplo, metadados tipo data de criação, departamento e outros serão extraídos de cada chunk, assim poderão ser usados como filtros.
- Chunks sao convertidos em embeddings e salvos num banco vetorial.

# Como o texto seria extraído?
- Existem libs Python que extraem texto de PDFs.

# Como você trataria PDFs com texto selecionável?
- Extrairia com libs Python, por exemplo pypdf, pdfplumber.

# E PDFs digitalizados (imagem escaneada, sem camada de texto)?
- OCR para imagens digitalizadas.

# Como trataria tabelas? (é importante manter?)
- Docling transforma PDF em conteúdo estruturado.

# Como trataria imagens? (posso descartar? quais informações elas tem?)
OCR. Não descartar. Imagens tem pixels, resolução, layout e metadados como data, GPS, etc...

# Como trataria documentos multimodais?(multimodais = texto + imagem, audio + video, texto + video e etc)
- Cada modalidade deve ser tratada separadamente
- Texto: via OCR
-  Imagem> via um modelo de visao, que poderia descrever a imagem
- Audio: um modelo de TTS - texto to Speech
- video: transcrição do video

# Parte 4 - Metadados
# Metadados do documento
# RH
```json
{
  "document_id": "...",
  "descricao": "...",
  "origem": "...",
  "ano": "...",
  "tipo_doc": "...",
}
```

# Suporte
```json
{
  "document_id": "...",
  "descricao": "...",
  "origem": "...",
  "ano": "...",
  "tipo_doc": "...",
}
```

# Metadados do chunk
# RH
```json
{
  "document_id": "123",
  "chunk_id": "123-05",
  "page": 5,
  "section": "...",
  "document_type": "...",
  "departamento": "...",
  "text": "..."
}
```

# Suporte
```json
{
  "document_id": "123",
  "chunk_id": "123-05",
  "page": 5,
  "section": "...",
  "document_type": "...",
  "departamento": "...",
  "equipamento": "...",
  "risco": "...",
  "text": "..."
}
```

- RH: ao executar uma busca na base de dados de RH, pode-se definir um filtro com base no metadados, por exemplo ano para restringir a busca.

- Suporte: ao executar uma busca na base de dados de Suporte, pode por exemplo filtrar por equipamento.

- Os metadados de documentos sao herdados por todos chunks gerados.

# Quais metadados você usaria para **filtrar** a busca? Dê um exemplo de pergunta em que o filtro é indispensável.

# RH
- Quantos funcionarios atuam no departamento de suporte desde 2020?
- Nesse caso, o filtro ano e departamento permitem efetuar a busca.

# Quais metadados você usaria para **citar a fonte** ao usuário? O que exatamente apareceria na tela junto da resposta?
- O titulo do documento, o nome do arquivo, a pagina.
- Dessa forma na resposta do RAG, estas informações poderiam ser visualizadas, reforçando a resposta obtida.

# Que metadado seria caríssimo de acrescentar depois que a base já estivesse indexada? Por quê?
- Se náo tiver previsto o metadado pagina, teria que criar os chunks e recalcular os embeddings.
# Como você vai extrair esses metadados?
- Pode ser via codigo, extraindo as informações e salvando num json.

# Exemplo:  
# Metadados em um RAG para Documentos de Suporte

Imagine uma empresa que possui centenas de documentos: **manuais técnicos, procedimentos, FAQs, documentação de produtos e instruções de manutenção**.

O objetivo é criar um sistema **RAG (Retrieval-Augmented Generation)** para auxiliar o departamento de suporte.

---

## 1. Começar pelas perguntas

Antes de definir os metadados, devemos pensar:

> **Quais perguntas o suporte precisará responder e quais informações serão necessárias para restringir e comprovar a resposta?**

Exemplos:

- Como configurar o equipamento modelo X200?
- Qual procedimento é válido para produtos da marca X?
- Existe diferença no procedimento para a versão 2025?
- Onde está documentada essa informação?

Essas perguntas ajudam a determinar quais metadados precisam existir.

---

## 2. Metadados do documento

São informações que caracterizam **o documento inteiro**.

Exemplo:

    {
        "marca": "Empresa X",
        "modelo": "X200",
        "ano": 2025,
        "tipo_documento": "manual_tecnico",
        "versao": "3.2",
        "arquivo": "manual_x200_v32.pdf"
    }

Esses metadados podem ser obtidos de diferentes formas:

- **Manualmente:** alguém cadastra marca, modelo, versão etc.
- **Nome do arquivo:** `manual_X200_2025_v32.pdf`
- **Propriedades do PDF:** autor, título, data de criação etc.
- **Conteúdo do documento:** regras, Regex, NLP ou LLM podem identificar informações presentes na capa ou nas primeiras páginas.

Em documentos corporativos, normalmente pode ser utilizada uma combinação dessas estratégias.

---

## 3. Metadados de página

Ao carregar um PDF página por página, o loader pode gerar automaticamente informações como:

    {
        "source": "manual_x200.pdf",
        "page": 42
    }

Depois podemos combinar essas informações com os metadados do documento:

    {
        "marca": "Empresa X",
        "modelo": "X200",
        "ano": 2025,
        "versao": "3.2",
        "source": "manual_x200.pdf",
        "page": 42
    }

A informação da página é especialmente importante para **rastreabilidade e confiabilidade**.

Ela permite apresentar uma resposta como:

> Reinicie o controlador mantendo o botão pressionado durante cinco segundos.  
> **Fonte: Manual X200 v3.2 — página 42.**

Assim, o usuário pode conferir a informação diretamente no documento original.

---

## 4. Metadados dos chunks

Depois, as páginas são divididas em chunks:

    Página 42
         ↓
    Chunk 150
    Chunk 151
    Chunk 152

Os chunks podem **herdar os metadados do documento e da página**.

Também podemos acrescentar informações específicas do chunk:

    {
        # Documento
        "marca": "Empresa X",
        "modelo": "X200",
        "ano": 2025,
        "versao": "3.2",
        "tipo_documento": "manual_tecnico",

        # Origem
        "arquivo": "manual_x200_v32.pdf",
        "pagina": 42,

        # Chunk
        "chunk_id": 151,
        "secao": "Configuração",
        "assunto": "Rede"
    }

O `chunk_id` pode ser criado automaticamente durante o processamento.

Outros campos, como `seção` ou `assunto`, podem ser obtidos pela estrutura do documento, regras, Regex ou classificação utilizando uma LLM.

---

## 5. Armazenamento no ChromaDB

Depois do chunking, são gerados os **embeddings**.

Conceitualmente, cada registro no banco vetorial terá:

    CHUNK
    │
    ├── texto
    │   "Para configurar o endereço IP..."
    │
    ├── embedding
    │   [0.217, -0.391, 0.812, ...]
    │
    └── metadata
        ├── marca: Empresa X
        ├── modelo: X200
        ├── ano: 2025
        ├── versão: 3.2
        ├── arquivo: manual_x200_v32.pdf
        ├── página: 42
        ├── seção: Configuração
        └── chunk_id: 151

Portanto:

> **Texto + embedding + metadados ficam associados ao mesmo registro no banco vetorial.**

---

## 6. Uso dos metadados na busca

Suponha que o atendente pergunte:

> **Como configurar a rede do modelo X200?**

O sistema pode identificar:

    modelo = "X200"

e restringir a busca:

    filter={"modelo": "X200"}

Depois, a busca vetorial procura os conteúdos semanticamente relevantes **somente dentro dos chunks correspondentes ao modelo X200**.

Isso reduz o risco de retornar uma instrução do modelo X100 ou X300 apenas porque o conteúdo é semanticamente parecido.

---

## 7. Duas funções principais dos metadados

| Finalidade | Exemplos |
|---|---|
| **Filtrar a busca** | marca, modelo, ano, versão, tipo_documento |
| **Rastrear/citar a resposta** | arquivo, página, seção, chunk_id |

Alguns metadados podem cumprir as duas funções.

---

## 8. Pipeline completo

    Documentos corporativos
            ↓
        PDF Loader
            ↓
    Extração por página
            ↓
    Metadados do documento
    marca / modelo / ano / versão / tipo
            ↓
    Metadados de origem
    arquivo / página
            ↓
        Chunking
            ↓
    Metadados do chunk
    chunk_id / seção / assunto
            ↓
        Embeddings
            ↓
        ChromaDB
    texto + embedding + metadata
            ↓
    Pergunta do suporte
            ↓
    Filtros de metadados
            ↓
        Busca vetorial
            ↓
        Top-K chunks
            ↓
            LLM
            ↓
        Resposta
            +
    fonte / documento / página

---

## 9. Regra principal

A melhor maneira de projetar os metadados é **partir do fim**:

> **Que perguntas o suporte precisará responder?**
>
> **Que filtros serão necessários?**
>
> **Que informações precisamos apresentar para comprovar a origem da resposta?**

A partir dessas necessidades, definimos os metadados **antes da indexação**.

Isso é importante porque algumas informações estruturais, como **página, seção ou versão**, podem ser trabalhosas ou caras de reconstruir depois que milhares de documentos já estiverem processados e indexados.

### Resumindo

**Metadados do documento**
→ descrevem o documento inteiro: marca, modelo, ano, versão, tipo.

**Metadados de página**
→ indicam a origem da informação e permitem rastreabilidade.

**Metadados do chunk**
→ identificam o fragmento: chunk_id, seção, assunto etc.

**Embedding**
→ permite encontrar conteúdos semanticamente semelhantes.

**Metadados + Embeddings**
→ permitem fazer uma busca semântica mais precisa, filtrada e rastreável.

# Parte 5 - Chunking / Splitting

# Qual estratégia de splitting você utilizaria?
- estratégia vai depender da estrutura e  conteúdo nos documentos.
- Teria que fazer testes com diferentes tamanhos de chunks e overlap, testar divisão por paragrafo e seções. Ou seja precisa fazer testes.

# Qual tamanho aproximado dos chunks?
- Chunks pequenos podem ser bons, mas podem separar informações relevantes da resposta desejada. Chunks muito grandes, podem trazer informação irrelevante. É preciso analisar para encontrar os o melhor valor. 

# Utilizaria overlap? Quanto?
- Sim, para manter a consistência da informação recuperada. O valor precisa ser testado e analisado quanto ao impacto. Um valor muito alto geraria informação redundante e custo de armazenamento e processamento. Poderia partir de valores iniciais e avaliar os resultados: chunk_size=1000 e chunk_overlap=100

# A divisão seria por caracteres, palavras, sentenças, parágrafos ou seções?
- Dependerá do tipo do documento.
- Por caracteres, palavras, sentença ou paragráfo seria ideal para documentos que sejam na maioria textos. 
- Documentos que apresentem titulos, seções, tabelas, podem usar essas divisões para serem divididos e extrair as informações.

# Utilizaria um splitter recursivo?
- Sim, nos testes feitos apresentou uma performance boa.
- Para os casos estudados, documentos de RH e Suporte, seriam adequados.

# Utilizaria uma estratégia específica para cada tipo de documento? Um contrato e uma transcrição de call center pedem o mesmo tratamento?
- São contextos bem diferentes. O ideal seriam estratégias diferentes, pois os termos relevantes poderiam estar em chunks bem distantes, consistência da resposta poderia ser impactada.
- Cada contexto tem blocos especificos tipo um contrato de trabalho no RH e um ticket de atendimento no Suporte.

# O que pode acontecer se os chunks forem muito pequenos?
- A informação relevante para a resposta pode ficar perdida e sem consistência, isolada. Além de gerar a criação de mais chunks no documento inteiro.

# O que pode acontecer se os chunks forem muito grandes?
- Informações irrelevantes podem ser recuperadas e que não acrescentam nada a resposta gerada.

# Como você trataria uma **tabela** na hora de dividir? Uma tabela cortada ao meio ainda significa alguma coisa? e uma imagem?
- Tabelas devem ser mantidas únicas, podem ter uma formatação especifica que deve ser preservada.
- Uma tabela cortada, pode perder a consistência.
- O mesmo vale para imagens.

# Como saber se a sua escolha de chunking foi boa? Que evidência você juntaria para provar isso?
- Pode-se testar utilizando um conjunto de perguntas que se as respostas corretas. Avalia-se as respostas obtidas entre as Top10 ou top5 retornadas.
- Avalia-se por exemplo:
-  Recall@K: o chunk correto apareceu entre os k primeiros?
- Precision@K: quantos dos chunks recuperados realmente eram relevantes?
- posição/rank do chunk correto
- qualidade da resposta final gerada
- presença de contexto suficiente no rank


# Parte 6 - Embeddings

# Escolha de Modelos de Embeddings — RH e Suporte

#Para os dois cenários foram escolhidos modelos diferentes, considerando não apenas a qualidade dos embeddings, mas também **privacidade, possibilidade de execução local, suporte ao português, custo e características dos documentos**.

---

# 1. Cenário: Recursos Humanos (RH)

## Modelo escolhido: BGE-M3

| Característica | BGE-M3 |
|---|---|
| **Modelo** | BAAI/bge-m3 |
| **Dimensão do embedding** | 1024 |
| **Suporta português?** | Sim |
| **É multilíngue?** | Sim — mais de 100 idiomas |
| **Tamanho máximo de entrada** | 8192 tokens |
| **É open source?** | Sim — licença MIT |
| **Pode ser executado localmente?** | Sim |
| **Possui API?** | Pode ser disponibilizado por API própria ou por serviços de inferência |
| **Custo aproximado** | Sem custo por token quando executado localmente; existe o custo da infraestrutura |
| **Fonte** | https://huggingface.co/BAAI/bge-m3 |

## Por que esse modelo é adequado para RH?

- Documentos de RH podem conter informações internas ou confidenciais, como políticas de remuneração, avaliações, dados de funcionários, benefícios, procedimentos internos e contratos.

Por esse motivo, a possibilidade de executar o modelo localmente é uma característica importante.

O fluxo poderia ser:

    Documentos RH
          ↓
       BGE-M3
    servidor local
          ↓
      Embeddings
          ↓
      ChromaDB
    servidor local

Dessa maneira, os documentos podem ser processados dentro da infraestrutura da empresa, sem a necessidade de enviar seu conteúdo para uma API externa.

Além disso, o BGE-M3 possui suporte a mais de 100 idiomas, incluindo português, gera embeddings de 1024 dimensões e suporta entradas de até 8192 tokens.

Essas características tornam o modelo adequado para documentos corporativos de RH, especialmente quando privacidade e controle sobre os dados são requisitos importantes.

---

# 2. Cenário: Suporte

## Modelo escolhido: Voyage 4 Large

| Característica | Voyage 4 Large |
|---|---|
| **Modelo** | voyage-4-large |
| **Dimensão do embedding** | 1024 por padrão; suporta também 256, 512 e 2048 |
| **Suporta português?** | Sim, como parte do suporte multilíngue |
| **É multilíngue?** | Sim |
| **Tamanho máximo de entrada** | 32.000 tokens |
| **É open source?** | Não |
| **Pode ser executado localmente?** | Não como modelo aberto para download e execução local |
| **Possui API?** | Sim |
| **Custo aproximado** | US$ 0,12 por 1 milhão de tokens |
| **Fonte** | https://docs.voyageai.com/docs/embeddings |
| **Fonte de preços** | https://docs.voyageai.com/docs/pricing |

## Por que esse modelo é adequado para Suporte?

No departamento de suporte podem existir diferentes tipos de documentos:

- Manuais técnicos;
- FAQs;
- Procedimentos;
- Documentação de produtos;
- Troubleshooting;
- Bases de conhecimento;
- Tickets históricos.

Nesse cenário, a qualidade da recuperação semântica possui grande importância.

Uma pergunta do usuário pode utilizar palavras completamente diferentes das utilizadas no documento.

Exemplo:

**Pergunta do usuário:**

> Minha impressora fica piscando três vezes e não imprime.

**Manual técnico:**

> Três sinais luminosos consecutivos indicam falha no sistema de alimentação.

Mesmo sem utilizar exatamente as mesmas palavras, um bom modelo de embeddings deve conseguir identificar a proximidade semântica entre os dois textos.

O `voyage-4-large` é apresentado pela Voyage AI como seu modelo de maior qualidade para recuperação generalista e multilíngue, sendo adequado para esse tipo de cenário.

---

# 3. Por que utilizar modelos diferentes?

A decisão considera requisitos diferentes para cada departamento.

    RAG CORPORATIVO
           │
     ┌─────┴─────┐
     ↓           ↓
    RH        SUPORTE
     ↓           ↓
  BGE-M3    Voyage 4 Large
     ↓           ↓
 Privacidade   Qualidade
 Execução      de retrieval
 local
 Open source
 Controle
 dos dados

No RH, a prioridade considerada foi **privacidade e controle dos dados**, mantendo a possibilidade de execução local.

No Suporte, a prioridade considerada foi **qualidade da recuperação semântica**, utilizando um modelo especializado em retrieval e acessível por API.

Isso não significa que o BGE-M3 não possa ser utilizado no Suporte. Ele também seria um candidato válido e poderia ser comparado por meio de testes.

---

# 4. Modelo alternativo considerado

## OpenAI text-embedding-3-large

Um modelo alternativo considerado seria o `text-embedding-3-large` da OpenAI.

Características importantes:

- Modelo de embeddings de alta capacidade;
- Suporte a diferentes idiomas;
- Disponível por API;
- Custo aproximado de US$ 0,13 por 1 milhão de tokens.

Fonte:

https://developers.openai.com/api/docs/models/text-embedding-3-large

Ele não seria descartado por falta de qualidade. Pelo contrário, seria um candidato interessante para comparação.

Um benchmark poderia comparar:

    BGE-M3
       vs
    Voyage 4 Large
       vs
    text-embedding-3-large

A decisão final deveria ser tomada utilizando perguntas e documentos reais da empresa.


# Referências usadas nas Partes de 1 a 6

# Relatório de Referências — RAG

## Atividades das Partes 1 a 6

Este documento reúne as principais fontes utilizadas para fundamentar as respostas das atividades relacionadas à construção de um sistema **RAG (Retrieval-Augmented Generation)** para documentos corporativos, considerando principalmente os cenários de **Recursos Humanos (RH)** e **Suporte**.

Os assuntos estudados incluem:

* carregamento de documentos;
* metadados;
* chunking;
* estratégias de splitting;
* embeddings;
* armazenamento vetorial;
* filtros por metadados;
* escolha de modelos de embeddings;
* privacidade e execução local.

---

# Parte 1 — Carregamento e estrutura dos documentos

## LangChain — Document Loaders

A documentação do LangChain apresenta os componentes utilizados para carregar documentos e transformá-los em objetos `Document`, que posteriormente podem ser divididos em chunks e utilizados em pipelines de RAG.

**Fonte oficial:**

https://docs.langchain.com/oss/python/integrations/document_loaders/

### Aplicação no projeto

O carregamento representa o início do pipeline:

```
PDF
  ↓
Document Loader
  ↓
Document
  ↓
páginas / conteúdo / metadata
```

Para arquivos PDF, loaders como o `PyPDFLoader` podem ser utilizados para preservar informações relacionadas à origem do conteúdo.

---

# Parte 2 — Metadados de documentos e chunks

Os metadados permitem associar informações adicionais aos documentos e chunks.

Exemplo:

```
{
    "marca": "Empresa X",
    "modelo": "X200",
    "ano": 2025,
    "arquivo": "manual_x200.pdf",
    "pagina": 42,
    "chunk_id": 151
}
```

Os metadados podem ter diferentes finalidades.

## Metadados para filtros

Exemplos:

* marca;
* modelo;
* ano;
* versão;
* tipo de documento;
* departamento.

## Metadados para rastreabilidade

Exemplos:

* arquivo;
* página;
* seção;
* chunk_id.

Essas informações permitem identificar exatamente de onde a resposta foi recuperada.

---

# Parte 3 — Armazenamento de documentos, embeddings e metadados no ChromaDB

O Chroma permite armazenar registros contendo:

```
ID
 +
Documento / Chunk
 +
Embedding
 +
Metadata
```

Exemplo conceitual:

```
Chunk 151
    │
    ├── texto
    │   "Para configurar o equipamento..."
    │
    ├── embedding
    │   [0.217, -0.391, ...]
    │
    └── metadata
        ├── modelo: X200
        ├── ano: 2025
        ├── página: 42
        └── chunk_id: 151
```

A documentação do Chroma confirma que os registros podem conter `documents`, `embeddings`, `metadatas` e identificadores. Se os embeddings já tiverem sido calculados, eles podem ser enviados junto com o documento e os metadados.

**Fonte oficial — Adding Data to Chroma Collections:**

https://docs.trychroma.com/docs/collections/add-data

---

# Parte 4 — Filtros utilizando metadados

Uma das vantagens dos metadados é restringir o universo onde será realizada a recuperação.

Por exemplo:

```
Pergunta:
"Como configurar o modelo X200?"
```

Podemos restringir:

```
modelo = X200
```

e somente depois realizar a recuperação semântica.

O Chroma utiliza o parâmetro `where` para realizar filtros por metadados.

Exemplo:

```
collection.query(
    query_texts=["Como configurar o equipamento?"],
    where={"modelo": "X200"}
)
```

Também podem ser combinados diversos filtros utilizando operadores como:

```
$and
$or
$eq
$gt
$gte
$lt
$lte
$in
$nin
```

**Fonte oficial — Metadata Filtering:**

https://docs.trychroma.com/docs/querying-collections/metadata-filtering

### Conceito importante

Os dois mecanismos possuem funções diferentes:

**Metadados**

```
"Onde devo procurar?"
```

**Embedding**

```
"Qual conteúdo é semanticamente mais próximo da pergunta?"
```

A combinação dos dois melhora a precisão da recuperação.

---

# Parte 5 — Chunking e estratégias de splitting

Os documentos precisam ser divididos em unidades menores para serem recuperados individualmente.

A documentação do LangChain divide as estratégias de splitting em diferentes categorias:

* baseadas na estrutura do texto;
* baseadas no tamanho;
* baseadas na estrutura do documento.

**Fonte oficial — Text Splitters:**

https://docs.langchain.com/oss/python/integrations/splitters

---

## RecursiveCharacterTextSplitter

Para documentos predominantemente textuais, uma boa estratégia inicial é utilizar:

```
RecursiveCharacterTextSplitter
```

O splitter tenta preservar unidades semanticamente maiores antes de realizar divisões menores.

Conceitualmente:

```
Parágrafo
    ↓
Sentença
    ↓
Palavra
    ↓
Caracteres
```

A documentação do LangChain recomenda o `RecursiveCharacterTextSplitter` como uma boa opção inicial para textos genéricos.

**Fonte oficial:**

https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter

---

## Chunk size

Não existe um tamanho universal de chunk.

Chunks muito pequenos podem:

* fragmentar informações relacionadas;
* perder contexto;
* aumentar a quantidade de vetores;
* aumentar armazenamento e processamento.

Chunks muito grandes podem:

* misturar assuntos;
* recuperar informações irrelevantes;
* diminuir a precisão da recuperação;
* consumir mais contexto posteriormente.

Por isso, diferentes valores devem ser testados.

Exemplo:

```
500 tokens
750 tokens
1000 tokens
1500 tokens
```

---

## Chunk overlap

O overlap permite que uma parte do conteúdo de um chunk seja repetida no próximo.

Exemplo:

```
Chunk 1
[--------------------]
             [--------------------]
                    Chunk 2
```

Isso reduz o risco de uma informação importante ser perdida por estar exatamente na fronteira entre dois chunks.

A documentação do `RecursiveCharacterTextSplitter` descreve `chunk_overlap` como uma forma de mitigar a perda de informação quando o contexto é dividido entre chunks.

**Fonte:**

https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter

---

## Splitting baseado em tokens

Quando é importante controlar o tamanho de acordo com os limites dos modelos, também é possível realizar splitting baseado em tokens.

**Fonte oficial:**

https://docs.langchain.com/oss/python/integrations/splitters/split_by_token

---

## Splitting baseado na estrutura

Documentos estruturados podem utilizar sua própria organização como parte da estratégia de chunking.

Exemplos:

```
Markdown → headers

HTML → tags

JSON → objetos

Código → funções/classes
```

Para documentos corporativos também podemos utilizar estruturas como:

```
títulos
capítulos
seções
cláusulas
parágrafos
blocos de diálogo
```

**Fonte oficial:**

https://docs.langchain.com/oss/python/integrations/splitters

---

## Preservação de metadados de seção

O LangChain possui, por exemplo, `MarkdownHeaderTextSplitter`, capaz de dividir documentos utilizando headers e preservar essas informações nos metadados.

Exemplo:

```
metadata={
    "Header 1": "Manual",
    "Header 2": "Configuração"
}
```

**Fonte oficial:**

https://docs.langchain.com/oss/python/integrations/splitters/markdown_header_metadata_splitter

Esse conceito é particularmente interessante para manuais e documentos estruturados.

---

## Como avaliar se o chunking foi adequado?

A estratégia deve ser avaliada utilizando perguntas conhecidas e verificando se os chunks que contêm as respostas são recuperados.

Algumas métricas possíveis:

* Recall@K;
* Precision@K;
* posição do chunk correto;
* relevância dos chunks recuperados;
* qualidade da resposta final.

A similaridade vetorial isoladamente não deve ser considerada prova suficiente de que o chunking está adequado.

Os metadados, por sua vez, fornecem **rastreabilidade**, permitindo identificar documento, seção, página e chunk utilizados.

---

# Parte 6 — Escolha dos modelos de embeddings

Foram considerados requisitos diferentes para RH e Suporte.

---

# RH — BGE-M3

## Modelo

```
BAAI/bge-m3
```

## Características

| Característica | BGE-M3                                            |
| -------------- | ------------------------------------------------- |
| Dimensão       | 1024                                              |
| Tamanho máximo | 8192 tokens                                       |
| Multilíngue    | Sim                                               |
| Idiomas        | Mais de 100                                       |
| Português      | Sim, dentro do suporte multilíngue                |
| Open source    | Sim                                               |
| Licença        | MIT                                               |
| Execução local | Sim                                               |
| Custo local    | Sem cobrança por token; depende da infraestrutura |

O BGE-M3 suporta três abordagens de recuperação:

* dense retrieval;
* sparse retrieval;
* multi-vector retrieval.

Também foi desenvolvido para trabalhar com textos de diferentes tamanhos, desde pequenas sentenças até documentos com 8192 tokens.

**Fonte principal — Hugging Face / BAAI:**

https://huggingface.co/BAAI/bge-m3

### Justificativa para RH

A execução local é especialmente interessante quando os documentos possuem informações confidenciais.

Exemplo:

```
Documentos RH
      ↓
   BGE-M3
   LOCAL
      ↓
  Embeddings
      ↓
  ChromaDB
   LOCAL
```

Isso permite construir uma arquitetura em que os documentos não precisam deixar a infraestrutura controlada pela organização.

---

# Suporte — Voyage 4 Large

## Modelo

```
voyage-4-large
```

## Características

| Característica        | Voyage 4 Large                                |
| --------------------- | --------------------------------------------- |
| Dimensão padrão       | 1024                                          |
| Dimensões disponíveis | 256, 512, 1024 e 2048                         |
| Contexto máximo       | 32.000 tokens                                 |
| Multilíngue           | Sim                                           |
| Português             | Sim, dentro do suporte multilíngue            |
| Open source           | Não                                           |
| API                   | Sim                                           |
| Custo                 | aproximadamente US$ 0,12 / 1 milhão de tokens |

A Voyage apresenta o modelo como sua opção de maior qualidade para recuperação generalista e multilíngue.

**Documentação oficial:**

https://docs.voyageai.com/docs/embeddings

---

## Preços Voyage AI

A documentação de preços informa atualmente aproximadamente:

```
voyage-4-large
US$ 0,12 / 1 milhão de tokens
```

A página também informa uma franquia inicial gratuita para determinados modelos da família Voyage 4.

Como preços podem mudar, essa informação deve sempre ser consultada novamente antes da implementação em produção.

**Fonte oficial:**

https://docs.voyageai.com/docs/pricing

---

# Modelo alternativo — OpenAI text-embedding-3-large

Também foi considerado:

```
text-embedding-3-large
```

A OpenAI apresenta esse modelo como seu modelo de embeddings de maior capacidade para tarefas em inglês e outros idiomas.

O preço publicado atualmente é aproximadamente:

```
US$ 0,13 / 1 milhão de tokens
```

**Fonte oficial:**

https://developers.openai.com/api/docs/models/text-embedding-3-large

---

## OpenAI — conceitos adicionais sobre embeddings

A documentação da OpenAI explica conceitos importantes utilizados durante o estudo, incluindo:

* embeddings como representação numérica de textos;
* utilização de bancos vetoriais para recuperação dos K vetores mais próximos;
* similaridade;
* redução de dimensões;
* embeddings multilíngues.

**Fonte oficial — FAQ de Embeddings:**

https://help.openai.com/pt-br/articles/6824809-faq-de-embeddings

---

# Relação entre embedding e chunking

O limite de entrada do modelo estabelece um limite técnico.

Exemplo:

```
BGE-M3
máximo = 8192 tokens

Voyage 4 Large
máximo = 32000 tokens
```

Entretanto:

> O tamanho máximo suportado pelo modelo não deve ser utilizado automaticamente como tamanho do chunk.

Um modelo aceitar 32.000 tokens não significa que um chunk de 30.000 tokens seja adequado para retrieval.

A estratégia de chunking deve ser definida pela qualidade da recuperação.

Portanto:

```
Limite do modelo
      ↓
Define o que é possível

Testes de retrieval
      ↓
Definem o que é adequado
```

---

# Privacidade — modelo local × API

A escolha entre execução local e API deve considerar a classificação das informações.

Para documentos altamente confidenciais:

```
Documento
   ↓
Modelo local
   ↓
Embedding
   ↓
Banco vetorial local
```

pode ser uma arquitetura apropriada quando existe a exigência de que o conteúdo não deixe a infraestrutura da organização.

Uma API externa não deve ser considerada automaticamente insegura. A decisão precisa considerar:

* políticas de retenção;
* contratos;
* criptografia;
* controle de acesso;
* governança;
* requisitos regulatórios;
* compliance;
* política interna da empresa.

---

# Resumo das principais fontes

## LangChain

**Text Splitters**

https://docs.langchain.com/oss/python/integrations/splitters

**RecursiveCharacterTextSplitter**

https://docs.langchain.com/oss/python/integrations/splitters/recursive_text_splitter

**Token-based splitting**

https://docs.langchain.com/oss/python/integrations/splitters/split_by_token

**Markdown Header Metadata Splitter**

https://docs.langchain.com/oss/python/integrations/splitters/markdown_header_metadata_splitter

**Document Loaders**

https://docs.langchain.com/oss/python/integrations/document_loaders/

---

## ChromaDB

**Adicionar documentos, embeddings e metadados**

https://docs.trychroma.com/docs/collections/add-data

**Metadata Filtering**

https://docs.trychroma.com/docs/querying-collections/metadata-filtering

---

## BGE-M3

**BAAI — Hugging Face**

https://huggingface.co/BAAI/bge-m3

---

## Voyage AI

**Embeddings**

https://docs.voyageai.com/docs/embeddings

**Pricing**

https://docs.voyageai.com/docs/pricing

---

## OpenAI

**text-embedding-3-large**

https://developers.openai.com/api/docs/models/text-embedding-3-large

**Embedding FAQ**

https://help.openai.com/pt-br/articles/6824809-faq-de-embeddings

---

# Conclusão

As referências utilizadas mostram que um pipeline RAG corporativo deve ser pensado como um conjunto de decisões relacionadas:

```
Documentos
    ↓
Carregamento
    ↓
Extração de metadados
    ↓
Chunking
    ↓
Embeddings
    ↓
Banco vetorial
    ↓
Filtros por metadata
    ↓
Retrieval
    ↓
LLM
    ↓
Resposta
    +
Rastreabilidade
```

A principal conclusão das atividades das Partes 1 a 6 é que **não existe uma configuração universal de RAG**.

A estratégia deve ser definida considerando:

* estrutura dos documentos;
* perguntas que precisam ser respondidas;
* metadados necessários;
* tamanho e estratégia dos chunks;
* modelo de embeddings;
* idioma;
* qualidade da recuperação;
* privacidade;
* custo;
* infraestrutura;
* rastreabilidade das respostas.

A qualidade final deve ser validada utilizando **documentos e perguntas representativos do cenário real da empresa**, e não apenas configurações padrão ou resultados de benchmarks.



