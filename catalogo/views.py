# from django.shortcuts import render

from django.http import HttpResponse
# # Create your views here.

# def home(request):
#     return HttpResponse("Bem-vinda Nega!")

# def sobre(request):
#     return HttpResponse("sobre")


from django.shortcuts import render


def home(request):
    produtos = [
        {
            "nome": "Action Figure Homem-Aranha",
            "descricao": "Figura colecionável do herói da Marvel.",
            "preco": 129.90,
            "imagem": "https://placehold.co/600x400/171717/ffffff?text=Homem-Aranha",
            "categoria": "Colecionáveis",
        },
        {
            "nome": "Teclado Mecânico RGB",
            "descricao": "Teclado gamer com iluminação colorida.",
            "preco": 249.90,
            "imagem": "https://placehold.co/600x400/171717/00ffcc?text=Teclado+RGB",
            "categoria": "Setup Gamer",
        },
        {
            "nome": "Caneca Darth Vader",
            "descricao": "Caneca temática para fãs de Star Wars.",
            "preco": 49.90,
            "imagem": "https://placehold.co/600x400/171717/ffffff?text=Darth+Vader",
            "categoria": "Acessórios",
        },
        {
            "nome": "Controle Gamer",
            "descricao": "Controle para suas sessões de jogos.",
            "preco": 189.90,
            "imagem": "https://placehold.co/600x400/171717/00ffcc?text=Controle+Gamer",
            "categoria": "Games",
        },
        {
            "nome": "Luminária Minecraft",
            "descricao": "Decore seu quarto com estilo gamer.",
            "preco": 79.90,
            "imagem": "https://placehold.co/600x400/171717/00ff00?text=Minecraft",
            "categoria": "Decoração",
        },
        {
            "nome": "Action Figure Goku",
            "descricao": "Uma peça especial para fãs de Dragon Ball.",
            "preco": 159.90,
            "imagem": "https://placehold.co/600x400/171717/ffcc00?text=Goku",
            "categoria": "Colecionáveis",
        },
    ]

    return render(
        request,
        "catalogo/home.html",
        {"produtos": produtos},
    )
