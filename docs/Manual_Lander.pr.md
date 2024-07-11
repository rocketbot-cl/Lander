# Lander
  
Este modulo é usado para conectar ao Lander e executar comandos.  

*Read this in other languages: [English](Manual_Lander.md), [Português](Manual_Lander.pr.md), [Español](Manual_Lander.es.md)*
  
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conectar-se ao Lander
  
Conecte-se ao Lander
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Adicione sua chave de API do Lander|Chave de API do Lander|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9|
|IP ou host em que o Lander está a correr|IP ou host em que o Lander está a correr|localhost|
|Porto em que o Lander está a correr|Porto em que o Lander está a correr|9999|
|Caminho do executável do Rocketbot|Caminho para o executável rocketbot.exe no ambiente onde o Lander executa.|C:/Users/Usuario/Documents/Rocketbot_win_20240528/rocketbot.exe|
|Parametros de linha de comando|Parâmetros adicionais que receberão o Rocketbot ao executar os robôs do Lander.|--log='log/path' --debug='false'|
|Atribuir resultado a variável|Nome da variável onde será atribuído o resultado da execução do comando.|result|

### Adicionar robo à fila de Lander
  
Adicione um robo à fila de Lander
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do robo|Nome do robo que deseja adicionar à fila de Lander|MyRobot|
|Modo de execução do robo|||
|Parametros de linha de comando|Parâmetros adicionais que receberão a linha de comando ao executar o robo.|--debug='false'|
|Informação extra do robo|Informação extra que deseja enviar ao executar o robo|{'times': 5, 'name': 'Jogn'}|
|Caminho da base de dados|Caminho para o executável robot.db.|C:/Users/Usuario/Documents/Rocketbot_win_20240528/robot.db|
|Atribuir resultado a variável|Nome da variável onde será atribuído o resultado da execução do comando.|result|

### Executar robo
  
Permite executar um robo da fila de Lander
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do robo|ID do robo que deseja executar|5|
|Modo de execução do robo|||
|Atribuir resultado a variável|Nome da variável onde será atribuído o resultado da execução do comando.|result|
