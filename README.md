# Análise de Desempenho Criptográfico

Projeto desenvolvido para a disciplina de Criptografia Aplicada da Pós-Graduação em Cibersegurança da PUCPR.

## Objetivo

O objetivo deste experimento é analisar o desempenho de diferentes algoritmos criptográficos, comparando:

- Criptografia Simétrica
- Criptografia Assimétrica
- Impacto do tamanho das chaves
- Tempo de geração de chaves
- Tempo de cifragem e decifragem

## Algoritmos Testados

### RSA
- RSA 1024
- RSA 2048
- RSA 4096
- RSA 8192

### ECC
- ECC 256 bits

### AES
- AES 128
- AES 256

### DES / 3DES
- DES 56 bits
- 3DES 112 bits
- 3DES 168 bits

---

## Ambiente Utilizado

| Item | Descrição |
|---|---|
| Processador | Ryzen 7 5800X3D |
| Memória RAM | 32GB DDR4 3200MHz |
| GPU | RX 9060 XT |
| Sistema Operacional | Windows 11 25H2 |
| Linguagem | Python 3.14.3 |
| Biblioteca | cryptography |

## Instale as dependências

- pip install cryptography

## Execute o script

- python3 atividade.py

## Metodologia

Cada algoritmo foi executado três vezes para minimizar inconsistências causadas por:
- Cache do sistema operacional;
- Inicialização de bibliotecas;
- Warmup da CPU;
- Backend criptográfico;

Foram medidos:
- Tempo de geração das chaves;
- Tempo de cifragem;
- Tempo de decifragem/verificação;

## Resultados Obtidos
Algoritmo	Execução 1 (s)	Execução 2 (s)	Execução 3 (s)	Média (s)
RSA 1024	0.010314	0.009336	0.012771	0.010807
RSA 2048	0.046164	0.019201	0.031495	0.032286
RSA 4096	0.595016	0.516897	0.485707	0.532540
RSA 8192	1.340084	9.481645	9.564805	6.795511
ECC 256	0.005982	0.000187	0.000168	0.002112
AES 128	0.007181	0.000047	0.000039	0.002423
AES 256	0.000035	0.000040	0.000028	0.000034
DES 56	0.000154	0.000044	0.000040	0.000079
3DES 112	0.000166	0.000047	0.000042	0.000085
3DES 168	0.000039	0.000039	0.000031	0.000036

## Conclusões
- Algoritmos simétricos apresentaram desempenho significativamente superior.
- RSA apresentou crescimento exponencial no tempo de execução conforme aumento do tamanho das chaves.
- ECC demonstrou excelente equilíbrio entre segurança e desempenho.
- AES apresentou o melhor desempenho geral.
- DES e 3DES são considerados algoritmos legados e obsoletos para aplicações modernas.

## Referências
- STALLINGS, William. Criptografia e Segurança de Redes.
- TANENBAUM, Andrew S. Redes de Computadores.
- https://cryptography.io/
- https://www.nist.gov/
- https://datatracker.ietf.org/doc/html/rfc8017

## Autor

Adão Correa da Costa Júnior
Especialização em Cibersegurança — PUCPR