RA:1129646 Kaue siqueira 
RA:1135161 Vinicius Casturino Souza

Função partial_sum: Realiza a soma de uma parte específica da lista de números e armazena o resultado parcial em uma lista.
Lista numbers: Lista de números a serem somados.
Número de threads: Definido como 2, mas pode ser ajustado conforme necessário.
Divisão da lista: Cada thread soma uma parte da lista.
Criação e início das threads: Cada thread executa a função partial_sum.
Aguarda a conclusão das threads: Usando join para garantir que todas as threads terminem antes de prosseguir.
Soma final: Soma dos resultados parciais para obter o total.
