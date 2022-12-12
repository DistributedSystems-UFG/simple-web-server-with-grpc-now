from __future__ import print_function
import logging

import grpc
import TemperaturaServidor_pb2
import TemperaturaServidor_pb2_grpc

import const

def Cliente():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = TemperaturaServidor_pb2_grpc.TemperaturaServiceStub(channel)

        data = input("Digite a data:")
        localizacao = input("Insira a localizacao")
        temperatura = input("insira a Temperatura")

        response = stub.CadastrarTemperatura(TemperaturaServidor_pb2.Temperatura(data, localizacao, temperatura))

        data_busca = input("Insira data de busca")
        response = stub.BuscarTemperaturaPorData(TemperaturaServidor_pb2.DataTemperatura(data_busca))

        localizacao_busca = input("Insira a localizacao de busca")
        response = stub.BuscarTemperaturaLocalizacao(TemperaturaServidor_pb2.DataTemperatura(localizacao_busca))


if __name__ == '__main__':
    Cliente()