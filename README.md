#  Protótipo Funcional: Sistema de Monitoramento e Controle Solar Residencial (SPRINT 3)

##  Visão Geral do Projeto

Este projeto consiste na simulação funcional de um sistema de energia solar inteligente para uma residência. O objetivo principal do **SPRINT 3** é demonstrar a **integração técnica e a sinergia** entre a geração de energia renovável (solar simulada), o armazenamento (baterias), a automação residencial e a visualização de dados em tempo real.

O protótipo utiliza Python e Streamlit para criar um Dashboard interativo que simula o funcionamento de um **Inversor Goodwe** e o controle de aparelhos domésticos.

## 🏗️ Esquema Detalhado de Integração dos Componentes

O sistema é modular, onde cada função em Python simula um componente real, garantindo a integração funcional. **A tabela abaixo detalha a sinergia entre os componentes e o fluxo de dados:**

| Componente da Casa | Simulação (Código Python) | Fluxo de Dados e Integração |
| :--- | :--- | :--- |
| **Painel Solar (Geração)** | `casa_inteligente.simular_energia_solar()` | Gera a potência (W) de acordo com a hora do sistema (simulando a radiação solar). |
| **Sensores de Consumo** | `casa_inteligente.calcular_consumo_total()` | Coleta a soma da potência (W) de todos os aparelhos com `estado = 'Ligado'`. |
| **Inversor Goodwe (Lógica Central)** | `casa_inteligente.atualizar_bateria()` | Recebe (Geração - Consumo) e decide o fluxo: **carregar** a bateria se positivo, **descarregar** se negativo, ou usar a **Rede Elétrica** se a bateria estiver vazia. |
| **Baterias** | Variável `self.nivel_bateria` | Armazena o saldo energético. Sua porcentagem é exibida e influencia a decisão do Inversor sobre o uso da Rede. |
| **Automação** | `app.toggle_aparelho()` | A ação do usuário (clicar no botão) altera o estado de um aparelho, o que força um novo cálculo de Consumo Total, **integrando a automação ao fluxo de energia**. |
| **HMI (Dashboard)** | `app.py` (Streamlit) | Exibe as métricas calculadas pelo Inversor e o **Gráfico em Tempo Real** (`st.line_chart`) dos dados de Geração e Consumo. |
| Critério Atendido no SPRINT 3 | Descrição |
| :--- | :--- |
| **Integração e Funcionamento** | Demonstração da alteração de consumo (Automação) e seu impacto imediato no nível da bateria (Inversor). |
| **Visualização de Dados** | Dashboard com métricas em tempo real e gráfico de potência (Geração vs. Consumo). |
| **Documentação Técnica** | Esquema de integração detalhado e justificativa das escolhas. |

---

OBS: Para rodar a simulação digitar no terminal streamlit run app.py

Integrantes : 

Miguel Vanucci Delgado RM- 563491

João Vitor Lima Caldeira RM- 566541

Igor Zuvela Villaça Felicio RM- 563602

Giovanna Fernandes Pereira RM- 565434
