# 🌐 Arquitetura IoT (Internet of Things)
## Plano de Estudos e Notas de Aula

Este documento centraliza o conteúdo programático e os registros das aulas focadas em desenvolvimento e arquitetura para soluções IoT.

---

### 🐍 1. Programação com Python
*Foco: Lógica e integração com hardware.*

- **Fundamentos:** Variáveis, tipos de dados e estruturas de repetição.
- **Manipulação de Dados:** Listas, dicionários e Tuplas.
- **Bibliotecas IoT Comuns:**
  - `paho-mqtt` (Protocolo MQTT)
  - `requests` (Consumo de APIs HTTP)
  - `RPi.GPIO` ou `MicroPython` (Controle de sensores/atuadores)
- **JSON:** Serialização e desserialização de dados de sensores.

---

### 📂 2. Controle de Versão (Git & GitHub)
*Foco: Colaboração e versionamento de firmware e software.*

- **Conceitos Git:** `init`, `add`, `commit`, `push`, `pull`.
- **Fluxo de Trabalho:** Uso de Branches (`git branch`, `checkout`) para novas funcionalidades.
- **GitHub:**
  - Gerenciamento de Repositórios.
  - Pull Requests e Code Review.
  - Uso de `.gitignore` (essencial para ignorar arquivos de configuração local).

---

### ✨ 3. Clean Code (Código Limpo)
*Foco: Manutenibilidade em sistemas de longo prazo.*

- **Nomes Significativos:** Variáveis e funções que revelam sua intenção.
- **Funções Pequenas:** Cada função deve fazer apenas uma coisa (Princípio da Responsabilidade Única).
- **Comentários:** Usar apenas o necessário; o código deve ser autoexplicativo.
- **Tratamento de Erros:** Uso de `try/except` para evitar que o dispositivo trave em campo.

---

### 🏗️ 4. Arquitetura e Projetos
*Foco: Visão sistêmica do ecossistema IoT.*

- **Camadas da Arquitetura:**
  1. **Percepção:** Sensores e Atuadores.
  2. **Rede/Transporte:** Wi-Fi, LoRaWAN, Zigbee, Bluetooth.
  3. **Processamento:** Gateway e Edge Computing.
  4. **Aplicação:** Dashboards e Nuvem (AWS, Azure, Google Cloud).
- **Projetos Práticos:**
  - [ ] **Projeto 1:** Monitor de Temperatura via MQTT com Python.
  - [ ] **Projeto 2:** Automação de Iluminação com controle via GitHub Actions (CI/CD simples).
  - [ ] **Projeto Final:** Protótipo de Smart City com integração de múltiplos sensores.

---

### 🔗 Links Úteis
- [Documentação Oficial Python](https://python.org)
- [Guia Prático de Git](https://github.io)
- [Principais Protocolos IoT](https://mqtt.org)
