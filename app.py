import streamlit as st
import pandas as pd
from casa_inteligente import SmartHome
from datetime import datetime, timedelta


st.set_page_config(layout="wide", page_title="Smart Home Sprint 3 - Real Time")



def carregar_estado():
    if 'home' not in st.session_state:
        st.session_state.home = SmartHome()


    if 'log_potencia' not in st.session_state:

        historico_tempo = [datetime.now() - timedelta(minutes=i) for i in range(5, 0, -1)]
        st.session_state.log_potencia = pd.DataFrame({
            'Tempo': historico_tempo,
            'Geração Solar (W)': [0] * 5,
            'Consumo Total (W)': [0] * 5
        })
    return st.session_state.home



def toggle_aparelho(nome):
    home = carregar_estado()
    estado_atual = home.aparelhos[nome]["estado"]
    novo_estado = "Desligado" if estado_atual == "Ligado" else "Ligado"
    home.controlar_aparelho(nome, novo_estado)
    st.rerun()


# --- Função de Log de Dados ---
def registrar_log(geracao, consumo):
    """Adiciona a leitura atual ao log e remove a leitura mais antiga."""
    log = st.session_state.log_potencia


    novo_log = pd.DataFrame({
        'Tempo': [datetime.now()],
        'Geração Solar (W)': [geracao],
        'Consumo Total (W)': [consumo]
    })


    st.session_state.log_potencia = pd.concat([log.iloc[1:], novo_log], ignore_index=True)



st.title("🏡 Protótipo Funcional - Smart Solar Home (SPRINT 3)")
st.caption(f"Simulação de Dados em Tempo Real: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

st.markdown("---")


st.header("1. Fluxo de Energia e Histórico de Potência")

home = carregar_estado()


geracao_solar = home.simular_energia_solar()
consumo_total = home.calcular_consumo_total()
nivel_bateria_perc, gasto_rede = home.atualizar_bateria(geracao_solar, consumo_total)


registrar_log(geracao_solar, consumo_total)


col_gen, col_con, col_bat, col_rede = st.columns(4)

col_gen.metric(
    label="⚡ Geração Solar (W) - (Referência PVWatts)",
    value=f"{geracao_solar:,}".replace(",", ".")
)
col_con.metric(
    label="🏠 Consumo Total (W)",
    value=f"{consumo_total:,}".replace(",", ".")
)
col_bat.metric(
    label="🔋 Nível da Bateria",
    value=f"{nivel_bateria_perc}%",
    delta=f"Capacidade: {int(home.nivel_bateria):,} Wh".replace(",", ".")
)
col_rede.metric(
    label="🌐 Gasto da Rede (W)",
    value=f"{gasto_rede:,}".replace(",", "."),
    delta_color="inverse",
    delta="Cuidado! Usando a Rede." if gasto_rede > 0 else "Energia 100% Própria."
)

st.subheader("Gráfico de Potência em Tempo Real")

st.line_chart(
    st.session_state.log_potencia,
    x='Tempo',
    y=['Geração Solar (W)', 'Consumo Total (W)'],
    use_container_width=True
)

st.markdown("---")


st.header("2. Controle e Status dos Aparelhos (Automação)")
st.caption("Altere o estado de um aparelho e veja o consumo mudar no gráfico acima!")

cols = st.columns(len(home.aparelhos))
i = 0

for nome, dados in home.aparelhos.items():
    comsumo_exibicao = f"({dados['consumo']}W)" if nome != "Geladeira" else "(Var.)"

    with cols[i]:
        st.subheader(nome)
        emoji = "🟢" if dados["estado"] == "Ligado" else "🔴"
        st.info(f"{emoji} **Status:** {dados['estado']} {comsumo_exibicao}")

        if st.button(f"Alternar Estado ({nome})", key=f"btn_{nome}"):
            toggle_aparelho(nome)

    i += 1

st.markdown("---")


st.header("3. Análise de Eficiência Energética e Logs de Dados")

saldo_energetico = geracao_solar - consumo_total

st.markdown(f"**Saldo Atual:** **{saldo_energetico}W** (Geração - Consumo)")

if saldo_energetico > 0:
    st.success(
        f"✅ **Superávit de Energia!** Geração Solar está {saldo_energetico}W acima do consumo. A **Bateria** está sendo carregada com a energia excedente.")
    st.info(
        f"O inversor está enviando a carga de bateria: {min(saldo_energetico, home.taxa_carga_max)}W (limitado pelo inversor).")

elif saldo_energetico < 0:
    if nivel_bateria_perc > 0:
        st.warning(
            f"⚠️ **Déficit de Energia!** A casa está consumindo {abs(saldo_energetico)}W a mais do que gerando. A energia está sendo puxada da **Bateria** para manter a casa ligada.")
    else:
        st.error(
            f"🚨 **BATERIA ZERADA!** Consumo de {abs(saldo_energetico)}W está sendo puxado diretamente da **Rede Elétrica**. Priorize a economia ou aguarde o pico solar.")

else:
    st.info("Sistema em equilíbrio. Geração e consumo se anulam no momento.")


st.subheader("Tabela de Histórico de Potência (Log)")
st.dataframe(
    st.session_state.log_potencia.sort_values(by='Tempo', ascending=False),
    hide_index=True
)