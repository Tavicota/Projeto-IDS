# Projeto-IDS
Projeto de um IDS para a aula do professor Cabrini, desenvolvido por Otávio Pogetti e Ingrid Oliveira

Para o funcionamento foi necessário um servidor Ubuntu Server 18.04 LTS para realizar o comando nmap nas portas udp e ser bloqueado pelo IDS
O IDS estará rodando em um Ubuntu Client 22.04 LTS.

Abra o arquivo main.py utilizando um terminal com permissão de super usuário

Ele irá rodar o IDS e irá ficar realizando uma analise de todos os pacotes que estão na sua rede,
caso ele identifique um pacote suspeito através do seu ML,
ele irá bloquear no firewall do Linux e após alguns segundosa desbloquear a comunicação daquele IP, porta e protocolo(UDP ou TCP).

IMPORTANTE!!!!!!!!

Verificar se o servidor está enviando as solicitações ao IP correto, basta alterar o comando do nmap
