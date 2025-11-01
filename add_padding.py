#!/usr/bin/env python3
"""
Script para adicionar padding à esquerda das imagens de background
para centralizar horizontalmente no inventário do Minecraft
"""

from PIL import Image
import os

# Diretório com as imagens
container_dir = "assets/minecraft/textures/gui/container"

# Lista de arquivos de background
backgrounds = [
    "lumberjack_background.png",
    "miner_background.png",
    "blacksmith_background.png",
    "alchemist_background.png",
    "farmer_background.png",
    "hunter_background.png",
    "paladin_background.png",
    "mage_background.png",
    "rogue_background.png",
    "barbarian_background.png",
    "archer_background.png",
    "engineer_background.png"
]

# Padding à esquerda (em pixels) - ajuste esse valor conforme necessário
# Para inventário de 6 linhas (176 pixels de largura), precisamos centralizar 256px
# Offset aproximado: (256 - 176) / 2 = 40 pixels
LEFT_PADDING = 40

def add_left_padding(image_path, padding):
    """Adiciona padding transparente à esquerda da imagem"""
    # Abre a imagem
    img = Image.open(image_path)
    
    # Obtém dimensões
    width, height = img.size
    
    # Cria nova imagem com padding
    new_width = width + padding
    new_img = Image.new('RGBA', (new_width, height), (0, 0, 0, 0))
    
    # Cola a imagem original com offset à esquerda
    new_img.paste(img, (padding, 0))
    
    # Salva a imagem modificada
    new_img.save(image_path)
    print(f"✓ Processado: {os.path.basename(image_path)} ({width}x{height} -> {new_width}x{height})")

def main():
    print(f"Adicionando {LEFT_PADDING}px de padding à esquerda das imagens...\n")
    
    processed = 0
    for filename in backgrounds:
        filepath = os.path.join(container_dir, filename)
        
        if os.path.exists(filepath):
            add_left_padding(filepath, LEFT_PADDING)
            processed += 1
        else:
            print(f"✗ Não encontrado: {filename}")
    
    print(f"\n{processed}/{len(backgrounds)} imagens processadas com sucesso!")
    print(f"\nAs imagens agora têm {LEFT_PADDING}px de padding à esquerda.")
    print("Recarregue o resource pack no jogo para ver as mudanças.")

if __name__ == "__main__":
    main()
