# Sistema de Gerenciamento de Eventos
> Data Entrega: 
> 
## Contexto do Projeto
A Comunidade Tech é uma iniciativa acadêmica que promove eventos educacionais, técnicos e colaborativos com foco em tecnologia e inovação. Ao longo do ano, são realizados **workshops, maratonas de programação, palestras com especialistas e minicursos** gratuitos abertos ao público. Para aprimorar a gestão dessas atividades, os organizadores decidiram desenvolver um sistema que **automatize o controle dos eventos, incrições, participantes e relatórios administrativos.** 

Cada evento possui um **nome único, data de realização, tema central** (como Inteligência Artificial, Web, Segurança, etc.), **e uma lista de participantes inscritos.** Os participantes são identificados por um **código único e armazenam dados como nome completo, e-mail e preferências temáticas**. ***Um mesmo participante pode estar inscrito em vários eventos, e os dados completos estão disponíveis em arquivos Python prontos para importação***.

O sistema deverá ser capaz de importar corretamente os dados de eventos e participantes a partir desses arquivos. A partir disso, deverá oferecer funcionalidades básicas como **exibição da lista de eventos, listagem dos participantes por evento, busca por participantes a partir de seu código, e a geração de estatísticas úteis para os organizadores, como os participantes mais ativos e os temas mais frequentes.**

Espera-se que o sistema evolua com funcionalidades mais avançadas, como: **remoção de eventos e participantes, adição de novos eventos com dados completos, atualização de informações específicas** (como troca de tema ou atualização de e-mail de um participante), **verificação de participantes duplicados, e busca filtrada por tema ou faixa de datas.** A navegação no sistema deverá ocorrer por meio de um menu textual no terminal, permitindo fácil interação com as opções disponíveis.

Outras funcionalidades desejáveis incluem a **capacidade de agrupar eventos por tema, listar todos os eventos em que um participante específico está inscrito, contabilizar quantos eventos cada tema possui, calcular a taxa média de participação por tema, identificar eventos com menos de dois participantes (para possível cancelamento), e detectar e remover automaticamente registros duplicados de participantes no mesmo evento.**

Por fim, o código deverá seguir boas práticas de organização: **as funções devem ser bem nomeadas, o código deve ser modularizado e reutilizável, e recursos como compreensão de listas, *argse **kwargs' devem ser utilizados quando apropriado**. A proposta é que este sistema sirva tanto como ferramenta prática quanto como forma de consolidação dos principais conceitos estudados em algoritmos e estruturas em Python.

A Comunidade Tech organiza diversos eventos ao longo do ano, como workshops, meetups e hackathons. O time de organização precisa informatizar o processo de gestão desses eventos para facilitar o registro de dados e o acompanhamento das inscrições.

Cada evento possui informações como **nome, data, tema e participantes.** Os participantes, por sua vez, possuem um **identificador único, nome, e-mail e preferências temáticas**. Os dados de eventos e participantes já estão disponíveis em arquivos py, devendo ser utilizados como base para as operações do sistema.

O sistema deverá importar esses arquivos e oferecer uma interface simples no terminal, permitindo que o organizador consulte, insira e manipule os dados de forma eficiente. Espera-se que o código seja modularizado, permitindo expansão futura.

A solução deve considerar diferentes formas de percorrer e manipular estruturas de dados, promovendo uma abordagem reflexiva sobre boas práticas de programação.

## Critérios de Avaliação.

 - Organização e modularização do código [ **1.5 ponto** ] 
 - Importação correta dos arquivos [ **1.0 ponto** ] 
 - Uso correto de estruturas de dados [ **2.0 pontos** ] 
 - Implementação das funcionalidades principais [ **2.0 pontos** ]  
 -  Geração de relatórios e estatísticas [ **1.5 ponto** ]
 -  Uso de conceitos avançados (compreensão, args/kwargs) [ **1.0 ponto** ]
 - Clareza na interação com o usuário [ **1.0 ponto**]
      
