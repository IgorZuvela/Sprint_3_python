#  Protótipo Funcional: Sistema de Monitoramento e Controle Solar Residencial (SPRINT 3)

##  Visão Geral do Projeto

Este projeto consiste na simulação funcional de um sistema de energia solar inteligente para uma residência. O objetivo principal do **SPRINT 3** é demonstrar a **integração técnica e a sinergia** entre a geração de energia renovável (solar simulada), o armazenamento (baterias), a automação residencial e a visualização de dados em tempo real.

O protótipo utiliza Python e Streamlit para criar um Dashboard interativo que simula o funcionamento de um **Inversor Goodwe** e o controle de aparelhos domésticos.

Esquema Detalhado de Integração dos Componentes
O sistema é modular, onde cada função em Python simula um componente real, garantindo a integração funcional.

Componente Real	Simulação em Código	Função no Sistema
Painel Solar (Geração)	Função simular_energia_solar()	Simula a geração de potência com base na hora do dia (referência PVWatts/NREL).
Inversor Goodwe	Funções de cálculo de fluxo e variáveis de saldo	Gerencia o saldo energético (Geração - Consumo) e decide carregar/descarregar a bateria.
Baterias	Variável self.nivel_bateria	Armazena o excedente de energia para uso noturno ou em momentos de pico.
Sensores de Consumo	Função calcular_consumo_total()	Calcula o consumo em tempo real de todos os aparelhos ligados.
Automação	Função toggle_aparelho() e Botões do Streamlit	Permite que o usuário (ou um sistema automatizado) ligue/desligue aparelhos.
HMI (Visualização)	st.line_chart e st.metric	Apresenta o fluxo de energia e o histórico de potência de forma intuitiva.

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
