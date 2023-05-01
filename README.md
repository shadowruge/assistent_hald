# assistent_hald
Home assistent linux desktop

Este script usa a biblioteca PocketSphinx para realizar reconhecimento de fala em tempo real em um microfone conectado ao seu computador. O script configura o decodificador com o modelo acústico padrão do Debian e o dicionário cmudict. Ele usa a biblioteca PyAudio para capturar áudio do microfone e enviar para o decodificador.

## Requisitos

- Python 3
- PocketSphinx
- PyAudio

## Uso

Para usar o script, execute o seguinte comando:
    O script irá iniciar a gravação de áudio e realizar o reconhecimento de fala em tempo real. Quando o reconhecimento for concluído, ele imprimirá a transcrição da fala no console.

## Créditos

Este script foi desenvolvido por shadowruge/chatGPT.
