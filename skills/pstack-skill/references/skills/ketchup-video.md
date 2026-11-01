# Ketchup video

Atualize o usuário como em [ketchup](ketchup.md), com um vídeo curto de slides legendados e as decisões pendentes em texto abaixo dele. Execute apenas quando o usuário pedir `ketchup-video` ou uma atualização em vídeo.

Siga ketchup, mas substitua seu resumo e seus visuais pelo vídeo. A janela começa na última mensagem do usuário antes de pedir `ketchup-video`. Escrever e renderizar o vídeo fora do repositório é a única exceção à regra de leitura. A resposta contém a frase de abertura de ketchup, o vídeo, uma linha sobre o trabalho que você ainda pode fazer e todas as decisões pendentes. Use os mesmos nomes do vídeo ao apresentar opções em texto.

## Escolha o renderizador

Detecte as ferramentas disponíveis antes de preparar os slides. Use um renderizador de slides ou frames e um codificador local, como FFmpeg. Um serviço de geração de vídeo não é necessário. Não dependa de uma ferramenta exclusiva do Cursor nem de outra skill instalada. Se usar um renderizador externo disponível na sessão, preserve as mesmas regras de evidência e verificação abaixo.

Não instale pacotes nem envie artefatos para serviços externos só para produzir a atualização. Se não houver renderizador disponível ou a renderização falhar, diga isso em uma linha e entregue as decisões pendentes em texto. Nunca invente um vídeo ou um link. Quando o chat não aceitar vídeo inline, forneça o arquivo renderizado por link.

## Prepare os slides

Use capturas, gravações, diffs e dados produzidos pelo trabalho. Antes de desenhar, escreva a frase que o usuário deve guardar e uma linha por slide. Essas notas não entram na resposta. Remova slides que não mudam o que o usuário sabe. Use no máximo dez.

Cada slide comunica uma ideia. Evolua uma mesma imagem entre slides quando isso explicar a mudança. Mantenha o significado de cores e formas. Mostre conexões, uma sequência de PRs, uma comparação de antes e depois ou opções lado a lado. Use setas, destaques e movimento para apontar a mudança. Não transforme listas de status, tabelas ou caixas sem conexão em slides.

Use poucas palavras e coloque os rótulos junto ao que nomeiam. Não repita um fato entre slides ou no texto abaixo. Mostre o resultado de cada pedido do usuário e se terminou, continua, falhou ou não foi verificado. Algo que aguarda uma decisão do usuário ainda não terminou. Inclua bugs encontrados e corrigidos. Se uma mudança visível não tiver captura, diga isso no slide e descreva a mudança na tela. Não invente números nem desenhe uma tela que você não capturou.

## Legende e renderize

Escreva uma legenda curta por slide, com cerca de dez palavras. Explique o significado da imagem usando apenas o que ela mostra. Coloque a legenda numa faixa abaixo da imagem, de altura constante. Ela não pode cobrir o conteúdo e deve ser legível no tamanho em que o chat exibe o vídeo.

Renderize um vídeo silencioso em paisagem, como MP4, com movimento entre slides. Gere frames a partir dos slides, sem gravar a tela. A imagem ocupa toda a área acima da faixa. Grave a legenda nos frames e mantenha-a durante toda a permanência do slide.

Conte as palavras novas de cada slide, incluindo a legenda e rótulos que mudaram. O primeiro slide adiciona todas as palavras. Não conte palavras dentro de capturas de tela. Mantenha cada slide totalmente visível por pelo menos um segundo a cada três palavras novas, sem contar as transições.

## Confira o arquivo final

Antes de entregar, abra um frame de cada slide no tamanho do chat. Confira se a legenda é legível e não cobre nada. Meça a permanência comparando os frames do arquivo final com o slide. Não use apenas um detector de frames parados, que pode contar o começo e o fim de um fade. Compare a duração medida com a contagem de palavras novas. Corrija, renderize e confira novamente qualquer slide que exija mais tempo de leitura.

Verifique o arquivo com o leitor ou analisador de mídia disponível, como `ffprobe`. Confirme duração, dimensões e reprodução. Entregue apenas o arquivo que você verificou.
