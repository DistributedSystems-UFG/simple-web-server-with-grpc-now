from concurrent import futures
import logging

import grpc
import TemperaturaServidor_pb2
import TemperaturaServidor_pb2_grpc

lista = []

class TemperaturaServidor(TemperaturaServidor_pb2_grpc.TemperaturaServidorServicer):
    def CadastrarTemperatura(self, request, context):
        dado = {
            'data': request.data,
            'localizacao': request.name.localizacao,
            'temperatura': request.temperatura
        }
        lista.append(dado)
        return TemperaturaServidor.StatusReply(status='OK')

    def ListaTodasTemperaturas(self, request, context):
        list = TemperaturaServidor_pb2.ListaDeTemperaturas()
        for item in lista:
            temp_data = TemperaturaServidor_pb2.Temperaturas(data=item['data'], localizacao=item['localizacao'], temperatura=item['temperatura'])
            list.temperatura_data.append(temp_data)
        return list

    def BuscarTemperaturaPorData(self, request, context):
        temp = [temp for temp in lista if (temp['data'] == request.data)]
        return TemperaturaServidor.TemperaturasList(temperatura_dado = temp)

    def BuscarTemperaturaPorLocalizacao(self, request, context):
        temp = [temp for temp in lista if (temp['localizacao'] == request.localizacao)]
        return TemperaturaServidor.TemperaturasList(temperatura_dado = temp)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TemperaturaServidor_pb2_grpc.add_TemperaturaServidorServicer_to_server(TemperaturaServidor(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()