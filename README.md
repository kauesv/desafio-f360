## Descrição

Proposto pela empresa [F360](https://f360.com.br/), estes desafios visam avaliar tecnicamente os candidatos ao processo seletivo para a vaga de **Desenvolvedor Python PL**.

## Sobre os Desafios
- Desafio 1: Integração com um Serviço de Terceiros.

Neste desafio, você deve integrar uma API de clima, processar e exibir as informações meteorológicas obtidas, implementar um sistema de cache para otimizar o uso da API e garantir o tratamento adequado de possíveis erros.

- Desafio 2: Manipulação e Análise de Dados.

Esse desafio é dividido em duas partes. A primeira parte envolve carregar e analisar dados de vendas usando a biblioteca Pandas, incluindo a filtragem e exportação dos resultados. A segunda parte foca em analisar e visualizar os dados para entender o comportamento dos clientes e as tendências de vendas.

- Desafio 3: Desenvolvimento de Algoritmos.

Aqui, você precisa desenvolver uma função para encontrar a maior soma de um subarray contínuo em uma lista de valores de transações. A função deve ser otimizada para eficiência e acompanhada de testes unitários para validar seu desempenho em diferentes cenários.

## Passo a passo para rodar os desafios
### 1. Arquivo .env
- Altere o arquivo .env que esta na raiz com suas APIs:
```
APIKEY_1=SUA_CHAVE_API_DO_OPENWEATHERMAP
APIKEY_2=SUA_CHAVE_API_DO_WEATHERSTACK
```

### 2. Libere a execução dos containers
- No arquivo docker-compose.yml os 3 desafios estão comentados, libere apenas os que você deseja executar

### 3. Execute os containers
- Execute o docker-compose:
    ```
    $  docker-compose up --build -d
    ```

## Contato

Para mais informações ou para discutir qualquer um dos repositórios, sinta-se à vontade para entrar em contato:

- **Email:** [kauesousavieira534@gmail.com](mailto:kauesousavieira534@gmail.com)
- **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/kaue-sousa-vieira/)

---
Obrigado por visitar meu repositório!
