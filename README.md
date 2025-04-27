# ProPPAGA - Seleção de Ações do Ibovespa

Este projeto implementa a metodologia **PrOPPAGA** (Prioridade Observada a Partir da Presunção de Atitude Gaussiana das Alternativas) para a seleção de ações do índice Ibovespa. A metodologia foi desenvolvida para oferecer uma ferramenta simples e eficiente para estruturar decisões que envolvem múltiplos critérios.

## 📖 Sobre o ProPPAGA

O método PrOPPAGA (Prioridade Observada a Partir da Presunção de Atitude Gaussiana das Alternativas) é uma ferramenta de Apoio Multicritério à Decisão (AMD) voltada para problemas do tipo P·γ, que envolvem a ordenação de alternativas com base em múltiplos critérios. Ele presume que o desempenho das alternativas segue uma distribuição normal (gaussiana) dentro de cada critério, permitindo calcular prioridades relativas de forma simples e intuitiva, mesmo para decisores sem experiência técnica. 

Mais informações sobre a metodologia podem ser encontradas no site oficial: [ProPPAGA](https://www.proppaga.com.br/).

## 🚀 Funcionalidades

- **Web Scraping**: Coleta automática de dados financeiros das ações no site [Fundamentus](https://www.fundamentus.com.br/).
- **Limpeza e Tratamento de Dados**: Processamento dos dados coletados para garantir consistência e qualidade.
- **Cálculo de Cardinalidade**: Aplicação da metodologia ProPPAGA para ranquear as ações.
- **Análise por Setor**: Possibilidade de aplicar a metodologia em setores específicos, como Energia Elétrica, Intermediários Financeiros e Petróleo.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Bibliotecas**:
  - `pandas`: Manipulação e análise de dados.
  - `numpy`: Operações matemáticas e estatísticas.
  - `scipy`: Funções estatísticas avançadas.
  - `matplotlib` e `seaborn`: Visualização de dados.
  - `selenium`: Web scraping para coleta de dados.

