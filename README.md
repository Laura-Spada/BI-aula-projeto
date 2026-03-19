# Business Intelligence - Trabalho

### Relatório de Faturas de Cartões

### Campos Utilizados

- <u>nome e final do cartão</u>  
importante para identificar o usuário

- <u>data da compra e data da parcela</u>  
importante já que elas irão dar a partida na análise dos dados, sendo separadas em seus respectivos períodos para análise  

- <u>categoria e descrição</u>  
ao separar os gastos por categoria fica mais fácil compreender os dados conforme as prioridades e necessidades do usuário

- <u>valor</u>  
o principal campo da análise de dados, já que com ele serão feitos os cálculos dos gastos especificados

### <u>Perguntas de Negócio</u>  
> total de transações por categoria  
> total de transações por usuário  
> total de parcelas únicas  
> total de parcelas únicas por usuário  
> quais categorias tiveram mais gastos por mês/bimestre/semestre  
> quais categorias tiveram menos gastos por mês/bimestre/semestre  
> evolução mensal dos gastos  
> rank de meses com mais gastos  
> rank de meses que mais tiveram gastos comparados com as categorias  
> rank dos anos que mais tiveram gastos  
> contagem de compras parceladas e compras à vista  

<u>Situação Atual</u>  
	hoje em dia o usuário pega o extrato da conta e analisa manualmente os gastos separando eles por categoria, parcelas, data de compra

<u>Benefícios de Aplicar BI</u>  
com o BI aplicado ficaria melhor a visualização de gastos conforme os campos especificados do usuário, para melhor compreensão visual dos gastos.

#

### Instalar Dependências

- pip install -r requirements.txt

### Run

- python main.py

