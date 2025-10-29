# Texturas de Fundo - Instruções Manuais

Como você não tem PIL/Pillow instalado, aqui estão as instruções para criar as texturas manualmente:

## Opção 1: Usar um Editor de Imagens

1. **Abra um editor de imagens** (GIMP, Photoshop, Paint.NET, Pixelmator, etc.)

2. **Crie uma nova imagem**:
   - Dimensões: 256 x 256 pixels
   - Fundo: Transparente

3. **Para Economy Background** (economy_background.png):
   - Desenhe um retângulo com as dimensões:
     - Posição X: 40, Y: 45
     - Largura: 176, Altura: 166
   - Cor: Verde (#00FF00) com opacidade ~10%
   - Salve como `economy_background.png`

4. **Para Combat Background** (combat_background.png):
   - Mesmo processo, mas use:
   - Cor: Vermelho (#FF0000) com opacidade ~10%
   - Salve como `combat_background.png`

5. **Coloque os arquivos em**:
   ```
   resource-pack/assets/minecraft/textures/gui/container/
   ```

## Opção 2: Baixar Texturas Prontas

Você pode baixar texturas de baú do Minecraft e adicionar um overlay colorido.

## Opção 3: Usar Texturas Simples

Crie arquivos PNG de 256x256 com apenas uma cor de fundo semi-transparente.

## Opção 4: Instalar PIL e Rodar o Script

```bash
pip3 install Pillow
python3 create_backgrounds.py
```

## Testando

Depois de criar as texturas:

1. Compile o plugin: `./gradlew build`
2. Recarregue o resource pack no servidor
3. Abra o JobSelectionUI
4. Navegue entre classes de economia e combate
5. O fundo deve mudar automaticamente!
