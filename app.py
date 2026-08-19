import streamlit as st
from caixa import adicionar_movimentacao, calcular_saldo
import pandas as pd

st.set_page_config(
    page_title="Sistema Financeiro",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Sistema de Gestão de Entradas e Saídas")

if "movimentacoes" not in st.session_state:
    st.session_state.movimentacoes = []

st.header("Cadastro de Movimentação")

tipo = st.selectbox(
    "Tipo",
    ["Entrada", "Saída"]
)

descricao = st.text_input(
    "Descrição"
)

valor = st.number_input(
    "Valor (R$)",
    min_value=0.0,
    step=0.01
)

if st.button("Adicionar Movimentação"):

    if descricao != "" and valor > 0:

        adicionar_movimentacao(
            st.session_state.movimentacoes,
            tipo,
            descricao,
            valor
        )

        st.success("Movimentação cadastrada com sucesso!")

    else:
        st.warning("Preencha todos os campos.")

st.divider()

saldo = calcular_saldo(st.session_state.movimentacoes)

st.metric(
    label="Saldo Atual",
    value=f"R$ {saldo:.2f}"
)

st.divider()

st.header("Histórico de Transações")

if len(st.session_state.movimentacoes) > 0:

    for mov in st.session_state.movimentacoes:
        st.write(
            f"📌 {mov['Tipo']} | "
            f"{mov['Descrição']} | "
            f"R$ {mov['Valor']:.2f}"
        )

else:
    st.info("Nenhuma movimentação cadastrada.")