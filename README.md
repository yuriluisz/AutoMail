
---

# Automail - Automatizando emails da SEPLAG

**Automail** é um projeto de automação desenvolvido em Python para facilitar processos administrativos da SEPLAG (Secretaria de Planejamento e Gestão de Mato Grosso). O principal objetivo é agilizar o envio de relatórios de ponto de diversos órgãos estaduais, processando uma planilha massiva com mais de 800 mil linhas e separando os dados automaticamente por órgão em arquivos individuais.

---

## 🚀 Funcionalidades 

- **Filtragem automatizada de dados**: Processa uma planilha principal e separa as informações por órgão em várias outras planilhas.
- **Interface gráfica com Tkinter**: Proporciona uma interface amigável para o uso do sistema.
- **Envio de e-mails automatizado com SMTP**: Planejado para enviar os relatórios processados diretamente aos destinatários de cada órgão.
- **Integração com Pandas**: Gerenciamento e manipulação eficiente de grandes volumes de dados.

---

## 📋 Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas para rodar o projeto:

- Python 3.8 ou superior
- Bibliotecas:
  - `tkinter` (para interface gráfica)
  - `pandas` (para manipulação de dados)
  - `smtplib` (para envio de e-mails)

---

## ⚙️ Como executar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/yuriluisz/AutoMail.git
   ```
2. Instale os pacotes necessários:
   ```bash
   pip install pandas
   ```
3. Execute o script principal:
   ```bash
   python automail.py
   ```

4. Siga as instruções na interface gráfica para carregar a planilha principal e iniciar o processamento. (Localizada na pasta "dist")

---

## 🛠️ Status do Projeto

O desenvolvimento está **80% concluído**, com os seguintes pontos já implementados:

- [x] Estrutura de filtragem por órgão concluída.
- [x] Divisão de planilhas automatizada funcionando.
- [x] Interface gráfica inicial criada.
- [ ] Envio de Emails para os responsáveis de cada orgão.

**Limitantes atuais**:
Devido a **restrições de rede e firewall** da SEPLAG e à falta de acesso à equipe de TI, o módulo de envio automático de e-mails ainda não foi integrado. No entanto, a filtragem e divisão dos dados já estão praticamente finalizadas e funcionando conforme o esperado.

---

## 🖇️ Contribuições

Contribuições são bem-vindas! Caso tenha interesse em colaborar com a finalização do projeto, especialmente na integração do envio de e-mails ou otimização de performance, sinta-se à vontade para abrir um _Pull Request_.

---

## ✒️ Autor

**Yuri Luis** - Estágiario SEPLAG  
Atualmente, desenvolvendo soluções administrativas para a SEPLAG.

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Sinta-se à vontade para alterar ou adicionar informações conforme necessário.