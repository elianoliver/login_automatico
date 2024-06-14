# Google Login Automation Script

Este script automatiza o processo de login no Google em uma janela anônima do Chrome e navega até o link do Google Remote Desktop.

## Pré-requisitos

1. **Python 3.x** - Certifique-se de ter o Python instalado em sua máquina.
2. **Bibliotecas Python necessárias**:
    - `pyautogui`
    - `python-dotenv`
3. **Google Chrome** - O script foi projetado para funcionar com o Google Chrome instalado nos caminhos padrão:
    - `C:\Program Files\Google\Chrome\Application\chrome.exe`
    - `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`

## Instalação

1. Clone este repositório ou copie os arquivos necessários para seu diretório local.

2. Instale as dependências Python:

    ```sh
    pip install pyautogui python-dotenv
    ```

3. Crie um arquivo `.env` no mesmo diretório que o script Python com as seguintes variáveis:

    ```plaintext
    EMAIL=seu_email@gmail.com
    SENHA=sua_senha_secreta
    ```

## Uso

1. Execute o script diretamente no Python:

    ```sh
    python seu_script.py
    ```

2. Para criar um executável do script, use o PyInstaller. Certifique-se de estar no diretório onde o script Python e o arquivo `.env` estão localizados:

    ```sh
    pyinstaller --onefile --add-data ".env;." seu_script.py
    ```

    Isso gerará um executável na pasta `dist`, que pode ser executado de qualquer local no sistema.

## Funcionalidades

1. **Abrir o Google Chrome em modo anônimo**: O script tenta localizar o executável do Chrome nos caminhos padrão e o abre em uma janela anônima.
2. **Login no Google**: O script navega até a página de login do Google e insere as credenciais fornecidas no arquivo `.env`.
3. **Navegar até o Google Remote Desktop**: Após o login, o script abre uma nova aba e navega até o link do Google Remote Desktop.

## Observações

- Certifique-se de que o Google Chrome está instalado em um dos caminhos padrão especificados no script. Se o Chrome estiver instalado em um local diferente, atualize o script com o caminho correto.
- O arquivo `.env` deve estar presente no mesmo diretório do executável ou script para que as variáveis de ambiente sejam carregadas corretamente.
- O script foi projetado para sistemas Windows. Pode não funcionar conforme esperado em outros sistemas operacionais sem modificações adicionais.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias ou correções.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.