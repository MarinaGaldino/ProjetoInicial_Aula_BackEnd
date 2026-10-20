from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    produtos = [
        {
        "nome": "Action Figure Homem-Aranha",
        "categoria": "Colecionáveis",
        "descricao": "Figura colecionável do herói da Marvel.",
        "preco": 129.90,
        "imagem": "https://images.unsplash.com/photo-1608889476561-6242cfdbf622?w=600"
        },
        {
        "nome": "Teclado Mecânico RGB",
        "categoria": "Setup Gamer",
        "descricao": "Teclado gamer com iluminação colorida.",
        "preco": 249.90,
        "imagem": "https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=600"
        },
        {
        "nome": "Caneca Darth Vader",
        "categoria": "Acessórios",
        "descricao": "Caneca temática para fãs de Star Wars.",
        "preco": 49.90,
        "imagem": "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=600"
        },
        {
        "nome": "Controle Gamer",
        "categoria": "Games",
        "descricao": "Controle para suas sessões de jogos.",
        "preco": 189.90,
        "imagem": "https://images.unsplash.com/photo-1592840496694-26d035b52b48?w=600"
        },
        {
        "nome": "Luminária Minecraft",
        "categoria": "Decoração",
        "descricao": "Decore seu quarto com estilo gamer.",
        "preco": 79.90,
        "imagem": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=600"
        },
        {
        "nome": "Action Figure Goku",
        "categoria": "Colecionáveis",
        "descricao": "Uma peça especial para fãs de Dragon Ball.",
        "preco": 159.90,
        "imagem": "https://m.media-amazon.com/images/I/71JW84CDmCL._AC_SL1500_.jpg?w=600"
        },
        {
            "nome": "Figura Colecionável",
            "categoria": "Colecionáveis",
            "descricao": "Uma peça especial para sua coleção geek.",
            "preco": 149.90,
            "imagem": "https://down-br.img.susercontent.com/file/br-11134207-7r98o-lt8gzgknfg8s91?w=600"
        },
        {
            "nome": "Universo Gamer",
            "categoria": "Games",
            "descricao": "Tudo para completar seu espaço gamer.",
            "preco": 299.90,
            "imagem": "https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=600"
        },
        {
            "nome": "Acessório Geek",
            "categoria": "Acessórios",
            "descricao": "Um acessório para os fãs de tecnologia.",
            "preco": 79.90,
            "imagem": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600"
        },
    ]

    return render(
        request,
        "catalogo/home.html",
        {"produtos": produtos},
    )
