from concurrent import futures
import logging

import grpc
import TemperaturaService_pb2
import TemperaturaService_pb2_grpc

dados = [
    {
        'id': 1,
        'data': '20/12/2022',
        'localizacao': 'Goiânia',
        'temperatura': 25
    },
    {
        'id': 2,
        'data': '22/12/2022',
        'localizacao': 'Brasilia',
        'temperatura': 20
    },
    {
        'id': 3,
        'data': '25/12/2022',
        'localizacao': 'Sao Paulo',
        'temperatura': 15
    },
    {
        'id': 4,
        'data': '26/12/2022',
        'localizacao': 'Cavalcante',
        'temperatura': 25
    },
    {
        'id': 5,
        'data': '27/12/2022',
        'localizacao': 'Belo Horizonte',
        'temperatura': 27
    }
]


class TemperaturaServidor(TemperaturaService_pb2_grpc.TemperaturaServiceServicer):
    def CadastrarTemperatura(self, request, context):
        dado = {
            'id': request.id,
            'data': request.data,
            'localizacao': request.name.localizacao,
            'temperatura': request.temperatura
        }
        dados.append(dado)
        return TemperaturaService_pb2.StatusReply(status='OK')

    def GetTemperaturaPorId(self, request, context):
        usr = [item for item in dados if (item['id'] == request.id)]

        return TemperaturaService_pb2.Temperatura(id=usr[0]['id'], data=usr[0]['data'], localizacao=usr[0]['localizacao'],
                                                  temperatura=usr[0]['temperatura'])

    def GetTemperaturaPorData(self, request, context):
        lista_filtrada = [item for item in dados if (item['data'] == request.data)]
        list = TemperaturaService_pb2.TemperaturaList()
        for item in lista_filtrada:
            emp_data = TemperaturaService_pb2.Temperatura(id=item['id'], data=item['data'],
                                                          localizacao=item['localizacao'],
                                                          temperatura=item['temperatura'])
            list.temperatura_dado.append(emp_data)
        return list

        return TemperaturaService_pb2.TemperaturaList(lista_filtrada)

    def GetTemperaturaPorLocalizacao(self, request, context):
        lista_filtrada = [item for item in dados if (item['localizacao'] == request.localizacao)]
        list = TemperaturaService_pb2.TemperaturaList()
        for item in lista_filtrada:
            emp_data = TemperaturaService_pb2.Temperatura(id=item['id'], data=item['data'],
                                                          localizacao=item['localizacao'],
                                                          temperatura=item['temperatura'])
            list.temperatura_dado.append(emp_data)
        return list

    def ListarTodasTemperaturas(self, request, context):
        list = TemperaturaService_pb2.TemperaturaList()
        for item in dados:
            emp_data = TemperaturaService_pb2.Temperatura(id=item['id'], date=item['data'],
                                                          location=item['localizacao'],
                                                          temperature=item['temperature'])
            list.temperatura_dado.append(emp_data)
        return list


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TemperaturaService_pb2_grpc.add_TemperaturaServiceServicer_to_server(TemperaturaServidor(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()