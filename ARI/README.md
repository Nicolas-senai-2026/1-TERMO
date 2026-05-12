# 🏛️ Curso: Arquitetura e Desenvolvimento IoT
**Foco:** Arduino, Linguagens de Programação (C++ e Python)

---

## 📌 Ementa do Curso
Este curso aborda os fundamentos da Internet das Coisas (IoT), desde a aquisição de dados com sensores, passando pelo processamento no dispositivo (Edge), até a comunicação com a nuvem.

### 🎯 Objetivos de Aprendizagem
*   Compreender a arquitetura de sistemas IoT (Dispositivo -> Gateway -> Nuvem).
*   Programar microcontroladores usando Arduino (C/C++).
*   Implementar scripts de automação e análise com Python.
*   Conectar dispositivos à internet (MQTT/HTTP).

---

## 📚 Conteúdo Programático

### Módulo 1: Introdução à IoT e Arduino (C++)
*   **O que é IoT:** Sensores, atuadores e arquitetura.
*   **Plataforma Arduino:** Hardware (Uno, Nano, ESP32).
*   **Arduino IDE:** Estrutura do código (`setup` e `loop`).
*   **Linguagem C++ para IoT:**
    *   Variáveis, Tipos de Dados (`int`, `float`, `char`, `bool`).
    *   Estruturas de Controle (`if`, `else`, `switch`).
    *   Laços de Repetição (`for`, `while`).
    *   Manipulação de Pinos (Digital/Analógico, `pinMode`, `digitalWrite`, `analogRead`).
*   **Projetos Práticos:** Piscar LED (Blink), Leitura de Sensor de Temperatura (DHT11/22).

### Módulo 2: Conectividade e Protocolos (ESP32)
*   **ESP32:** Introdução ao Wi-Fi e Bluetooth.
*   **Protocolo HTTP:** Envio de dados para APIs.
*   **Protocolo MQTT:** Comunicação leve (Broker, Publish, Subscribe).
*   **JSON:** Estruturação de dados IoT.

### Módulo 3: Python na IoT e Edge Computing
*   **Por que Python em IoT?** Uso em Gateways (Raspberry Pi) e análise de dados.
*   **Sintaxe Python:** Variáveis, Listas, Dicionários.
*   **Bibliotecas essenciais:** `paho-mqtt`, `requests`, `serial`.
*   **Projetos Práticos:**
    *   Lendo dados da Serial do Arduino com Python.
    *   Enviando dados para nuvem (ThinkSpeak/AWS IoT) via Python.

### Módulo 4: Arquitetura Final e Projeto Integrador
*   **Dashboard:** Visualização de dados (Grafana/Node-RED).
*   **Segurança:** Básico sobre segurança em IoT.
*   **Projeto Final:** Sistema de Monitoramento Ambiental (Arduino + ESP32 + Python/Cloud).

---

## 🛠️ Ferramentas e Pré-requisitos
1.  **Arduino IDE:** [Download](https://arduino.cc)
2.  **Python:** [Download](https://python.org)
3.  **Hardware sugerido:** Kit Iniciante Arduino + ESP32.

---

## 🔗 Referências Úteis
*   [Documentação Oficial Arduino](https://arduino.cc)
*   [Documentação Python](https://python.org)
*   [Wokwi - Simulador de IoT](https://wokwi.com)

---
> 💡 *Dica: Pratique a conversão de dados entre C++ (no microcontrolador) e Python (no servidor).*
