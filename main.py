import speech_recognition as sr

# Configura o reconhecedor de fala
r = sr.Recognizer()

# Configura o microfone
mic = sr.Microphone()

# Loop principal do assistente de voz
while True:
    # Tenta ouvir a fala do usuário
    try:
        # Inicia a gravação do áudio
        with mic as source:
            print("Diga algo...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        # Tenta reconhecer a fala
        command = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + command)

    # Se não conseguir ouvir ou reconhecer a fala, trata o erro
    except sr.UnknownValueError:
        print("Não foi possível reconhecer a fala.")
    except sr.RequestError as e:
        print(f"Não foi possível se conectar ao serviço do Google: {e}")
