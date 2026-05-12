# Anotações de Aula: Arquitetura IoT

## 1. Sistemas Operacionais para IoT (RTOS)
Diferente dos sistemas convencionais (Windows/Linux), os SOs para IoT são projetados para dispositivos com recursos limitados (CPU e Memória).

*   **RTOS (Real-Time Operating System):** Sistemas focados em previsibilidade e tempo de resposta imediato.
*   **Características Principais:**
    *   **Pegada de Memória (Footprint):** Ocupam poucos KB de RAM/Flash.
    *   **Gerenciamento de Energia:** Modos de *Deep Sleep* para economizar bateria.
    *   **Escalabilidade:** Capazes de rodar em microcontroladores simples.
*   **Exemplos Comuns:** 
    *   **FreeRTOS:** O mais popular, código aberto.
    *   **Zephyr Project:** Focado em segurança e modularidade.
    *   **Contiki-NG:** Especializado em conectividade IP de baixa potência.

---

## 2. Requisitos Não Funcionais (RNF) em IoT
Os requisitos não funcionais definem *como* o sistema deve se comportar, indo além das funcionalidades básicas.

*   **Escalabilidade:** Capacidade de suportar a adição de milhares de novos sensores sem perda de desempenho.
*   **Latência:** Tempo entre a captura do dado e a ação (crítico em sistemas de saúde ou automotivo).
*   **Segurança:** Proteção de dados ponta a ponta (Criptografia, Autenticação).
*   **Interoperabilidade:** Capacidade de diferentes dispositivos e marcas "conversarem" entre si.
*   **Disponibilidade:** Garantia de que o sistema estará online 24/7, mesmo com falhas parciais.
*   **Consumo de Energia:** Crucial para dispositivos alimentados por bateria que devem durar anos.

---

## 3. Ecossistema Arduino na IoT
O Arduino atua como a camada de **Percepção/Atuação** na arquitetura IoT.

*   **O Microcontrolador:** Geralmente baseado em arquitetura AVR (ATmega) ou ARM (versões Pro/IoT).
*   **Componentes de Conectividade:**
    *   **Shields/Módulos:** Ethernet, Wi-Fi (ESP8266/ESP32), Bluetooth, LoRa.
    *   **Arduino Cloud:** Plataforma oficial para gerenciamento remoto e dashboards.
*   **Fluxo de Dados no IoT:**
    1.  **Input:** Sensores captam grandezas físicas (Temperatura, Umidade, Presença).
    2.  **Processamento:** O código no Arduino decide o que fazer ou formata o dado.
    3.  **Output/Transmissão:** Envia os dados via protocolos (como MQTT ou HTTP) para um Broker ou Nuvem.

---

## Dicas de Estudo
- [ ] Pesquisar a diferença entre **Single-tasking** vs **Multitasking** em microcontroladores.
- [ ] Praticar o envio de dados via protocolo **MQTT** usando uma placa ESP32 (compatível com Arduino IDE).
- [ ] Analisar o impacto da segurança no consumo de bateria (Criptografia gasta mais processamento).
