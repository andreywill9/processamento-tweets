import datetime
from string import punctuation

import nltk
from nltk import tokenize

token_espaco = tokenize.WhitespaceTokenizer()


termos_todos_candidatos = {
    'lula': ['lula', 'luiz inacio lula da silva', '@lulaoficial'],
    'bolsonaro': ['bolsonaro', 'jair messias bolsonaro', '@jairbolsonaro'],
    'ciro': ['ciro', 'ciro gomes', '@cirogomes'],
    'simone_tebet': ['tebet', 'simone tebet', '@simonetebetbr'],
    'eymael': ['eymael', 'eymael o democrata cristao', '@eymaelpr2022'],
    'sofia_manzano': ['sofia manzano', 'manzano pcb', '@sofiamanzanopcb'],
    'soraya_thronicke': ['soraya thronicke', 'soraya união brasil', '@sorayathronicke'],
    'felipe_d_avila': ['felipe davila', 'felipe davila novo', '@fdavilaoficial'],
    'vera_lucia': ['vera lucia', 'vera lucia pstu', '@verapstu'],
    'leo_pericles': ['leo pericles', 'leonardo pericles', '@leopericlesup'],
    'padre_kelmon': ['kelmon', '@padrekelmon', '@pekelmon']
}

termos_candidatos_segundo_turno = {
    'lula': ['lula', 'luiz inacio lula da silva', '@lulaoficial'],
    'bolsonaro': ['bolsonaro', 'jair messias bolsonaro', '@jairbolsonaro']
}

nomes_candidatos = ['lula', 'luiz', 'inacio', 'lula', 'silva', '@lulaoficial',
                    'bolsonaro', 'jair', 'messias', 'bolsonaro', '@jairbolsonaro',
                    'ciro', 'ciro', 'gomes', '@cirogomes',
                    'tebet', 'simone', 'tebet', '@simonetebetbr',
                    'eymael', 'eymael', '@eymaelpr2022',
                    'sofia', 'manzano', '@sofiamanzanopcb',
                    'soraya', 'thronicke', 'soraya', '@sorayathronicke',
                    'felipe', 'davila', '@fdavilaoficial',
                    'vera', 'lucia', 'vera', 'lucia', 'pstu', '@verapstu',
                    'leo', 'pericles', 'leonardo', 'pericles', '@leopericlesup',
                    'kelmon', '@pekelmon', '@padrekelmon'
                    ]

arroba_candidato = {'@lulaoficial': 'lula',
                    '@jairbolsonaro': 'bolsonaro',
                    '@cirogomes': 'ciro',
                    '@simonetebetbr': 'simone_tebet',
                    '@eymaelpr2022': 'eymael',
                    '@sofiamanzanopcb': 'sofia_manzano',
                    '@sorayathronicke': 'soraya_thronicke',
                    '@fdavilaoficial': 'felipe_d_avila',
                    '@verapstu': 'vera_lucia',
                    '@leopericlesup': 'leo_pericles',
                    '@pekelmon': 'padre_kelmon',
                    '@padrekelmon': 'padre_kelmon'}

abreviacoes = {
    'vc': 'voce',
    'vcs': 'voces',
    'pq': 'porque',
    'pra': 'para',
    'pro': 'para o',
    'q': 'que',
    'mn': 'mano',
    'blz': 'beleza',
    'pdc': 'pode crer',
    'gnt': 'gente',
    'mds': 'meu deus',
    'vlw': 'valeu',
    'hj': 'hoje',
    'lix': 'lixo',
    'nd': 'nada',
    'pfv': 'por favor',
    'hrs': 'horas',
    'aq': 'aqui',
    'pft': 'perfeito',
    'glr': 'galera',
    'clr': 'celular',
    'n': 'nao',
    's': 'sim',
    'ctz': 'certeza',
    'dps': 'depois',
    'dnv': 'denovo',
    'msm': 'mesmo',
    'sla': 'sei la',
    'ngm': 'ninguem',
    'p': 'para',
    'mt': 'muito',
    'mto': 'muito',
    'mta': 'muita',
    'd': 'de',
    'tar': 'estar',
    'tb': 'tambem',
    'tbm': 'tambem'
}

