# recipe_app

"As suas receitas na palma da mão"

A recipe_app tem como obejetivo manter um registo de todas as suas receitas (incluindo a receita do molho secreto da avó). 
Intuitivamente apenas tem que selecionar uma das três opções disponíveis.
Pode procurar pelo nome das suas receitas para obter mais informações sobre estas, e por exemplo saber quais os ingredientes que estas levam para planear a sua lista de compras.
Pode adicionar novas receitas à sua lista ou se precisar de inspiração, é ainda possível, procurar entre 2600 ingredientes e mais de 5000 receitas disponíveos no site "spoonacular".


O projeto contém cinco ficheiros:
-
-README.md, o presente ficheiro introdutório e explicativo do projeto;
-project.py, que contém o código criado para fazer a aplicação;
-test_project.py, com testes para algumas das funções do código;
-requirements.txt, um ficheiro de texto, que contém as intalações necessárias para o funcionamento e correr do código;
-Recipes.xlsx, o ficheiro excel no qual se encontram as receitas;

O ficheiro project.py consiste em duas classes: Recipe, que pretende representar os vários atributos (título, ingredientes, instruções, tempo e dificuldade); e RecipeApp, esta classe representa uma aplicação que permite adicionar receitas a uma lista, pesquisar receitas com base numa palavra-chave e salvar as receitas num ficheiro Excel.


Foi necessário criar uma conta no site https://spoonacular.com/ e criar uma API key, gerada aleatóriamente.




Notas adicionais:
-
N1- Á medida que ia fazendo várias tentativas, aconteceu-me a API key ter expirado e necessitar de fazer outra, a atual é "cd73c8c7ed7b4b68858b59d394336523" e foi criada no dia da entrega. 
N2- O código tem que ser alterado e substituir o seguinte caminho: "C:\\Users\\maria\\OneDrive\\Área de Trabalho\\Introdução ao Python\\Recipes.xlsx".
Deve ser alterado pelo "path" no qual está guardado o ficheiro excel no computador do utilizador.
N3- O intuito do excel será o utilizador colocar as suas própias receitas, para efeitos de testagem, este já contém algumas sendo que a opção "1. Search for your recipes" só funcionará para os nomes da receitas que já lá estão.
