# Renderizar um gráfico

Renderize cada arquivo `.mmd` que for mostrar com o pacote npm `pele@1.9.0` e entregue o SVG. Instale Pele uma vez, fora do repositório. Grave cada SVG ao lado do `.mmd`, com o mesmo nome. Consulte a [API do Pele](https://pele.run/api). Passe `{ limit: 1_000_000, outputLimit: 8_000_000, maxEdges: 10_000 }` como opções de `render`; os limites padrão podem ser insuficientes para um gráfico de 500 estados. Se o Pele lançar um `PeleError`, entregue o Mermaid e o erro.

## Cores

Pele ignora `theme` e `themeVariables` do Mermaid. Configure as variáveis CSS `--pele-*` em `.pele`, conforme a [documentação de temas](https://pele.run/theming). O compilador aplica a classe de cor de cada grupo, por exemplo `class sN teal`. Também aplica `breaks` ou `mayBreak` aos estados com regras quebradas, `bugPath` aos estados no caminho mais curto de um bug e `repeats` aos estados repetidos para sempre por um contraexemplo de `PROPERTY`. Pele coloca essas classes no nó do estado. Estilize-as com CSS.

O `.mmd` inclui `classDef` para `breaks` e `mayBreak`, para que as marcas apareçam em qualquer visualizador Mermaid. Não inclui `classDef` para as cores dos grupos, `bugPath` ou `repeats`. Pele converte `classDef` em atributos `style`, que têm precedência sobre CSS comum. Por isso, as regras abaixo usam `!important` nas marcas. Coloque-as depois das cores dos grupos. A marca controla preenchimento e texto; `bugPath` e `repeats` controlam a borda.

As cores abaixo são sugestões herdadas do porte anterior. Insira o bloco em um elemento `<style>` no início de cada SVG. O SVG acompanhará a preferência de tema claro ou escuro do visualizador.

```css
.pele {
  --pele-bg: #ffffff;
  --pele-fg: #1c1c1c;
  --pele-muted: #656565;
  --pele-line: #808080;
  --pele-surface: #fcfcfc;
  --pele-surface-alt: #f1f1f1;
  --pele-border: #c9c9c9;
}
.pele .blue rect { fill: #c3e0ff; }
.pele .orange rect { fill: #f0d3bf; }
.pele .purple rect { fill: #e3d5ff; }
.pele .yellow rect { fill: #f0dcbf; }
.pele .teal rect { fill: #bfe3df; }
.pele .tan rect { fill: #e5d9ce; }
.pele .pink rect { fill: #ffcbe6; }
.pele .breaks rect {
  fill: #ffecee !important;
  stroke: #e72e3b !important;
  stroke-width: 2.5px !important;
}
.pele .breaks text {
  fill: #cd2834 !important;
}
.pele .mayBreak rect {
  fill: #fff3e6 !important;
  stroke: #e8730c !important;
  stroke-width: 2.5px !important;
}
.pele .mayBreak text {
  fill: #b85a06 !important;
}
.pele .bugPath rect {
  stroke: #1680f3 !important;
  stroke-width: 2.5px !important;
}
.pele .repeats rect {
  stroke: #9b35d6 !important;
  stroke-width: 2.5px !important;
  stroke-dasharray: 6 3;
}
@media (prefers-color-scheme: dark) {
  .pele {
    --pele-bg: #1f1f1f;
    --pele-fg: #f5f5f5;
    --pele-muted: #acacac;
    --pele-line: #939393;
    --pele-surface: #121212;
    --pele-surface-alt: #2c2c2c;
    --pele-border: #4e4e4e;
  }
  .pele .blue rect { fill: #1b3857; }
  .pele .orange rect { fill: #573117; }
  .pele .purple rect { fill: #3c2e57; }
  .pele .yellow rect { fill: #573d17; }
  .pele .teal rect { fill: #174641; }
  .pele .tan rect { fill: #3d3127; }
  .pele .pink rect { fill: #57233e; }
  .pele .breaks rect {
    fill: #2e2021 !important;
    stroke: #cf2b35 !important;
  }
  .pele .breaks text {
    fill: #ff6463 !important;
  }
  .pele .mayBreak rect {
    fill: #2e2619 !important;
    stroke: #d0700f !important;
  }
  .pele .mayBreak text {
    fill: #ffa257 !important;
  }
  .pele .bugPath rect {
    stroke: #116dd2 !important;
  }
  .pele .repeats rect {
    stroke: #9a3fcf !important;
  }
}
```
