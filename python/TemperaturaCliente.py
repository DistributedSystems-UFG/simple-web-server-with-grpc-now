from __future__ import print_function
import logging

import grpc
import TemperaturaService_pb2
import TemperaturaService_pb2_grpc

import const


def Cliente():
    with grpc.insecure_channel(const.IP + ':' + const.PORT) as channel:
        stub = TemperaturaService_pb2_grpc.TemperaturaServiceStub(channel)

        print('##################################')
        print('### 1 - Cadastrar')
        print('### 2 - Buscar por id')
        print('### 3 - Buscar por data')
        print('### 4 - Buscar por localização')
        print('### 5 - Listar todos os dados')
        print('### Qualquer opção diferente sairá do sitema')
        print('##################################')
        opcao = input('Digite sua opção: ')

        if opcao is 1:
            id = input("Digite a id: ")
            data = input("Digite a data: ")
            localizacao = input("Insira a localizacao: ")
            temperatura = input("insira a Temperatura: ")

            response = stub.CadastrarTemperatura(TemperaturaService_pb2.Temperatura(data=data, localizacao=localizacao, temperatura=temperatura))
            print('Cadastro: ' + str(response));
        elif opcao is 2:
            response = stub.GetTemperaturaPorId(TemperaturaService_pb2.Id(id=1))
            print('Busca por ID: \n' + str(response));
        elif opcao is 3:
            data_busca = input('Insira data de busca: ')
            response = stub.GetTemperaturaPorData(TemperaturaService_pb2.Data(data='25/12/2022'))
            print('Busca por Data: ' + str(response));
        elif opcao is 4:
            localizacao_busca = input("Insira a localizacao de busca: ")
            response = stub.getTemperaturaPorLocalizacao(TemperaturaService_pb2.Localizacao(localizacao_busca))
            print('Busca por Localização: ' + str(response));
        elif opcao is 5:
            response = stub.ListarTodasTemperaturas(TemperaturaService_pb2.EmptyMessage())
            print('Todas as temperaturas da lista: ' + str(response));
        else:
            exit('até mais...')

if __name__ == '__main__':
    logging.basicConfig()
    Cliente()
