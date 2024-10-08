# função que vai criar um bloco recebendo 2 parametros
def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == "__main__":
    print(tag_bloco('bloco'))
    # 3 parametro
    # texto 'inline e classe'
    # classe 'info'
    # inline True(tag)
    print(tag_bloco('inline e classe', 'info', True))
    # resultado <spanclass="info">inline e classe</span>

    # usamos parametro nomeado inline não precisa estar na ordem se for nomeado
    # parametro texto é inline
    # parametro classe é o padrão da função
    # parametro inline(tag) true retorna span
    print(tag_bloco('inline', inline=True))
    # resultado <spanclass="success">inline</span>
    # foi mudado a ordem mas o resultado sai o mesmo
    # pelo fato de serem nomeados inline e texto
    print(tag_bloco(inline=True, texto='inline'))
    # resultado <spanclass="success">inline</span>

    # parametro texto 'falhou'
    # parametro classe 'error'
    # parametro inline(tag) não foi colocado então padrão false retorna div
    print(tag_bloco('falhou', classe='error'))
    # resultado retorna <div class="error">falhou</div>