palavras_classificadas = {
    "acertar": 2,
    "adorar": 2,
    "agradecer": 2,
    "amar": 2,
    "amer": 2,
    "amor": 2,
    "apoiar": 2,
    "argumento": 2,
    "bem": 2,
    "boa": 2,
    "bom": 2,
    "brabo": 2,
    "certeza": 2,
    "certo": 2,
    "comemorar": 2,
    "consciencia": 2,
    "conseguir": 2,
    "coragem": 2,
    "correto": 2,
    "crescimento": 2,
    "cristao": 2,
    "cuidar": 2,
    "defender": 2,
    "defesa": 2,
    "democracia": 2,
    "deus": 2,
    "direito": 2,
    "eleger": 2,
    "elogiar": 2,
    "emprego": 2,
    "equipe": 2,
    "esperanca": 2,
    "esperancar": 2,
    "excelente": 2,
    "familia": 2,
    "fato": 2,
    "feliz": 2,
    "festa": 2,
    "ganhar": 2,
    "gostar": 2,
    "honesto": 2,
    "importante": 2,
    "incrivel": 2,
    "inteligente": 2,
    "interessante": 2,
    "jesus": 2,
    "justica": 2,
    "justico": 2,
    "justo": 2,
    "liberdade": 2,
    "lider": 2,
    "liderar": 2,
    "lindo": 2,
    "livrar": 2,
    "livre": 2,
    "lulano1oturno": 2,
    "lulanoprimeiroturno": 2,
    "lulapresidente13": 2,
    "maximo": 2,
    "melhor": 2,
    "melhorar": 2,
    "muito": 2,
    "otimo": 2,
    "otimos": 2,
    "pai": 2,
    "patria": 2,
    "paz": 2,
    "perfeito": 2,
    "plano": 2,
    "pontuar": 2,
    "popular": 2,
    "prefiro": 2,
    "prefirociro": 2,
    "professor": 2,
    "propor": 2,
    "reforma": 2,
    "respeitar": 2,
    "respeito": 2,
    "salvar": 2,
    "sim": 2,
    "somar": 2,
    "sonhar": 2,
    "trabalhador": 2,
    "uniao": 2,
    "vacina": 2,
    "vdd": 2,
    "vencer": 2,
    "verdade": 2,
    "verdadeiro": 2,
    "vida": 2,
    "vitoria": 2,
    "1o": 1,
    "2o": 1,
    "abrir": 1,
    "aceitar": 1,
    "achar": 1,
    "acontecer": 1,
    "acordar": 1,
    "acreditar": 1,
    "agir": 1,
    "ajudar": 1,
    "aliado": 1,
    "alianca": 1,
    "amigo": 1,
    "anunciar": 1,
    "apoiador": 1,
    "apoio": 1,
    "aprender": 1,
    "aprovar": 1,
    "aproveitar": 1,
    "arrumar": 1,
    "atitude": 1,
    "auxilio": 1,
    "baixar": 1,
    "bandeira": 1,
    "bastante": 1,
    "bonito": 1,
    "bora": 1,
    "brasil": 1,
    "brasileiro": 1,
    "capaz": 1,
    "capitao": 1,
    "carater": 1,
    "chance": 1,
    "chegar": 1,
    "cheio": 1,
    "claro": 1,
    "classe": 1,
    "combater": 1,
    "comer": 1,
    "concordar": 1,
    "confiar": 1,
    "confirmar": 1,
    "conhecer": 1,
    "considerar": 1,
    "consigo": 1,
    "continuar": 1,
    "contratar": 1,
    "coracao": 1,
    "crer": 1,
    "crescer": 1,
    "crianca": 1,
    "criar": 1,
    "cumprir": 1,
    "debater": 1,
    "declarar": 1,
    "demais": 1,
    "democrata": 1,
    "democratico": 1,
    "demonstrar": 1,
    "descobrir": 1,
    "dever": 1,
    "educacao": 1,
    "eleicao": 1,
    "eleitor": 1,
    "entender": 1,
    "entendi": 1,
    "escola": 1,
    "escolher": 1,
    "estrategia": 1,
    "estudar": 1,
    "fa": 1,
    "favor": 1,
    "fe": 1,
    "forca": 1,
    "forte": 1,
    "funcionar": 1,
    "futuro": 1,
    "garantir": 1,
    "gerar": 1,
    "gestao": 1,
    "gosto": 1,
    "governar": 1,
    "governo": 1,
    "grande": 1,
    "homem": 1,
    "humano": 1,
    "ideia": 1,
    "igreja": 1,
    "informar": 1,
    "inocentar": 1,
    "inocente": 1,
    "intencoes": 1,
    "inventar": 1,
    "investigar": 1,
    "irmao": 1,
    "justamente": 1,
    "legal": 1,
    "lei": 1,
    "liberar": 1,
    "limpo": 1,
    "lutar": 1,
    "mae": 1,
    "maioria": 1,
    "mandato": 1,
    "mercado": 1,
    "merecer": 1,
    "mito": 1,
    "moral": 1,
    "mostrar": 1,
    "movimento": 1,
    "mudar": 1,
    "mulher": 1,
    "ne": 1,
    "necessario": 1,
    "nocao": 1,
    "novo": 1,
    "objetivo": 1,
    "obra": 1,
    "ok": 1,
    "oportunidade": 1,
    "organizar": 1,
    "parabem": 1,
    "patriota": 1,
    "pensar": 1,
    "pesquisar": 1,
    "populacao": 1,
    "possibilidade": 1,
    "povo": 1,
    "preocupar": 1,
    "preparar": 1,
    "presidencia": 1,
    "presidente": 1,
    "principal": 1,
    "projeto": 1,
    "prometer": 1,
    "proposta": 1,
    "provar": 1,
    "provavelmente": 1,
    "puro": 1,
    "querer": 1,
    "querido": 1,
    "razao": 1,
    "realmente": 1,
    "reeleger": 1,
    "representar": 1,
    "republicar": 1,
    "resolver": 1,
    "rico": 1,
    "saber": 1,
    "saude": 1,
    "seguranca": 1,
    "sempre": 1,
    "serio": 1,
    "servir": 1,
    "simples": 1,
    "simplesmente": 1,
    "social": 1,
    "sociedade": 1,
    "solucao": 1,
    "sonho": 1,
    "subir": 1,
    "tanto": 1,
    "tentar": 1,
    "torcer": 1,
    "totalmente": 1,
    "trabalhar": 1,
    "trabalho": 1,
    "tranquilo": 1,
    "unico": 1,
    "unir": 1,
    "util": 1,
    "valer": 1,
    "vantagem": 1,
    "vender": 1,
    "viver": 1,
    "vivo": 1,
    "vontade": 1,
    "votar": 1,
    "vote": 1,
    "voto": 1,
    "acusar": -1,
    "adversario": -1,
    "aguentar": -1,
    "ainda": -1,
    "apertar": -1,
    "apesar": -1,
    "atacar": -1,
    "ataque": -1,
    "aumentar": -1,
    "aumento": -1,
    "bater": -1,
    "bilhoes": -1,
    "bla": -1,
    "bolha": -1,
    "bolsonarismo": -1,
    "bolsonarista": -1,
    "cair": -1,
    "causar": -1,
    "cirista": -1,
    "cobrar": -1,
    "contrario": -1,
    "cortar": -1,
    "cpi": -1,
    "cuidado": -1,
    "culpar": -1,
    "deixar": -1,
    "derrotar": -1,
    "derrubar": -1,
    "desculpa": -1,
    "desistir": -1,
    "dificil": -1,
    "dinheiro": -1,
    "discutir": -1,
    "droga": -1,
    "duvidar": -1,
    "engolir": -1,
    "engracado": -1,
    "entregar": -1,
    "envolver": -1,
    "esconder": -1,
    "esquecer": -1,
    "evitar": -1,
    "extremo": -1,
    "falta": -1,
    "faltar": -1,
    "fechar": -1,
    "feio": -1,
    "ficar": -1,
    "fugir": -1,
    "fundo": -1,
    "impedir": -1,
    "indeciso": -1,
    "indicar": -1,
    "indignar": -1,
    "infelizmente": -1,
    "interesse": -1,
    "jato": -1,
    "julgar": -1,
    "juro": -1,
    "justificar": -1,
    "lavar": -1,
    "mandar": -1,
    "massa": -1,
    "menos": -1,
    "mente": -1,
    "militancia": -1,
    "militante": -1,
    "nada": -1,
    "negar": -1,
    "nenhum": -1,
    "news": -1,
    "ninguem": -1,
    "nojo": -1,
    "nunca": -1,
    "obrigar": -1,
    "oposicao": -1,
    "parar": -1,
    "partido": -1,
    "passado": -1,
    "pena": -1,
    "pequeno": -1,
    "petista": -1,
    "polarizacao": -1,
    "politica": -1,
    "politico": -1,
    "pouco": -1,
    "precisar": -1,
    "preco": -1,
    "preocupado": -1,
    "processo": -1,
    "prova": -1,
    "quebrar": -1,
    "questionar": -1,
    "repetir": -1,
    "responsavel": -1,
    "risco": -1,
    "sair": -1,
    "salario": -1,
    "sequer": -1,
    "sistema": -1,
    "temer": -1,
    "tirar": -1,
    "tomar": -1,
    "urgente": -1,
    "vermelho": -1,
    "abandonar": -2,
    "aborto": -2,
    "absurdo": -2,
    "ameaca": -2,
    "antipetismo": -2,
    "assassino": -2,
    "atrapalhar": -2,
    "bandido": -2,
    "banqueiro": -2,
    "bolsominion": -2,
    "bosta": -2,
    "bostonaro": -2,
    "bozo": -2,
    "brigar": -2,
    "bundao": -2,
    "burro": -2,
    "cadeia": -2,
    "cagar": -2,
    "calar": -2,
    "canalha": -2,
    "capanga": -2,
    "caralho": -2,
    "cego": -2,
    "censurar": -2,
    "centrao": -2,
    "chato": -2,
    "chorar": -2,
    "circo": -2,
    "comunismo": -2,
    "comunista": -2,
    "condenar": -2,
    "contra": -2,
    "corrupcao": -2,
    "corrupto": -2,
    "corte": -2,
    "covarde": -2,
    "covid": -2,
    "crime": -2,
    "criminoso": -2,
    "criticar": -2,
    "cu": -2,
    "culpa": -2,
    "denunciar": -2,
    "derrota": -2,
    "desesperar": -2,
    "desespero": -2,
    "desgoverno": -2,
    "desgraca": -2,
    "destruir": -2,
    "desviar": -2,
    "ditador": -2,
    "ditadura": -2,
    "doente": -2,
    "doido": -2,
    "enganar": -2,
    "errar": -2,
    "erro": -2,
    "escandalo": -2,
    "esquema": -2,
    "esquerdista": -2,
    "estranho": -2,
    "expresidiario": -2,
    "fake": -2,
    "falso": -2,
    "familicia": -2,
    "fanatico": -2,
    "fascismo": -2,
    "fascista": -2,
    "fingir": -2,
    "foda": -2,
    "fome": -2,
    "fraco": -2,
    "fraude": -2,
    "fuder": -2,
    "gado": -2,
    "gastar": -2,
    "genocida": -2,
    "golpe": -2,
    "golpear": -2,
    "golpista": -2,
    "gritar": -2,
    "guerra": -2,
    "hipocrisia": -2,
    "hipocrito": -2,
    "idiota": -2,
    "ignorar": -2,
    "imbecil": -2,
    "impeachment": -2,
    "impossivel": -2,
    "imposto": -2,
    "inferno": -2,
    "inflacao": -2,
    "inimigo": -2,
    "jamais": -2,
    "ladrao": -2,
    "ladroes": -2,
    "lixo": -2,
    "louco": -2,
    "luladrao": -2,
    "lulista": -2,
    "mal": -2,
    "maluco": -2,
    "matar": -2,
    "mau": -2,
    "medo": -2,
    "mensalao": -2,
    "mentir": -2,
    "mentira": -2,
    "mentiroso": -2,
    "merda": -2,
    "miliciano": -2,
    "molusco": -2,
    "morer": -2,
    "morra": -2,
    "morrer": -2,
    "morte": -2,
    "nao": -2,
    "odeiar": -2,
    "odio": -2,
    "oportunista": -2,
    "orcamento": -2,
    "pandemia": -2,
    "patetico": -2,
    "pau": -2,
    "pcc": -2,
    "perder": -2,
    "pessimo": -2,
    "piada": -2,
    "pilantra": -2,
    "pior": -2,
    "pobre": -2,
    "podre": -2,
    "porra": -2,
    "pqp": -2,
    "prender": -2,
    "presidiario": -2,
    "preso": -2,
    "prisao": -2,
    "problema": -2,
    "puta": -2,
    "quadrilha": -2,
    "quadrilhao": -2,
    "reclamar": -2,
    "rejeicao": -2,
    "retardada": -2,
    "retardado": -2,
    "ridiculo": -2,
    "roubar": -2,
    "roubo": -2,
    "ruim": -2,
    "saco": -2,
    "safado": -2,
    "secreto": -2,
    "sigilo": -2,
    "sofrer": -2,
    "sujo": -2,
    "terrorista": -2,
    "tiro": -2,
    "traidor": -2,
    "trair": -2,
    "triste": -2,
    "trouxa": -2,
    "vagabundo": -2,
    "venezuela": -2,
    "vergonha": -2,
    "verme": -2,
    "violencia": -2,
    "xingar": -2
}

inicio_primeiro_turno = datetime.datetime(year=2022, month=8, day=16)

fim_primeiro_turno = datetime.datetime(year=2022, month=10, day=1)

inicio_segundo_turno = datetime.datetime(year=2022, month=10, day=3)

fim_segundo_turno = datetime.datetime(year=2022, month=10, day=29)

inicio_debate_globo_primeiro_turno = datetime.datetime(year=2022, month=9, day=25)

fim_debate_globo_primeiro_turno = datetime.datetime(year=2022, month=10, day=1)

inicio_debate_globo_segundo_turno = datetime.datetime(year=2022, month=10, day=23)

fim_debate_globo_segundo_turno = datetime.datetime(year=2022, month=10, day=29)

stopwords = nltk.corpus.stopwords.words("portuguese")
palavras_irrelevantes = [*punctuation] + stopwords
token_pontuacao = tokenize.WordPunctTokenizer()
