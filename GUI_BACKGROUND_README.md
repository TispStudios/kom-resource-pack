# GUI Background Customization

## Como Funciona

O sistema de fundos customizados para o JobSelectionUI funciona assim:

1. **ProtocolLib Packet Listener**: Intercepta o pacote `OPEN_WINDOW` quando o inventário é aberto
2. **Modificação do Título**: Adiciona um caractere especial invisível no início do título baseado no tipo de classe:
   - `\uF001` para classes de Economia (verde)
   - `\uF002` para classes de Combate (vermelho)
3. **Resource Pack**: Define esses caracteres como texturas de fundo no arquivo `font/default.json`

## Arquivos Necessários

### 1. Texturas de Fundo

Você precisa criar duas imagens PNG (256x256 pixels) em:

- `assets/minecraft/textures/gui/container/economy_background.png` - Fundo verde para economia
- `assets/minecraft/textures/gui/container/combat_background.png` - Fundo vermelho para combate

Essas imagens devem ter o layout de um baú do Minecraft (176x166 pixels centralizados em 256x256).

### 2. Font Definition

O arquivo `assets/minecraft/font/default.json` já foi criado e mapeia os caracteres especiais para as texturas.

### 3. Código Java/Kotlin

O `JobSelectionPacketListener.kt` já intercepta os pacotes e modifica o título com os caracteres especiais.

## Criando as Texturas

Você pode usar ferramentas como GIMP, Photoshop, ou Paint.NET para criar as texturas:

1. Comece com a textura padrão do baú: `generic_54.png` (176x166)
2. Adicione overlay verde ou vermelho com transparência
3. Centralize em uma imagem 256x256
4. Salve como PNG com transparência

## Alternativa Simples

Se você quiser apenas mudar a cor de fundo sem criar texturas customizadas, você pode:

1. Usar texturas existentes do Minecraft
2. Modificar apenas as bordas/decorações
3. Usar o sistema de panes coloridos que já está implementado no código

## Testando

1. Compile o plugin com `./gradlew build`
2. Coloque o resource pack na pasta de resource packs do servidor
3. Configure o servidor para enviar o resource pack automaticamente
4. Abra o JobSelectionUI e navegue entre classes de economia e combate
5. O fundo deve mudar automaticamente
