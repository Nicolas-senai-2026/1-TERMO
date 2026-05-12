# Notas de Aula: Arquitetura IoT

## 1. Fundamentos do Sistema Operacional: Debian
O Debian é uma das distribuições Linux mais populares para projetos de IoT devido à sua estabilidade, segurança e vasta gama de pacotes suportados.

### Por que Debian em IoT?
*   **Estabilidade:** Ciclos de lançamento rigorosos garantem um sistema robusto para dispositivos de campo.
*   **Versatilidade:** Roda em diversas arquiteturas (ARM, x86, MIPS), essencial para diferentes hardwares IoT.
*   **Repositório Amplo:** Facilidade para instalar ferramentas de rede, MQTT brokers e runtimes de linguagens.

### Comandos Essenciais (Cheat Sheet)
*   `sudo apt update && sudo apt upgrade`: Atualiza a lista de pacotes e o sistema.
*   `ip addr show`: Verifica interfaces de rede e endereços IP.
*   `systemctl status [serviço]`: Gerencia processos de fundo (daemons).
*   `df -h`: Verifica o espaço em disco (crítico em sistemas embarcados).

---

## 2. Requisitos de Sistema em IoT
Ao projetar a arquitetura de um dispositivo ou rede IoT, dividimos as necessidades em requisitos funcionais e não funcionais.

### 2.1. Requisitos Funcionais
Descrevem **o que** o sistema deve fazer (as funcionalidades diretas).
*   **Coleta de Dados:** O sistema deve ler a temperatura do sensor X a cada 5 segundos.
*   **Atuação Remota:** O usuário deve ser capaz de ligar/desligar uma lâmpada via aplicativo.
*   **Notificações:** Enviar um alerta via e-mail se a umidade do solo estiver abaixo de 20%.
*   **Armazenamento Local:** Logar dados em um cartão SD caso a conectividade caia.

### 2.2. Requisitos Não Funcionais
Descrevem **como** o sistema deve operar (características de qualidade).
*   **Desempenho (Latência):** O tempo de resposta entre o sensor e o alerta não deve exceder 200ms.
*   **Consumo de Energia:** O dispositivo deve operar por 2 anos com uma bateria CR2032 (Modo Deep Sleep).
*   **Segurança:** Toda a comunicação entre o gateway e a nuvem deve ser criptografada via TLS/SSL.
*   **Escalabilidade:** A arquitetura deve suportar o acréscimo de até 1.000 sensores sem perda de pacotes.
*   **Disponibilidade:** O sistema deve estar online 99,9% do tempo.

---

## 3. Atividade Prática / Reflexão
1. Identifique no seu hardware (Raspberry Pi/BeagleBone) a versão do Debian instalada (`cat /etc/debian_version`).
2. Liste 3 requisitos não funcionais prioritários para um sistema de monitoramento hospitalar IoT.
