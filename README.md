# Projeto Data Engineering – Olist E-commerce

## 📖 Visão Geral
Este projeto tem como objetivo construir uma **arquitetura completa de Engenharia de Dados**, partindo de dados brutos do e-commerce Olist até a entrega de dados analíticos modelados em **Star Schema**, prontos para consumo por ferramentas de BI.

O projeto foi desenvolvido com foco em **boas práticas de mercado**, cobrindo todo o ciclo de dados: ingestão, organização de camadas, infraestrutura como código, orquestração, transformações, modelagem dimensional e qualidade de dados.

---

## 🧱 Arquitetura do Projeto

### 🔄 Fluxo de Dados

1. **Fonte**
   - Dataset público do Olist (arquivos CSV)

2. **Data Lake (GCP – Google Cloud Storage)**
   - **RAW**  
     - Armazenamento dos dados brutos, sem qualquer transformação  
     - Fidelidade total à fonte  
     - Organização por data de carga  

3. **Data Warehouse (Google BigQuery)**
   - **Silver**
     - Tipagem correta
     - Padronização de nomes
     - Limpeza básica de dados
   - **Staging**
     - Camada intermediária
     - Aplicação de regras de negócio
     - Preparação para modelagem dimensional
   - **Gold**
     - Modelagem analítica 
     - Tabelas fato e dimensão
   - **Views (VW)**
     - Agregações
     - Métricas de negócio
     - Camada semântica para consumo por BI

4. **Infraestrutura como Código**
   - Provisionamento dos recursos na GCP 

5. **Orquestração**
   - Apache Airflow

---

## 🏗️ Infraestrutura como Código (Terraform)

Toda a infraestrutura do projeto é criada e versionada utilizando **Terraform**

### Recursos provisionados
- Buckets no Google Cloud Storage (Data Lake – RAW)
- Datasets no BigQuery (Silver, Gold)
- Estrutura base para tabelas e views
- Organização e controle dos recursos em ambiente cloud

---

## 🔁 Orquestração (Apache Airflow)

O Apache Airflow é responsável por orquestrar todo o pipeline de dados, incluindo:

- Ingestão dos arquivos CSV para o Data Lake (RAW)
- Carga dos dados do GCS para o BigQuery (Silver)
- Processamento das camadas Staging e Gold
- Atualização das Views analíticas

### Características dos DAGs
- Controle de falhas com retries
- Logs centralizados
- Separação clara por etapa do pipeline
- Facilidade de manutenção e escalabilidade

---

## 🧪 Qualidade de Dados

A qualidade dos dados é garantida por meio de testes, com foco na confiabilidade da camada analítica.

### Tipos de validações
- `not_null`
- `unique`
- testes de chave composta
- consistência entre fatos e dimensões

---

## 📊 Modelagem de Dados

A camada **Gold** segue o padrão **Star Schema**, facilitando consultas analíticas e melhorando a performance.

### Tabelas Fato
- fVendas
- fPagamentos

### Tabelas Dimensão
- dClientes
- dProdutos
- dVendedores
- dCalendario

### Views (VW)
As Views atuam como camada semântica, sendo utilizadas para:
- Métricas consolidadas
- Análises por período
- Consumo direto por ferramentas de BI
