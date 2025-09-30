
import random
from datetime import datetime


class SmartHome:
    def __init__(self):
        # Simulação dos Aparelhos com estados e consumo em Watts
        self.aparelhos = {
            "Geladeira": {"estado": "Ligado", "consumo": 150},
            "Chuveiro": {"estado": "Desligado", "consumo": 5000},
            "Ar Condicionado": {"estado": "Desligado", "consumo": 1200},
            "Luzes Sala": {"estado": "Desligado", "consumo": 80},
        }
        self.capacidade_bateria = 10000  # Wh (Watt-hora)
        self.nivel_bateria = 7000  # Wh (70% inicial)
        self.taxa_carga_max = 2000  # W (Limite de carga do inversor)

    def simular_energia_solar(self):
        """Simula a geração de energia solar baseada na hora do dia (simulando Painel Solar)."""
        hora_atual = datetime.now().hour

        # Simulação de geração apenas entre 8h e 17h
        if 8 <= hora_atual <= 17:
            pico = 2500  # Capacidade máxima do painel simulado (W)
            variacao = random.randint(-200, 200)  # Simula variações climáticas

            # Fator de multiplicação baseado na hora
            if hora_atual <= 12:
                fator = (hora_atual - 8) / 4
            else:
                fator = (17 - hora_atual) / 5

            geracao = max(0, pico * fator + variacao)
            return int(geracao)
        return 0

    def calcular_consumo_total(self):
        """Calcula o consumo total de todos os aparelhos ligados (simulando Sensores de Consumo)."""
        consumo_total = 0
        for nome, dados in self.aparelhos.items():
            if dados["estado"] == "Ligado":
                # Adiciona variação aleatória para simular vida real
                variacao = random.uniform(0.9, 1.1)
                consumo_total += dados["consumo"] * variacao
        return int(consumo_total)

    def atualizar_bateria(self, geracao_solar, consumo_total):
        """Simula a carga/descarga da bateria (simulando o Inversor/Bateria)."""

        saldo = geracao_solar - consumo_total
        gasto_rede = 0

        # 1. Carregamento
        if saldo > 0:
            carga_aplicada = min(saldo, self.taxa_carga_max)
            self.nivel_bateria += carga_aplicada / 3600  # Simula "tick" de tempo
            self.nivel_bateria = min(self.nivel_bateria, self.capacidade_bateria)

        # 2. Descarga
        elif saldo < 0:
            descarga = abs(saldo) / 3600

            # Tenta usar a bateria
            if self.nivel_bateria > 0:
                self.nivel_bateria = max(0, self.nivel_bateria - descarga)

            # Se a bateria zerou, usa a rede elétrica
            if self.nivel_bateria == 0:
                gasto_rede = abs(saldo)  # Déficit coberto pela Rede Elétrica

        # Nível da bateria em porcentagem
        nivel_percentual = int((self.nivel_bateria / self.capacidade_bateria) * 100)

        return nivel_percentual, gasto_rede

    def controlar_aparelho(self, nome, novo_estado):
        """Muda o estado de um aparelho (Automação)."""
        if nome in self.aparelhos and novo_estado in ["Ligado", "Desligado"]:
            self.aparelhos[nome]["estado"] = novo_estado
            return f"{nome} alterado para {novo_estado}."
        return f"Aparelho {nome} ou estado {novo_estado} inválido."